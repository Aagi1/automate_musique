from Classes.Etat import Etat
from Classes.Alphabet import Alphabet
from Classes.Transition import Transition
from Classes.Automate import Automate


def est_deterministe(automate):
        """Vérifie si un automate est déterministe."""
        # Vérifier qu'il n'y a qu'un seul état initial
        if len(automate.listInitiaux) != 1:
            return False

        # Vérifier que chaque état a au plus une transition pour chaque symbole de l'alphabet
        transitions_par_etat = {}
        for transition in automate.listTransition:
            if (transition.etatSource.idEtat, transition.alphabet.lettre) in transitions_par_etat:
                return False
            transitions_par_etat[(transition.etatSource.idEtat, transition.alphabet.lettre)] = transition.etatDestination.idEtat

        return True


def determiniser(automate):
    # Créer un mapping pour les états composites
    etats_composites = {}
    nouvelles_transitions = []

    # Initialiser l'état initial du nouvel automate
    etats_initiaux = [etat for etat in automate.listEtat if etat.typeEtat == "initial"]
    etat_initial_composite = frozenset(etats_initiaux)
    etats_composites[etat_initial_composite] = Etat(0, f"{{{','.join(str(etat.idEtat) for etat in etat_initial_composite)}}}", "initial")

    # Utiliser une liste pour traiter les nouveaux états trouvés
    a_traiter = [etat_initial_composite]
    traites = set()

    while a_traiter:
        courant = a_traiter.pop()
        if courant in traites:
            continue
        traites.add(courant)

        for alphabet in automate.listAlphabet:
            etats_suivants = set()
            for etat in courant:
                for transition in automate.listTransition:
                    if transition.etatSource == etat and transition.alphabet == alphabet:
                        etats_suivants.add(transition.etatDestination)

            if not etats_suivants:
                continue

            etat_composite_suivant = frozenset(etats_suivants)
            if etat_composite_suivant not in etats_composites:
                nouvel_id = len(etats_composites)
                type_etat = "intermediaire"
                if any(etat.typeEtat == "final" for etat in etats_suivants):
                    type_etat = "final"
                if any(etat.typeEtat == "initial" for etat in etats_suivants):
                    type_etat += "+initial"
                label = f"{{{','.join(str(etat.idEtat) for etat in etat_composite_suivant)}}}"
                etats_composites[etat_composite_suivant] = Etat(nouvel_id, label, type_etat)
                a_traiter.append(etat_composite_suivant)

            nouvelles_transitions.append(Transition(len(nouvelles_transitions) + 1, etats_composites[courant], etats_composites[etat_composite_suivant], alphabet))

    # Créer les nouvelles listes d'états et de transitions
    nouveaux_etats = list(etats_composites.values())
    etat_initial = etats_composites[etat_initial_composite]
    etats_finaux = [etat for etat in nouveaux_etats if "final" in etat.typeEtat]

    nouvel_automate = Automate(nouveaux_etats, automate.listAlphabet, [etat_initial], etats_finaux, nouvelles_transitions)
    
    return nouvel_automate
