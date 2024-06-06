
def addition(a, b):
    """
    Cette fonction retourne la somme de deux nombres.
    """
    return a + b


def soustraction(a, b):
    """
    Cette fonction retourne la différence entre deux nombres.
    """
    return a - b


def multiplication(a, b):
    """
    Cette fonction retourne le produit de deux nombres.
    """
    return a * b


def division(a, b):
    """
    Cette fonction retourne le quotient de deux nombres.
    Si le diviseur est zéro, elle retourne 'None' et affiche  message d'erreur.
    """
    if b == 0:
        print("Erreur: Division par zéro.")
        return None
    else:
        return a / b
