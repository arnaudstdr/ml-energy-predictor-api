# 🔍 ML Energy Predictor API

Ce projet est une démonstration de la mise en production d’un modèle de Machine Learning à travers une API Flask et une interface utilisateur Streamlit.

## 🚀 Fonctions principales
- Entraînement d’un modèle de régression Scikit-Learn pour estimer la consommation énergétique d’un logement
- API REST pour effectuer des prédictions à partir de données JSON
- Interface utilisateur simple avec Streamlit
- Déploiement avec Docker
- Code clair, structuré et documenté

## 🛠 Stack technique
- Python, Scikit-Learn, Pandas, Flask, Streamlit
- joblib, Docker, Git

## 🗂️ Arborescence du projet
```bash
ml-energy-predictor-api/
├── README.md
├── requirements.txt
├── Dockerfile
├── app/
│   ├── api.py           # API Flask
│   ├── model.pkl        # Modèle ML sérialisé (joblib)
│   ├── predict.py       # Code de prédiction
│   ├── utils.py         # Fonctions de preprocessing
│   └── data/
│       └── energy.csv   # Données d'exemple (fake ou open-source)
├── streamlit_app/
│   └── dashboard.py     # Interface utilisateur
├── notebooks/
│   └── training.ipynb   # Notebook d'entraînement du modèle
└── .gitignore
```


## ▶️ Lancer le projet

### En local
```bash
pip install -r requirements.txt
python app/api.py
streamlit run streamlit_app/dashboard.py
```

### Avec Docker
```bash
docker build -t ml-energy-api .
docker run -p 5000:5000 ml-energy-api
```

## 📄 Exemple de requête API
```json
POST /predict
{
  "surface": 80,
  "occupants": 3,
  "isolation": "bonne"
}
```

## 🧠 Auteur
Ce projet a été réalisé par Arnaud STADLER dans le cadre d’une activité freelance Python / MLOps.
