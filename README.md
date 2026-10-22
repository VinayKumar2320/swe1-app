# Django Polls Application

[![Build Status](https://app.travis-ci.com/VinayKumar2320/swe1-app.svg?branch=main)](https://app.travis-ci.com/github/VinayKumar2320/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/VinayKumar2320/swe1-app/badge.svg?branch=main)](https://coveralls.io/github/VinayKumar2320/swe1-app?branch=main)

A Django web application based on the official Django Polls tutorial (Parts 1–4). The project includes automated testing and code quality checks using Travis CI, Black, Flake8, and Coveralls, with deployment configured for AWS Elastic Beanstalk.

## Live Application

**AWS Elastic Beanstalk Deployment**

Previous deployment URL:

http://swe1-app-env.eba-xnafp89x.us-east-2.elasticbeanstalk.com/

The previous environment was terminated. A new deployment will be configured as part of the continuous integration and deployment setup.

## Features

- View available polls
- View poll questions and choices
- Submit votes
- Display voting results
- Vote multiple times
- Django Admin integration
- Django template-based frontend
- SQLite database
- Database migrations during deployment
- Sample poll data created through a Django data migration
- Travis CI integration
- Automated formatting and linting checks
- Test coverage reporting with Coveralls
- AWS Elastic Beanstalk deployment configuration

## Technologies

- Python
- Django
- SQLite
- Gunicorn
- Travis CI
- Black
- Flake8
- Coverage.py
- Coveralls
- AWS Elastic Beanstalk
- Amazon EC2
- Git and GitHub

## Continuous Integration

The project uses Travis CI to automatically check code changes pushed to GitHub.

The `.travis.yml` configuration runs the following checks:

1. Install project dependencies.
2. Validate Python formatting using Black.
3. Check code quality using Flake8.
4. Run Django system checks.
5. Run the Django test suite with Coverage.py.
6. Report test coverage to Coveralls.

**Travis CI Dashboard:**

https://app.travis-ci.com/github/VinayKumar2320/swe1-app

**Coveralls Dashboard:**

https://coveralls.io/github/VinayKumar2320/swe1-app

## Project Structure

```text
swe1-app/
├── .ebextensions/
│   └── django.config
├── .flake8
├── .travis.yml
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── polls/
│   ├── migrations/
│   ├── templates/
│   │   └── polls/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md
```

## Running Locally

Clone the repository:

```bash
git clone https://github.com/VinayKumar2320/swe1-app.git
cd swe1-app
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

The root URL redirects to `/polls/`.

## Code Quality and Testing

Check formatting:

```bash
black --check --exclude '/(venv|\.venv|migrations)/' .
```

Run Flake8:

```bash
flake8 .
```

Run Django tests:

```bash
python manage.py test
```

Check code coverage:

```bash
coverage run --source=polls manage.py test
coverage report
```

## Elastic Beanstalk Deployment

The project includes AWS Elastic Beanstalk configuration in:

```text
.ebextensions/django.config
```

The configuration specifies the Django settings module and WSGI application and runs database migrations during deployment.

Manual deployment, once an environment has been configured:

```bash
eb deploy
```

Automatic deployment through Travis CI will be configured to run after successful checks on the `main` branch.

## Django Tutorial

This project implements Parts 1–4 of the official Django tutorial:

- **Part 1:** Project and Polls application setup
- **Part 2:** Database models, migrations, and Django Admin
- **Part 3:** Views, URLs, and templates
- **Part 4:** Forms, voting, generic views, and results

## Author

**Vinay Kumar**  
M.S. Computer Science  
NYU Tandon School of Engineering