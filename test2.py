import ast
import json

def expor(body):
    body = bytes.decode(body, encoding='utf-8')
    body = body.replace('true',"'true'")
    
    body = ast.literal_eval(body)
    if body['roles'] != []:
        print(True)
    else:
        print(False)
    print(body['roles'])
    

body = b'{"id":"B9629FE7-167A-496C-A5AC-5BBA186F8F17","positions":[],"study":[{"code":"1816384","orgId":"301A33F6-CF7E-4879-89A0-48A09E9B43A8","academicGroup":"\xd0\xa2\xd0\x93\xd0\xa0-\xd1\x81-\xd0\xb7-21-1","academicGroupUuid":"FADA1FB0-EC0F-4CEF-A479-E2610EE38856","specialityCode":"21.05.03"}],"roles":["Student"],"personal":{"lastName":"\xd0\xa3\xd0\xb4\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xb2","firstName":"\xd0\x94\xd0\xbc\xd0\xb8\xd1\x82\xd1\x80\xd0\xb8\xd0\xb9","middleName":"\xd0\xae\xd1\x80\xd1\x8c\xd0\xb5\xd0\xb2\xd0\xb8\xd1\x87","gender":true}}'

msg = json.loads(body)
print(msg['personal']['gender'])
# expor(body)