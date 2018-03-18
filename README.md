# Application to bookmark images from other websites developed using Django framework

## REQUIREMENTS
All application requirements are on requrements.txt.
You can install all at once with the following command `pip install -r requirements.txt`

## CACHING
I did use Redis 4.0.8 as caching database running on port 6379.
You will not be able to run this application without redis

## Fist launch
1. Create a super user to access database
  `python manage.py createsuperuser`

2. Lauch a local server
  `python manage.py runserver`

3. Visit `120.0.0.1:8000/account` to access user dashboard
