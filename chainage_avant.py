from regles import REGLES, ANIMAUX_FINAUX


def chainage_avant(F_init):
    BF = set(F_init)
    trace = []
    regles_dec = set()

    chang = True

    while chang:
        chang = False

        for id, conditions, conclusion in REGLES:
            if id in regles_dec:
                continue

            if conditions.issubset(BF) and conclusion not in BF:
                BF.add(conclusion)
                regles_dec.add(id)
                chang = True

                trace.append(
                    {
                        "regle": id,
                        "conditions": sorted(list(conditions)),
                        "conclusion": conclusion,
                        "base_apres": sorted(list(BF)),
                    }
                )

    animaux_trouves = [animal for animal in ANIMAUX_FINAUX if animal in BF]

    return BF, trace, animaux_trouves
