#Importation de la bibliothèque graphviz
from graphviz import Digraph

#Définition de la fonction afficher_graphe_transition : 
#La fonction afficher_graphe_transition prend en paramètre un objet automate et initialise un objet Digraph nommé dot.
def afficher_graphe_transition(automate):
    dot = Digraph()

    # Ajouter les noeuds
    for etat in automate.listEtat:
        shape = 'doublecircle' if etat in automate.listFinaux else 'circle'
        # Ajouter une flèche de début à l'état initial
        if etat in automate.listInitiaux:
            dot.node(str(etat.idEtat), shape=shape, style='filled', fillcolor='yellow')
        else:
            dot.node(str(etat.idEtat), shape=shape)

    # Ajouter les transitions
    for transition in automate.listTransition:
        dot.edge(str(transition.etatSource.idEtat), str(transition.etatDestination.idEtat), label=transition.alphabet.lettre)

    # Afficher le graphe
    dot.render('automate', format='png', view=True)
