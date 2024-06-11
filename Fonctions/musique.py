from midiutil import MIDIFile
from tkinter import messagebox
import pygame
import time

def generer_midi(sequence, fichier_sortie):
    # Création d'un objet MIDIFile
    midi = MIDIFile(1)  # Un seul piste
    piste = 0
    temps = 0  # En temps de battements
    canal = 0
    volume = 100

    # Ajouter une piste de musique
    midi.addTrackName(piste, temps, "Automate Track")
    midi.addTempo(piste, temps, 120)

    # Ajouter les notes de la séquence à la piste
    note_map = {
        'do': 60,  # Note C4
        're': 62,  # Note D4
        'mi': 64,  # Note E4
        'fa': 65,  # Note F4
        'sol': 67, # Note G4
        'la': 69,  # Note A4
        'si': 71   # Note B4
    }

    for etat, note, rythme in sequence:
        note_number = note_map[note]
        duree = rythme
        midi.addNote(piste, canal, note_number, temps, duree, volume)
        temps += duree

    # Écrire le fichier MIDI sur le disque
    with open(fichier_sortie, "wb") as sortie:
        midi.writeFile(sortie)

