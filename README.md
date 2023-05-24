# Blogify Backend

This is the Django backend for the Blogify web app. All apps are located in the `siteapps` directory.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mulfranck/blogify.git
    ```

2. Install the dependencies:

    Install dependencies using pipenv:

    ```bash
    cd backend
    pipenv shell
    pipenv install
    ```

3. Run migrations:

   ```bash
   python manage.py makemigrations <modelFilename>
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

Once the development server is running, you can access the API at `http://localhost:8000/api/v1/`.
You can access the documentations at `http://localhost:8000/`

## Contributing
