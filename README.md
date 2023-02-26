# DjangoERP

A complete set of ERP tools built with Django Rest Framework and Vue js

Structural Architecture of the Project
- Everything resides in the core directory
- The apps are named by the following convention core/apps/crm, core/apps/common, core/apps/hrm, core/apps/fintech etc
- The frontend code resides in core/frontend and it is separated by app name e.g frontend/crm, frontend/hrm/ etc

High Level Overview of the Backend architecture and the Why?
- I have decided not to go with the ideal MVT architecture of Django.

- Taking inspiration from DDD, I have structured the project into the following :
        1. domain - where all the domain logic goes.
        2. repo - where all the repository logic goes.
        3. logic - where all the busines logic goes.
        4. handlers - where the usual views and webhooks go.
        5. tests - where the tests go. However, the tests are further broken down by domain/ , repo/, logic/ , handlers/ 
        
- All the Django apps will follow the above structure. This design has been chosen also to separate Infrastructure concerns coupling the code.
        

## Backend
1. Django Rest Framework
2. Djoser
3. Postgres
4. Django - Filter
5. Swagger

### Frontend
1. Vue js

#### How to run the Backend
1. Copy the .env-example to .env file
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py runserver

##### How to run the Frontend
1. cd core/frontend/crm
2. npm install
3. npm run serve

###### Project Priorities
1. Human Resources - TODO
2. Customer Relationship Management (CRM) - Ongoing
3. Supply Chain Management (SCM) - TODO
4. Inventory Management - TODO
5. Accounting/Financial Management - TODO

