import unittest
import json, time
from app import app

class ScriptsExecutionTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.payload = '''
            echo 'hello'
            sleep 2
            echo "sleep"
            sleep 3
            '''
        self.script_name = "hello"
    
    def test_get_script_list(self):
        response = self.client.get('/')
        expected_resp = {} 
        self.assertEqual(response.status_code, 200)

    def test_create_script(self):
        expected_res = {'status': 'Script has been created successfully'} 
        response = self.client.post('/script/'+self.script_name, data=self.payload)
        self.assertEqual(response.status_code, 201)
        self.assertDictEqual(response.get_json(), expected_res)

    def test_trigger_script(self):
        expected_res = {'status': 'Script scheduled for execution'} 
        response = self.client.put('/script/'+self.script_name)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.get_json(), expected_res)
    
    def test_script_exe_status(self):
        time.sleep(1)
        expected_res = {'status': 'NotScheduled'}
        response = self.client.get('/script/'+self.script_name)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.get_json(), expected_res)

    def test_script_exe_status_with_nonexisting_script(self):
        time.sleep(1)
        expected_res = {'status': 'NotScheduled'}
        response = self.client.get('/script/test1')
        self.assertEqual(response.status_code, 400)
    
    def test_script_output(self):
        expected_res = {'output': ''}
        response = self.client.get('/script/output/'+self.script_name)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.get_json(), expected_res)
        

    def tearDown(self) -> None:
        return super().tearDown()

    

if __name__ == "__main__":
    unittest.main()