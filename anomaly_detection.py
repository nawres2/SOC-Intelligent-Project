import pandas as pd
from sklearn.ensemble import IsolationForest

# Chargement des données nettoyées
data = pd.read_csv('clean_logs.csv')

# Transformation des données pour le modèle
data_numeric = pd.get_dummies(data[['event_type', 'severity']], drop_first=True)

# Détection d'anomalies
model = IsolationForest(contamination=0.05, random_state=42)
data['anomaly'] = model.fit_predict(data_numeric)

# Marque les anomalies
data['anomaly'] = data['anomaly'].map({1: 0, -1: 1})

# Sauvegarde des résultats
data.to_csv('logs_with_anomalies.csv', index=False)
print("Détection d'anomalies terminée. Résultats sauvegardés dans 'logs_with_anomalies.csv'")
