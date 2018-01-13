[![Build Status](https://travis-ci.org/ChristopherSClosser/try-to-get-by.svg?branch=master)](https://travis-ci.org/ChristopherSClosser/try-to-get-by) [![Coverage Status](https://coveralls.io/repos/github/ChristopherSClosser/try-to-get-by/badge.svg)](https://coveralls.io/github/ChristopherSClosser/try-to-get-by)
# try-to-get-by
---
### Description

Version: *pre-beta*

An Experiment...

### Authors
---
* [ChristopherSClosser](https://github.com/ChristopherSClosser/try-to-get-by)

### Dependencies
---
* http
* shortcuts
* generic
* contrib
* Django

### Getting Started
---
##### *Prerequisites*
* [python (3.6+)](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [git](https://git-scm.com/)

##### *Installation*
First, clone the project repo from Github. Then, change directories into the cloned repository. To accomplish this, execute these commands:

`$ git clone https://github.com/ChristopherSClosser/try-to-get-by.git`

`$ cd try-to-get-by`

Now now that you have cloned your repo and changed directories into the project, create a virtual environment named "ENV", and install the project requirements into your VE.

`$ python3 -m venv ENV`

`$ source ENV/bin/activate`

`$ pip install -r requirements.txt`
##### *Serving Locally*
Once you have cloned the application and installed the requirements, you can serve the project on your local machine by executing this command from your terminal, on the same level as `manage.py`.
`$ ./manage.py runserver`
Once you have executed this command, open your browser, and go to `localhost:8000/`.
### Test Suite
---
##### *Running Tests*
This is a Django application, and therefore to run tests, run the following command at the same level as `./manage.py`.

`./manage.py test`
##### *Test Files*
The testing files for this project are:

| File Name | Description |
|:---:|:---:|
| `./intell/tests.py` | Test intell. |

### URLs
---
The URLS for this project can be found in the following modules:

| URL module | Description |
|:---:|:---:|
| ./intell/urls.py |  |
| ./getby/urls.py | getby URL ConfigurationThe `urlpatterns` list routes URLs to views. For more information please see:https://docs.djangoproject.com/en/2.0/topics/http/urls/Examples:Function views1. Add an import:  from my_app import views2. Add a URL to urlpatterns:  path('', views.home, name='home')Class-based views1. Add an import:  from other_app.views import Home2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')Including another URLconf1. Import the include() function: from django.urls import include, path2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))from django.contrib import adminfrom django.conf.urls import include, urlfrom getby.views import HomeViewurlpatterns = [url(r'^$', HomeView.as_view(), name='home'),url(r'^intell/', include('intell.urls')),url(r'^admin/', admin.site.urls),] |

### Development Tools
---
* *python* - programming language
* *django* - web framework

### License
---
This project is licensed under MIT License - see the LICENSE.md file for details.
### Acknowledgements
---
* Coffee

*This README was generated using [writeme.](https://github.com/chelseadole/write-me)*
