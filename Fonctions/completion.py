from Classes.Etat import Etat
from Classes.Transition import Transition

def estComplet(automate):
    """Vérifie si l'automate est complet."""
    alphabet = automate.listAlphabet
    etats = automate.listEtat
    transitions = automate.listTransition
    
    for etat in etats:
        for lettre in alphabet:
            if not any(t.etatSource == etat and t.alphabet == lettre for t in transitions):
                return False
    return True

def completerAutomate(automate):
    """Rend un automate complet s'il ne l'est pas déjà."""
    if estComplet(automate):
        print("L'automate est déjà complet.")
        return automate

    alphabet = automate.listAlphabet
    etats = automate.listEtat
    transitions = automate.listTransition

    # Créer un état "puits"
    id_puits = max(etat.idEtat for etat in etats) + 1
    etat_puits = Etat(id_puits, "Puits", "intermediaire")
    transitions_puits = []

    for lettre in alphabet:
        transitions_puits.append(Transition(len(transitions) + 1, etat_puits, etat_puits, lettre))

    # Ajouter les transitions manquantes pour chaque état
    for etat in etats:
        for lettre in alphabet:
            if not any(t.etatSource == etat and t.alphabet == lettre for t in transitions):
                transitions.append(Transition(len(transitions) + 1, etat, etat_puits, lettre))

    # Ajouter les transitions de l'état "puits"
    transitions.extend(transitions_puits)

    # Ajouter l'état "puits" à la liste des états
    etats.append(etat_puits)

    # Mise à jour des listes d'états et de transitions de l'automate
    automate.listEtat = etats
    automate.listTransition = transitions

    return automate
