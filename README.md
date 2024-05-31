# Resume Portfolio Website

This website, built with Django and hosted on PythonAnywhere, showcases my educational background, work experiences, and personal projects. It's a simple, direct way to share my journey and skills with potential employers or anyone interested in my professional path.

Link to website: https://www.fredriknystrom.tech/

## Technology Stack

- **Front-End:** HTML, CSS (custom and Bootstrapv5), JavaScript
- **Back-End:** Django (Python-based web framework) is on the server-side
- **Libraries & Plugins:** jQuery, Font Awesome icons and Google Fonts

## Django Local Development Guide

1. **Activate Your Virtual Environment** 
   - Activate venv on macOS/Linux: `source venv/bin/activate`

2. **Database Migrations**
   - Django uses migrations to propagate changes you make to your models (adding a field, deleting a model, etc.) into your database schema.
   - **Create Migrations**:
     ```
     python3 manage.py makemigrations
     ```
     This command looks for changes to your models and creates new migrations based on those changes.
   - **Apply Migrations**:
     ```
     python3 manage.py migrate
     ```
     This command applies the migrations to your database, updating the database schema.

3. **Running the Development Server**
   - Django comes with a built-in development server that lets you test your app locally.
   - Start the server with:
     ```
     python3 manage.py runserver
     ```
   - By default, the server runs on port 8000. You can access your app by going to `http://127.0.0.1:8000/` in your web browser.
   - If you want to run the server on a different port, you can specify it by adding the port number at the end of the command, e.g., `python3 manage.py runserver 8080`.

## Other Development Commands

- **Creating a Superuser**
  - To access the Django admin site, you'll need to create a superuser account.
  - Create a superuser with:
    ```
    python3 manage.py createsuperuser
    ```
  - Follow the prompts to set up the username, email, and password.

- **Accessing Database**
  - One can easily check the current state of the database and try raw sql commands on it. 
  - Run the dbshell command:
    ```
    python3 manage.py dbshell
    ```

- **Checking for Problems**
  - Django can check for problems in your project without making database migrations or starting the server.
  - Run the check command:
    ```
    python3 manage.py check
    ```

- **Collecting Static Files**
  - If your app uses static files (CSS, JavaScript, images), Django can collect all of these into a single directory.
  - Collect static files with:
    ```
    python3 manage.py collectstatic
    ```

- **Adding Social Providers**
  - How to add providers so that users can login and be able to take part of personalized usage of apps. 
  - Log in with superuser and go to admin view.
  - Add the domain name and display name under sites.
  - One can see the site ID when editing a site in the url, eg: http://127.0.0.1:8000/admin/sites/site/2/change/
  - Add the SITE_ID in the settings.py file. Use .env (dot-env) file to prepare for production.
  - Also add the new prodiver under the installed apps in settings.py, eg for github: 'allauth.socialaccount.providers.github'
  - Now back to the django admin page and click add Social Application. If everything is set up the new provider should be available in the dropdown menu.
  - Now just fill in the Client_ID and Secret Key from the provider (this you have to get for each provider) and link to the site where the authentication should be applied.

## PythonAnywhere Deployment Guide

1. **Save Local Changes**
   - Before pulling new changes stash local settings file:
     ```
     git stash save "stash message"
     ```

2. **Pull Latest Changes**
     ```
     git pull
     ```

3. **Reapply Saved Changes**
   - If stashed changes (step 1), now reapply them with:
     ```
     git stash pop
     ```

4. **Activate Your Virtual Environment**
   - To activate virtual environment on server use:
     ```
     workon venv
     ```

5. **Database Migrations**
   - Django uses migrations to propagate changes you make to your models (adding a field, deleting a model, etc.) into your database schema.
   - **Create Migrations**:
     ```
     python3 manage.py makemigrations
     ```
     This command looks for changes to your models and creates new migrations based on those changes.
   - **Apply Migrations**:
     ```
     python3 manage.py migrate
     ```
     This command applies the migrations to your database, updating the database schema.

6. **Collect Static Files on the Server**
   - Django manages static files (CSS, JavaScript, images) separately from your dynamic content. To apply changes to static files on live site, run:
     ```
     python3 manage.py collectstatic
     ```
