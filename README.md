# TradexaTask1
Django Web Application with two apps using different databases

Problem : Create an application that has two apps-

Users with User and Post model User : first_name, last_name, email, password, username Post : user, text, created_at, updated_at

Note:- Foreign key relationship exists between User and Post on Model level not on Database level.

Products app with Product model. Product : name, weight, price, created_at, updated_at

Note:- Both of the apps should use two different databases.

-> Create a form that an authenticated user can use to create a post. Note: Register all models on admin dashboard.

--> Admin site: username : 'admin' password : 'admin'

--> Another user username : 'lalkrishna' password : 'lalu1234'

Requirements :
  1. django
  2. pip install django-money
  
  Can be installed via pip
