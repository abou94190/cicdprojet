# fichier: main.py

from app.function1 import addition, soustraction, multiplication, division


def afficher_menu():
    """
    Affiche le menu des opérations disponibles.
    """
    print("Choisissez l'opération:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")


def obtenir_entree():
    """
    Demande à l'utilisateur de saisir deux nombres.
    """
    a = float(input("Entrez le premier nombre: "))
    b = float(input("Entrez le deuxième nombre: "))
    return a, b


def main():
    while True:
        afficher_menu()
        choix = input("Entrez votre choix (1/2/3/4/5): ")

        if choix == '5':
            print("Merci d'avoir utilisé la calculatrice. Au revoir!")
            break

        if choix in ['1', '2', '3', '4']:
            a, b = obtenir_entree()

            if choix == '1':
                print(f"{a} + {b} = {addition(a, b)}")
            elif choix == '2':
                print(f"{a} - {b} = {soustraction(a, b)}")
            elif choix == '3':
                print(f"{a} * {b} = {multiplication(a, b)}")
            elif choix == '4':
                resultat = division(a, b)
                if resultat is not None:
                    print(f"{a} / {b} = {resultat}")

        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
