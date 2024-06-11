# Class Etat
class Etat:
    def __init__(self, idEtat, labelEtat, typeEtat):
        self._idEtat = idEtat
        self._labelEtat = labelEtat
        self._typeEtat = typeEtat

    #renvoie une chaîne conviviale décrivant l'objet Etat
    def __str__(self):
           return f"Etat(id={self._idEtat}, label={self._labelEtat}, typeEtat={self._typeEtat})"

    @property
    def idEtat(self):
        return self._idEtat

    @idEtat.setter
    def idEtat(self, value):
        self._idEtat = value

    @property
    def labelEtat(self):
        return self._labelEtat

    @labelEtat.setter
    def labelEtat(self, value):
        self._labelEtat = value

    @property
    def typeEtat(self):
        return self._typeEtat

    @typeEtat.setter
    def typeEtat(self, value):
        self._typeEtat = value

    def ajouterEtat(self, etat):              
        """Ajoute un état à l'automate."""
        self._listEtat.append(etat)
        if etat.typeEtat == "initial":
            self._listInitiaux.append(etat)
        elif etat.typeEtat == "final":
            self._listFinaux.append(etat)

    def modifierEtat(self, idEtat, newLabel=None, newType=None):
        """Modifie les attributs d'un état existant dans l'automate."""
        for etat in self._listEtat:
            if etat.idEtat == idEtat:
                if newLabel is not None:
                    etat.labelEtat = newLabel
                if newType is not None:
                    # Retirer l'état des listes initiaux ou finaux s'il y est présent
                    if etat.typeEtat == "initial" and etat in self._listInitiaux:
                        self._listInitiaux.remove(etat)
                    elif etat.typeEtat == "final" and etat in self._listFinaux:
                        self._listFinaux.remove(etat)

                    # Mettre à jour le type de l'état
                    etat.typeEtat = newType

                    # Ajouter l'état aux listes initiaux ou finaux si nécessaire
                    if newType == "initial":
                        self._listInitiaux.append(etat)
                    elif newType == "final":
                        self._listFinaux.append(etat)
                return
        raise ValueError(f"Etat avec id {idEtat} non trouvé")
    

    def supprimerEtat(self, idEtat):
        """Supprime un état de l'automate."""
        etatASupprimer = None
        for etat in self._listEtat:
            if etat.idEtat == idEtat:
                etatASupprimer = etat
                break
        if etatASupprimer:
            self._listEtat.remove(etatASupprimer)
            if etatASupprimer in self._listInitiaux:
                self._listInitiaux.remove(etatASupprimer)
            if etatASupprimer in self._listFinaux:
                self._listFinaux.remove(etatASupprimer)
        else:
            raise ValueError(f"Etat avec id {idEtat} non trouvé")

