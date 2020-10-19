IQVIA
===================================

Description
-----------------

This repository contains Flask API that determines whether given disease had activity or not for a given number of days for given RSS feeds from ClinicalTrials.gov

Technical stack used :
-----------------
- Docker
- Python
- Flask

Getting Started
-----------------
Clone the repository to local machine for development and testing.
```  
git clone [`https://github.com/chintanmodi36/iqvia_assessment.git`]https://github.com/chintanmodi36/iqvia_assessment.git
```

##Commands to setup and run the application
## Prerequisites
Create virtual environment for Flask API 

###Create and activate virtual environment
```
virtualenv -p python3 venv
source venv/bin/activate
```
###Docker
## Run command
```
docker-compose up
```
Now the activities should be visible in the browser at
[`http://0.0.0.0:5000/`](http://0.0.0.0:5000/).

Modify URL like 
[`http://0.0.0.0:5000/disease_name/number_of_days`](http://0.0.0.0:5000/disease_name/number_of_days/).
   
## Config Test
A reusable test has been prepared to make assertions on the application 
## Test Execution
Test the application by running the command on Terminal 
## Testing flask application by running the createed test cases
```
python -m unittest test_app.py
```
