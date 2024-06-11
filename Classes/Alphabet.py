# Class Alphabet
class Alphabet:
    def __init__(self, lettre):
        self.__lettre = lettre

    @property
    def lettre(self):
        return self.__lettre

    @lettre.setter
    def lettre(self, value):
        self.__lettre = value

    def ajouterAlphabet(automate, alphabet):
        automate.listAlphabet.append(alphabet)

    def supprimerAlphabet(automate, lettre):
        automate.listAlphabet = [alphabet for alphabet in automate.listAlphabet if alphabet.lettre != lettre]
        automate.listTransition = [transition for transition in automate.listTransition if transition.alphabet.lettre != lettre]

    def modifierAlphabet(automate, oldLettre, newLettre):
        for alphabet in automate.listAlphabet:
            if alphabet.lettre == oldLettre:
                alphabet.lettre = newLettre
                for transition in automate.listTransition:
                    if transition.alphabet.lettre == oldLettre:
                        transition.alphabet.lettre = newLettre
                return
        raise ValueError(f"Alphabet avec lettre '{oldLettre}' non trouvé")
