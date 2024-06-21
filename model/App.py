import pandas as pd
from deep_translator import GoogleTranslator
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Carrega os dados do arquivo CSV

df = pd.read_csv('../data/spam.csv', encoding='latin-1')

# Limpa os dados nulos, se houver

data = df.where((pd.notnull(df)), '')

# Mapeia 'spam' para 0 e 'ham' para 1

data.loc[data['v1'] == 'spam', 'v1'] = 0
data.loc[data['v1'] == 'ham', 'v1'] = 1

# Define features (X) e target (Y)

X = data['v2']
Y = data['v1']

# Divide em conjunto de treino e teste

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

# Vetorização com TF-IDF

feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

# Converte Y_train e Y_test para inteiros

Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

# Treinamento do modelo de Regressão Logística

model = LogisticRegression()
model.fit(X_train_features, Y_train)

# Inicialização do aplicativo Flask

app = Flask(__name__)

# Configuração do CORS

CORS(app, resources={r"/predict": {"origins": "http://localhost:3000"}})


# Rota para receber POST com o email e retornar se é spam ou não

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Recebe o email enviado via POST

        content = request.json
        email_text = content['email']

        # Traduz o email para inglês

        translator = GoogleTranslator(source='pt', target='en')
        translated_text = translator.translate(email_text)

        # Extrai features do email traduzido

        input_data_features = feature_extraction.transform([translated_text])

        # Realiza a previsão

        prediction = model.predict(input_data_features)

        # Retorna o resultado

        if prediction[0] == 1:
            result = 'Não spam'
        else:
            result = 'spam'

        return jsonify({'prediction': result}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
