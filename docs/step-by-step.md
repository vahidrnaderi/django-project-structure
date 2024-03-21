
# Step by step making the base structure:

## 1. Making base project structure:

```
$ mkdir <project-root>
$ git init
$ touch README.md .gitignore LICENSE
```
* Edit all new files
```
$ git add .
$ git commit -m "Initial commit"
$ git remote add origin <your/repository/ssh/link>
$ git push origin main
$ pipenv install --python "3.12" 'django>=5.0' 'djangorestframework>=3.14'
$ mkdir requirements
$ pipenv requirements > requirements/requirements.txt
$ pipenv run django-admin startproject project_name
$ mv project_name/project_name project_name/config
$ mkdir project_name/config/settings
$ mv project_name/config/settings.py project_name/config/settings/development.py
$ touch project_name/config/settings/__init__.py \
        project_name/config/settings/production.py \
        project_name/config/settings/staging.py
$ mv project_name/manage.py .
```
* Open 'manage.py', 'settings/development.py', 'asgi.py', and 'wsgi.py' to change all:
    > project_name.

    to 
    > project_name.config.


## 2. Adding 'core' app to project
```
$ mkdir project_name/apps
$ mkdir project_name/apps/core
$ pipenv run django-admin startapp core project_name/apps/core
$ touch project_name/apps/core/constants.py \
        project_name/apps/core/exceptopns.py \
        project_name/apps/core/helpers.py \
        project_name/apps/core/services.py \
        project_name/apps/core/urls.py
$ mkdir project_name/apps/core/api
$ mkdir project_name/apps/core/api/v1
$ mkdir project_name/apps/core/api/v2
$ mkdir project_name/apps/core/fixtures
$ mkdir project_name/apps/core/management
$ mkdir project_name/apps/core/management/commands
$ mkdir project_name/apps/core/templates
$ mkdir project_name/apps/core/tests
$ mv project_name/apps/core/tests.py project_name/apps/core/tests/test_core_name.py
$ touch project_name/apps/core/tests/__init__.py
$ touch project_name/apps/core/api/__init__.py \
$       project_name/apps/core/api/v1/__init__.py \
        project_name/apps/core/api/v1/serializers.py \
        project_name/apps/core/api/v1/urls.py \
        project_name/apps/core/api/v1/views.py
$ touch project_name/apps/core/api/v2/__init__.py \
        project_name/apps/core/api/v2/serializers.py \
        project_name/apps/core/api/v2/urls.py \
        project_name/apps/core/api/v2/views.py
$ touch project_name/apps/core/fixtures/.gitkeep \
        project_name/apps/core/management/__init__.py \
        project_name/apps/core/management/commands/__init__.py \
        project_name/apps/core/management/commands/command.py \
        project_name/apps/core/management/commands/__init__.py \
        project_name/apps/core/templates/.gitkeep
```
## 3. Adding 'app1' app to project:
```
$ mkdir project_name/apps/app1
$ pipenv run django-admin startapp app1 project_name/apps/app1
$ mkdir project_name/apps/app1/api
$ mkdir project_name/apps/app1/api/v1
$ mkdir project_name/apps/app1/api/v2
$ mkdir project_name/apps/app1/fixtures
$ mkdir project_name/apps/app1/management
$ mkdir project_name/apps/app1/management/commands
$ mkdir project_name/apps/app1/templates
$ mkdir project_name/apps/app1/tests
$ mv project_name/apps/app1/tests.py project_name/apps/app1/tests/test_app1_name.py
$ touch project_name/apps/app1/tests/__init__.py 
$ touch project_name/apps/app1/api/__init__.py \
        project_name/apps/app1/api/v1/__init__.py \
        project_name/apps/app1/api/v1/serializers.py \
        project_name/apps/app1/api/v1/urls.py \
        project_name/apps/app1/api/v1/views.py
$ touch project_name/apps/app1/api/v2/__init__.py \
        project_name/apps/app1/api/v2/serializers.py \
        project_name/apps/app1/api/v2/urls.py \
        project_name/apps/app1/api/v2/views.py
$ touch project_name/apps/app1/management/__init__.py \
        project_name/apps/app1/management/commands/command.py \
        project_name/apps/app1/management/commands/__init__.py \
        project_name/apps/app1/templates/.gitkeep \
        project_name/apps/app1/services.py \
        project_name/apps/app1/urls.py
```
## 4. Adding 'app2' app to project:
```
$ mkdir project_name/apps/app2
$ pipenv run django-admin startapp app2 project_name/apps/app2
$ mkdir project_name/apps/app2/api
$ mkdir project_name/apps/app2/api/v1
$ mkdir project_name/apps/app2/api/v2
$ mkdir project_name/apps/app1/fixtures
$ mkdir project_name/apps/app1/management
$ mkdir project_name/apps/app1/management/commands
$ mkdir project_name/apps/app1/templates
$ mkdir project_name/apps/app1/tests
$ mv project_name/apps/app2/tests.py project_name/apps/app2/tests/test_app2_name.py
$ touch project_name/apps/app2/tests/__init__.py 
$ touch project_name/apps/app2/api/__init__.py \
        project_name/apps/app2/api/v1/__init__.py \
        project_name/apps/app2/api/v1/serializers.py \
        project_name/apps/app2/api/v1/urls.py \
        project_name/apps/app2/api/v1/views.py
$ touch project_name/apps/app2/api/v2/__init__.py \
        project_name/apps/app2/api/v2/serializers.py \
        project_name/apps/app2/api/v2/urls.py \
        project_name/apps/app2/api/v2/views.py
$ touch project_name/apps/app2/management/__init__.py \
        project_name/apps/app2/management/commands/command.py \
        project_name/apps/app2/management/commands/__init__.py \
        project_name/apps/app2/templates/.gitkeep \
        project_name/apps/app2/services.py \
        project_name/apps/app2/urls.py

```
## 5. Initializing apps configuration in the project:

1. First open 'settings.py' and do bellow changes:
    ```
    INSTALLED_APPS = [
        ... 

        # Add your apps here:
        'project_name.apps.core',
        'project_name.apps.app1',
        'project_name.apps.app2',
    ]
    ```
2. Then open 'apps.py' from all apps and do changes:
    ```
    name = 'apps.core'
    name = 'apps.app1'
    name = 'apps.app2'
    ```
    to 

    ```
    name = 'project_name.apps.core'
    name = 'project_name.apps.app1'
    name = 'project_name.apps.app2'
    ```
## 6. Add other structure to project:
```
$ mkdir project_name/common
$ touch project_name/common/__init__.py \
        project_name/common/common.py \
        project_name/common/constants.py \
        project_name/common/generics.py \
        project_name/common/helpers.py \
        project_name/common/mixins.py \
        project_name/common/models.py \
        project_name/common/serializers.py
$ mkdir deployments docs local_db locale
$ touch deployments/docker-compose.yml \
        deployments/Dockerfile \
        deployments/Dockerfile_dev \
        deployments/Dockerfile_prod
$ touch docs/CHANGELOG.md \
        docs/CONTRIBUTING.md \
        docs/deployment.md \
        docs/local-development.md \
        docs/schema.yml \
        docs/step-by-step.md
$ touch local_db/db.sqlite3.example
$ touch locale/.gitkeep

$ mkdir logs media scripts static static/css
$ mkdir static/css static/images static/js 
$ touch logs/.gitkeep \
        media/.gitkeep \
        scripts/entrypoint.sh \
        static/css/.gitkeep \
        static/images/.gitkeep \
        static/js/.gitkeep

$ touch requirements/common.txt \
        requirements/development.txt \
        requirements/local.txt \
        requirements/production.txt

$ cp .gitignore .dockerignore
$ touch .env \
        .flake8 \
        pyproject.toml \
        pytest.ini \
        setup.cfg \
        setup.py \
        tox.ini \

$ pipenv requirements --dev-only > requirements/requirements-dev.txt
```

