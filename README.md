# Dash-Template

Good practice Dash-Template

## Install and Setup

Create a virtual environment, install requirements and run the app:

```bash
# On Windows
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
python src\app.py

# On Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 src\app.py
```

## Structure

This repository serves as a guide for structuring large Dash applications.

```bash
dash-template structure
|-- .venv
|   |-- *
|-- requirements.txt
|-- .env
|-- .gitignore
|-- License
|-- README.md
|-- src
|   |-- assets
|   |   |-- logos/
|   |   |-- css/
|   |   |-- images/
|   |   |-- scripts/
|   |   |-- favicon.ico
|   |-- components
|   |   |-- __init__.py
|   |   |-- footer.py
|   |   |-- navbar.py
|   |   |-- login.py
|   |-- pages
|   |   |-- __init__.py
|   |   |-- complex_page
|   |   |   |-- __init__.py
|   |   |   |-- layout.py
|   |   |   |-- comp1.py
|   |   |-- home.py
|   |   |-- 404.py
|   |   |-- login.py
|   |   |-- logout.py
|   |   |-- page2.py
|   |-- app.py
|   |-- gunicorn_config.py
|   |-- settings.py
```

## Virtual Environment

The `.venv` directory is the virtual environment itself where the project specific Python package versions are located.
There are various ways and modules to create a virtual python environment nowadays.
Note that `.venv` is a common name to use for your virtual environment.
The `requirements.txt` file contains the required Python packages and their respective versions for running the application.

## Environment Variables

The `.env` file is where you should house any passwords or keys.
This is a common practice as we do not want to directly hardcode keys into your application where a malicious actor could see them.
Some common values found in `.env` files are `DATABASE_URI` or `API_KEY`.
Later on we will see how the data is loaded into our scripts.

## .gitignore

The `.gitignore` file is essential when using git.
If you aren't using git, you can ignore this. However, you should be using git or some other Version Control System.
The `.gitignore` file specifies files or directories which should not be included when you commit or push your code.

I use the basic Python `.gitignore` file, located at [https://github.com/github/gitignore/blob/main/Python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore).
Notice that both the `.venv` directory and `.env` file are included here.

## License

The `LICENSE` file determines how your code should be shared.
If you are keeping your code completely private, you do not need a license; however, you should still include one.

For more inforamtion on choosing the correct license, see [https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).

## README

The `README.md` file should specify how to install and run your application.
This includes, but is not limited to, installing packages, mentioning which environemnt variables need to be set, and running the application.

## src

The `src` directory is where to house all of the code.
We will dive into each item below.

### Assets

The assets directory contains css files, javascript files, locally hosted images, site logos, and the application icon.
These should be organized into folders based on their purpose.

### Components

The components directory should contain common components used throughout the application.
The dash-template contains the navigation `navbar.py` and the footer element `footer.py`.
All-in-one components should also be stored here.
Defining each of these components in their own file is good practice.
Additionally, I import each component into the `__init__.py` file.
This allows for easier imports like the following:

```python
from components import navbar, footer
```

### Pages

Large structured applications rely on the Dash Pages feature, published with Dash 2.5.

The pages directory houses the individual pages of your application.
I split the pages into 2 categories, static and complex pages.
The static pages are ones that do not have any or minimal callbacks, such as your home, privacy policy, about, 404 or contact page.
The complex pages are ones that contain more complex layouts and callbacks.

The static pages should be included immediately under the pages directory.
While the complex pages should be included in their own directory inside the pages.

See the files within the `complex_page` directory and the pages forum post for more information about how to structure more complex pages.

### App

The `app.py` file is the entrypoint to defining and running the application.
This is where we define the Dash app, set external stylesheets and run the app.

As it stands, Dash requires the `app` object for defining `long_callbacks`.
Since this is the only place in the codebase that can access the app object, without ciruclar imports, this file should house any `long_callbacks`.

### Settings
In the `settings.py` file we store essential constants and variables with their default value and override them with the values stored in the `.env` file. 

We can import the `settings.py` file with their variables anywhere in our project to get the desired values.
