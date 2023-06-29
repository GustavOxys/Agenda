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
criar pasta templates/contact dentro de contact com arquivo index.html
Criar views e urls.py dentro do app contact

Em urls do projeto fazer include da url do contato

Criar model contact

```
com first_name, last_name, phone, email, created_data, description, show, picture(blank e upload_to=''), category (foreignkey de classe Category, on_delete=models.SET_NULL, blank=True, null=True), owner(foreignkey de User).
```
Registrar esse model em admin usando decorator

```
@admin.register(contact)
criando a classe Contact_admin com opções de list display, links, pagination, editable, etc...
```

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
instalar faker e executar script de utils para criar 1000 contatos na agenda

Criar em project
```
local_settings.py para arquivos locais que não irão p/ github
```
Criar arquivo de style.css dentro de basestatic

No arquivo base.html criar uma main com a class content (uma classe de estilização css dentro de style.css)

Dentro de contact.views.py

```
Importar o Contact, dentro da função index criar uma variavel contacts = Contact.objects.all()
e criar uma variavel context = {'contacts' : 'contacts'}
return render(request, 'contact/index.html', context)
```

