
from flask import Flask 
import json, unittest



app = Flask(__name__)

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.test_client = app.test_client() 
        self.request_data = {
            "id":1,
            "fullname":"nazirini",
            "email":"hansu@gmail.com",
            "phone":"536780",
            "department":"Team Lead",
            "compuetrID":"AAA53",
            "description":"Screen freezes when handing heavy apps",
           
        }

    
    def tearDown(self):
        pass

class RequestTestCase(BaseTestCase):
    
    def test_create_request(self):
        response = self.test_client.post('/nazirini/api/v1.0/details', data=json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("You request has been successful",str(response.data))

    def test_get_all_requests(self):
        

        response = self.test_client.post('/nazirini/api/v1.0/details', data=json.dumps(self.request_data), content_type = 'application/json')
        response = self.test_client.get('/nazirini/api/v1.0/details', data=json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 302)
          
    def test_get_single_request(self):
     
        response = self.test_client.get('/nazirini/api/v1.0/details/1', data=json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_can_update_request(self):
        user_data = json.dumps(self.request_data)
        response = self.test_client.put('/nazirini/api/v1.0/details', data=user_data, content_type= 'application/json')
        self.assertEqual(response.status_code, 201) 
        response_data = json.loads(response.data.decode())
        self.assertEqual(self.user, response_data.get('user'))


if __name__ == '__main__':
    unittest.main()