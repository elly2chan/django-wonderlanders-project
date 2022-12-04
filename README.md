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
<a href='https://wonderlanders.tk'> Click here to see the deployed project </a>
<br><br>
	
[About](#about) | [Installation](#installation) | [Urls](#urls) | [Roadmap](#roadmap) | [Credits](#credits) | [License](#license)

</h3>
	 
</div>

 <a href="https://wonderlanders.tk">
 <img src="https://i.postimg.cc/Y2WCpxFB/Screenshot-2022-11-22-at-16-25-44.png" alt="Demo">
 </a

<!-- ABOUT -->
## About

<p align='justify'>
Wonderlanders is a project inspired by the world around us and our endless opportunities to explore it.
It is a very simple, user-friendly website where you can create posts by uploading photos and
details about your journeys.<br><br>
The site is fully functional. It has a lot of features, with the key ones listed below:<br><br>
 - It has a log in, log out system and a cart functionality.<br>
 - There are three types of users - normal, staff and administrators.<br>
 - It has a public part, accessible by both authorized and non-authorized viewers.<br>
 - It has a private part - functionalities that only authorized users can use.<br>
 - Some of the features of the private part are usable only by staff and superusers.<br>
 - The project is deployed in AWS.<br>
 - The storage used for saving photos, uploaded by users is Cloudinary.<br>
</p>
<br>
This is my first actual web project and here is the tech stack used so far:
<br><br>

[![My Skills](https://skillicons.dev/icons?i=py,django,html,css,docker,github,postgres)](https://skillicons.dev)
<br><br>
For more information, you can also see the [Credits](#credits).
	
<!-- INSTALLATION -->
## Installation

<h4>First you should do two things:</h4>

```bash
git clone https://github.com/elly2chan/django-wonderlanders-project
```
	
```bash
pip install -r requirements.txt
```
***Note: If you are on a Mac, change "psycopg2" to "psycopg2-binary" in requirements.txt before running the command above!***

<br>

<h4>Next you should configure your "settings.py" file by either changing values below (like config['SECRET_KEY'])<br>
or setting them up in a .env file: </h4>

```python
SECRET_KEY = config['SECRET_KEY'] # Change to a valid secret key or set it up in a .env file

DEBUG = bool(config['DEBUG']) # Change to True/False or set it up in a .env file

ALLOWED_HOSTS = config['ALLOWED_HOSTS'].split(' ') # Change to valid hosts or set them in .env file
```

<h4>Do the same for your database configuation:</h4>
	
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

<h4>Or use the default database configuration:</h4>

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
	
<h4>If you want to use cache, you can configure it as well:</h4>

```python
CACHES = {
    'default': {
        'BACKEND': config['CACHE_BACKEND'],
        'LOCATION': config['CACHE_LOCATION'],
    },
}
```

<h4>Set Cloudinary configuration:</h4>

```python
cloudinary.config(
    cloud_name=config['CLOUD_NAME'], # Change to valid Cloudinary cloud name or set it up in .env file
    api_key=config['API_KEY'], # Change to valid Cloudinary api key or set it up in .env file
    api_secret=config['API_SECRET'], # Change to valid Cloudinary api secret or set it up in .env file
    secure=bool(config['SECURE']), # Change to True/False or set it up in .env file
)
```

<!-- URLS -->
## Urls

<h4>The application integrates the following urls for each application:</h4>

<h4>Main urls:</h4>
	
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wonderlanders.common.urls')),
    path('posts/', include('wonderlanders.posts.urls')),
    path('profile/', include('wonderlanders.profiles.urls')),
    path('products/', include('wonderlanders.products.urls')),
    path('store/', include('wonderlanders.store.urls')),
]
```
<h4>Common:</h4>
	
```python
urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
)
```
<h4>Posts:</h4>
	
```python
urlpatterns = (
    path('create/', CreatePostView.as_view(), name='create post'),
    path('details/<int:pk>', PostDetailsView.as_view(), name='post details'),
    path('category/<slug>', PostCategoryView.as_view(), name='post category'),
    path('edit/<int:pk>', EditPostView.as_view(), name='edit post'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete post'),
    path('comment/<int:pk>/', include([
        path('', comment_post, name='comment post'),
        path('delete/', delete_comment, name='delete comment'),
    ])),
)
```
<h4>Products:</h4>
	
```python
urlpatterns = (
    path('', ProductsView.as_view(), name='all products'),
    path('add-product/', AddProductView.as_view(), name='add product'),
    path('add-product-category/', AddProductCategoryView.as_view(), name='add product category'),
    path('edit-product/<int:pk>', EditProductView.as_view(), name='edit product'),
    path('delete-product/<int:pk>', DeleteProductView.as_view(), name='delete product'),
    path('product-categories/', include([
        path('', ProductCategories.as_view(), name='product categories'),
        path('edit/<int:pk>', EditProductCategoryView.as_view(), name='edit product category'),
        path('delete/<int:pk>', DeleteProductCategoryView.as_view(), name='delete product category'),
    ])),
)

```
<h4>Profiles:</h4>
	
```python
urlpatterns = (
    path('login/', LoginView.as_view(), name='login user'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('logout/', LogoutView.as_view(), name='logout user'),
    path('<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)

```
<h4>Store:</h4>
	
```python
urlpatterns = (
    path('cart/add/<int:pk>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:pk>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:pk>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:pk>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail, name='cart_detail'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
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
- [x] Host the application in a cloud environment
- [x] Extend Django User

<!-- Credits -->
## Credits

<!-- LICENSE -->
## License

Distributed under the [MIT](https://github.com/elly2chan/wonderlanders-django-project/blob/main/LICENSE) License.
