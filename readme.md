About this app
=============
I created an app in django in order to replace [This ](http://projects.cs.unipi.gr/OTE-museum-ugrads/)

installation
-------------
`pip install -r requirements.txt`

then create the database (its sqlite)
with:
`./manage.py syncdb`

collect the static directories with:
`./manage.py collectstatic`
(i include a small css file just for fun)

finally run the developement server:
`./manage.py runserver`

You can visite the app in your browser at:
[localhost:8000 ](http://localhost:8000 )


