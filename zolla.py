import requests

url = 'https://moscow.hh.ru/account/login'
rr2="https://hh.ru/vacancy/52829286?from=vacancy&hhtmFrom=vacancy&hhtmFromLabel=suitable_vacancies"
# Важно. По умолчанию requests отправляет вот такой 
# заголовок 'User-Agent': 'python-requests/2.22.0 ,  а это приводит к тому , что Nginx
# отправляет 404 ответ. Поэтому нам нужно сообщить серверу, что запрос идет от браузера  

user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

# Создаем сессию и указываем ему наш user-agent
session = requests.Session()
r = session.get(url, headers = {
    'User-Agent': user_agent_val
})
session.headers.update({'Referer':url})
session.headers.update({'User-Agent':user_agent_val})
_xsrf = session.cookies.get('_xsrf', domain=".hh.ru")
post_request = session.post(url, {
     'backUrl': 'https://moscow.hh.ru/',
     'username': 'логин',
     'password': 'пароль',
     '_xsrf':_xsrf,
     'remember':'yes',
})
ll=session.get('https://hh.ru/vacancy/48763372?from=main')
rr =session.post(rr2,data={
     '_xsrf':_xsrf, 
     'remember':'yes',
     "vacancy_id":'52829286',# айди вакансии
     'ignore_postponed':'true',
     "incomplete":'false',
     "hhtmFromLabel":'undefined',
     "withotTest":'no',
     "hhtmSourceLabel":'undefined',
     "resume_hash":'3b4d4225ff08f038930039ed1f694c70517741'}) #айди резюме

print(rr)