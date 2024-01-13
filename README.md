House rental management system
---
1. Open terminal and Clone Project from github
   ```sh
      git clone https://github.com/shakiill/house-rental.git
   ```
2. Enter project directory
      ```sh
    cd house-rental
    ```
3. Create virtualenv
      ```sh
    $ virtualenv venv
    ```
4. Activate Virtualenv
   ```sh
    $ source venv/Scripts/activate
    ```
5. Install Requirements
   ```sh
    $ pip install -r requirements.txt
    ```
6. Add project specific information in .env

7. Make migration
    ```sh
    $ python manage.py makemigrations
    ```
8. Migrate
    ```sh
    $ python manage.py migrate
    ```
9. Create Superuser
    ```sh
    $ python manage.py createsuperuser
    ```
9. Start Server
    ```sh
    $ python manage.py runserver
    ```
