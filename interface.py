import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
    QPushButton,
    QComboBox,
    QTextEdit,
    QGroupBox
)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre
        self.setWindowTitle("Système Expert - Identification des animaux")
        self.setMinimumSize(900, 650)

        # Création de l'interface
        self.creer_interface()

    def creer_interface(self):

        # =========================
        # TITRE
        # =========================

        titre = QLabel("🧠 SYSTÈME EXPERT")
        sous_titre = QLabel("Identification des animaux")

        # =========================
        # FAITS
        # =========================

        groupe_faits = QGroupBox("Faits connus")

        layout_faits = QVBoxLayout()

        self.faits = [
            "Animal à poils",
            "Animal donne du lait",
            "Animal à plumes",
            "Animal vole",
            "Animal pond des œufs",
            "Animal mange de la viande",
            "Animal à dents pointues",
            "Animal à griffes",
            "Animal a les yeux devant",
            "Animal à sabots",
            "Animal rumine",
            "Animal à couleur brune",
            "Animal à taches sombres",
            "Animal à raies noires",
            "Animal à long cou",
            "Animal à longues pattes",
            "Animal nage",
            "Animal noir et blanc",
            "Animal vole bien"
        ]

        self.checkboxes = []

        for fait in self.faits:
            checkbox = QCheckBox(fait)
            self.checkboxes.append(checkbox)
            layout_faits.addWidget(checkbox)

        groupe_faits.setLayout(layout_faits)

        # =========================
        # OBJECTIF
        # =========================

        groupe_objectif = QGroupBox("Objectif à démontrer")

        layout_objectif = QVBoxLayout()

        self.objectif = QComboBox()

        self.objectif.addItems([
            "Est un mammifère",
            "Est un oiseau",
            "Est un carnivore",
            "Est un ongulé",
            "Est un guépard",
            "Est un tigre",
            "Est une girafe",
            "Est un zèbre",
            "Est une autruche",
            "Est un pingouin",
            "Est un albatros"
        ])

        layout_objectif.addWidget(self.objectif)

        groupe_objectif.setLayout(layout_objectif)

        # =========================
        # BOUTON
        # =========================

        bouton = QPushButton("🔍 Lancer le raisonnement")

        bouton.clicked.connect(self.lancer_raisonnement)

        # =========================
        # RÉSULTAT
        # =========================

        groupe_resultat = QGroupBox("Résultat du raisonnement")

        layout_resultat = QVBoxLayout()

        self.resultat = QTextEdit()
        self.resultat.setReadOnly(True)

        layout_resultat.addWidget(self.resultat)

        groupe_resultat.setLayout(layout_resultat)

        # =========================
        # ORGANISATION
        # =========================

        layout_principal = QVBoxLayout()

        layout_principal.addWidget(titre)
        layout_principal.addWidget(sous_titre)

        layout_principal.addWidget(groupe_faits)
        layout_principal.addWidget(groupe_objectif)

        layout_principal.addWidget(bouton)

        layout_principal.addWidget(groupe_resultat)

        self.setLayout(layout_principal)

    # =========================
    # ACTION DU BOUTON
    # =========================

    def lancer_raisonnement(self):

        faits_selectionnes = []

        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                faits_selectionnes.append(checkbox.text())

        objectif = self.objectif.currentText()

        self.resultat.clear()

        self.resultat.append("=== CHAÎNAGE ARRIÈRE ===\n")

        self.resultat.append(f"Objectif : {objectif}\n")

        self.resultat.append("Faits sélectionnés :")

        if faits_selectionnes:
            for fait in faits_selectionnes:
                self.resultat.append(f"✓ {fait}")
        else:
            self.resultat.append("Aucun fait sélectionné.")

        self.resultat.append("\nLe moteur de chaînage arrière sera connecté ici.")


# =========================
# PROGRAMME PRINCIPAL
# =========================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    fenetre = MainWindow()
    fenetre.show()

    sys.exit(app.exec())
