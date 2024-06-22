# Machine Learning - Spam Detection

Projeto final da matéria de Machine Learning, no curso de Engenharia de Software.

O objetivo deste projeto é criar um modelo de Machine Learning, onde seja possível detectar e validar e-mails considerados como Spam.


### Equipe:

- Kauã Machado Grathwohl [@KauaGrathwohl](https://github.com/KauaGrathwohl)
- Ana Julia Santinoni [@anasantinoni](https://github.com/anasantinoni)
- Laura Silveira Gonçalves [@laurasilveirag](https://github.com/laurasilveirag)
- Janaina Carlos João [@janainacarlos](https://github.com/janainacarlos)


# Funcionamento do projeto:

O projeto foi desenvolvido em Python, utilizando a biblioteca Pandas para manipulação dos dados e a biblioteca Scikit-learn para a criação do modelo de Machine Learning.


### Estrutura do projeto:

```

├── data
│   ├── spam.csv

├── frontend
│   ├── node_modules
│   ├── public
│   ├── src
│   ├── gitignore
│   ├── package.json
│   ├── package-lock.json

├── model
│   ├── notebooks
│   ├── App.py
│   ├── AppTest.py

├── venv

├── README.md

```


# Execução do projeto:

### Para executar o modelo, siga os passos abaixo:

```

1. Clonar o repositório
2. Acessar a pasta do projeto
3. Executar o comando: `python3 model/Application.py`
4. O modelo será treinado e validado
5. Após a validação, o modelo estará pronto para ser utilizado

```


### Para executar o Frontend, siga os passos abaixo:

```

1. Acessar a pasta frontend
2. Executar o comando: `npm start`
3. Acessar o endereço: `http://localhost:3000/`

```

# Detecção de Spam com Flask e Regressão Logística

Este projeto implementa um detector de spam simples utilizando Flask e Regressão Logística. O modelo é treinado com base em um conjunto de dados que contém emails classificados como 'spam' ou 'não spam' ('ham').


### Funcionalidades

- **Previsão de Spam**: Envia um email através da API e recebe uma previsão se é spam ou não.


### Como Funciona

1. **Pré-requisitos**:
    - Certifique-se de ter Python instalado.
    - Instale os pacotes necessários com `pip install -r requirements.txt`.

2. **Carregamento e Preparação dos Dados**:
    - Os dados são carregados de um arquivo CSV (`dataset/spam.csv`) usando Pandas.
    - Limpeza dos dados nulos e mapeamento das classes 'spam' e 'ham'.

3. **Treinamento do Modelo**:
    - Divide os dados em conjuntos de treino e teste.
    - Vetoriza os textos dos emails usando TF-IDF.
    - Treina um modelo de Regressão Logística para prever se um email é 'spam' ou 'não spam'.

4. **API Flask**:
    - Implementa uma rota `/predict` que recebe um email via POST.
    - Traduz o email para inglês usando o Google Translator.
    - Vetoriza o texto traduzido com o mesmo TF-IDF usado no treinamento.
    - Usa o modelo treinado para prever se o email é 'spam' ou 'não spam'.
    - Retorna o resultado da previsão.


### Uso

1. **Executando a Aplicação**:
    - Execute `python app.py` para iniciar o servidor Flask localmente.
    - Certifique-se de ter o CORS configurado corretamente para permitir as requisições da sua aplicação front-end.

2. **Enviando Requisições**:
    - Envia um POST para `http://localhost:5000/predict` com o corpo JSON contendo o email.
    - Recebe uma resposta JSON com a previsão ('spam' ou 'não spam').


### Bibliotecas Utilizadas

- Pandas: Para manipulação e análise de dados.
- Flask: Framework web para construção da API.
- Flask-CORS: Para configurar CORS e permitir requisições de outros domínios.
- Scikit-learn (sklearn): Para implementar a vetorização TF-IDF e treinamento do modelo de Regressão Logística.
- deep_translator: Para tradução automática dos textos.


### Resultados:

O modelo foi treinado e validado com sucesso, obtendo uma acurácia de 98% na validação.


### Referências:

- [Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)



