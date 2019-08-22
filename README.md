
# BBQ Planner App
Barbeque event organizer app. Register or login to create new events or view event details. Add types of meat to your event and optain the link to send to friends who can use this to register.

## Requirements
* Git
* Pip / Pipenv
* Python 3
* Docker

## Development

### Clone Repository
1. clone repository `git clone https://github.com/Schayik/bbq`
2. move to directory `cd bbq`

### Without Docker
1. install dependencies* `pipenv install`
2. start virtual env `pipenv shell`
3. migrate database `python manage.py migrate`
4. run dev server `./manage.py runserver`
5. create super user `python manage.py createsuperuser` (optional)
2. visit in browser `localhost:8000`, admin: `localhost:8000/admin`

*note: if pipenv isn't installed: install first `pip install pipenv`

### With Docker
1. start host `docker-machine start`
2. build server* `docker-compose build`
3. start server `docker-compose up -d`
4. run migrations `docker-compose exec web python manage.py migrate`
5. create super user `docker-compose exec web python manage.py createsuperuser` (optional)
6. visit in browser** `<ip>:8000`, admin: `<ip>:8000/admin`

*note: I had to run `docker-machine env --shell=powershell | Invoke-Expression` after this command to be able to build.
**note: get ip with `docker-machine ip`, you might have to add this ip to ALLOWED_HOSTS in the bbq/settings.py file.

## Schema
* User: Django's User model will do for Organizers.
* Event: id, user_id, title, datetime
* Visitor: id, event_id, name, number_of_extra_guests
* Meat: id, event_id, type
* Quantity: id, meat_id, visitor_id, quantity

## Functional Requirements
**Creating a BBQ event**
* A BBQ event organizer needs to be able to register and login
* Create a new BBQ event
* Be able to set a date for a BBQ event
* Be able to register types of meat you want to serve during the BBQ
* Each BBQ event has a public link, which you can share with your friends to let them register for the event

**BBQ event visitors**
* Can register for an event without an account using the public shared link of the BBQ event organizer
* When registering, the visitor needs to enter his name.
* When registering, the visitor can select how many guests he will bring.
* When registering, the visitor can select how many types of which meat he wants. The list of meat shown is configured by the BBQ organizer.

**BBQ event summary / shopping list**  
A logged in BBQ event organizer can an overview of his BBQ events.  
Per BBQ event, the organizer sees:
* How many people have registered in total (sum of visitors + guests).
* Per type of meat, how many people would like a piece
* List of all the names of visitors who have registered