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
Criar a classe Contact_admin com opções de list display, links, pagination, editable, etc...
Registrar category e criar Category_admin
```

dentro de settings

```
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

Add a templates o base_templates
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
Criar arquivo de style.css dentro de base_static/global/css

dentro de settings STATICFILES_DIRS = [BASE_DIR / 'base_static']

Criar base.html dentro de base_templates/global

No arquivo base.html criar uma main com a class content (uma classe de estilização dentro de style.css)
Criar um bloco de content
Dentro da head criar um link com rel stylesheet e href de static de global/css/style.css

Dentro de contact.views.py

```
Importar o Contact, dentro da função index criar uma variavel contacts = Contact.filter(show=True).order_by('-id')
e criar uma variavel context = {'contacts' : 'contacts'}
return render(request, 'contact/index.html', context)
```

Dentro de index.html

```
Apagar conteudo dentro de block
Testar tudo sem as classes
Criar uma div com a class "responsive-table" 
Dentro da div criar uma table com classe "contacts-table"
Dentro da table criar uma caption com classe "table-caption" com título 'Contacts'

Dentro de table criar um thead
Dentro de thead criar tr com classe "table-row table-row-header"
Dentro de tr criar 5 th com classe "table-header" id, fn, ln, phone, email

Dentro de table criar tbody
dentro tbody criar {% for contact in contacts%}
dentro de for criar tr classe "table-row"
dentro tr criar 5 td class "table-cel"
dentro de td criar <a> class "table-link"
por fim dentro de a colocar os dados {{contact.}}




Criar contact.html dentro de templates/contact
deve extender de base e ter um block content
com div single-contact dentro h1 single-contact-name e {{contact.fn}}{{contact.ln}}
E dentro da div ter <p><b>ID:</b> {{contact.id}}</p> p/ tds os models

nas views criar funcao contact com parametro contact_id, com variavel single_contact com queryset GET
nas urls add novo path p/ contact com '<int:contact_id>/'

dentro de index.html em cada href {% url 'contact:contact' contact.id %}

Trocar no contact views single_contact = get_object_or_404(Contact, id=contact_id, show=True)
```

Em base.html em body acima de main criar uma header.header e dentro uma h1.header-heading com um link
a.header-link
o link vai ser para a pagina inicial(index)(usando {% url 'contact:index' %})

Ainda dentro de header criar uma nav.menu, ul.menu-list, li.menu-item, a.menu-link e duplicar mais uma vez o li.menu-item para ter 2 itens no menu

ainda dentro de header criar uma div search.search com um form:get com input.search-input com atributos type="search", placeholder="Search", id="search", name="q"


Se Tiver alguma tag muito grande(apenas se estiver grande) pode adicionar um diretorio dentro de global com nome partials e criar por exemplo o <nav> e criar um arquivo _header.html e depois apenas ir no base e colocar um {% include 'global/partials/_header.html' %}

Faça também com a head

Dentro da _head.html no titulo colocar {{ site_title }} e então nos context das views adicionar o site_title, no index colocar 'site_title' : Contacts -, e no contact add uma variavel com nome do contato inteiro site_title = f'{single_contact.first_name} {single_contact.last_name} - ' e no context 'site_title': site_title   

Criar nova view search
Criar url search
no action do search colocar a url "{% url 'contact:search' %}"
