# BELL

## how to run the amazing creation for services and service requests

**1)** cd bell
**2)** pip install -r requirements.txt
**3)** on the command line, run "python manage.py makemigrations" 
**4)** on the command line, run "python manage.py migrate" 
**5)** on the command line, run "python manage.py runserver" 
**6)** should be on localhost:8000 -- enjoy

## routes
- /admin | django admin portal
- / | splash page, explanation of product
- /login | login, signup page
- /profile/< username > | username's profile page with their bells and rings
- /random | random fact and random post

## design considerations, code structure 
- created two different types of Posts: Bells and Rings 
- allowed users to delete their own posts when they feel they no longer need it
- users can comment on every post and work things out 
