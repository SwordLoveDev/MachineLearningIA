import math
import csv
import random

def constructionBase():
  with open("iris.data","r")as fichier:
    reader = csv.reader(fichier)
    listeApprentissage = []
    listeTest = []
    for i in reader:
      x = random.randint(0,150)
      if x <= 67:
        listeApprentissage.append(i)
      else:
        listeTest.append(i)
  return listeApprentissage, listeTest

data = constructionBase()

def distanceEuclidienne(instance1, instance2, nb_caracteristiques):
  d=0
  for i in range(0,nb_caracteristiques):
    d+=(float(instance1[i])-float(instance2[i]))**2
  return math.sqrt(d)

def kppv(apprentissage, test, k):
  tmp = []
  tmp2 = []
  resultat = []
  for x in range(len(apprentissage)):
    compteur = distanceEuclidienne(apprentissage[x], test, 4)
    tmp.append([compteur, x])
  for x in range(k):
    minimum = min(tmp)
    emplacement = tmp.index(minimum)
    tmp2.append(minimum)
    del tmp[emplacement]
  for x in range(k):
    position = tmp2[x][1]
    resultat.append(apprentissage[position])
  return resultat

def predire(kppv):
  choix = ["Iris-setosa","Iris-versicolor","Iris-virginica"]
  compteur = [[0],[0],[0]]
  for x in range(len(kppv)):
    if kppv[x][4] == "Iris-setosa":
      compteur[0][0] += 1
    elif kppv[x][4] == "Iris-versicolor":
      compteur[1][0] += 1
    else:
      compteur[2][0] += 1
  tmp = max(compteur)
  position = compteur.index(tmp)
  return choix[position]

def pourcentage(listeTest, k):
  compteur = 0
  for x in range(len(listeTest)):
    valeur = listeTest[x][4]
    tmp = predire(kppv(data[0], listeTest[x], k))
    if valeur == tmp:
      compteur += 1
  return (compteur / len(listeTest)) * 100

def main():
  testPrecision = input("Voulez-vous tester la précision de l'algorithm (oui/non) : ")
  if testPrecision == "oui":
    nombreKppv = int(input("Nombre de k voisin maximal : "))
    for x in range(1, nombreKppv + 1):
      compteur = 0
      for i in range(100):
        compteur += pourcentage(data[1], x)
      print("Pour", x, "voisins, la prédiction est de", compteur/100, "% de réussite")
  testPrediction = data[1][random.randint(0,len(data[1][0]))]
  print("Voici un test de prédiction avec une valeur aléatoire tiré du fichier iris.data, l'algo n'aura que les valeur décimal et non directement le nom de la fleur evidemment.")
  nombreKppv = 0
  nombreKppv = int(input("Nombre de k voisin pour le test de prédiction : "))
  print("Voici l'échantillon de la fleur :", testPrediction,". L'algo va donc essayer de prédire le nom de la fleur.")
  print("Prédiction en cour ...")
  print(predire(kppv(data[0], testPrediction, 5)))


main()