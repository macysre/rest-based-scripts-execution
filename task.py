import subprocess

def run_script(script_name, scripts_dict):
    try:
        script_path = scripts_dict[script_name]['location']
        print("Running script : "+script_path)
        res = subprocess.run([script_path], stdout = subprocess.PIPE)
        res_str = res.stdout.decode('utf-8')
        scripts_dict[script_name]['status'] = "Completed"
        scripts_dict[script_name]['output'] = res_str
        print("Running script : "+script_path+" execution completed")
    except:
        scripts_dict[script_name]['status'] = "Completed"