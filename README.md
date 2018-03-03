[![Build Status](https://travis-ci.org/ChristopherSClosser/try-to-get-by.svg?branch=master)](https://travis-ci.org/ChristopherSClosser/try-to-get-by) [![Coverage Status](https://coveralls.io/repos/github/ChristopherSClosser/try-to-get-by/badge.svg)](https://coveralls.io/github/ChristopherSClosser/try-to-get-by)
# try-to-get-by
---
### Description

Version: *beta 0.0.1*

##### *An Experiment in AI and Hive Mind Swarm Intelligence*
Pondering research involving nano technology, and observing insect and avian swarms, peaked my curiosity to see if I could create a two dimensional representation of this behavior. Using Django for the front end and fundamental data structure and algorithm theories on the back end, I was able to come up with something quite convincingly life like... of course totaly under my control.

###### As of now they are able to:
- move freely
- eat
- procreate
- die
- all while wanting to be near each other

###### I am able to:
- put a population cap or not
- limit life spans or not
- auto feed to sustain population
- give them a queen or not

*From here it will be fairly straight forward to implement a three dimensional environment and initiate tasks.*

<br/>

### Author
---
* [ChristopherSClosser](https://github.com/ChristopherSClosser/try-to-get-by)

<br/>

### Dependencies
---
* http
* shortcuts
* contrib
* Django

<br/>

### Getting Started
---
##### *Prerequisites*
* [python (3.6+)](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [git](https://git-scm.com/)

##### *Installation*
First, clone or fork the project repo from Github. Then, change directories into the cloned repository. To accomplish this, execute these commands from your terminal:

`$ git clone https://github.com/ChristopherSClosser/try-to-get-by.git`

`$ cd try-to-get-by`

Now now that you have cloned your repo and changed directories into the project, create a virtual environment named "ENV", and install the project requirements into your VE.

`$ python3 -m venv ENV`

`$ source ENV/bin/activate`

`$ pip install -r requirements.txt`

`$ export SECRET_KEY='secret'`

`$ export DEBUG=True`

##### *Serving Locally*
Once you have cloned the application and installed the requirements, you can serve the project on your local machine by executing this command from your terminal, on the same level as `manage.py`.

`$ ./manage.py runserver`

Once you have executed this command, open your browser, and go to `localhost:8000/`.

Currently the bug and size selectors are not functioning, but click the run button and a standard 18x18 matrix with 9 bugs will start. Make sure you click the feed button often or they will die.

<br/>

### Test Suite
---
##### *Running Tests*
This is a Django application, and therefore to run tests, run the following command at the same level as `./manage.py`.

`$ ./manage.py test`

For testing coverage report run the following command:

`$ coverage run ./manage.py test`

Once testing is complete:

`$ coverge report -m`

##### *Test Files*
The testing files for this project are:

| File Name | Description |
|:---:|:---:|
| `./intell/tests.py` | Test intell. |

<br/>

### URLs
---
The URLS for this project can be found in the following modules:

| URL module | Description |
|:---:|:---:|
| ./intell/urls.py | intell URL Configuration |
| ./getby/urls.py | getby URL Configuration |

<br/>

### Development Tools
---
* *python* - programming language
* *Django* - web framework
* *jQuery* - programming language

<br/>

### License
---
This project is licensed under MIT License - see the LICENSE.md file for details.

<br/>

### Acknowledgements
---

<center>

*This README was generated using [writeme.](https://github.com/chelseadole/write-me)*

</center>
