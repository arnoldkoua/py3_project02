"""Dans cet exercice, on veut vérifier que l'on est bien en train d'apprendre le langage de programmation Python.
Vous devez donc à l'aide d'une structure conditionnelle simple, vérifier si le nom du 
langage de programmation contenu dans la variable "language" est bien egal a "python".

Si c'est le cas, vous affichez la phrase : Vous êtes bien en train d'apprendre le language Python."""

#Solution - Structure conditionnelle simple

language = str(input("Veuillez entrer le langage de programmation"))

print("")

if language == "Python" or language == "python":
    print("Vous êtes bien en train d'apprendre le language Python.")