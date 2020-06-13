# import requests
# import json
# from content_management_portal.models import *


# def control_flow():

#     Question.objects.all().delete()

#     headers = {"Content-Type":"application/json"}
#     data = '{"username":"raviteja","password":"Maths@143"}'
#     url="http://localhost:8080/api/content_management_portal/login/v1/"
#     request = requests.post(url=url,data=data, headers=headers)
#     accesstoken = json.loads(request.content)['access_token']

#     print("Generation of Access token")
#     print()

#     print("********",accesstoken,"*********")
#     print()

#     headers = {
#         'Authorization': f"Bearer {accesstoken}",
#         "Content-Type":"application/json"
#     }
#     params = {"offset": 1, "limit": 8}
#     url="http://localhost:8080/api/content_management_portal/coding_questions/v1/"
#     request = requests.get(url=url, headers=headers, params=params)
#     response = json.loads(request.content)
#     print("Home page")
#     print()
#     print("----->",response,"<-------")
#     print()
#     assert response == {'total_questions': 0,'offset': 1, 'limit':1, 'questions_list': []}

#     content = {
#         "question_id": None,
#         "short_text": "string",
#         "problem_description": {
#             "content_type": "MARKDOWN",
#             "content": "string"
#         }
#     }
#     content = json.dumps(content)
#     url="http://localhost:8080/api/content_management_portal/coding_questions/statement/v1/"

#     request = requests.post(url=url, data=content, headers=headers)

#     print("Creating a Question")
#     print()
#     question_id = json.loads(request.content)['question_id']
#     print(json.loads(request.content))
#     print()
#     print("Home page")
#     url="http://localhost:8080/api/content_management_portal/coding_questions/v1/"
#     request = requests.get(url=url, headers=headers, params=params)
#     print(json.loads(request.content))
#     print()
#     content = [{
#         "rough_solution_id": 1,
#         "file_name": "updated string",
#         "language": "PYTHON",
#         "solution_content": "updated string"
#     },
#     {
#         "rough_solution_id": None,
#         "file_name": "string",
#         "language": "PYTHON",
#         "solution_content": "string"
#     }]
#     content = json.dumps(content)
#     url=f"http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/rough_solution/v1/"
#     request = requests.post(url=url, headers=headers, data=content)
#     print("Creating a rough solution id")
#     print()
#     rough_id = json.loads(request.content)[0]['rough_solution_id']
#     print(json.loads(request.content))
#     print()
#     print("Home page")
#     print()
#     url="http://localhost:8080/api/content_management_portal/homepage/coding_questions/v1/"
#     request = requests.get(url=url, headers=headers)
#     print(json.loads(request.content))
#     print()
#     assert json.loads(request.content)['questions_details'][0]['rough_solutions'] == True
#     url=f"http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/rough_solution/{rough_id}/v1/"
#     request = requests.delete(url=url, headers=headers)
#     print("Deleted the Rough id")
#     print()
#     print("Home page")
#     print()
#     url="http://localhost:8080/api/content_management_portal/homepage/coding_questions/v1/"
#     request = requests.get(url=url, headers=headers)
#     print(json.loads(request.content))
#     print()
#     assert json.loads(request.content)['questions_details'][0]['rough_solutions'] == False
#     url=f"http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/v1/"
#     request = requests.get(url=url, headers=headers)
#     print("Get complete details of specific question id")
#     print()
#     print(json.loads(request.content))
#     print()
#     content = [
#         {
#             "header_text": {
#                 "file_name": "prime.py",
#                 "language_type": "PYTHON"
#             },
#             "text_code": "code python"
#         }
#     ]
#     content = json.dumps(content)
#     url=f"http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/rough_solution/v1/"
#     request = requests.post(url=url, headers=headers, data=content)
#     print("Creating rough solution again")
#     print()
#     rough_id = json.loads(request.content)[0]['rough_solution_id']
#     print(json.loads(request.content))
#     print()

#     print("Get complete details of specific question id")
#     print()
#     url=f"http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/v1/"
#     request = requests.get(url=url, headers=headers)

#     print(json.loads(request.content))
#     print()

#     request = requests.get(
#         url="http://localhost:8080/api/content_management_portal/homepage/coding_questions/v1/",
#         headers=headers
#     )
#     response = json.loads(request.content)
#     print("Home page")
#     print("----->",response,"<-------")
#     print()

#     print("creating and updating rough solutions")
#     print()
#     rough_dict_1 = {
#         'header_text': {
#             'file_name': 'ruby_file',
#             'language_type': 'RUBY'
#         },
#         'text_code': 'code ruby'
#     }
#     rough_dict_2 = {
#         'rough_solution_id': rough_id,
#         'header_text': {
#             'file_name': 'prime.py',
#             'language_type': 'PYTHON'
#         },
#         'text_code': 'python code updated'
#     }
#     content = [rough_dict_1, rough_dict_2]
#     content = json.dumps(content)
#     url=f"http://localhost:8080/api/content_management_portal/coding_questions/{question_id}/rough_solution/v1/"
#     request = requests.post(url=url, headers=headers, data=content)

#     print(json.loads(request.content))
#     print()

# control_flow()
