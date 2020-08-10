## Manga exchage project

developer - abiogenesis70ru@gmail.com

###### Stack:

##### Backend - Django Rest framework https://www.django-rest-framework.org/

##### Frontend - Nuxt.js & vuetify.js https://nuxtjs.org https://vuetifyjs.com

## Server config

##### Nginx, Node.js, Gunicorn, celery, redis

##API endpoints
http://manga-exchange.ru/api/v1/ - REST Swagger

##Admin panel
http://manga-exchange.ru/admin/

###Commands

####Clear cache - `python manage.py thumbnail cleanup`
####Apply changes for frontend - `npm run build && pm2 restart`
####Restart gunicorn - `sudo systemctl restart manga.service`


