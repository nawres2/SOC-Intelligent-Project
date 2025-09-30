# SOC Intelligent et Analyse Avancée des Données

## Description
Projet de fin d’études combinant **cybersécurité (SOC)** et **Data Science** pour détecter, analyser et prévoir les incidents de sécurité.  

Le projet comprend :  
- **SOC** : Collecte et corrélation des logs grâce à Wazuh, Suricata, OpenVAS et The Hive.  
- **Data Science** : Nettoyage et standardisation des logs, détection d’anomalies, classification des incidents, et visualisation interactive des KPIs et tendances.  
- **Automation et CI/CD** : Scripts Python et pipelines CI/CD pour garantir la qualité des données et automatiser les workflows.

## Architecture

![Architecture du SOC](architecture.png)

### Outils principaux
- **Wazuh** : collecte des logs et alertes  
- **Suricata** : détection d’intrusions réseau  
- **OpenVAS** : scanner de vulnérabilités  
- **The Hive** : gestion et traitement des incidents  

Les données collectées sont ensuite analysées via des scripts Python pour détecter les anomalies, générer des insights et visualiser les tendances de sécurité.

## Organisation du projet
SOC-Intelligent-Project/
│
├── README.md
├── requirements.txt
├── etl.py
├── anomaly_detection.py
├── visualization.py
└── logs.csv
## Usage
1. Préparer les données : `python etl.py`  
2. Détecter les anomalies : `python anomaly_detection.py`  
3. Visualiser les incidents : `python visualization.py`
