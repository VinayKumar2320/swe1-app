# Django Polls Application

[![Build Status](https://app.travis-ci.com/VinayKumar2320/swe1-app.svg?branch=main)](https://app.travis-ci.com/github/VinayKumar2320/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/VinayKumar2320/swe1-app/badge.svg?branch=main)](https://coveralls.io/github/VinayKumar2320/swe1-app?branch=main)

A Django web application based on the official Django Polls tutorial (Parts 1–4), extended with automated testing, code quality checks, and a CI/CD pipeline using Travis CI and AWS Elastic Beanstalk.

The application allows users to browse polls, submit votes, and view results. The project also demonstrates how pull request validation, automated testing, and cloud deployment can be integrated into a Django development workflow.

## Live Application

**AWS Elastic Beanstalk Deployment:**

http://swe1-app-env.eba-idxvzdiu.us-east-2.elasticbeanstalk.com/polls/

**Project Links:**

- [GitHub Repository](https://github.com/VinayKumar2320/swe1-app)
- [Travis CI Dashboard](https://app.travis-ci.com/github/VinayKumar2320/swe1-app)
- [Coveralls Dashboard](https://coveralls.io/github/VinayKumar2320/swe1-app)
- [GitHub Pull Request Checks](https://github.com/VinayKumar2320/swe1-app/pull/3/checks)

## Features

- View available polls and their questions
- Select choices and submit votes
- View voting results and vote counts
- Django Admin integration
- Django template-based frontend
- SQLite database
- Database migrations during deployment
- Sample poll data created through a Django data migration
- Automated formatting and linting checks
- Automated Django tests and coverage reporting
- Travis CI integration with GitHub pull requests
- Automatic deployment to AWS Elastic Beanstalk after successful builds on `main`

## Technologies

- Python and Django
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

## Continuous Integration and Deployment

Travis CI is configured to run automatically when changes are pushed to GitHub or a pull request is opened.

The `.travis.yml` configuration performs the following steps:

1. Install project dependencies.
2. Check Python formatting using Black.
3. Run Flake8 to detect code quality issues.
4. Run Django system checks.
5. Execute the Django test suite with Coverage.py.
6. Send coverage results to Coveralls.
7. Deploy to AWS Elastic Beanstalk after a successful build on the `main` branch.

If a formatting check, linting check, or automated test fails, Travis CI marks the build as failed.

GitHub branch protection requires the Travis CI status check before changes can be merged into `main`.

### CI/CD Workflow

```text
GitHub Push / Pull Request
           |
           v
       Travis CI
           |
           v
     Black + Flake8
           |
           v
   Django System Checks
           |
           v
     Automated Tests
           |
           v
   Coverage + Coveralls
           |
           v
     Build Successful?
        /       \
       No       Yes
       |         |
       v         v
     Failed   Main Branch?
                 |
          Yes -> AWS EB
                 |
                 v
          App Deployed
```

Deployments use AWS credentials stored securely in Travis CI environment variables rather than hardcoded in the repository.

## Code Quality and Testing

The project includes 18 automated Django tests covering the polling application.

**Latest verified CI results:**

| Check | Result |
|---|---|
| Django Tests | 18 passed |
| Test Coverage | 100% |
| Black | Passed |
| Flake8 | Passed |
| Django System Checks | Passed |
| Travis CI Build | Passed |
| AWS Deployment | Successful |

### Run Checks Locally

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

Set the Django secret key for local development:

```bash
export DJANGO_SECRET_KEY="your-local-development-secret"
```

Run database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/polls/ in your browser.

The root URL redirects to `/polls/`.

## AWS Elastic Beanstalk Deployment

The Django application is deployed to AWS Elastic Beanstalk in the `us-east-2` region.

**Deployment Configuration:**

```text
.ebextensions/django.config
```

The configuration specifies the Django WSGI application, runs database migrations, and handles the SQLite permissions required by the deployed application.

**AWS Environment Details:**

| Setting | Value |
|---|---|
| Application | swe1-app |
| Environment | swe1-app-env |
| Region | us-east-2 |
| Platform | Python on Amazon Linux 2023 |
| Instance | t3.micro |
| Deployment | Travis CI |

After the Travis CI checks pass on the `main` branch, the pipeline automatically deploys the updated application to Elastic Beanstalk.

The current deployment uses SQLite at `/tmp/db.sqlite3`. This is sufficient for the assignment, but the database is temporary and may be reset when the instance is replaced. A persistent database would be required for production use.

## Django Tutorial

This project implements Parts 1–4 of the official Django tutorial:

- **Part 1:** Project and Polls application setup
- **Part 2:** Database models, migrations, and Django Admin
- **Part 3:** Views, URLs, and templates
- **Part 4:** Forms, voting, generic views, and results

## What I Learned

This project helped me understand how continuous integration and deployment work in practice.

I worked on configuring Travis CI checks for pull requests, integrating code formatting and linting tools, and deploying a Django application to AWS Elastic Beanstalk.

During deployment, I also worked through AWS IAM permission issues, WSGI configuration problems, and SQLite file permission errors. Resolving these helped me better understand how a Django application behaves outside a local development environment.

## Author

**Vinay Kumar**  
M.S. Computer Science  
NYU Tandon School of Engineering

[GitHub](https://github.com/VinayKumar2320)