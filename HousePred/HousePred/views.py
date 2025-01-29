import os
from django.conf import settings
import pandas as pd
import numpy as np
from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

# Chemin absolu vers le fichier CSV
CSV_PATH = r"C:\Users\Fddkk\PycharmProjects\House Price\USA_Housing.csv"

def result(request):
    try:
        # Vérification si le fichier CSV existe
        if not os.path.isfile(CSV_PATH):
            return render(request, 'predict.html', {'result2': "Error: CSV file not found. Please check the file path."})

        # Chargement des données avec gestion des erreurs d'encodage
        try:
            data = pd.read_csv(CSV_PATH, encoding="utf-8")
        except UnicodeDecodeError:
            data = pd.read_csv(CSV_PATH, encoding="ISO-8859-1")

        # Suppression de la colonne "Address" si elle existe
        if 'Address' in data.columns:
            data = data.drop(['Address'], axis=1)

        # Vérification si la colonne "Price" existe
        if 'Price' not in data.columns:
            return render(request, 'predict.html', {'result2': "Error: 'Price' column not found in dataset."})

        # Définition des variables
        X = data.drop('Price', axis=1)
        y = data['Price']

        # Vérification si les données sont bien numériques
        if not np.issubdtype(X.dtypes[0], np.number):
            return render(request, 'predict.html', {'result2': "Error: Dataset contains non-numeric values."})

        # Séparation en jeu d'entraînement et de test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

        # Entraînement du modèle
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Récupération des valeurs entrées par l'utilisateur
        try:
            var1 = float(request.GET.get('n1', 0))
            var2 = float(request.GET.get('n2', 0))
            var3 = float(request.GET.get('n3', 0))
            var4 = float(request.GET.get('n4', 0))
            var5 = float(request.GET.get('n5', 0))
        except ValueError:
            return render(request, 'predict.html', {'result2': "Error: Invalid input. Please enter numbers only."})

        # Prédiction
        input_data = np.array([[var1, var2, var3, var4, var5]])
        prediction = model.predict(input_data)[0]
        prediction = round(prediction, 2)

        # Affichage du résultat
        price = f"The predicted house price is: ${prediction:,.2f}"

    except Exception as e:
        price = f"An error occurred: {str(e)}"

    return render(request, 'predict.html', {'result2': price})

