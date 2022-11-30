<div align="center">
<p align=center>
<a href="https://softuni.bg">
<img src="http://innovationstarterbox.bg/wp-content/uploads/2016/05/Softuni_logo_trasparent.png" alt="Logo" width="600">
</a>
<p>
<br><br>
<h1 align=center>Wonderlanders</h1>
<h3 align=center>
A stylish website for travellers built with Django and Python.<br>
Final project for the Web Framework Course in Software University.<br>
<br>
<a href='https://wonderlanders.tk'> To see the demo click here </a>
<br><br>
	
[About](#about) | [Installation](#installation) | [Roadmap](#roadmap) | [Credits](#credits) | [License](#license)

</h3>
	 
</div>

 <a href="https://wonderlanders.tk">
 <img src="https://i.postimg.cc/Y2WCpxFB/Screenshot-2022-11-22-at-16-25-44.png" alt="Demo">
 </a

<!-- ABOUT -->
## About

<h4> 
	Wonderlanders is a project inspired by the world around us and our endless opportunities to explore it.<br>
	The functionalities are as follows: <br>
	
	1) For unregistered users:
	   - You can view 
</h4>
	
<!-- INSTALLATION -->
## Installation

**First**
```bash
git clone https://github.com/elly2chan/wonderlanders-django-project
```
**Then**
```bash
pip install -r requirements.txt
```
***Note: If you are on a Mac, change "psycopg2" to "psycopg2-binary" in requirements.txt before running the command above!***

## In order to use the app, you should change the following in settings.py:

```python
SECRET_KEY = config['SECRET_KEY'] # Change to a valid secret key or set it up in a .env file

DEBUG = bool(config['DEBUG']) # Change to True/False or set it up in a .env file

ALLOWED_HOSTS = config['ALLOWED_HOSTS'].split(' ') # Change to valid hosts or set them in .env file
```

Change database credentials to valid ones or set them up in a .env file and leave them as they are:

```python
DATABASES = {
    'default': {
        'ENGINE': config['DB_ENGINE'],
        'NAME': config['DB_NAME'],
        'USER': config['DB_USER'],
        'PASSWORD': config['DB_PASSWORD'],
        'HOST': config['DB_HOST'],
        'PORT': config['DB_PORT'],
    }
}
```

Or use the default database configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Set Redis Cache configuration (same as DB - change values to valid ones or set them up in .env file):

```python
CACHES = {
    'default': {
        'BACKEND': config['CACHE_BACKEND'],
        'LOCATION': config['CACHE_LOCATION'],
    },
}
```

Set Cloudinary configuration:

```python
cloudinary.config(
    cloud_name=config['CLOUD_NAME'], # Change to valid Cloudinary cloud name or set it up in .env file
    api_key=config['API_KEY'], # Change to valid Cloudinary api key or set it up in .env file
    api_secret=config['API_SECRET'], # Change to valid Cloudinary api secret or set it up in .env file
    secure=bool(config['SECURE']), # Change to True/False or set it up in .env file
)
```

<!-- ROADMAP -->
## Roadmap

- [x] The application must have at least 10 web pages
- [x] Shoulb be created using function-based views and at least 5 class-based views
- [x] The application must have at least 5 independent models
- [x] The application must have at least 5 templates
- [x] Use PostgreSQL as a DB Service
- [x] Well-looking UI
- [x] Good UX
- [x] Login/Register/Logout Functionality
- [x] Public part
- [x] Private part
- [x] Customized admin site (accessible only by admins)
	- [x] Add at least 5 custom options (e.g., filters, list display, ordering, etc.)
- [x] Unauthenticated users (public part) have only 'get' permissions
- [x] Authenticated users (private part) have full CRUD for all their created content 
- [x] Admins have 2 groups
	- [x] Superusers - have permission to do full CRUD functionalities
	- [x] Staff - have permission to do limited CRUD functionalities
- [x] User roles could be manageable from the admin site
- [x] Make sure the role management is secured and error-safe
- [x] When validating data, show appropriate messages to the user
- [x] Security (prevent SQL injection, XSS, CSRF, parameter tampering, etc)
- [x] Write tests (Unit & Integration) for your views/models/forms - at least 10 test
- [ ] Writing asynchronous view/s somewhere in the project
- [ ] Extend your Django project with REST Capabilities
- [x] Host the application in a cloud environment
- [ ] Extend Django User

<!-- Credits -->
## Credits

<!-- LICENSE -->
## License

Distributed under the [MIT](https://github.com/elly2chan/wonderlanders-django-project/blob/main/LICENSE) License.

<p align="left"><a href="#readme-top">Back to top</a></p>
