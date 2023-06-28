Como criar uma agenda do zero no Django.

Configurar ambiente virtual

```
python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py startapp contact
```

Configurar o git

```
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
git push origin main
```

Migrando a base de dados do Django

```
python manage.py makemigrations
python manage.py migrate
```

Criando e modificando a senha de um super usuário Django

```
python manage.py createsuperuser
python manage.py changepassword USERNAME
```

Criar model contact com first_name, last_name, phone, email, created_data, description, show, picture(blank e upload_to=''), category (foreignkey de classe Category).

Registrar esse model em admin usando decorator @admin.register(contact)
criando a classe Contact_admin com opções de list display, links, pagination, editable, etc...

dentro de settings

```
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

python manage.py collectstatic

Adicionar ao gitignore 
```
static/
media/
```

dentro de urls do projeto

```
from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```


