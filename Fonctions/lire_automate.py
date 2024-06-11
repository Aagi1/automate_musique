from Classes.Etat import Etat
from Classes.Alphabet import Alphabet
from Classes.Transition import Transition
from Classes.Automate import Automate

def lire_automate(data):
    alphabet_data, etats_data, etats_initiaux_data, etats_finaux_data, transitions_data = data

    # Création des objets Alphabet
    alphabets = [Alphabet(lettre) for lettre in alphabet_data]

    # Création des objets Etat
    etats = []
    for idEtat in etats_data:
        etat_types = []
        if idEtat in etats_initiaux_data:
            etat_types.append("initial")
        if idEtat in etats_finaux_data:
            etat_types.append("final")
        if not etat_types:
            etat_types.append("intermediaire")
        etats.append(Etat(idEtat, f"Etat_{idEtat}", " + ".join(etat_types)))

    # Définir les états initiaux et finaux
    etats_initiaux = [etat for etat in etats if etat.idEtat in etats_initiaux_data]
    etats_finaux = [etat for etat in etats if etat.idEtat in etats_finaux_data]

    # Création des objets Transition
    transitions = []
    for idx, (src, lettre, dst) in enumerate(transitions_data):
        etatSource = next((etat for etat in etats if etat.idEtat == src), None)
        etatDestination = next((etat for etat in etats if etat.idEtat == dst), None)
        alphabet = next((alpha for alpha in alphabets if alpha.lettre == lettre), None)
        transitions.append(Transition(idx + 1, etatSource, etatDestination, alphabet))

    # Création de l'automate
    automate = Automate(etats, alphabets, etats_initiaux, etats_finaux, transitions)

    return automate
