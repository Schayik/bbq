
## BBQ
Barbeque event organizer app.

### Requirements
* Python 3
* Git
* Pipenv
* Docker

### Development
1. clone repository `git clone https://github.com/Schayik/bbq`
2. move to directory `cd bbq`
3. install dependencies `pipenv install`
4. migrate database `python manage.py migrate`
5. run dev server `python manage.py runserver`
6. visit in browser `localhost:8000`

### Dev with Docker
1. clone repository `git clone https://github.com/Schayik/bbq`
2. move to directory `cd bbq`
3. start host* `docker-machine start`
4. get ip address `docker-machine ip`
5. build server `docker-compose build`
6. run migrations `docker-compose run web python manage.py migrate`
7. start server `docker-compose up`
8. visit in browser** `<ip>:8000`

*note: I had to run `docker-machine env --shell=powershell | Invoke-Expression` after this command to be able to build.
**note: you might have to add the host to ALLOWED_HOSTS is the bbq/settings.py file.

### Schema
* User: Django's User model will do for Organizers.
* Event: id, user_id, date, link?
* Visitor: id, event_id, name, number_of_extra_guests
* Meat: id, event_id, type
* Quantity: id, meat_id, visitor_id, quantity

### Functional Requirements
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