# Django Forms


⌨️  Creating a Blank Django Project :
```
    sudo django-admin startproject django_forms
```
To Run the Application in Server :
```
    python manage.py runserver
    python3 manage.py runserver
```
 * Starting development server at,
 ```
    http://127.0.0.1:8000/
```
⌨️  Setup in VS Code Text Editor :
 * You can install Python or Django Extension in your vs code.

⌨️  Project Settings :
This command will migrate all our database in to SQLite3 file.
```
    python manage.py migrate
    OR,
    python3 manage.py migrate
```

⌨️  Built-In Components :
 * In the Chrome or Any browser to navigate into django admin panel check this url and it will show django administration,
```
   http://127.0.0.1:8000/admin/login/?next=/admin/
```
 * Create your user Id in Django Administration, run this command:
```
  python manage.py createsuperuser
  OR,
  python3 manage.py createsuperuser
```
 * Next Log In with your user ID and Password and the Dashboard will show you in this url,
 ```
    http://127.0.0.1:8000/admin/
```
⌨️  Working with Apps : URLs & Views

 * While working on app we can need multiple django templates so we can use this command

```
 python3 manage.py startapp socialize
```

###  Getting Started with Templates :
⌨️  Static Files & taking initial mark in the Django Template Language

 * To check the new template which we created we can see in the browser,
```
  http://127.0.0.1:8000/socialize/
```
 * To create Static site we need to add its bases styles UI.

⌨️  Key Django Template Language Features & Tags

⌨️  Adding a Detail Page

⌨️  Dynamic Paths : Dynamic URLs in Templates

⌨️  Using Django Template Inheritance

⌨️  Data Definition 

 * Data has 3 main categories that will be temporary data, semi-persistent data and persistent data.
 * Temporary Data has User Input, Selected Blog Posts. This data is also used immediately and lost thereafter. It also stored in memory including Variables.
 * Semi-Persistent Data is used for user authentication status. This data is also stored for a longer time but may be lost so that it can be re-created.
 * Persistent Data is used for blog posts, orders and so on. It is used for the data to stored forever and must not be lost. It can be also stored in a Database.

⌨️  Using Models

⌨️  Using the Admin Panel & Querying Data

⌨️  Adding Image Upload & Serving & Displaying Images

⌨️  Configuring the Admin Area

⌨️  Setting one-to-many Relations

⌨️  Many-to-many Relations

⌨️  More Meetup Fields & Outputting Related Data

⌨️  Render Data from the Database with a Model

⌨️  Creating a Modelform

⌨️  Handling Form Submission

⌨️  More on Form Submission & Validation

⌨️  From Modelform to Form

⌨️  Optimizing URLs



