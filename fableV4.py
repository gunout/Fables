import turtle
import time

# Configuration de la fenêtre
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")
screen.title("Le Corbeau et le Renard - Jean de La Fontaine")

# Fonction pour dessiner un arbre réaliste
def dessiner_arbre(x, y):
    # Tronc de l'arbre
    tronc = turtle.Turtle()
    tronc.hideturtle()
    tronc.penup()
    tronc.goto(x, y)
    tronc.pendown()
    tronc.color("saddlebrown")
    tronc.begin_fill()
    for _ in range(2):
        tronc.forward(40)
        tronc.left(90)
        tronc.forward(100)
        tronc.left(90)
    tronc.end_fill()

    # Feuillage de l'arbre
    feuillage = turtle.Turtle()
    feuillage.hideturtle()
    feuillage.penup()
    feuillage.goto(x - 50, y + 100)
    feuillage.pendown()
    feuillage.color("forestgreen")
    feuillage.begin_fill()
    feuillage.circle(60)
    feuillage.end_fill()

# Fonction pour dessiner le sol
def dessiner_sol():
    sol = turtle.Turtle()
    sol.hideturtle()
    sol.penup()
    sol.goto(-400, -150)
    sol.pendown()
    sol.color("green")
    sol.begin_fill()
    for _ in range(2):
        sol.forward(800)
        sol.right(90)
        sol.forward(300)
        sol.right(90)
    sol.end_fill()

# Fonction pour dessiner des nuages
def dessiner_nuage(x, y):
    nuage = turtle.Turtle()
    nuage.hideturtle()
    nuage.penup()
    nuage.goto(x, y)
    nuage.pendown()
    nuage.color("white")
    nuage.begin_fill()
    nuage.circle(30)
    nuage.end_fill()
    nuage.penup()
    nuage.goto(x + 40, y)
    nuage.pendown()
    nuage.begin_fill()
    nuage.circle(40)
    nuage.end_fill()
    nuage.penup()
    nuage.goto(x + 80, y)
    nuage.pendown()
    nuage.begin_fill()
    nuage.circle(30)
    nuage.end_fill()

# Fonction pour dessiner un corbeau
def dessiner_corbeau(x, y):
    corbeau = turtle.Turtle()
    corbeau.hideturtle()
    corbeau.penup()
    corbeau.goto(x, y)
    corbeau.pendown()
    corbeau.color("black")
    corbeau.begin_fill()
    corbeau.circle(20)  # Corps du corbeau
    corbeau.end_fill()
    corbeau.penup()
    corbeau.goto(x - 15, y + 30)
    corbeau.pendown()
    corbeau.begin_fill()
    corbeau.circle(10)  # Tête du corbeau
    corbeau.end_fill()
    corbeau.penup()
    corbeau.goto(x - 25, y + 40)
    corbeau.pendown()
    corbeau.color("orange")
    corbeau.begin_fill()
    corbeau.circle(5)  # Bec du corbeau
    corbeau.end_fill()
    return corbeau

# Fonction pour dessiner un renard
def dessiner_renard(x, y):
    renard = turtle.Turtle()
    renard.hideturtle()
    renard.penup()
    renard.goto(x, y)
    renard.pendown()
    renard.color("orange")
    renard.begin_fill()
    renard.circle(30)  # Corps du renard
    renard.end_fill()
    renard.penup()
    renard.goto(x - 20, y + 40)
    renard.pendown()
    renard.begin_fill()
    renard.circle(15)  # Tête du renard
    renard.end_fill()
    renard.penup()
    renard.goto(x - 30, y + 50)
    renard.pendown()
    renard.color("black")
    renard.begin_fill()
    renard.circle(5)  # Nez du renard
    renard.end_fill()
    return renard

# Fonction pour dessiner un fromage
def dessiner_fromage(x, y):
    fromage = turtle.Turtle()
    fromage.hideturtle()
    fromage.penup()
    fromage.goto(x, y)
    fromage.pendown()
    fromage.color("yellow")
    fromage.begin_fill()
    for _ in range(2):
        fromage.forward(40)
        fromage.left(90)
        fromage.forward(20)
        fromage.left(90)
    fromage.end_fill()
    return fromage

# Fonction pour animer le renard
def animer_renard(renard, start_x, start_y, end_x, end_y):
    renard.penup()
    renard.goto(start_x, start_y)
    renard.pendown()
    renard.showturtle()
    for _ in range(50):
        renard.goto(renard.xcor() + (end_x - start_x) / 50, renard.ycor() + (end_y - start_y) / 50)
        time.sleep(0.05)

# Fonction pour animer le fromage qui tombe
def animer_fromage(fromage, start_x, start_y, end_x, end_y):
    fromage.penup()
    fromage.goto(start_x, start_y)
    fromage.pendown()
    fromage.showturtle()
    for _ in range(50):
        fromage.goto(fromage.xcor() + (end_x - start_x) / 50, fromage.ycor() + (end_y - start_y) / 50)
        time.sleep(0.05)

# Dessiner le sol
dessiner_sol()

# Dessiner un arbre réaliste
dessiner_arbre(-250, -50)

# Dessiner des nuages
dessiner_nuage(-300, 200)
dessiner_nuage(100, 250)

# Dessiner le corbeau
corbeau = dessiner_corbeau(-200, 100)

# Dessiner le fromage
fromage = dessiner_fromage(-200, 120)

# Dessiner le renard
renard = dessiner_renard(200, -100)

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

# Le renard arrive
afficher_texte("Tenait en son bec un fromage.", 2)
animer_renard(renard, 200, -100, 0, -100)

# Le renard flatte le corbeau
afficher_texte("Maître Renard, par l'odeur alléché,", 2)
afficher_texte("Lui tint à peu près ce langage :", 2)

# Le renard parle
afficher_texte("Et bonjour, Monsieur du Corbeau.", 2)
afficher_texte("Que vous êtes joli ! Que vous me semblez beau !", 2)

# Le corbeau ouvre le bec
afficher_texte("Sans mentir, si votre ramage", 2)
afficher_texte("Se rapporte à votre plumage,", 2)

# Le fromage tombe
afficher_texte("Vous êtes le Phénix des hôtes de ces bois.", 2)
animer_fromage(fromage, -200, 120, -200, -100)
time.sleep(1)

# Le renard attrape le fromage
afficher_texte("À ces mots, le Corbeau ne se sent pas de joie ;", 2)
afficher_texte("Et pour montrer sa belle voix,", 2)

# Le corbeau ouvre le bec et le fromage tombe
afficher_texte("Il ouvre un large bec, laisse tomber sa proie.", 2)
afficher_texte("Le Renard s'en saisit, et dit : Mon bon Monsieur,", 2)

# Le renard s'en va avec le fromage
afficher_texte("Apprenez que tout flatteur", 2)
animer_renard(renard, 0, -100, 200, -100)
afficher_texte("Vit aux dépens de celui qui l'écoute.", 2)

# Fin de l'animation
afficher_texte("Cette leçon vaut bien un fromage, sans doute.", 2)
afficher_texte("Fin.", 2)

# Fermer la fenêtre au clic
screen.exitonclick()


