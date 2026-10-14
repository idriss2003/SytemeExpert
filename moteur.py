# moteur.py

from regles import REGLES, ANIMAUX_FINAUX


def regle_applic(BF, conditions):
    return conditions.issubset(BF)


def appliq_regle(BF, regle):
    id, conditions, conclusion = regle

    if regle_applic(BF, conditions) and conclusion not in BF:
        BF.add(conclusion)
        return True

    return False


def regle_conclut(but):
    regles_trvs = []

    for regle in REGLES:
        id, conditions, conclusion = regle
        if conclusion == but:
            regles_trvs.append(regle)

    return regles_trvs


def animal_final(fait):
    return fait in ANIMAUX_FINAUX


def animaux_in_BF(BF):
    return [fait for fait in ANIMAUX_FINAUX if fait in BF]
