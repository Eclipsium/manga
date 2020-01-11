import glob
import os
import shutil

from celery.utils.log import get_task_logger
from django.core.files import File
from pyunpack import Archive, PatoolError

from apps.manga_api.celery import app as celery_app
from apps.manga_api.models import MangaArchive, MangaImage, MangaVolume

logger = get_task_logger(__name__)


def get_images_from_path(temp_path):
    os.chdir(temp_path)
    files = [f for f in glob.glob("*/*.jpg", recursive=True)]
    if not files:
        files = [f for f in glob.glob("*/*.png", recursive=True)]
    return files


def parse_data_from_archive(archive_id, manga_volume):
    response = []
    instance = MangaArchive.objects.get(pk=archive_id)
    volume = MangaVolume.objects.get(id=manga_volume)
    archive_path = instance.archive.path
    temp_path = os.path.join('/media/temp', str(instance.id) + '/')
    logger.info(temp_path)

    if not os.path.exists(temp_path):
        os.makedirs(temp_path)
        logger.info('temp path created')

    try:
        Archive(archive_path).extractall(temp_path)
    except PatoolError as e:
        shutil.rmtree(temp_path)
        instance.delete()
        logger.error(e)
        return

    opened_file = []
    extract_image = get_images_from_path(temp_path)
    logger.info('Images: ' + str(extract_image))
    logger.info('Archive path' + archive_path)

    if len(extract_image) < 1:
        volume.delete()
    else:
        for index in range(len(extract_image)):
            current_image = MangaImage()
            opened_file.append(open(extract_image[index], 'rb'))  # use 'rb' mode for python3
            data = File(opened_file[index])
            current_image.image = data
            current_image.sort_index = index + 1
            current_image.volume = volume
            response.append(current_image)

        MangaImage.objects.bulk_create(response)

        for file in opened_file:
            file.close()

    shutil.rmtree(temp_path)
    instance.delete()


@celery_app.task
def parse_task_data(archive_id, manga_volume):
    parse_data_from_archive(archive_id, manga_volume)
