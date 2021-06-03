from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import subprocess, os, stat
import threading
from task import run_script

app = Flask(__name__)
api = Api(app)

scripts = {}

f = open('state_file.json', 'w')

class ScriptTask(Resource):
    def get(self, script_name):
        if script_name in scripts:
            return {'status': scripts[script_name]['status']}
        else:
            return {'status': 'script not found'}, 400
    
    def post(self, script_name):
        script = request.get_data()
        script_path = "scripts/"+script_name+".sh"
        scripts[script_name] = {"location": script_path, "status": "NotScheduled", "output": ""}
        with open(script_path, 'w') as fh:
            fh.write(script.decode('utf-8'))
        os.chmod(script_path, stat.S_IRWXU)
        return {'status': 'Script has been created successfully'}, 201
    
    def put(self, script_name):
        if script_name in scripts:
            script = scripts[script_name]['location']
            if scripts[script_name]['status'] == "Scheduled" or scripts[script_name]['status'] == "Running":
                return {'Status': 'Script has been '+scripts[script_name]['status']}, 500
            else:
                scripts[script_name]['output'] = ""
                x = threading.Thread(target = run_script, args=(script_name, scripts, ) )
                x.start()
                scripts[script_name]['status'] = "Running"
                return {'status': 'Script scheduled for execution'}
        else:
            return {'status': 'Script not founds'}, 400

class ScriptsList(Resource):
    def get(self):
        return jsonify(scripts)

# Script output 
class ScriptsOutput(Resource):
    def get(self, script_name):
        if script_name in scripts:
            return {'output': scripts[script_name]['output']}
        else:
            return {'status': "Script doesn't exists"}, 400


api.add_resource(ScriptsList, '/')
api.add_resource(ScriptTask, '/script/<string:script_name>')
api.add_resource(ScriptsOutput, '/script/output/<string:script_name>')

# if __name__ == '__main__':
#     app.run()