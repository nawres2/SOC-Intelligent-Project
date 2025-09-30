import pandas as pd
import matplotlib.pyplot as plt

# Chargement des résultats
data = pd.read_csv('logs_with_anomalies.csv')

# Nombre d'incidents par type d'événement
counts = data['event_type'].value_counts()
plt.figure(figsize=(10,6))
counts.plot(kind='bar', color='skyblue')
plt.title("Nombre d'incidents par type d'événement")
plt.xlabel("Type d'événement")
plt.ylabel("Nombre d'incidents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('incident_counts.png')
plt.show()

# Histogramme des anomalies par sévérité
plt.figure(figsize=(8,5))
data[data['anomaly']==1]['severity'].hist(bins=10, color='salmon')
plt.title("Distribution des anomalies par sévérité")
plt.xlabel("Sévérité")
plt.ylabel("Nombre d'anomalies")
plt.tight_layout()
plt.savefig('anomaly_severity.png')
plt.show()
