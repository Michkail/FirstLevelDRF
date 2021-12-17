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
        |__ job_slurp
        |    |__ __pycache__
        |    |    |__ __init__.cpython-39.pyc
        |    |    |__ settings.cpython-39.pyc
        |    |    |__ urls.cpython-39.pyc
        |    |    |__ wsgi.cpython-39.pyc
        |    |  
        |    |__ __init__.py
        |    |__ settings.py
        |    |__ urls.py
        |    |__ wsgi.py
        |
        |__ slurp
        |    |__ __pycache__
        |    |    |__ __init__.cpython-39.pyc
        |    |    |__ admin.cpython-39.pyc
        |    |    |__ models.cpython-39.pyc
        |    |    
        |    |__ migrations
        |    |    |__ __pycache__
        |    |    |    |__ __init__.cpython-39.pyc
        |    |    |    |__ 0001_initial.cpython-39.pyc
        |    |    |
        |    |    |__ __init__.py
        |    |    |__ 0001_initial.py
        |    |
        |    |__ __init__.py
        |    |__ admin.py
        |    |__ apps.py
        |    |__ models.py
        |    |__ tests.py
        |    |__ views.py
        |
        |__ manage.py       
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