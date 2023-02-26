# DjangoERP

A complete set of ERP tools built with Django Rest Framework and Vue js

Structural Architecture of the Project
- Everything resides in the core directory
- The apps are named by the following convention `core/apps/crm`, `core/apps/common`, `core/apps/hrm`, `core/apps/fintech` etc
- The frontend code resides in core/frontend and it is separated by app name e.g `frontend/crm`, `frontend/hrm/` etc

High Level Overview of the Backend architecture and the Why?
- I have decided not to go with the ideal MVT architecture of Django.

- Taking inspiration from DDD, I have structured the project into the following :

        domain - where all the domain logic goes.
        
        repo - where all the repository logic goes.
        
        logic - where all the busines logic goes.
        
        handlers - where the usual views and webhooks go.
        
        tests - where the tests go. However, the tests are further broken down by domain/ , repo/, logic/ , handlers/ 
        
- All the Django apps will follow the above structure. This design has been chosen also to separate Infrastructure concerns coupling the code.

- Since, I am designing the architecture with complete freedom, I am going with Pydantic for data validation, serialization and de-serialization instead
of the inbuilt DRF serializers.
        
        - Inspiration was taken from this thread - https://news.ycombinator.com/item?id=24161828

## How processing occurs ?

- On a high level, let's understand the different layers of processing

- User request is routed through the url patterns and hits the right view.

- The correct view function based on the request.method gets the data.

- The data is then handed over to a logic function which is typically the business logic layer.

- The logic then interacts with the repository method and invokes the right repo method.

- Repository interacts with the database and saves or gets the data.

- The data is then returned to the view

Small gotcha ?

 - The view uses something called a use_case_type. What the heck is a use_case_type ? Well, put it this way - Think about if you decide to save the data
 to an external crm e.g hubspot. Then the use_case_type="hubspot" and based on the use_case_type, the `get_repository_for_{entity_name}` will return the 
 right repository. So, technically nothing changes in the view and you can plug external crms to save data or get data easily.
 
 - Additionally, the repository abstracts away all the CRUD logic. So, plugging things in and out without worrying about the Infrastructure is a charm.
 
 

Backend
1. Django Rest Framework
2. Djoser
3. Postgres
4. Django - Filter
5. Swagger
6. Pydantic

Frontend
1. Vue js

How to run the Backend
1. Copy the .env-example to .env file
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py runserver

How to run the Frontend
1. cd core/frontend/crm
2. npm install
3. npm run serve

Project Priorities
1. Human Resource Management - TODO
2. Customer Relationship Management (CRM) - Ongoing
3. Supply Chain Management (SCM) - TODO
4. Inventory Management - TODO
5. Accounting/Financial Management - TODO

