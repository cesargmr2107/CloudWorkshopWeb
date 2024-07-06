# CloudWorkshopWeb

## Overview

This repository contains the web application code for a cloud workshop. The project is built using Python and Flask, with HTML, CSS, and other static resources.

## Folder Structure

- `.github`: Contains GitHub-specific configurations.
- `static`: Contains static files like CSS, JavaScript, and images.
- `templates`: Contains HTML templates used by Flask.

## Key Files

- `.gitignore`: Specifies files and directories to be ignored by Git.
- `app.py`: The main Flask application file that defines the web routes and logic.
- `requirements.txt`: Lists Python dependencies required for the project.
- `wsgi.py`: WSGI entry point for deploying the Flask application.

## File Descriptions

- **.github/**
  - GitHub configuration files for CI/CD and other workflows.

- **static/**
  - `css/`: Contains CSS files for styling the web pages.
  - `js/`: Contains JavaScript files for client-side scripting.
  - `images/`: Stores image files used in the web application.

- **templates/**
  - `base.html`: Base template that includes common HTML structure and components.
  - `index.html`: Homepage template.
  - `about.html`: About page template.

- **.gitignore**
  - Ensures that unnecessary files like virtual environments, cache files, and other temporary files are not tracked by 

- **app.py**
  - The core of the Flask application. It initializes the Flask app, defines routes, and contains the logic for handling requests and responses.

- **requirements.txt**
  - Specifies the Python packages needed for the project. These dependencies can be installed using `pip install -r requirements.txt`.

- **wsgi.py**
  - Entry point for the application when deploying using a WSGI server. It ensures that the Flask app is properly loaded and served.

## Usage

To run the web application locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/cesargmr2107/CloudWorkshopWeb.git
   cd CloudWorkshopWeb
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000` to see the application in action.

