import os

def func_if(condition_type, condition1, condition2, negation):

    #tests sur les repertoires
    if condition_type == "-e":              #si le repertoire existe
        return os.path.exists(condition1)
    elif condition_type == "-d":            #si le repertoire est un dossier
        return os.path.isdir(condition1)
    elif condition_type == "-f":            #si le repertoire est un fichier
        return os.path.isfile(condition1)
    elif condition_type == "-r":            #si le fichier est lisible
        return os.access(condition1, os.R_OK)
    elif condition_type == "-w":            #si le fichier est ecrivable
        return os.access(condition1, os.W_OK)
    elif condition_type == "-x":            #si le fichier est executable
        return os.access(condition1, os.X_OK)

    #tests sur les chaines
    elif condition_type == "-z":
        return len(str(condition1)) == 0
    elif condition_type == "-n":
        return len(str(condition1)) > 0
    elif condition_type == "=":
        return str(condition1) == str(condition2)
    elif condition_type == "!=":
        return str(condition1) != str(condition2)

    #tests numeriques
    elif condition_type == "-eq":
        return str(condition1) == str(condition2)
    elif condition_type == "-ne":
        return str(condition1) != str(condition2)
    elif condition_type == "-gt":
        return str(condition1) > str(condition2)
    elif condition_type == "-lt":
        return str(condition1) < str(condition2)
    elif condition_type == "-ge":
        return str(condition1) >= str(condition2)
    elif condition_type == "-le":
        return str(condition1) <= str(condition2)

    #manque la negation et les combinaisons logiques