# Django Polls Application

A Django web application based on the official Django Polls tutorial (Parts 1–4), deployed to AWS using Elastic Beanstalk.

## Live Application

**AWS Elastic Beanstalk Deployment**

http://swe1-app-env.eba-xnafp89x.us-east-2.elasticbeanstalk.com/

The root URL automatically redirects to the Polls application.

## Features

- View available polls
- View poll questions and choices
- Submit votes
- Display voting results
- Vote multiple times
- Django Admin integration
- Django template-based frontend
- SQLite database
- Automatic database migrations during deployment
- Sample poll data created through a Django data migration
- AWS Elastic Beanstalk deployment

## Technologies

- Python 3.14
- Django 6.1.1
- SQLite
- Gunicorn
- AWS Elastic Beanstalk
- Amazon EC2
- Git
- GitHub

## Project Structure

```text
swe1-app/
├── .ebextensions/
│   └── django.config
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

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run database migrations:

```bash
python manage.py migrate
```

Start the Django development server:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

The root URL redirects to `/polls/`.

## Elastic Beanstalk Deployment

The project is configured for AWS Elastic Beanstalk through:

```text
.ebextensions/django.config
```

The configuration specifies the Django settings module and WSGI application and automatically runs database migrations during deployment.

The application is deployed using:

```bash
eb deploy
```

## Django Tutorial

This project implements the core functionality covered in Parts 1–4 of the official Django tutorial:

- **Part 1:** Project and Polls application setup
- **Part 2:** Database models, migrations, and Django Admin
- **Part 3:** Views, URLs, and templates
- **Part 4:** Forms, voting, generic views, and results

## Author

**Vinay Kumar**  
M.S. Computer Science  
NYU Tandon School of Engineering
