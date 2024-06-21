import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [emailText, setEmailText] = useState('');
  const [predictionResult, setPredictionResult] = useState('');
  const [error, setError] = useState('');

  const predictSpam = async () => {
    try {
      const response = await axios.post('http://localhost:5000/predict', {
        email: emailText
      });

      if (response.status === 200) {
        setPredictionResult(response.data.prediction);
        setError('');
      } else {
        setError('Erro ao prever spam. Resposta inválida da API.');
      }
    } catch (error) {
      console.error('Erro ao prever spam:', error);
      setError('Erro ao prever spam. Verifique o console para mais detalhes.');
    }
  };

  return (
    <div className="container">
      <h1>Detector de Spam</h1>
      <div className="form-group">
        <label htmlFor="emailText">Digite seu email:</label>
        <textarea
          id="emailText"
          rows="5"
          placeholder="Digite seu email aqui..."
          value={emailText}
          onChange={(e) => setEmailText(e.target.value)}
        ></textarea>
      </div>
      <button onClick={predictSpam}>Verificar Spam</button>
      <div id="predictionResult" className="result">
        {error && <p className="error">{error}</p>}
        {predictionResult && (
          <>
            <h2>Resultado da Predição:</h2>
            <p>{predictionResult}</p>
          </>
        )}
      </div>
    </div>
  );
}

export default App;
