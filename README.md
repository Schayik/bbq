
## BBQ
Barbeque event organizer app.

### Requirements
* Python 3
* Git
* Pipenv

### Development
1. clone repository `git clone ...`
2. move to directory `cd bbq`
3. install dependencies `pipenv install`
4. migrate database `python manage.py migrate`
5. run dev server `python manage,py runserver`

### Schema
* User: Django's User model will do for Organizers.
* Event: id, user_id, date, link?
* Visitor: id, event_id, name, number_of_extra_guests
* Meat: id, event_id, type
* Quantity: id, meat_id, visitor_id, quantity
