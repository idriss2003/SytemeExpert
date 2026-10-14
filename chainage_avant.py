from regles import REGLES, ANIMAUX_FINAUX


def chainage_avant(faits_initiaux):
    base_faits = set(faits_initiaux)
    trace = []
    regles_declenchees = set()

    changement = True

    while changement:
        changement = False

        for identifiant, conditions, conclusion in REGLES:
            if identifiant in regles_declenchees:
                continue

            if conditions.issubset(base_faits) and conclusion not in base_faits:
                base_faits.add(conclusion)
                regles_declenchees.add(identifiant)
                changement = True

                trace.append(
                    {
                        "regle": identifiant,
                        "conditions": sorted(list(conditions)),
                        "conclusion": conclusion,
                        "base_apres": sorted(list(base_faits)),
                    }
                )

    animaux_trouves = [animal for animal in ANIMAUX_FINAUX if animal in base_faits]

    return base_faits, trace, animaux_trouves
