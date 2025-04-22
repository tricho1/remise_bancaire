import tkinter as tk
from tkinter import filedialog

# Cacher la fenêtre principale Tkinter
root = tk.Tk()
root.withdraw()

# Ouvrir la boîte de dialogue pour sélectionner un fichier
file_path = filedialog.askopenfilename(
    title="Sélectionnez un fichier texte",
    filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
)

# Vérification et affichage du chemin
if file_path:
    
    input = file_path

    output = input.replace(".txt", "_modifiee.txt")

    # Caractères ASCII à ajouter
    SOH = chr(1)  # Début du fichier
    STX = chr(2) # Fin du fichier
    
    try:
        # Lecture de la remise bancaire
        with open(input, 'r', encoding='utf-8') as f:
            fichier = f.read()
        
        # Ajout des caractères ASCII
        fichier_modifie = SOH + fichier + STX
        
        # Écriture dans le fichier de sortie
        with open(output, 'w', encoding='utf-8') as f:
            f.write(fichier_modifie)
            
        print(f"Le fichier a été modifié avec succès. Résultat sauvegardé dans : {output}")
        
    except FileNotFoundError:
        print(f"Erreur : Le fichier {input} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")
else:
    print("Aucun fichier sélectionné.")

