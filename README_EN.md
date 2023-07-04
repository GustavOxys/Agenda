How to create a Planner with Django

Configure Virtual Envirement

```
Install Django
Start the project with name project
Create app contact
```

Configure git

```
git config --global user.name 'name'
git config --global user.email 'your_email@gmail.com'
git config --global init.defaultBranch main
# Configure the .gitignore
git init
git add .
git commit -m 'Message'
git remote add origin URL_DO_GIT
git push origin main
```

Migrate your db

```
python manage.py makemigrations
python manage.py migrate
```

Create your superuser

```
python manage.py createsuperuser
python manage.py changepassword USERNAME
```
Create directory templates/contact inside contact with file index.html
Create views and urls.py inside app contact

In urls of project make include of url of contact

Create model contact

```
With first_name, last_name, phone, email, created_date, description, show, picture(blank e upload_to=''), category (foreignkey of class Category, on_delete=models.SET_NULL, blank=True, null=True), owner(foreignkey of User).
```
Register this model in admin using decorator

```
@admin.register(contact)
Create a class Contact_admin with options of list display, links, pagination, editable, etc...
Register category and create Category_admin
```

Inside settings

```
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

Add to templates base_templates
```

Execute python manage.py collectstatic

Add to gitignore 

```
static/
media/
```

Inside urls of the project

```
from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
install faker and execute script of utils to create 1000 contact in the planner

Create in project
```
local_settings.py to local files that cant go to github so put in gitignore
```
Create file of style.css inside base_static/global/css

Inside settings

STATICFILES_DIRS = [BASE_DIR / 'base_static']

Create base.html inside base_templates/global

In the file base.html create a main with class content (A class of styling within style.css)
Create a block with content
Inside the head create a link with rel stylesheet and href static of global/css/style.css

Inside contact.views.py

```
Import the Contact, inside the function index create a variable contacts = Contact.filter(show=True).order_by('-id')
And create a variable context = {'contacts' : 'contacts'}
return render(request, 'contact/index.html', context)
```

Inside index.html

```

Extends from base, create a block content with a div responsible-table
the create a table with contacts-table
the caption is 'Planner' (table-caption)

The head is with a table row (table-row table-row-header)
and with 5 table headers(table-header) id, fn, ln, phone, email

And the body is using for from django to get the contact from contacts
Using a table row(table-row) you will make a table date(table-cel) with a anchor(table-link)







Criar uma div com a class "responsive-table" 
Dentro da div criar uma table com classe "contacts-table"
Dentro da table criar uma caption com classe "table-caption" com título 'Contacts'

Dentro de table criar um thead
Dentro de thead criar tr com classe "table-row table-row-header"
Dentro de tr criar 5 th com classe "table-header" id, fn, ln, phone, email

Dentro de table criar tbody
dentro tbody criar {% for contact in contacts%}
dentro de for criar tr classe "table-row"
dentro tr criar td class "table-cel"
dentro de td criar <a> class "table-link"
por fim dentro de a colocar os dados {{contact.}}
fazer 5x




Criar contact.html dentro de templates/contact
deve extender de base e ter um block content
com div single-contact dentro h1 single-contact-name e {{contact.fn}}{{contact.ln}}
E dentro da div ter <p><b>ID:</b> {{contact.id}}</p> p/ tds os models

nas views criar funcao contact com parametro contact_id, com variavel single_contact com queryset GET
nas urls add novo path p/ contact com '<int:contact_id>/'

dentro de index.html em cada href {% url 'contact:contact' contact.id %}

Trocar no contact views single_contact = get_object_or_404(Contact, id=contact_id, show=True)
```
