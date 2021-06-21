#!/usr/bin/env python3

import pickle

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#For training
def train():
    dataset = pd.read_csv('../data/data.csv')
    # Supprimer les lignes où l'une des colonnes contient des valeurs nulles.
    dataset = dataset.dropna(axis=0, how='any')
    X = dataset[['distance_from_shore','distance_from_port', 'speed', 'lat', 'lon']]
    Y = dataset[["is_fishing"]]
    
    #Diviser data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 101)
    
    #Fixer le taux de régularisation
    reg = 0.01
    
    # entraîner un modèle de régression logistique sur l'ensemble d'apprentissage
    model = LogisticRegression(C=1/reg, solver="liblinear").fit(X_train, Y_train)
    
    #Enregistrer le modèle en tant que fichier Pickle
    with open('../model/model.pkl','wb') as m:
        pickle.dump(model, m)
    test(X_test,Y_test)

#Tester la précision du modèle
def test(X_test,Y_test):
    with open('../model/model.pkl','rb') as mod:
        p = pickle.load(mod)
    pre = p.predict(X_test)
    print ("Precision :" ,accuracy_score(Y_test.values.ravel(),pre.ravel())) #Prints the accuracy of the model


if __name__=='__main__':
    train()    
