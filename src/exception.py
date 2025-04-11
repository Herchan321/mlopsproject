import sys  # Module qui permet d'accéder à des informations sur les erreurs, les arguments, etc.
import logging
# 🔧 Fonction pour créer un message d'erreur détaillé
def error_message_detail(error, error_detail: sys):
    # Récupère les infos sur l'exception en cours
    _, _, exc_tb = error_detail.exc_info()

    # Nom du fichier où l'erreur s'est produite
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Crée un message détaillé : nom du fichier, ligne, et message d'erreur
    error_message = "Erreur dans le fichier [{0}], ligne [{1}], message : [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


# 🎯 Classe personnalisée d'exception
class customException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # 🛠️ Appel du constructeur de la classe mère Exception
        super().__init__(error_message)  # 🟢 CORRIGÉ ici ! (tu avais mis `super.__init__`)

        # On crée un message d'erreur détaillé à partir de l'erreur capturée
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    # 🔁 Quand on affiche l'exception avec str(), on retourne le message détaillé
    def __str__(self):
        return str(self.error_message)



