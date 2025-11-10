# ShellPy
Projet de fin de semestre du module "Langage Script" en L3 Informatique parcours Administration Système en Réseaux co-réalisé avec Mehnana Ilyes. L'objectif est de développer un mini interpréteur de commandes similaire à un Shell Unix basique.

# Projet Shell Python – Rendu 1 : Noyau minimal et fonctionnalités

## Groupe
- Nom du groupe : D. Xebec
- Membres :
  - Laghsal Riwan – 20233810
  - Mehnana Ilyes – 20234622

## Sujet
Développement d’un mini shell Unix en Python, capable d’être utilisé en mode interactif et en mode script, avec support progressif des fonctionnalités essentielles d’un interpréteur de commandes.

---

## 1. Fonctionnalités indispensables (noyau minimal)

| ID | Fonctionnalité | Description | Dépendances |
|----|----------------|-------------|--------------|
| #1 | Lecture d'une ligne de commane - Parsing basique | Découper la ligne en tokens (commandes + arguments) | Aucune |
| #2 | Exécution de programmes externes | Permet d'exécuter des commandes comme `ls`, `cat`, `rm`, etc. | #1 |
| #3 | Commandes internes de base | Implémentation de `cd`, `if`, `for` etc. | #1 |

✅ À la fin de #1 → #5, on a un shell fonctionnel minimal.

---

## 2. Fonctionnalités additionnelles

| ID | Fonctionnalité | Description | Dépendances |
|----|----------------|-------------|--------------|
| #4 | Variables | Affectation et expansion : `VAR=val` puis `echo $VAR` | #1 |
| #5 | Redirections | `>`, `>>`, `<` pour rediriger entrée/sortie | #2 |
| #6 | Pipes | `cmd1 \| cmd2` permettant de connecter plusieurs commandes | #2, #5 |
| #7 | Gestion du background | Exécution d’un programme avec `&` sans bloquer le shell (usage de `fork()`) | #2 |
| #8 | Mode script | Lire un fichier et exécuter les commandes ligne par ligne | #1, #2, #3 |
| #9 | Commande interne `help` | Affiche la liste des commandes internes disponibles | #1, #3 |
| #10 | Historique navigable des commandes | Mémoriser commandes précédentes et naviguer à l'aide des flèches directionelles  | #1 |
| #11 | Bannière ShellPy + clear screen | Au lancement, l’écran est nettoyé et une bannière ASCII est affichée | Aucun |
| #12 | Invite de commande personnalisée | Affichage de `ShellPy:/chemin >` en couleur au lieu de `$` | #1 |

---

## 3. Priorisation

| Priorité | Fonctionnalités |
|----------|-----------------|
| 🎯 **Haute (obligatoire – noyau minimal)** | #1, #2, #3|
| ✅ **Moyenne (fonctionnalités usuelles d’un shell)** | #4, #5, #6, #7, #8 |
| ⭐ **Faible (extras / confort utilisateur)** | #9, #10, #11, #12 |

---

