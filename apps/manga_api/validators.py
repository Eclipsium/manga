from django.core.exceptions import ValidationError

allowed_file_extension = (
    '7z', 'ace', 'alz', 'a', 'arc', 'arj', 'bz2', 'cab', 'z', 'cpio', 'deb', 'dms', 'gz', 'lrz', 'lha',
    'lzh', 'lz', 'lzma', 'lzo', 'rpm', 'rar', 'rz', 'tar', 'xz', 'zip', 'jar', 'zoo'
)


def validate_file_size_and_ext(value):
    filesize = value.size
    file_extension = value.name.split('.')[-1].lower()
    if file_extension not in allowed_file_extension:
        raise ValidationError('Supported ' + str(allowed_file_extension) + ' file extension')
    if filesize > 214958080:
        raise ValidationError("The maximum file size that can be uploaded is 250MB")
    return value
