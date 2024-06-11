# Class Transition
class Transition:
    def __init__(self, idtransition, etatSource, etatDestination, alphabet):
        self._idtransition = idtransition
        self._etatSource = etatSource
        self._etatDestination = etatDestination
        self._alphabet = alphabet

    @property
    def idtransition(self):
        return self._idtransition

    @idtransition.setter
    def idtransition(self, value):
        self._idtransition = value

    @property
    def etatSource(self):
        return self._etatSource

    @etatSource.setter
    def etatSource(self, value):
        self._etatSource = value

    @property
    def etatDestination(self):
        return self._etatDestination

    @etatDestination.setter
    def etatDestination(self, value):
        self._etatDestination = value

    @property
    def alphabet(self):
        return self._alphabet

    @alphabet.setter
    def alphabet(self, value):
        self._alphabet = value

    def ajouterTransition(automate, transition):
        """Ajoute une transition à l'automate."""
        automate.listTransition.append(transition)

    def supprimerTransition(automate, idTransition):
        """Supprime une transition de l'automate."""
        automate.listTransition = [transition for transition in automate.listTransition if transition.idtransition != idTransition]

    def modifierTransition(automate, idTransition, newEtatSource=None, newEtatDestination=None, newAlphabet=None):
        """Modifie les attributs d'une transition existante dans l'automate."""
        for transition in automate.listTransition:
            if transition.idtransition == idTransition:
                if newEtatSource is not None:
                    transition.etatSource = newEtatSource
                if newEtatDestination is not None:
                    transition.etatDestination = newEtatDestination
                if newAlphabet is not None:
                    transition.alphabet = newAlphabet
                return
        raise ValueError(f"Transition avec id {idTransition} non trouvee")