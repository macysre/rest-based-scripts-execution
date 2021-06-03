# Getting Started
Flask RestFul service to run shell scripts that are defined and provided by user through REST APIs. This service exposes multiple REST endpoints to clients/users to perform below operations.

1. Clients/Users should be able to submit shell script with name
2. Clients/Users should be able to schedule shell scription for execution with script name
3. Clients/Users should be able to query script status
4. Clients/Users should be able to see script output
5. Clients/Users should be able to see all scripts, statuses and outputs

# Technical Design Details
> This service created with Python Flash framework, and using *dictionary* to store scripts details, status and scripts execution output. Tasks are scheduling with threads upon users/client make *PUT* request to schedule scripts for execution.

User providing scripts will be created under "scripts" directory with <script_name>.sh with executable permissions.

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
   python3 -m flask run  
```

If app running successfully, you will see below message.

```sh
* Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```


# Usage

1. Create Script with curl<br/>
Url: `http://127.0.0.1:5000/script/{script_name} `<br/>
Method: `POST`
Payload: `#!/bin/bash\necho "Hello World!"`

```sh
curl -d $'#!/bin/bash\necho "Hello"' -X POST http://127.0.0.1:5000/script/helloscript
```

### Postman Code

```sh
POST /script/script1 HTTP/1.1
Host: 127.0.0.1:5000
Cache-Control: no-cache
Postman-Token: 49f181cd-af3e-55a7-c47c-748c6d3e86ef

#!/bin/bash
echo "Hello World!"
for i in {1..10}; do
  echo $i
  sleep 2
 done
```

2. Schedule Script for execution <br/>
Url: `http://127.0.0.1:5000/script/{script_name} `<br/>
Method: `PUT`

```sh
curl -X PUT http://127.0.0.1:5000/script/helloscript
```

3. Get status of script<br/>
Url: `http://127.0.0.1:5000/script/<script_name> `<br/>
Method: `GET`

```sh
curl -X GET http://127.0.0.1:5000/script/helloscript
```

4. Get output of script<br/>
Url: `http://127.0.0.1:5000/script/output/{script_name} `<br/>
Method: `GET`

```sh
curl -X GET http://127.0.0.1:5000/script/output/helloscript
```

5. Get all scripts<br/>
Url: `http://127.0.0.1:5000/`\n
Method: `GET`

```sh
curl -X GET http://127.0.0.1:5000/
```

# How to run test cases
```sh
python3 test_remote_scripts.py
```


# Docker Build and Run
1. Build Image locally
```sh
    docker build . -t flask-rest-api:1.0
```

2. Run container
```sh
    docker run -d -p 5000:5000 flask-rest-api:1.0
```
