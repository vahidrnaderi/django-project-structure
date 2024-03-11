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
├── .env.example                # An example of your .env configurations. Add necessary comments.
├── .gitignore                  # https://github.com/github/gitignore/blob/main/Python.gitignore
├── entrypoint.sh               # Any bootstrapping necessary for your application
├── LICENSE
├── manage.py
├── pytest.ini
└── README.md
```

## References
- [Two Scoops of Django by Daniel and Audrey Feldroy](https://www.feldroy.com/books/two-scoops-of-django-3-x)
- [Django Best Practices](https://django-best-practices.readthedocs.io/en/latest/index.html)
- [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)
- [HackSoft Django Style Guide](https://github.com/HackSoftware/Django-Styleguide)
- [Radoslav Georgiev - Django Structure for Scale and Longevity](https://www.youtube.com/watch?v=yG3ZdxBb1oo)
- [Build APIs You Won't Hate](https://apisyouwonthate.com/books/build-apis-you-wont-hate/)
- [Tuxedo Style Guides](https://github.com/saqibur/tuxedo)
