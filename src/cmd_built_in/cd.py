import os

def cd(path = None):

    try :
        if path is None or path.strip() == "":
            path = os.path.expanduser("~")
        os.chdir(path)
    except FileNotFoundError:
        print(f"cd : {path}: Aucun fichier ou dossier de ce type")
    except PermissionError:
        print(f"cd : {path}: Permission refusée")
    except NotADirectoryError:
        print(f"cd : {path}: Ce n'est pas un répertoire")