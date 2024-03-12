[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3.12.2](https://img.shields.io/badge/python-3.12.2-blue.svg)](https://www.python.org/downloads/release/python-3122//)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)


# Django Project Structure
This is one of the best practices template/project structure for developing django-based applications -
either strictly through the `django-rest-framework` or just `django`.

The project is meant to be easily clone-able, and used as the starter template
for the next big thing you develop.


## Getting Started
1. Since this is a template repository, simply hit "Use this template" on GitHub
and follow the instructions. Otherwise, you can just clone the repo, remove/add
anything you see fit.
1. Run the project using `pipenv run python manage.py runserver` and you should see the
default success page provided by Django at
[http://127.0.0.1:8000/](http://127.0.0.1:8000/).
3. Read [Make this structure step_by_step](./docs/step-by-step.md) if you like to make this structure by yourself from the ground.

### Creating an App
1. Create a folder with the app name in `apps/`. For example: `poll`
1. Run `pipenv run python manage.py startapp poll project_name/apps/poll` from the root directory of the
project


## Project Tree
``` bash
.
├── project_name/
│   ├── apps/
│   │   ├── app1/               # A django rest app
│   │   │   ├── api/
│   │   │   │   ├── v1/         # Only the "presentation" layer exists here.
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── serializers.py
│   │   │   │   │   ├── urls.py
│   │   │   │   │   └── views.py
│   │   │   │   ├── v2/         # Only the "presentation" layer exists here.
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── serializers.py
│   │   │   │   │   ├── urls.py
│   │   │   │   │   └── views.py
│   │   │   │   └── __init__.py
│   │   │   ├── fixtures/       # Constant "seeders" to populate your database
│   │   │   ├── management/
│   │   │   │   ├── commands/   # Try and write some database seeders here
│   │   │   │   │   └── command.py
│   │   │   │   └── __init__.py
│   │   │   ├── migrations/
│   │   │   │   └── __init__.py
│   │   │   ├── templates/      # App-specific templates go here
│   │   │   ├── tests/          # All your integration and unit tests for an app go here.
│   │   │   │   └── tests.py
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── services.py     # Your business logic and data abstractions go here.
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── app2/               # A django rest app same as app1 structure
│   │   └── core/               # A django rest core same as app1 structure plus following files
│   │       ├── constants.py
│   │       ├── exceptopns.py
│   │       └── helpers.py
│   └── config/
│       ├── __init__.py
│       ├── asgi.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
├── common/                     # An optional folder containing common "stuff" for the entire project
├── deployments/                # Isolate Dockerfiles and docker-compose files here.
│   ├── Dockerfile
│   ├── Dockerfile_dev
│   ├── Dockerfile_prod
│   └── docker-compose.yml
├── docs/
│   ├── CHANGELOG.md
│   ├── CONTRIBUTING.md
│   ├── deployment.md
│   ├── local-development.md
│   └── swagger.yaml
├── requirements/
│   ├── common.txt              # Same for all environments
│   ├── development.txt         # Only for a development server
│   ├── local.txt               # Only for a local server (example: docs, performance testing, etc.)
│   ├── production.txt          # Production only
│   └── requirements.txt 
├── scripts/                    # Your script files
├── static/                     # Your static files
├── .dockerignore
├── .env.example                # An example of your .env configurations. Add necessary comments.
├── .gitignore                  # https://github.com/github/gitignore/blob/main/Python.gitignore
├── entrypoint.sh               # Any bootstrapping necessary for your application
├── LICENSE
├── manage.py
├── pytest.ini
└── README.md
```


## Rationale
Each `app` should be designed in way to be plug-able, that is, dragged and dropped
into any other project and it’ll work independently.


### `apps` Folder
* A mother-folder containing all apps for our project. Congruent to any
JS-framework's `src` folder. If you really wanted to, you could even call it the
`src` folder. Again, it's up to you.
* An app can be a django template project, or an rest framework API.

### `services`
* We’ll be writing business logic in services instead of anywhere else.
* There's a common argument: "Why not just use model managers?", and honestly,
that's a fair point. However, for our use case, we've often noticed that a single
service can leverage more zero to many models. Either way, managers or services,
both work towards the same goal - isolating business logic away from views, and
brings it closer to the data.

### `api` Folder
* We like to place all our API components into a package within an app called
`api`. For example, in this repository it's the `core/api` folder. That
allows us to isolate our API components in a consistent location. If
we were to put it in the root of our app, then we would end up with a huge list
of API-specific modules in the general area of the app. That's without getting
into the mess of API versioning.

For projects with a lot of small, interconnecting apps, it can be hard to hunt
down where a particular API view lives. In contrast to placing all API code
within each relevant app, sometimes it makes more sense to build an app
specifically for the API. This is where all the serializers, renderers, and views
are placed. Therefore, the name of the app should reflect its API version


#### API Versioning
It might often be necessary to support multiple versions of an API throughout
the lifetime of a project. Therefore, we're adding in support right from the
start.

For different API versions, we're assuming the following will change:
- Serializers: That is, how the data is presented to a consumer
- Views: That is, how the data is accessed and modified by a consumer
- URLs: That is, where the consumer access the data

`model`s and `service`s can be thought of as shared between versions. Therefore,
migrating changes should be versioned carefully without breaking different
versions of the API. After all, your API version is simply a presentation of how
data is handled and managed within your application.

Sufficient unit tests and integration tests should wrap services and API
endpoints to ensure full compatibility.


#### What's `v2` of an API?
Currently we're proposing that major changes to the following, constitutes a new API version:
1. Representation of data, either for submission or retrieval
1. Major optimizations
1. Major code reorganization and code refactor
1. Usually, in a Django project, you won't need to worry about API versioning


### `config`
* Contains project configuration files, including the primary URL file
* ~~Contains settings split into `base`, `local`, `production` and `development`.~~.
Update: As environment specific variables will be handled using environment
variables, we've deemed it unnecessary to have separate settings files for now.

### `deployments`
* Contains Docker, Docker-Compose and nginx specific files for deploying in
different environments.


### Exception handling
You should probably add a custom exception handler to your project based on
who consumes your APIs. To learn how to create a custom exception handler,
you can check out the Django Rest Framework documentation at:
https://www.django-rest-framework.org/api-guide/exceptions/#custom-exception-handling


## References
- [Two Scoops of Django by Daniel and Audrey Feldroy](https://www.feldroy.com/books/two-scoops-of-django-3-x)
- [Django Best Practices](https://django-best-practices.readthedocs.io/en/latest/index.html)
- [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)
- [HackSoft Django Style Guide](https://github.com/HackSoftware/Django-Styleguide)
- [Radoslav Georgiev - Django Structure for Scale and Longevity](https://www.youtube.com/watch?v=yG3ZdxBb1oo)
- [Build APIs You Won't Hate](https://apisyouwonthate.com/books/build-apis-you-wont-hate/)
- [Tuxedo Style Guides](https://github.com/saqibur/tuxedo)
- [Django project structure](https://github.com/saqibur/django-project-structure)
