from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import tkinter as tk
from tkinter import messagebox 
import os


def valider(espace):  # Récupérer les valeurs saisies par l'utilisateur
    
    def erreur ():
            try:
                driver.close()
            except:
                pass
    # En cas d'erreur, afficher un message d'erreur graphique
            messagebox.showerror("Erreur de Connexion", "Vérifiez vos informations de connexion à votre espace")
            # Réinitialiser les champs de saisie pour permettre à l'utilisateur de réessayer
            
            fenetre.mainloop()
    
    utilisateur = champ_utilisateur.get()
    mot_de_passe = champ_mot_de_passe.get()
    
    if utilisateur == '':
        erreur()
    elif mot_de_passe == '':
        erreur()
    else:
        edge_options = webdriver.EdgeOptions()

        driver = webdriver.Edge(options=edge_options)
        
        driver.get('https://pierre-brossolette-le-perreux-sur-marne.moncollege.valdemarne.fr/')
        os.startfile('a.bat')
        time.sleep(0.2)

        # bouton se conecter
        element = driver.find_element(By.XPATH, '/html/body/div/div/div/div/a[2]')
        element.click()
        time.sleep(0.1)
        #choix entre les categorie
        element = driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/div/div/form/div[1]/div/label')
        element.click()
        element = driver.find_element(By.XPATH, '//*[@id="button-submit"]')
        element.click()
        time.sleep(0.1)
        if espace == 'eleve':
            element = driver.find_element(By.XPATH, '//*[@id="bouton_eleve"]')
            element.click()
        elif espace == 'parent':
            element = driver.find_element(By.XPATH, '//*[@id="bouton_responsable"]')
            element.click()
        try:
            # user
            element = driver.find_element(By.XPATH, '//*[@id="username"]')
            element.click()
            element.send_keys(utilisateur)
            #pasword
            element = driver.find_element(By.XPATH, '//*[@id="password"]')
            element.click()
            element.send_keys(mot_de_passe)
            
            #valide
            element = driver.find_element(By.XPATH, '//*[@id="bouton_valider"]')
            element.click()
            try:
                #code pour la premiere conection
                element = driver.find_element(By.XPATH, '//*[@id="panel-v8"]/p[1]/label')
                element.click()
                time.sleep(0.5)
                element = driver.find_element(By.XPATH, '//*[@id="panel-v8"]/p[2]/input')
                element.click()
                time.sleep(0.5)
                
                
            except:
                pass

            element = driver.find_element(By.XPATH, '/html/body/div[1]/button')
            element.click()
            time.sleep(1)
            if espace == 'eleve':
                element = driver.find_element(By.XPATH, '/html/body/div[1]/nav/ul[3]/li[4]/button')
                element.click()
            elif espace == 'parent':
                element = driver.find_element(By.XPATH, '/html/body/div[1]/nav/ul[3]/li[3]/button')
                element.click()
                
            time.sleep(1)
            element = driver.find_element(By.XPATH, '//*[@id="2"]/li[2]/a')
            element.click() 
            fenetre.destroy()
            os.startfile('a.bat')
            while True:
                   pass
        except:
            erreur()
    


fenetre = tk.Tk()
fenetre.title("Connexion")
fenetre.geometry('400x300')
fenetre.iconbitmap('unnamed.ico')

etiquette_mot_de_passe = tk.Label(fenetre, text=" ")
etiquette_mot_de_passe.pack()

etiquette_mot_de_passe = tk.Label(fenetre, text=" ")
etiquette_mot_de_passe.pack()

etiquette_utilisateur = tk.Label(fenetre, text="Nom d'utilisateur:")
etiquette_utilisateur.pack()

champ_utilisateur = tk.Entry(fenetre)
champ_utilisateur.pack()

etiquette_mot_de_passe = tk.Label(fenetre, text=" ")
etiquette_mot_de_passe.pack()

etiquette_mot_de_passe = tk.Label(fenetre, text="Mot de passe:")
etiquette_mot_de_passe.pack()

champ_mot_de_passe = tk.Entry(fenetre, show="**")  # Le mot de passe est masqué
champ_mot_de_passe.pack()

etiquette_mot_de_passe = tk.Label(fenetre, text=" ")
etiquette_mot_de_passe.pack()

# Créer un bouton de connexion en tant que parent
# Créer un bouton de connexion en tant que parent
bouton_connexion_parent = tk.Button(fenetre, text="Se connecter en tant que parent ", command=lambda: valider('parent'))
bouton_connexion_parent.pack()

# Créer un bouton de connexion en tant qu'élève
bouton_connexion_eleve = tk.Button(fenetre, text="Se connecter en tant qu'élève ", command=lambda: valider('eleve'))
bouton_connexion_eleve.pack()


# Exécuter la boucle principale de l'interface graphique
fenetre.mainloop()




