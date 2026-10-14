# ==========================================================
# MOTEUR D'INFERENCE
# ==========================================================

from chainage_arriere import ChainageArriere


class MoteurInference:

    def __init__(self):

        self.chainage_arriere = ChainageArriere()

    # ======================================================
    # CHAÎNAGE ARRIÈRE
    # ======================================================

    def executer_chainage_arriere(
        self,
        faits,
        objectif
    ):

        return self.chainage_arriere.resoudre(
            objectif,
            faits
        )
