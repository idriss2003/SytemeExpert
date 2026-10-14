# moteur.py

from regles import REGLES, ANIMAUX_FINAUX


def regle_applicable(base_faits, conditions):
    return conditions.issubset(base_faits)


def appliquer_regle(base_faits, regle):
    identifiant, conditions, conclusion = regle

    if regle_applicable(base_faits, conditions) and conclusion not in base_faits:
        base_faits.add(conclusion)
        return True

    return False


def trouver_regles_conclusion(but):
    regles_trouvees = []

    for regle in REGLES:
        identifiant, conditions, conclusion = regle
        if conclusion == but:
            regles_trouvees.append(regle)

    return regles_trouvees


def est_animal_final(fait):
    return fait in ANIMAUX_FINAUX


def animaux_dans_base(base_faits):
    return [fait for fait in ANIMAUX_FINAUX if fait in base_faits]
