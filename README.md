# Getting Started
Flask RestFul service to run shell scripts that are defined and provided by user through REST APIs. This service exposes multiple REST endpoints to clients/users to perform below operations.

1. Clients/Users should be able to submit shell script with name
2. Clients/Users should be able to schedule shell scription for execution with script name
3. Clients/Users should be able to query script status
4. Clients/Users should be able to see script output
5. Clients/Users should be able to see all scripts, statuses and outputs

# Technical Design Details
> This service created with Python Flash framework, and using *dictionary* to store scripts details, status and scripts execution outputs as in-memory. Using threads to schedule tasks (script execution) whenever users/client make *PUT* request to schedule scripts for execution.

User inputed scripts will be created under "scripts" directory with executable permissions.

# Execution Steps
*Prerequisites* : Python3

1. Clone git repository

2. Create Virtual Environment
```sh
   python3 -m venv venv
```

3. Activate Environment
```sh
   python3 venv/bin/activate
```

4. Install flask and flask-restuful modules
```sh
   pip3 install -r requirements.txt
```
5. Run flask app
```sh
   python3 app.py   
```

App will be running and you will see below message.

```sh
* Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

# Usage

1. Create Script with curl
Url: `http://127.0.0.1:5000/script/<script_name> `
Method: `POST`
Payload: `#!/bin/bash\necho "Hello World!"`

```sh
curl -d $'#!/bin/bash\necho "Hello"' -X POST http://127.0.0.1:5000/script/helloscript
```

2. Schedule Script for execution
Url: `http://127.0.0.1:5000/script/<script_name> `
Method: `PUT`

```sh
curl -X PUT http://127.0.0.1:5000/script/helloscript
```

3. Get status of script
Url: `http://127.0.0.1:5000/script/<script_name> `
Method: `GET`

```sh
curl -X GET http://127.0.0.1:5000/script/helloscript
```

4. Get output of script
Url: `http://127.0.0.1:5000/script/output/<script_name> `
Method: `GET`

```sh
curl -X GET http://127.0.0.1:5000/script/output/helloscript
```

5. Get all scripts
Url: `http://127.0.0.1:5000/`
Method: `GET`

```sh
curl -X GET http://127.0.0.1:5000/
```

# How to run test cases
```sh
python3 test_remote_scripts.py
```
