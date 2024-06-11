from Classes.Etat import Etat
from Classes.Alphabet import Alphabet
from Classes.Transition import Transition
from Classes.Automate import Automate

# Fonction pour minimiser l'automate
def minimiser_automate(automate):
    # Étape 1: Déterminer les états accessibles
    def etats_accessibles(etat_initial, transitions):
        accessibles = set()
        a_traiter = [etat_initial]
        while a_traiter:
            etat = a_traiter.pop()
            if etat not in accessibles:
                accessibles.add(etat)
                for transition in transitions:
                    if transition.etatSource == etat and transition.etatDestination not in accessibles:
                        a_traiter.append(transition.etatDestination)
        return accessibles

    accessibles = etats_accessibles(automate.listInitiaux[0], automate.listTransition)
    etats = [etat for etat in automate.listEtat if etat in accessibles]
    transitions = [t for t in automate.listTransition if t.etatSource in accessibles and t.etatDestination in accessibles]
    etats_finaux = [etat for etat in automate.listFinaux if etat in accessibles]

    # Étape 2: Déterminer les états équivalents
    def etats_equivalents(etats, etats_finaux, alphabet, transitions):
        non_finaux = [etat for etat in etats if etat not in etats_finaux]
        partitions = [set(etats_finaux), set(non_finaux)]

        def trouver_partitions(etat, partitions):
            for i, part in enumerate(partitions):
                if etat in part:
                    return i
            return -1

        stable = False
        while not stable:
            stable = True
            nouvelle_partition = []
            for part in partitions:
                sous_partitions = {}
                for etat in part:
                    signature = []
                    for lettre in alphabet:
                        dest = next((t.etatDestination for t in transitions if t.etatSource == etat and t.alphabet == lettre), None)
                        signature.append(trouver_partitions(dest, partitions))
                    signature = tuple(signature)
                    if signature not in sous_partitions:
                        sous_partitions[signature] = set()
                    sous_partitions[signature].add(etat)
                if len(sous_partitions) > 1:
                    stable = False
                    for sous_part in sous_partitions.values():
                        nouvelle_partition.append(sous_part)
                else:
                    nouvelle_partition.append(part)
            partitions = nouvelle_partition
        return partitions

    partitions = etats_equivalents(etats, etats_finaux, automate.listAlphabet, transitions)
    etat_partition = {etat: i for i, part in enumerate(partitions) for etat in part}

    # Étape 3: Construire l'automate minimal
    etats_minimaux = [Etat(i, f"Etat_{i}", "intermediaire") for i in range(len(partitions))]
    etat_initial_minimal = etats_minimaux[etat_partition[automate.listInitiaux[0]]]
    etats_finaux_minimaux = [etats_minimaux[i] for i, part in enumerate(partitions) if any(etat in etats_finaux for etat in part)]
    transitions_minimales = []

    for transition in transitions:
        nouvelle_src = etats_minimaux[etat_partition[transition.etatSource]]
        nouvelle_dst = etats_minimaux[etat_partition[transition.etatDestination]]
        nouvelles_transitions = [t for t in transitions_minimales if t.etatSource == nouvelle_src and t.alphabet == transition.alphabet]
        if not nouvelles_transitions:
            transitions_minimales.append(Transition(len(transitions_minimales) + 1, nouvelle_src, nouvelle_dst, transition.alphabet))

    nouvel_automate = Automate(
        etats_minimaux,
        automate.listAlphabet,
        [etat_initial_minimal],
        etats_finaux_minimaux,
        transitions_minimales
    )

    return nouvel_automate