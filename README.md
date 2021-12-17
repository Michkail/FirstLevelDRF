# FirstLevelDRF
```
The test consists in creating a Web API Project for a JobBoard website. Similar to indeed.com, companies will be able to create and publish new job offers that people will then be able to see.
```

##  Client will be able to communicate with our Web API from 2 URL Endpoints:
```
1.  api/slurp/ - accepts GET and POST methods,
    allowing to create new instances and retrieve a list with all the available job offer instances.

2   api/slurp/<int:pk>/ - accepts GET, PUT and
    DELETE, allowing a user to retrieve, update or delete an object instance.
```

## Folder Structure
```
    FirstLevelDRF
        |_____/job_slurp
        |        |_____ __pycache__
        |        |        |_____ __init__.cpython-39.pyc
        |        |        |_____ settings.cpython-39.pyc
        |        |        |_____ urls.cpython-39.pyc
        |        |        |_____ wsgi.cpython-39.pyc
        |        |  
        |        |_____ __init__.py
        |        |_____ settings.py
        |        |_____ urls.py
        |        |_____ wsgi.py
        |
        |_____ slurp
        |        |_____ __pycache__
        |        |        |_____ __init__.cpython-39.pyc
        |        |        |_____ admin.cpython-39.pyc
        |        |        |_____ models.cpython-39.pyc
        |        |    
        |        |_____ migrations
        |        |        |_____ __pycache__
        |        |        |        |_____ __init__.cpython-39.pyc
        |        |        |        |_____ 0001_initial.cpython-39.pyc
        |        |        |
        |        |        |_____ __init__.py
        |        |        |_____ 0001_initial.py
        |        |
        |        |_____ __init__.py
        |        |_____ admin.py
        |        |_____ apps.py
        |        |_____ models.py
        |        |_____ tests.py
        |        |_____ views.py
        |
        |_____ manage.py       
```

## Only one model is needed for the project, you can call it SlurpOffer. It must have the following fields:
```
♬  company_name  
♫  company_email  
♩  job_title
♪  job_description
♬  fee  
♫  city  
♩  created_at
♪  available
```