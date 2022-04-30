# expiryDateManager
Backend intern developer test for CodaBene

## To build and run the app locally (linux)
Install [postgresql](https://www.postgresql.org/download/)

#### Create and setup the database
> sudo -u postgres psql
> 
> CREATE DATABASE expiracydate;
> 
> CREATE USER codabene WITH PASSWORD 'codabene';
> 
> ALTER ROLE utilisateur SET client_encoding To 'utf8';
> 
> ALTER ROLE codabene SET default_transaction_isolation TO 'read committed';
> 
> ALTER ROLE codabene SET timezone TO 'Europe/Paris';
> 
> GRANT ALL PRIVILEGES ON DATABASE projet TO utilisateur;
> 

#### Install django
> pip install django

or

> python3 -m pip install django

#### Run the project

Go in expiryDateManager/expiryDateManager

python manage.py migrate

python manage.py runserver
