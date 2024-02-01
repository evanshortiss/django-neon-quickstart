# Python, Django, and Neon's Serverless Postgres

_This repository is a companion to a [Python & Django with Neon post](https://neon.tech/blog/python-django-and-neons-serverless-postgres) on the Neon blog._

An example Django application that connects to Neon's serverless Postgres, and uses HTMX for interactions.

![Elements Application in Google Chrome](/images/elements-app.png)

# Usage

## Optional Environment Setup

Follow the [pyenv installation instructions](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) for your OS, then run the following commands to install and use Python 3.12.1:

```bash
# This will list existing python versions on your system
pyenv versions

# Install Python 3.12.1 and set it as the version for this terminal session
pyenv install 3.12.1
pyenv local 3.12.1

# Confirm the python version in use is 3.12.1
python --version
```

Use [venv](https://docs.python.org/3/library/venv.html) in the same shell to create a virtual environment that uses Python 3.12, and use the source command to activate it:

```bash
# This path is an example. You can store the virtual environment wherever you want
python -m venv $HOME/.venv/neon-and-django-env

# Activate the virtual environment in the current shell. Note that fish, powershell,
# and Windows users must use the activate script for their specific shell per
# https://docs.python.org/3/library/venv.html#how-venvs-work 
source $HOME/.venv/neon-and-django-env/bin/activate
```

## Run the Application

### Install Project Dependencies

From the root of the project, run:

```bash
pip install -r requirements.txt
```

### Define Postgres Connection Details

1. Visit [console.neon.tech](https://console.neon.tech/app/projects) and create a new project, or new database in an existing project.
1. Copy the `.env.example` file in root of this repository into a new file named `.env`.
1. Replace the sample values in `.env` with the **Connection Details** from [console.neon.tech](https://console.neon.tech/app/projects) for your chosen database.

### Apply Database Migrations

This will create Django's tables, and tables for the application's Element model.

```bash
python manage.py makemigrations
python manage.py migrate
```

### Start the Application

Prior to starting the application, uise the **SQL Editor** in the Neon Console to add some data to your `elements_element` table:

```sql
INSERT INTO elements_element (name, symbol, atomic_number)
VALUES
('Hydrogen', 'H', 1),
('Helium', 'He', 2),
('Lithium', 'Li', 3),
('Beryllium', 'Be', 4),
('Boron', 'B', 5),
('Carbon', 'C', 6);
```

Start the application in development mode using `python manage.py runserver`, and visit http://localhost:8000 to see a list of elements.

