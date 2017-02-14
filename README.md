# Python
This project is developed on python 3.5 (Please use this or higher)


LOCAL CONFIGURATION

# Run Requirement file
1. pip install -r requirement.txt

# Migrate Data  (Please use existing database in settings.py or create a new database named my_contact_db )
2. python manage.py makemigrations contact_app
3. python manage.py migrate

# Run Python Server
4. python manage.py runserver

# Testing
5. For Testing Data use: curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://localhost:8000/api/v1/contact/

For more query please contact: aliimran.pust@gmail.com


