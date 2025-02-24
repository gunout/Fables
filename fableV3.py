import turtle
import time

# Configuration de la fenêtre
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")
screen.title("Le Corbeau et le Renard - Jean de La Fontaine")

# Fonction pour dessiner un arbre
def dessiner_arbre(x, y):
    arbre = turtle.Turtle()
    arbre.hideturtle()
    arbre.penup()
    arbre.goto(x, y)
    arbre.pendown()
    arbre.color("brown")
    arbre.begin_fill()
    for _ in range(2):
        arbre.forward(40)
        arbre.left(90)
        arbre.forward(100)
        arbre.left(90)
    arbre.end_fill()
    arbre.penup()
    arbre.goto(x - 30, y + 100)
    arbre.pendown()
    arbre.color("green")
    arbre.begin_fill()
    arbre.circle(50)
    arbre.end_fill()

# Dessiner un arbre
dessiner_arbre(-250, -50)

# Création du corbeau
corbeau = turtle.Turtle()
corbeau.shape("circle")
corbeau.color("black")
corbeau.shapesize(2, 2)  # Taille du corbeau
corbeau.penup()
corbeau.goto(-200, 100)
corbeau.pendown()

# Création du fromage
fromage = turtle.Turtle()
fromage.shape("square")
fromage.color("yellow")
fromage.shapesize(1, 1)  # Taille du fromage
fromage.penup()
fromage.goto(-200, 120)
fromage.pendown()

# Création du renard
renard = turtle.Turtle()
renard.shape("triangle")
renard.color("orange")
renard.shapesize(2, 2)  # Taille du renard
renard.penup()
renard.goto(200, -100)
renard.pendown()

# Texte de la fable
texte = turtle.Turtle()
texte.hideturtle()
texte.penup()
texte.goto(0, 200)
texte.color("black")

# Fonction pour afficher le texte
def afficher_texte(message, delay=2):
    texte.clear()
    texte.write(message, align="center", font=("Arial", 16, "normal"))
    time.sleep(delay)

# Animation de la fable
afficher_texte("Le Corbeau et le Renard", 2)

# Le corbeau tient le fromage
afficher_texte("Maître Corbeau, sur un arbre perché,", 2)
corbeau.goto(-200, 100)
fromage.goto(-200, 120)

# Le renard arrive
afficher_texte("Tenait en son bec un fromage.", 2)
renard.goto(200, -100)

# Le renard flatte le corbeau
afficher_texte("Maître Renard, par l'odeur alléché,", 2)
renard.goto(0, -100)
afficher_texte("Lui tint à peu près ce langage :", 2)

# Le renard parle
afficher_texte("Et bonjour, Monsieur du Corbeau.", 2)
renard.goto(-50, -100)
afficher_texte("Que vous êtes joli ! Que vous me semblez beau !", 2)

# Le corbeau ouvre le bec
afficher_texte("Sans mentir, si votre ramage", 2)
corbeau.goto(-200, 100)
corbeau.shape("circle")
afficher_texte("Se rapporte à votre plumage,", 2)

# Le fromage tombe
afficher_texte("Vous êtes le Phénix des hôtes de ces bois.", 2)
fromage.goto(-200, -100)
time.sleep(1)

# Le renard attrape le fromage
afficher_texte("À ces mots, le Corbeau ne se sent pas de joie ;", 2)
renard.goto(-200, -100)
fromage.hideturtle()
afficher_texte("Et pour montrer sa belle voix,", 2)

# Le corbeau ouvre le bec et le fromage tombe
afficher_texte("Il ouvre un large bec, laisse tomber sa proie.", 2)
corbeau.shape("circle")
afficher_texte("Le Renard s'en saisit, et dit : Mon bon Monsieur,", 2)

# Le renard s'en va avec le fromage
afficher_texte("Apprenez que tout flatteur", 2)
renard.goto(200, -100)
afficher_texte("Vit aux dépens de celui qui l'écoute.", 2)

# Fin de l'animation
afficher_texte("Cette leçon vaut bien un fromage, sans doute.", 2)
afficher_texte("Fin.", 2)

# Fermer la fenêtre au clic
screen.exitonclick()
