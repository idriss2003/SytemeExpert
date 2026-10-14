import sys

from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtGui import (
    QPainter,
    QPixmap,
    QColor,
    QLinearGradient,
    QBrush,
    QPen,
    QFont,
)
from moteur import MoteurInference

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QCheckBox,
    QPushButton,
    QComboBox,
    QTextEdit,
    QGroupBox,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QScrollArea,
    QSizePolicy,
)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        # ======================================================
        # TITRE DE LA FENÊTRE
        # ======================================================

        self.setWindowTitle("Système Expert - Animal")

        self.resize(1400, 850)
        self.setMinimumSize(950, 620)

        self.moteur = MoteurInference()

        self.creer_interface()

    # ==========================================================
    # ARRIÈRE-PLAN GRAPHIQUE
    # ==========================================================

    def paintEvent(self, event):

        painter = QPainter(self)

        # ======================================================
        # IMAGE RÉELLE EN ARRIÈRE-PLAN
        # ======================================================

        image_path = "Dreamy Savanna Wildlife AI Landscape.png"

        pixmap = QPixmap(image_path)

        if not pixmap.isNull():

            pixmap = pixmap.scaled(
                self.size(),
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation
            )

            x = (self.width() - pixmap.width()) // 2
            y = (self.height() - pixmap.height()) // 2

            painter.drawPixmap(x, y, pixmap)

            # Voile blanc léger pour atténuer les couleurs de l'image
            # et améliorer la lisibilité du texte et des panneaux.
            painter.fillRect(
                self.rect(),
                QColor(255, 255, 255, 75)
            )

        else:
            # Fond de secours si l'image n'est pas trouvée
            painter.fillRect(
                self.rect(),
                QColor("#dceeff")
            )

        painter.end()


    # ==========================================================
    # ARBRE
    # ==========================================================

    def dessiner_arbre(
        self,
        painter,
        x,
        y,
        taille
    ):

        painter.setPen(
            Qt.PenStyle.NoPen
        )

        # Tronc
        painter.setBrush(
            QColor(95, 70, 45, 80)
        )

        painter.drawRoundedRect(
            int(x),
            int(y),
            int(14 * taille),
            int(85 * taille),
            5,
            5
        )

        # Branches
        painter.setPen(
            QPen(
                QColor(95, 70, 45, 75),
                max(2, int(4 * taille))
            )
        )

        painter.drawLine(
            int(x + 7 * taille),
            int(y + 35 * taille),
            int(x - 25 * taille),
            int(y)
        )

        painter.drawLine(
            int(x + 7 * taille),
            int(y + 40 * taille),
            int(x + 35 * taille),
            int(y + 5 * taille)
        )

        painter.setPen(
            Qt.PenStyle.NoPen
        )

        # Feuillage
        painter.setBrush(
            QColor(55, 115, 65, 65)
        )

        painter.drawEllipse(
            int(x - 55 * taille),
            int(y - 55 * taille),
            int(90 * taille),
            int(70 * taille)
        )

        painter.drawEllipse(
            int(x - 5 * taille),
            int(y - 70 * taille),
            int(100 * taille),
            int(75 * taille)
        )

        painter.drawEllipse(
            int(x - 75 * taille),
            int(y - 20 * taille),
            int(95 * taille),
            int(65 * taille)
        )

    # ==========================================================
    # GIRAFE
    # ==========================================================

    def dessiner_girafe(
        self,
        painter,
        x,
        y
    ):

        couleur = QColor(
            130,
            95,
            55,
            48
        )

        painter.setPen(
            QPen(
                couleur,
                5
            )
        )

        # Corps
        painter.drawEllipse(
            x,
            y + 80,
            80,
            40
        )

        # Cou
        painter.drawLine(
            x + 65,
            y + 85,
            x + 85,
            y + 10
        )

        # Tête
        painter.drawEllipse(
            x + 75,
            y,
            35,
            25
        )

        # Oreilles
        painter.drawLine(
            x + 82,
            y + 4,
            x + 73,
            y - 7
        )

        painter.drawLine(
            x + 100,
            y + 4,
            x + 110,
            y - 7
        )

        # Pattes
        painter.drawLine(
            x + 15,
            y + 110,
            x + 10,
            y + 155
        )

        painter.drawLine(
            x + 35,
            y + 110,
            x + 35,
            y + 155
        )

        painter.drawLine(
            x + 65,
            y + 110,
            x + 70,
            y + 155
        )

        painter.drawLine(
            x + 78,
            y + 105,
            x + 85,
            y + 150
        )

    # ==========================================================
    # ÉLÉPHANT
    # ==========================================================

    def dessiner_elephant(
        self,
        painter,
        x,
        y
    ):

        couleur = QColor(
            70,
            95,
            100,
            45
        )

        painter.setPen(
            QPen(
                couleur,
                5
            )
        )

        # Corps
        painter.drawEllipse(
            x,
            y - 50,
            110,
            60
        )

        # Tête
        painter.drawEllipse(
            x - 35,
            y - 55,
            60,
            55
        )

        # Oreille
        painter.drawEllipse(
            x - 30,
            y - 45,
            35,
            40
        )

        # Trompe
        painter.drawLine(
            x - 25,
            y - 15,
            x - 50,
            y + 20
        )

        painter.drawLine(
            x - 50,
            y + 20,
            x - 43,
            y + 30
        )

        # Pattes
        painter.drawLine(
            x + 20,
            y,
            x + 20,
            y + 45
        )

        painter.drawLine(
            x + 45,
            y,
            x + 45,
            y + 45
        )

        painter.drawLine(
            x + 80,
            y,
            x + 80,
            y + 45
        )

        painter.drawLine(
            x + 100,
            y - 2,
            x + 100,
            y + 45
        )

    # ==========================================================
    # ZÈBRE
    # ==========================================================

    def dessiner_zebre(
        self,
        painter,
        x,
        y
    ):

        couleur = QColor(
            60,
            70,
            75,
            38
        )

        painter.setPen(
            QPen(
                couleur,
                4
            )
        )

        # Corps
        painter.drawEllipse(
            x,
            y - 35,
            90,
            35
        )

        # Tête
        painter.drawEllipse(
            x + 80,
            y - 45,
            35,
            30
        )

        # Oreille
        painter.drawLine(
            x + 90,
            y - 43,
            x + 85,
            y - 55
        )

        # Pattes
        painter.drawLine(
            x + 15,
            y - 5,
            x + 10,
            y + 35
        )

        painter.drawLine(
            x + 35,
            y - 5,
            x + 35,
            y + 35
        )

        painter.drawLine(
            x + 65,
            y - 5,
            x + 70,
            y + 35
        )

        painter.drawLine(
            x + 82,
            y - 5,
            x + 88,
            y + 30
        )

    # ==========================================================
    # INTERFACE
    # ==========================================================

    def creer_interface(self):

        # ======================================================
        # TITRE
        # ======================================================

        titre = QLabel(
            "🧠  SYSTÈME EXPERT"
        )
        titre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titre.setObjectName(
            "titre"
        )

        sous_titre = QLabel(
            "Identification intelligente des animaux"
        )
        sous_titre.setAlignment(Qt.AlignmentFlag.AlignCenter)

        sous_titre.setObjectName(
            "sous_titre"
        )

        # ======================================================
        # BADGE
        # ======================================================

        badge = QLabel(
            "🔴  CHAÎNAGE ARRIÈRE"
        )

        badge.setObjectName(
            "badge"
        )

        badge.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        # ======================================================
        # FAITS
        # ======================================================

        groupe_faits = QGroupBox(
            "📋  Faits connus"
        )

        widget_faits = QWidget()

        layout_faits = QGridLayout(
            widget_faits
        )

        layout_faits.setContentsMargins(
            5,
            5,
            5,
            5
        )

        layout_faits.setHorizontalSpacing(
            10
        )

        layout_faits.setVerticalSpacing(
            8
        )

        # Répartition uniforme de la largeur des 3 colonnes
        layout_faits.setColumnStretch(0, 1)
        layout_faits.setColumnStretch(1, 1)
        layout_faits.setColumnStretch(2, 1)

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

            "Animal vole bien",
        ]

        self.checkboxes = []

        for i, fait in enumerate(
            self.faits
        ):

            checkbox = QCheckBox(
                fait
            )

            checkbox.setMinimumHeight(
                40
            )
            checkbox.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Fixed
            )

            checkbox.stateChanged.connect(
                self.mettre_a_jour_compteur
            )

            self.checkboxes.append(
                checkbox
            )

            ligne = i // 3
            colonne = i % 3

            layout_faits.addWidget(
                checkbox,
                ligne,
                colonne
            )

        # ======================================================
        # SCROLL
        # ======================================================

        scroll = QScrollArea()

        scroll.setWidget(
            widget_faits
        )

        scroll.setWidgetResizable(
            True
        )

        scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        scroll.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        scroll.setFrameShape(
            QScrollArea.Shape.NoFrame
        )

        scroll.setMinimumHeight(210)
        scroll.setMaximumHeight(330)

        layout_faits_groupe = QVBoxLayout()

        layout_faits_groupe.setContentsMargins(
            8,
            15,
            8,
            8
        )

        layout_faits_groupe.addWidget(
            scroll
        )

        groupe_faits.setLayout(
            layout_faits_groupe
        )

        # ======================================================
        # COMPTEUR
        # ======================================================

        self.info_faits = QLabel(
            "✓  0 fait sélectionné"
        )

        self.info_faits.setObjectName(
            "info_faits"
        )

        # ======================================================
        # OBJECTIF
        # ======================================================

        groupe_objectif = QGroupBox(
            "🎯  Objectif du raisonnement"
        )

        layout_objectif = QVBoxLayout()

        label_objectif = QLabel(
            "Que souhaitez-vous démontrer ?"
        )

        label_objectif.setObjectName(
            "label_objectif"
        )

        self.objectif = QComboBox()

        self.objectifs = [

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
            "Est un albatros",
        ]

        self.objectif.addItems(
            self.objectifs
        )

        layout_objectif.addWidget(
            label_objectif
        )

        layout_objectif.addWidget(
            self.objectif
        )

        groupe_objectif.setLayout(
            layout_objectif
        )

        # ======================================================
        # BOUTONS
        # ======================================================

        self.bouton_lancer = QPushButton(
            "🔍   LANCER LE RAISONNEMENT"
        )

        self.bouton_lancer.setMinimumHeight(
            52
        )

        self.bouton_lancer.clicked.connect(
            self.lancer_raisonnement
        )

        self.bouton_reset = QPushButton(
            "↻   Réinitialiser"
        )

        self.bouton_reset.setObjectName(
            "bouton_reset"
        )

        self.bouton_reset.setMinimumHeight(
            52
        )

        self.bouton_reset.clicked.connect(
            self.reinitialiser
        )

        # ======================================================
        # RESULTAT
        # ======================================================

        groupe_resultat = QGroupBox(
            "🔎  Raisonnement"
        )

        layout_resultat = QVBoxLayout()

        self.resultat = QTextEdit()

        self.resultat.setReadOnly(
            True
        )

        self.resultat.setPlaceholderText(
            "Le raisonnement du système expert "
            "apparaîtra ici..."
        )

        layout_resultat.addWidget(
            self.resultat
        )

        groupe_resultat.setLayout(
            layout_resultat
        )

        # ======================================================
        # STATUT
        # ======================================================

        self.statut = QLabel(
            "●  Prêt à analyser"
        )

        self.statut.setObjectName(
            "statut"
        )

        # ======================================================
        # GAUCHE
        # ======================================================

        gauche = QVBoxLayout()

        gauche.setSpacing(7)

        gauche.addWidget(
            groupe_faits
        )

        gauche.addWidget(
            self.info_faits
        )

        gauche.addWidget(
            groupe_objectif
        )

        boutons = QHBoxLayout()

        boutons.setSpacing(
            10
        )

        boutons.addWidget(
            self.bouton_lancer,
            2
        )

        boutons.addWidget(
            self.bouton_reset,
            1
        )

        gauche.addLayout(
            boutons
        )

        # ======================================================
        # DROITE
        # ======================================================

        droite = QVBoxLayout()

        droite.setSpacing(7)

        droite.addWidget(
            badge
        )

        droite.addWidget(
            groupe_resultat,
            1
        )

        droite.addWidget(
            self.statut
        )

        # ======================================================
        # CONTENU
        # ======================================================

        contenu = QHBoxLayout()

        contenu.setSpacing(14)

        contenu.addLayout(
            gauche,
            5
        )

        contenu.addLayout(
            droite,
            5
        )

        # ======================================================
        # LAYOUT PRINCIPAL
        # ======================================================

        layout_principal = QVBoxLayout()

        layout_principal.setContentsMargins(
            18,
            10,
            18,
            10
        )

        layout_principal.setSpacing(
            4
        )

        # En-tête fixe
        layout_principal.addWidget(
            titre
        )

        layout_principal.addWidget(
            sous_titre
        )

        # Page principale défilable : les boutons restent accessibles
        # même lorsque la fenêtre est réduite.
        page = QWidget()
        page.setLayout(contenu)

        scroll_page = QScrollArea()
        scroll_page.setWidget(page)
        scroll_page.setWidgetResizable(True)
        scroll_page.setFrameShape(QScrollArea.Shape.NoFrame)
        scroll_page.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        scroll_page.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        layout_principal.addWidget(
            scroll_page,
            1
        )

        self.setLayout(
            layout_principal
        )

        self.appliquer_style()

    # ==========================================================
    # COMPTEUR
    # ==========================================================

    def mettre_a_jour_compteur(
        self
    ):

        nombre = sum(
            checkbox.isChecked()
            for checkbox in self.checkboxes
        )

        if nombre == 0:

            texte = "✓  0 fait sélectionné"

        elif nombre == 1:

            texte = "✓  1 fait sélectionné"

        else:

            texte = (
                f"✓  {nombre} faits sélectionnés"
            )

        self.info_faits.setText(
            texte
        )

    # ==========================================================
    # MAPPING DES OBJECTIFS
    # ==========================================================

    def obtenir_objectif_moteur(self):
        correspondance = {
            "Est un mammifère": "mammifère",
            "Est un oiseau": "oiseau",
            "Est un carnivore": "carnivore",
            "Est un ongulé": "ongulé",
            "Est un guépard": "guépard",
            "Est un tigre": "tigre",
            "Est une girafe": "girafe",
            "Est un zèbre": "zèbre",
            "Est une autruche": "autruche",
            "Est un pingouin": "pingouin",
            "Est un albatros": "albatros",
        }
        return correspondance[self.objectif.currentText()]

    # ==========================================================
    # RAISONNEMENT RÉEL - CHAÎNAGE ARRIÈRE
    # ==========================================================

    def lancer_raisonnement(self):

        faits_selectionnes = [
            checkbox.text()
            for checkbox in self.checkboxes
            if checkbox.isChecked()
        ]

        objectif_affiche = self.objectif.currentText()
        objectif_moteur = self.obtenir_objectif_moteur()

        self.resultat.clear()

        if not faits_selectionnes:
            self.resultat.append("⚠️  Aucun fait n'a été sélectionné.")
            self.resultat.append("")
            self.resultat.append(
                "Sélectionnez au moins un fait avant de lancer le raisonnement."
            )
            self.statut.setText("●  En attente de faits")
            return

        resultat = self.moteur.executer_chainage_arriere(
            faits_selectionnes,
            objectif_moteur
        )

        self.resultat.append(
            "╔══════════════════════════════════════╗"
        )
        self.resultat.append(
            "║          CHAÎNAGE ARRIÈRE           ║"
        )
        self.resultat.append(
            "╚══════════════════════════════════════╝"
        )
        self.resultat.append("")
        self.resultat.append(f"🎯 Objectif : {objectif_affiche}")
        self.resultat.append("")
        self.resultat.append("📋 Faits connus :")

        for fait in faits_selectionnes:
            self.resultat.append(f"   ✓ {fait}")

        self.resultat.append("")
        self.resultat.append(
            "──────────────────────────────────────"
        )
        self.resultat.append("")
        self.resultat.append("🧠 Démonstration de l'objectif :")

        for etape in resultat["etapes"]:
            self.resultat.append(etape)

        self.resultat.append("")
        self.resultat.append(
            "──────────────────────────────────────"
        )
        self.resultat.append("")

        if resultat["reussi"]:
            self.resultat.append(
                f"✅ OBJECTIF DÉMONTRÉ : {objectif_affiche}"
            )

            if resultat["regles_utilisees"]:
                self.resultat.append(
                    "📌 Règles utilisées : "
                    + ", ".join(resultat["regles_utilisees"])
                )

            self.statut.setText("●  Objectif démontré")

        else:
            self.resultat.append(
                f"❌ OBJECTIF NON DÉMONTRÉ : {objectif_affiche}"
            )
            self.resultat.append(
                "Les faits connus ne permettent pas de démontrer cet objectif."
            )
            self.statut.setText("●  Objectif non démontré")

    # ==========================================================
    # RESET
    # ==========================================================

    def reinitialiser(
        self
    ):

        for checkbox in self.checkboxes:

            checkbox.setChecked(
                False
            )

        self.objectif.setCurrentIndex(
            0
        )

        self.resultat.clear()

        self.info_faits.setText(
            "✓  0 fait sélectionné"
        )

        self.statut.setText(
            "●  Prêt à analyser"
        )

    # ==========================================================
    # STYLE
    # ==========================================================

    def appliquer_style(
        self
    ):

        self.setStyleSheet("""

            QWidget {
                color: #172033;
                font-family: "Segoe UI";
                font-size: 14px;
            }

            QLabel#titre {
                color: #102a43;
                font-size: 34px;
                font-weight: 800;
                background-color: rgba(255,255,255,185);
                border-radius: 16px;
                padding: 8px 18px;
            }

            QLabel#sous_titre {
                color: #30445f;
                font-size: 16px;
                font-weight: 600;
                background-color: rgba(255,255,255,145);
                border-radius: 12px;
                padding: 5px 14px;
            }

            QGroupBox {
                background-color: rgba(255,255,255,220);

                border: 1px solid rgba(190,200,215,220);

                border-radius: 14px;

                margin-top: 12px;

                padding: 12px;

                font-size: 15px;

                font-weight: 700;
            }

            QGroupBox::title {
                subcontrol-origin: margin;

                left: 15px;

                padding: 0px 8px;

                color: #26364d;

                background-color: rgba(255,255,255,230);
            }

            QLabel#badge {
                background-color: rgba(255,240,240,245);

                color: #d92d20;

                border: 1px solid #fecdca;

                border-radius: 12px;

                padding: 12px;

                font-weight: bold;

                font-size: 15px;
            }

            QCheckBox {
                background-color: rgba(248,250,252,240);

                border: 1px solid #e4e7ec;

                border-radius: 9px;

                padding: 7px;

                spacing: 8px;

                color: #172033;

                font-size: 13px;

                min-height: 25px;
            }

            QCheckBox:hover {
                background-color: #eef4ff;

                border: 1px solid #84adff;
            }

            QCheckBox:checked {
                background-color: #eef4ff;

                color: #175cd3;

                border: 1px solid #84adff;

                font-weight: 600;
            }

            QCheckBox::indicator {
                width: 18px;
                height: 18px;
            }

            QCheckBox::indicator:unchecked {
                border: 2px solid #98a2b3;

                border-radius: 5px;

                background-color: white;
            }

            QCheckBox::indicator:checked {
                border: 2px solid #3155d4;

                border-radius: 5px;

                background-color: #3155d4;
            }

            QLabel#info_faits {
                color: #3155d4;

                font-size: 13px;

                font-weight: 700;

                padding-left: 5px;
            }

            QLabel#label_objectif {
                color: #475467;

                font-size: 14px;

                font-weight: 600;
            }

            QComboBox {
                background-color: rgba(255,255,255,230);

                border: 1px solid #98a2b3;

                border-radius: 9px;

                padding: 10px;

                min-height: 22px;
            }

            QComboBox:hover {
                border: 1px solid #5276e8;
            }

            QPushButton {
                background-color: #3155d4;

                color: white;

                border: none;

                border-radius: 10px;

                padding: 12px 18px;

                font-weight: 700;

                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #2544b5;
            }

            QPushButton:pressed {
                background-color: #19358f;
            }

            QPushButton#bouton_reset {
                background-color: rgba(255,255,255,230);

                color: #344054;

                border: 1px solid #d0d5dd;
            }

            QPushButton#bouton_reset:hover {
                background-color: #f2f4f7;
            }

            QTextEdit {
                background-color: #101828;

                color: #e6edf7;

                border: none;

                border-radius: 10px;

                padding: 15px;

                font-family: "Consolas";

                font-size: 13px;
            }

            QLabel#statut {
                color: #12b76a;

                background-color: rgba(236,253,243,240);

                border: 1px solid #abefc6;

                border-radius: 9px;

                padding: 9px;

                font-weight: 600;
            }

            QScrollArea {
                background: transparent;
                border: none;
            }

            QScrollArea > QWidget > QWidget {
                background: transparent;
            }

            QScrollBar:vertical {
                background: rgba(242,244,247,180);

                width: 10px;

                border-radius: 5px;
            }

            QScrollBar::handle:vertical {
                background: #98a2b3;

                border-radius: 5px;

                min-height: 30px;
            }

            QScrollBar::handle:vertical:hover {
                background: #667085;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0px;
            }

        """)


# ==============================================================
# LANCEMENT
# ==============================================================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    fenetre = MainWindow()

    fenetre.show()

    sys.exit(app.exec())
