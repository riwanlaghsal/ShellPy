# ShellPy
Projet de fin de semestre du module "Langage Script" en L3 Informatique parcours Administration Système en Réseaux co-réalisé avec Mehnana Ilyes. L'objectif est de développer un mini interpréteur de commandes similaire à un Shell Unix basique.

# Projet Shell Python – Rendu 1 : Noyau minimal et fonctionnalités

## Groupe
- Nom du groupe : ShellPy
- Membres :
  - Laghsal Riwan – 20233810
  - Mehnana Ilyes – 20234622

## Sujet
Développement d’un mini shell Unix en Python, capable d’être utilisé en mode interactif et en mode script, avec support progressif des fonctionnalités essentielles d’un interpréteur de commandes.

---

## 1. Fonctionnalités indispensables (noyau minimal)

| ID | Fonctionnalité | Description | Dépendances |
|----|----------------|-------------|--------------|
| #1 | Lecture d’une ligne de commande | Le shell lit une commande saisie par l’utilisateur ou issue d’un script | Aucune |
| #2 | Parsing basique | Découper la ligne en tokens (commandes + arguments) | #1 |
| #3 | Exécution de programmes externes | Permet d'exécuter des commandes comme `ls`, `cat`, `rm`, etc. | #2 |
| #4 | Commandes internes de base | Implémentation de `cd`, `if`, `for` etc. | #2 |
| #5 | Mode script | Lire un fichier et exécuter les commandes ligne par ligne | #1, #2, #3, #4 |

✅ À la fin de #1 → #5, on a un shell fonctionnel minimal.

---

## 2. Fonctionnalités additionnelles

| ID | Fonctionnalité | Description | Dépendances |
|----|----------------|-------------|--------------|
| #6 | Variables | Affectation et expansion : `VAR=val` puis `echo $VAR` | #2 |
| #7 | Redirections | `>`, `>>`, `<` pour rediriger entrée/sortie | #3 |
| #8 | Pipes | `cmd1 \| cmd2` permettant de connecter plusieurs commandes | #3, #7 |
| #9 | Gestion du background | Exécution d’un programme avec `&` sans bloquer le shell | #3 |
| #10 | Historique navigable des commandes | Mémoriser commandes précédentes et naviguer à l'aide des flèches directionelles  | #1 |
| #11 | Bannière ShellPy + clear screen | Au lancement, l’écran est nettoyé et une bannière ASCII est affichée | Aucun |
| #12 | Invite de commande personnalisée | Affichage de `ShellPy:/chemin >` en couleur au lieu de `$` | #1 |
| #13 | Commande interne `help` | Affiche la liste des commandes internes disponibles | #2 |

---

## 3. Priorisation

| Priorité | Fonctionnalités |
|----------|-----------------|
| 🎯 **Haute (obligatoire – noyau minimal)** | #1, #2, #3, #4, #5 |
| ✅ **Moyenne (fonctionnalités usuelles d’un shell)** | #6, #7, #8 |
| ⭐ **Faible (qualité de vie / extras)** | #9, #10 |

---

