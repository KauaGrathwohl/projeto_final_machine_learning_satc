import requests

url = 'http://localhost:5000/predict'
data = {'email': 'Você ganhou um prêmio! Clique aqui para resgatar!'}

# Envia a requisição POST

response = requests.post(url, json=data)

# Verifica se a requisição foi bem-sucedida (código de status 200)

if response.status_code == 200:
    print(response.json())
else:
    print(f'Erro ao enviar requisição: {response.status_code}, {response.text}')
