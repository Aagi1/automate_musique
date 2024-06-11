from Classes.Etat import Etat
from Classes.Alphabet import Alphabet
from Classes.Transition import Transition
from Classes.Automate import Automate
from Fonctions.lire_automate import lire_automate
from Fonctions.determinisation import est_deterministe, determiniser
from Fonctions.completion import completerAutomate
from Fonctions.minimisation import minimiser_automate
from Fonctions.dessin_aut import afficher_graphe_transition
from Fonctions.musique import generer_midi
import tkinter as tk
from tkinter import messagebox
from midiutil import MIDIFile
import pygame
import time

#Fonction lire automate 
# Exemple d'utilisation pour la phase initiale
dataset = [
    ['a', 'b', 'c', 'd', 'e'],
    [1, 2, 3, 4, 5, 6],
    [1],
    [6],
    [
        (1, 'a', 4),
        (1, 'a', 5),
        (2, 'a', 2),
        (2, 'c', 5),
        (2, 'd', 5),
        (3, 'b', 2),
        (4, 'b', 4),
        (4, 'c', 5),
        (4, 'd', 5),
        (5, 'e', 6)
    ]
]



# Exemple d'utilisation pour la phase
data = (
    ['do', 're', 'mi', 'fa', 'sol', 'la', 'si'],  # alphabet_data
    [1, 2],  # etats_data
    [1],  # etats_initiaux_data
    [2],  # etats_finaux_data
    [
        (1, 'do', 2),  # transitions_data (src, lettre, dst)
    ]
)

automate = lire_automate(dataset)

# Générer la séquence musicale
#sequence = automate.generer_sequence("ab")
#print(sequence)  # Affiche la séquence musicale générée

# Générer le fichier MIDI


#automate = lire_automate(data)
#print("Lecture de l'automate")
automate.afficherAutomate()

# Modification d'un état existant
# modifierEtat(automate, 2, newLabel="Etat2_Modified", newType="final")

# Affichage de l'automate après modification de l'état
# print("\nAutomate apres modification d'un etat:")
# automate.afficherAutomate()

# Vérification si l'automate est déterministe
#if est_deterministe(automate):
 #   print("L'automate est deterministe.")
#else:
 #   print("L'automate n'est pas deterministe.")

# Déterminiser l'automate
#automate_deterministe = determiniser(automate)
#print("Automate determinise:")
#automate_deterministe.afficherAutomate()


#Rendre l'automate complet
#automate_complet = completerAutomate(automate_deterministe)
#print("\nAutomate apres completion:")
#automate_complet.afficherAutomate()


# Minimiser l'automate
#automate_minimal = minimiser_automate(automate)
#print("\nAutomate apres minimisation:")
#automate_minimal.afficherAutomate()

# Afficher le graphe de transition
dot = afficher_graphe_transition(automate)

def generer_musique():
    texte = entree_texte.get()
    if not texte:
        messagebox.showwarning("Avertissement", "Veuillez entrer du texte.")
        return

    sequence = automate.generer_sequence(texte)
    if not sequence:
        messagebox.showerror("Erreur", "Aucun motif musical généré.")
        return

    nom_fichier = "musique_generee.mid"
    generer_midi(sequence, nom_fichier)
    messagebox.showinfo("Succès", f"Fichier MIDI généré: {nom_fichier}")

def jouer_musique():
    nom_fichier = "musique_generee.mid"
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(nom_fichier)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de lire le fichier MIDI: {str(e)}")


# Interface utilisateur avec tkinter
fenetre = tk.Tk()
fenetre.title("Générateur de Musique Automatique")

fenetre.geometry("400x300")  # Définir la taille de la fenêtre

# Ajouter des cadres pour organiser les éléments
cadre_instruction = tk.Frame(fenetre, padx=10, pady=10)
cadre_instruction.pack(pady=(20, 10))

cadre_texte = tk.Frame(fenetre, padx=10, pady=10)
cadre_texte.pack(pady=(0, 20))

cadre_boutons = tk.Frame(fenetre, padx=10, pady=10)
cadre_boutons.pack(pady=(0, 10))

# Label d'instruction
label_instruction = tk.Label(cadre_instruction, text="Entrez du texte pour générer de la musique:", font=("Helvetica", 12))
label_instruction.pack()

# Entrée de texte
entree_texte = tk.Entry(cadre_texte, width=50, font=("Helvetica", 12))
entree_texte.pack()

# Boutons de génération et de lecture
bouton_generer = tk.Button(cadre_boutons, text="Générer Musique", command=generer_musique, bg="#4CAF50", fg="white", font=("Helvetica", 12), width=15)
bouton_generer.grid(row=0, column=0, padx=10, pady=5)

bouton_jouer = tk.Button(cadre_boutons, text="Jouer Musique", command=jouer_musique, bg="#008CBA", fg="white", font=("Helvetica", 12), width=15)
bouton_jouer.grid(row=0, column=1, padx=10, pady=5)

fenetre.mainloop()