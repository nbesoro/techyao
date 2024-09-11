# TechYAO Invoice App

[![ci-cd](https://github.com/nbesoro/techyao/actions/workflows/ci_cd.yml/badge.svg?branch=main)](https://github.com/nbesoro/techyao/actions/workflows/ci_cd.yml)

Ce projet est une application web Django qui fonctionne avec Docker et Docker Compose. Il inclut une configuration pour lancer l'application localement en utilisant Docker.

## Installation
### Avec Docker
Pour exécuter ce projet localement, assurez-vous d'avoir installé Docker et Docker Compose sur votre système. Vous pouvez les installer en suivant les instructions officielles :

-   [Docker](https://docs.docker.com/get-docker/)
-   [Docker Compose](https://docs.docker.com/compose/install/)

Une fois que `Docker` et `Docker` Compose sont installés, suivez ces étapes :

1. Clonez le dépôt depuis GitHub :

    ````bash
    $ git clone git@github.com:nbesoro/techyao.git
    $ cd techyao

    ````

2. Copiez le fichier .env.example en tant que .env :

    ```bash
    $ cp .env.sample .env
    ```

    Modifiez les variables d'environnement dans le fichier `.env` selon vos besoins.

3. Construisez les conteneurs Docker :

    ```bash
    $ docker-compose build
    ```

4. Lancez les conteneurs Docker

    ```bash
    $ docker-compose up -d
    $ docker-compose exec web python manage.py createsuperuser
    ```

5. Les conteneurs Docker seront démarrés, et l'application sera accessible à l'adresse:

- http://localhost:8005

### Sans Docker


1. Clonez le dépôt depuis GitHub :

    ````bash
    $ git clone git@github.com:nbesoro/techyao.git
    $ cd techyao
    ````

2. Copiez le fichier .env.example en tant que .env :

    ```bash
    $ cp .env.sample .env
    ```

    Modifiez les variables d'environnement dans le fichier `.env` selon vos besoins.


3. Créer et activer un environnement virtuel:

    ```sh
    $ python3.12 -m venv venv && source venv/bin/activate
    ```

4. Installer les requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

5. Appliquer les migrations:

    ```sh
    (venv)$ python manage.py migrate
    ```

6. Créer un superutilisateur et alimenter la base de données:

    ```sh
    (venv)$ python manage.py createsuperuser
    ```
	
7. Lancer le projet:

    ```sh
    (venv)$ python manage.py runserver
    ```
    
l'application sera accessible à l'adresse:

- http://localhost:8005


## Réalisé avec

Ce projet a été développé en utilisant les technologies suivantes :

-   ![Python Badge](https://img.shields.io/badge/Python-3.12-blue?logo=python)
-   ![Django Badge](https://img.shields.io/badge/Django-5.1.1-green?logo=django)
-   ![Django REST framework Badge](https://img.shields.io/badge/Django%20REST%20framework-3.15.2-orange?logo=django)
-   ![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql)

-   ![Docker Badge](https://img.shields.io/badge/Docker-20.10-blue?logo=docker)

