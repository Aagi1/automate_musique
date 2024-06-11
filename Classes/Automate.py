# Class Automate
from Fonctions.char import char_to_music

class Automate:
    def __init__(self, listEtat, listAlphabet, listInitiaux, listFinaux, listTransition):
        self._listEtat = listEtat
        self._listAlphabet = listAlphabet
        self._listInitiaux = listInitiaux
        self._listFinaux = listFinaux
        self._listTransition = listTransition
        self._etat_courant = listInitiaux[0] if listInitiaux else None 
        
    @property
    def listEtat(self):
        return self._listEtat

    @listEtat.setter
    def listEtat(self, value):
        self._listEtat = value

    @property
    def listAlphabet(self):
        return self._listAlphabet

    @listAlphabet.setter
    def listAlphabet(self, value):
        self._listAlphabet = value

    @property
    def listInitiaux(self):
        return self._listInitiaux

    @listInitiaux.setter
    def listInitiaux(self, value):
        self._listInitiaux = value

    @property
    def listFinaux(self):
        return self._listFinaux

    @listFinaux.setter
    def listFinaux(self, value):
        self._listFinaux = value

    @property
    def listTransition(self):
        return self._listTransition

    @listTransition.setter
    def listTransition(self, value):
        self._listTransition = value

    #fonction afficher automate 
    def afficherAutomate(self):
        print("Etats:")
        for etat in self.listEtat:
            print(f"  ID: {etat.idEtat}, Label: {etat.labelEtat}, Type: {etat.typeEtat}")
        print("Etats initiaux:")
        for etat in self.listInitiaux:
            print(f"  ID: {etat.idEtat}, Label: {etat.labelEtat}, Type: {etat.typeEtat}")
        print("Etats finaux:")
        for etat in self.listFinaux:
            print(f"  ID: {etat.idEtat}, Label: {etat.labelEtat}, Type: {etat.typeEtat}")
        print("Transitions:")
        for t in self.listTransition:
            print(f"  {t.etatSource.idEtat} --> {t.alphabet.lettre} --> {t.etatDestination.idEtat}")

    #a comprendre 
    def generer_sequence(self, texte):
        sequence = []
        for char in texte:
            if char in char_to_music:
                accord, rythme = char_to_music[char]
                etat_actuel = self._etat_courant
                self.transition(accord)  # Utilise l'accord comme signal de transition
                sequence.append((etat_actuel, accord, rythme))
        return sequence

    def etat_actuel(self):
        return self._etat_courant

    def transition(self, lettre):
        for t in self._listTransition:
            if t.etatSource == self._etat_courant and t.alphabet.lettre == lettre:
                self._etat_courant = t.etatDestination
                break

    
