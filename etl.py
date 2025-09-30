import pandas as pd

# Exemple : lecture de logs fictifs
data = pd.read_csv('logs.csv')

# Conversion des dates en datetime
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Sélection et nettoyage des colonnes
data = data[['timestamp', 'source_ip', 'destination_ip', 'event_type', 'severity']]
data.fillna({'source_ip': 'unknown', 'destination_ip': 'unknown', 'severity': 0}, inplace=True)

# Sauvegarde des données nettoyées
data.to_csv('clean_logs.csv', index=False)
print("Données nettoyées et sauvegardées dans 'clean_logs.csv'")
