EMBL-EBI test
==============================



What Is This?
-------------

This is a simple Python/Falcon application intended to provide a working example of searching EMBL database <b>ensembl_website_97</b>. 


How To start the API service using docker
---------------
Run the following commands 
1. docker-compose build
2. docker-compose up

The service will start to listen on port <b>80</b>

Testing
-------

1. Login to the `app_server` docker container 
2. Run the command `python -m unittest test/api_test.py`


Making Requests
---------------

Please go to `http://localhost:80/swagger` to find more about the API documentation. 