# Contact Agenda

This is a contact agenda project developed with Django, as part of Luiz Otávio Miranda's course. The goal of the project is to allow users to register, log in, and manage their contacts easily and efficiently.

## Features

- **Registration and Login**: Users can register and log in to the application.
- **Contact Management**: Users can create, edit, and delete contacts.
- **Contact Information**:
  - First Name
  - Last Name
  - Phone Number
  - Email
  - Contact Photo
- **Search System**: Users can search for contacts by name, phone number, or email.
- **Data Sharing**: All contacts are shared among users who log in.

## Technologies Used

- Django
- Python
- HTML/CSS
- Database (PostgreSQL)
- **Deployment**:
  - **Google Cloud**: The application is hosted on Google Cloud Platform.
  - **Gunicorn**: WSGI server for Python applications.
  - **Nginx**: Web server used to serve the application and manage requests.

## Installation

To run the project locally, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/GustavOxys/Agenda.git

2. Navigate to the project directory:
    ```bash
    cd agenda

3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate  # Para Windows

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt

5.  Apply database migrations:
    ```bash
    python manage.py migrate

6. Start the server:
    ```bash
    python manage.py runserver

7. Access the application at http://127.0.0.1:8000

Contributions
Feel free to fork the project and contribute with improvements!


Acknowledgments
I would like to thank Luiz Otávio Miranda for the excellent course that helped me develop this project.