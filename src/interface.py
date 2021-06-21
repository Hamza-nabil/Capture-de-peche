#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QApplication
from PyQt5.QtGui import QDoubleValidator, QFont
from PyQt5.QtCore import Qt
import os
import pandas as pd
import pickle

class Diabetes(QWidget):

    def __init__(self) -> None :
        super(Diabetes, self).__init__()
        self.sub_head = QLabel("Détails du navire")
        self.sub_head.setFont(QFont("Times",24, weight=QFont.Bold))
        self.l0 = QLineEdit()
        self.l1 = QLineEdit()
        self.l2 = QLineEdit()
        self.l3 = QLineEdit()
        self.l4 = QLineEdit()
        self.l5 = QLineEdit()
        self.t0 = QLabel("identifiant :")
        self.t1 = QLabel("Distance du rivage:")
        self.t2 = QLabel("Distance du port:")
        self.t3 = QLabel("Vitesse:")
        self.t4 = QLabel("Latitude :")
        self.t5 = QLabel("Longitude:")
        self.r1 = QLabel("(mètres)")
        self.r2 = QLabel("(mètres)")
        self.r3 = QLabel("(nœuds)")
        self.r4 = QLabel("(degrés décimaux)")
        self.r5 = QLabel("(degrés décimaux)")
        self.h1 = QHBoxLayout()
        self.h0 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h5 = QHBoxLayout()
        self.clbtn = QPushButton("Effacer")
        self.clbtn.setFixedWidth(100)
        self.submit = QPushButton("Soumettre")
        self.submit.setFixedWidth(100)
        self.v1_box = QVBoxLayout()
        self.v2_box = QVBoxLayout()
        self.final_hbox = QHBoxLayout()
        self.initui()

    def initui(self) -> None:
        """ L'interface graphique est créée et les éléments des widgets sont définis ici """
        self.v1_box.addWidget(self.sub_head)
        self.v1_box.addSpacing(10)
        self.v1_box.setSpacing(5)
        self.l1.setValidator(QDoubleValidator())
        self.l2.setValidator(QDoubleValidator())
        self.l3.setValidator(QDoubleValidator())
        self.l4.setValidator(QDoubleValidator())
        self.l5.setValidator(QDoubleValidator())
        self.l0.setToolTip("")
        self.l1.setToolTip("")
        self.l2.setToolTip("")
        self.l3.setToolTip("")
        self.l4.setToolTip("")
        self.l5.setToolTip("")
        self.l0.setFixedSize(260, 30)
        self.l1.setFixedSize(100,30)
        self.l2.setFixedSize(100,30)
        self.l3.setFixedSize(100,30)
        self.l4.setFixedSize(100,30)
        self.l5.setFixedSize(100,30)
        self.h0.addWidget(self.t0)
        self.h0.addWidget(self.l0)
        self.v1_box.addLayout(self.h0)
        self.h1.addWidget(self.t1)
        self.h1.addWidget(self.l1)
        self.h1.addWidget(self.r1)        
        self.v1_box.addLayout(self.h1)
        self.h2.addWidget(self.t2)
        self.h2.addWidget(self.l2)
        self.h2.addWidget(self.r2)       
        self.v1_box.addLayout(self.h2)
        self.h3.addWidget(self.t3)
        self.h3.addWidget(self.l3)
        self.h3.addWidget(self.r3)       
        self.v1_box.addLayout(self.h3)
        self.h4.addWidget(self.t4)
        self.h4.addWidget(self.l4)
        self.h4.addWidget(self.r4)      
        self.v1_box.addLayout(self.h4)
        self.h5.addWidget(self.t5)
        self.h5.addWidget(self.l5)
        self.h5.addWidget(self.r5)      
        self.v1_box.addLayout(self.h5)
        self.h6 = QHBoxLayout()
        self.submit.clicked.connect(lambda: self.test_input())
        self.submit.setToolTip("Cliquez pour vérifier si le navire pêche")
        self.clbtn.clicked.connect(lambda: self.clfn())
        self.h6.addWidget(self.submit)
        self.h6.addWidget(self.clbtn)
        self.v1_box.addLayout(self.h6)
        self.report_ui()
        self.final_hbox.addLayout(self.v1_box)
        self.final_hbox.addSpacing(40)
        self.final_hbox.addLayout(self.v2_box)
        self.setLayout(self.final_hbox)

    def report_ui(self):
        self.v2_box.setSpacing(6)
        self.report_subhead = QLabel("À propos")
        self.report_subhead.setAlignment(Qt.AlignCenter)
        self.report_subhead.setFont(QFont("Times",24, weight=QFont.Bold))
        self.v2_box.addWidget(self.report_subhead)
        self.details = QLabel("Ce modèle utilise LogisticRegression.\n\nPrécision du modèle : 70 %\n\nNous avons utilisé l'ensemble de données « Anonymized AIS training data » de Global Watch Fishing.")
        self.details.setFont(QFont("Arial",14, weight=QFont.Bold))
        self.details.setAlignment(Qt.AlignLeft)
        self.details.setWordWrap(True)
        self.model_details = QLabel("Remplissez les détails et appuyez sur Soumettre pour voir la resultat.")
        self.model_details.setWordWrap(True)
        self.v2_box.addWidget(self.details)
        self.results = QLabel(" ")
        self.results.setWordWrap(True)
        self.v2_box.addWidget(self.results)
        self.v2_box.addWidget(self.model_details)

    def clfn(self):
        """ effacer tous les champs de texte via le bouton Effacer"""
        self.l0.clear()
        self.l1.clear()
        self.l2.clear()
        self.l3.clear()
        self.l3.clear()
        self.l4.clear()
        self.l5.clear()
        self.report_subhead.setText("À propos")
        self.model_details.setText("Remplissez les détails et appuyez sur Soumettre pour voir la resultat.")
        self.results.setText(" ")
        self.details.setText("Ce modèle utilise LogisticRegression.\nPrécision du modèle : 70 %\nNous avons utilisé l'ensemble de données « Anonymized AIS training data » de Global Watch Fishing.")

    def test_input(self) -> None:
        """ test pour l'événement peche"""
        my_dict = {"distance_from_shore":float(self.l1.text()), "distance_from_port":float(self.l2.text()),"speed":float(self.l3.text()), "lat":float(self.l4.text()), "lon": float(self.l5.text())}
        output = check_input(my_dict)
        self.report_subhead.setText("Resultat :")
        self.details.setText("identifiant : {}\nLatitude : {}\nLongitude: {}".format(self.l0.text(),  self.l3.text(),self.l4.text(),self.l5.text()))
        #
        if output==0:
            self.results.setText("le navire n'est pas en pêche.")
        else:
            self.results.setText("le navire est en train de pêche.")
        self.results.setFont(QFont("Arial",14, weight=QFont.Bold))           

    def mwindow(self) -> None:
        """ 
        les fonctionnalités de la fenêtre sont définies ici et 
        l'application est chargée dans l'affichage
        """
        self.setFixedSize(898, 422)
        self.setWindowTitle("Capture de pêche")
        self.show()
        
def find_data_file(filename):
    if getattr(sys, "frozen", False):
        # The application is frozen.
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen.
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)


def check_input(data) ->int :
    df=pd.DataFrame(data=data,index=[0])
    with open(find_data_file('../model/model.pkl'),'rb') as model:
        p=pickle.load(model)
    op=p.predict(df)
    return op[0]

if __name__=="__main__":
    app = QApplication(sys.argv)
    a_window = Diabetes()
    a_window.mwindow()
    sys.exit(app.exec_())
