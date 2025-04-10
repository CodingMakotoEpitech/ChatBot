# ChatBot détecteur d'humeur - Version simplifiée pour collégiens
# Ce programme crée un robot conversationnel qui détecte l'humeur de vos messages
# et vous répond avec un emoji approprié

# La fonction "import" permet d'utiliser des fonctionnalités supplémentaires
# Ici, on importe "random" qui permet de faire des choix aléatoires
import random

# ===== PARTIE 1: PRÉPARATION DES DONNÉES =====

# Un dictionnaire est comme une liste, mais au lieu d'utiliser des numéros (indices),
# on utilise des "clés" pour accéder aux valeurs
# Ici, on crée un dictionnaire qui associe chaque humeur à un emoji
# La syntaxe est: {"clé1": "valeur1", "clé2": "valeur2", ...}
emojis = {
    "joie": "😊",     # Quand on détecte de la joie, on affiche 😊
    "tristesse": "😢", # Quand on détecte de la tristesse, on affiche 😢
    "colère": "😡",   # Quand on détecte de la colère, on affiche 😡 
    "surprise": "😲",  # Quand on détecte de la surprise, on affiche 😲
    "neutre": "😐"    # Par défaut, si on ne détecte rien de spécial, on affiche 😐
}

# Ce dictionnaire contient les mots-clés qui nous aident à détecter l'humeur
# Pour chaque humeur, on a une liste de mots qui peuvent l'indiquer
mots_humeur = {
    "joie": ["content", "heureux", "super", "génial", "bien"],
    "tristesse": ["triste", "malheureux", "pas bien", "déçu"],
    "colère": ["énervé", "fâché", "en colère", "agacé"],
    "surprise": ["wow", "incroyable", "étonnant", "surpris"],
}

# ===== PARTIE 2: FONCTIONS =====

# Une fonction est un bloc de code qui réalise une tâche spécifique
# Ici, cette fonction prend un message et détecte quelle humeur il exprime
def detecter_humeur(message):
    # On convertit d'abord le message en minuscules pour faciliter la recherche
    # Par exemple, "CONTENT" et "content" seront traités de la même manière
    message = message.lower()
    
    # On vérifie si le message contient un des mots-clés
    # Pour chaque type d'humeur dans notre dictionnaire
    for humeur, mots in mots_humeur.items():
        # Pour chaque mot associé à cette humeur
        for mot in mots:
            # Si ce mot est présent dans le message
            if mot in message:
                # On retourne l'humeur correspondante
                return humeur
    
    # Si aucun mot-clé n'est trouvé, on considère l'humeur comme neutre
    return "neutre"

# Cette fonction principale gère toute la conversation avec l'utilisateur
def chatbot():
    # On affiche un message de bienvenue
    print("Bonjour ! Je suis un ChatBot qui détecte votre humeur. Discutons !")
    print("(Tapez 'au revoir' pour quitter)")
    
    # Cette boucle permet de continuer la conversation jusqu'à ce que l'utilisateur dise "au revoir"
    while True:
        # On demande à l'utilisateur d'écrire un message
        message = input("\nVous: ")
        
        # Si l'utilisateur écrit "au revoir", on sort de la boucle et le programme se termine
        if message.lower() == "au revoir":
            print("ChatBot: Au revoir ! À bientôt ! 👋")
            break
        
        # On utilise notre fonction pour détecter l'humeur du message
        humeur = detecter_humeur(message)
        
        # On affiche l'emoji correspondant à l'humeur détectée
        print("ChatBot:", emojis[humeur])

# ===== PARTIE 3: DÉMARRAGE DU PROGRAMME =====

# Cette condition vérifie si ce fichier est exécuté directement
# Si c'est le cas, on lance le chatbot
if __name__ == "__main__":
    chatbot()
