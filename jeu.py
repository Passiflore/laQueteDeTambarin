vieTotale = 100
forceMin = 10
forceMax = 20
argent = 100
inventaire = []
lieuvisite = []

#Global imports
from random import randint
import secrets

#Slow reading system
import sys, time
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

# 1ere partie du jeu 
def TutoChoix1(choix1):

  while choix1 != 5:
   if choix1 ==  1:
     print('Vous vous dirigez vers votre bureau')
     suite = input()
     print('Un vieux mac de 2012. On fait avec ce qu’on peut…')
     suite = input()
     print('Un carnet et une plume… Il faudrait continuer ce roman un jour. Ce serait bien de réussir à devenir un célèbre auteur tel Michel Bussi.')
     suite = input()

   if choix1 == 2:
     print('Vous vous dirigez vers votre bibliothèque')
     suite = input()
     print("C'est une vieille bibliothèque en bois de sapin, elle sent comme les vieux livres qui la compose.")
     print('Il y a là des livres, des histoires, du savoir... toutes ces ouvrages vous les connaissez presque par coeur')
     suite = input()
     print("Vous balayez les titres du regard")
     suite = input()
     print('Des livres sur la magie, sur les meilleurs lieux secrets de Tambarin, sur des contrées lointaines au-délà des mers')
     print("Des enquêtes passionantes comme 'le mystère de l'écharpe verte' ou 'Qui a tué les villageois ?', ")
     print("il y a aussi des livres remplis de savoir comme 'coder en react pour les nuls' ou 'comment être un bon imposteur' ou sinon 'Les secrets de Linkedin par SDT'")
     suite = input()

   if choix1 == 3:
     print('Vous vous dirigez vers votre fenêtre')
     suite = input()
     print('Vous pouvez distinguer le clocher du village,')
     suite = input()
     print('Au loin, on peut voir les montagnes interdites et le soleil, déjà bien haut dans le ciel')
     suite = input()
     print('Il fait beau aujourd’hui, non ?')
     suite = input()

   if choix1 == 4:
     print ('Vous vous dirigez vers votre armoire')
     suite = input()
     print("Elle a toujours été là et elle le restera toujours")
     suite = input()
     print ('Littéralement, elle pèse une tonne et ne peut bouger. ')
     suite = input()
     print ('Comment n’a-t-elle pas défoncé le sol ? ')
     suite = input()

   print('Examinez:')
   print('1.Le bureau')
   print('2.La bibliothèque')
   print('3.La fenêtre')
   print('4.L’armoire')
   print('5.La porte')
   choix1 = None
   while choix1 not in [1, 2, 3, 4, 5]:
    try:
      choix1 = int(input())
    except ValueError:
      print("Vous devez faire un choix")
      pass

def sortir(peur):
  if peur == 2: 
    print("Reprends toi, il est grand temps d'affronter le monde. C'est la même chose tous les jours et ça ne changera jamais")

def nomSexe(nom,sexe):
  monBrave = "mon brave"
  if nom == "Pouet":
    print("Pouet pouet")
  if nom =="Boubou":
    print("Oh c'est donc vous Monsieur Bourienne !")
  if sexe == 1:
    monBrave = "jeune fille"
    print("Moi, je suis",nom,"la fille de la gérante de ce bar. Je l’aide en cuisine. Bienvenue à vous dans notre beau village !")
    suite = input()
    print("Gaston: Merci jeune fille")
    return monBrave
  elif sexe == 2:
    monBrave = "mon brave"
    print("Moi, je suis",nom,"le fils de la gérante de ce bar. Je l’aide en cuisine. Bienvenue à vous dans notre beau village !")
    suite = input()
    print("Gaston: Merci jeune homme")
    return monBrave
  elif sexe == 3:
    monBrave = "héros"
    print("Comment vous définissez vous?")
    sexe2 = input()
    print("Moi, je suis",nom,"je suis",sexe2,"enfant de la gérante de ce bar. Je l’aide en cuisine. Bienvenue à vous dans notre beau village !")
    suite = input()
    print("Gaston: Merci, heureux de te renconter")
    return monBrave

def choixDeVie(cVie):
  if cVie == 2: 
    print("Si vous choisisez cette option voici ce qui va se passer...")
    suite = input()
    print('Vous continuez votre vie, et l’auberge continue de bien marcher.')
    suite = input()
    print('L’auberge devient connue de tout le royaume grâce à votre histoire, narrée dans les journaux')
    suite = input()
    print('et notamment par Christophe Hondelatte, rédacteur en Chef du magazine criminel FELA stories.')
    suite = input()
    print('Vous avez fait de belles funérailles à votre mère, mais n’avez jamais trouvé son tueur.')
    suite = input()
    print('Vous êtes rongé de regrets et vous ne finirez jamais heureux.')
    suite = input()
    print('Non ça ne peux pas se finir comme ça. Pensez à votre mère car même quand tout le monde est contre toi, elle restait ta mailleure amie')

def choixObjetDepart(objetDepart):
  if objetDepart == 1:
    print("Pour résoudre une enquête, il est certain qu’une loupe est très utile")
    suite = input()
    inventaire.append("loupe")
    print("Excellent choix !")
    return inventaire
  elif objetDepart == 2: 
    print("Ça peut toujours vous dépanner et vous sauver de situations périlleuses")
    suite = input()
    inventaire.append("couteau")
    print("Excellent choix !")
    return inventaire
  elif objetDepart == 3: 
    print("Vous aurez forcément froid… C’est ce que disent toutes les mamans.")
    inventaire.append("pull")
    suite = input()
    print("Excellent choix !")
    return inventaire

def choixDirection(direction):
  while direction != 3:
    if direction == 1: 
        print("Vous rencontrez des enfants qui jouent avec un papillon")
        suite = input()
        print("Qu’avez-vous vu passer ?")
        suite = input()
        print("Un monsieur a couru vers l’entrée de la ville, mais il est loin maintenant…")
        suite = input()
        if "loupe" in inventaire:
          print("Inspecter le papillon : il a les pattes pleines de poussière…")
          suite = input()
        print("Rebrousser Chemin")
    elif direction == 2:
      print("Vous arrivez à l’entrée d’une maison. Vous toquez mais personne ne répond. La porte est entre-ouverte…")
      suite = input()
      print("Vous...")
      print("1.Entrez")
      print("2.Rebroussez chemin")
      revenir  = None
      while revenir not in [1, 2]:
        try:
          revenir = int(input())
        except ValueError:
          print("Vous devez faire un choix")
        pass
      if revenir == 1:
        print("Une femme nous hurle dessus et nous menace avec une casserole parce qu’on est rentrés chez elle par effraction")
        suite = input()
        print("Vous: Mais dans les autres jeux-vidéo ça marche !")
        suite = input()
        print("Femme: Qu’est-ce que vous racontez ?! Sortez de chez moi !")
        suite = input()
        print("Vous: Mais ! Aie ! Je veux juste une arme moi !")
        suite = input()
        print("Allez à l’Ouest ! Au magasin Général ! Et ne revenez plus ici !")
        suite = input()
      elif revenir == 2:
          print("Vous rebroussez chemin et revenez à votre point de départ.")
      print("Quel chemin prendre ?")
      print("1.Aller à gauche")
      print("2.Aller en face")
      print("3.Aller à droite")
    direction = None
    while direction not in [1, 2, 3]:
      try:
        direction = int(input())
      except ValueError:
        print("Vous devez faire un choix")
      pass
    choixDirection(direction)

def choixArme(armement, argent):
  if armement == 1 and argent >= 150:
    arme = "arc"
    return argent-150, arme
  elif armement == 2 and argent >= 100:
    arme = "hache"
    print(argent)
    return  argent-100, arme
    print("Vous a choisissez")
  elif armement == 3 and argent >= 25:
    arme = "bâton"
    return argent-25 , arme
  elif armement == 4 and argent >= 20:
    arme = "marteau"
    return argent-20, arme
  else:
    print("Vous n'avez pas assez d'argent pour cela, refaites un choix:")
    print("Vous choisissez:")
    print("1.Un arc/arbalète (150 pièces)")
    print("2.Une hache (100 pièces)")
    print("3.Un bâton (25 pièces)")
    print("4.Un marteau (20 pièces)")
    armement  = None
    while armement not in [1, 2, 3, 4]:
      try:
        armement = int(input())
      except ValueError:
        print("Vous devez faire un choix")
        pass
    choixArme(armement, argent)

def Intro(): 
  #Commecer l'intro
  print('Mère : Hé ! Qu’est ce que tu fais encore là à roupiller viens m’aider plutôt. Les jeunes de nos jours…')
  print('(Appyuez sur ent. pour la suite)')
  suite = input()
  print('Vous ouvrez lentement les yeux, pour découvrir baignant dans la lumière du matin, le plafond en bois de chêne de votre chambre.')
  suite = input()
  print('Encore ensommeillé, vous percevez des odeurs de lait chaud, de miel, de confiture et de pain fraichement sorti du four.')
  print('Depuis la fenêtre, vous entendez l’agitation de la ville, le bruit des passants, le brouhaha du marché et les résonnements du clocher.')
  suite = input()
  print('Derrière votre porte, vous percevez les bruit étouffés de clients parlant, vaisselles s’entrechoquant,') 
  print('de viande grillant et d’eau portée à ébullition. Vous vous redressez et examinez votre chambre.')
  suite = input()

  #Tuto Choix
  print('Examinez: (taper le chiffre correspondant à ce que vous voulez examinez)')
  print('1.Le bureau')
  print('2.La bibliothèque')
  print('3.La fenêtre')
  print('4.L’armoire')
  print('5.La porte')
  choix1 = None
  while choix1 not in [1, 2, 3, 4, 5]:
    try:
      choix1 = int(input())
    except ValueError:
      print("Vous devez faire un choix")
      pass

  TutoChoix1(choix1)
  print('Une banale porte en bois. Le bas de porte est parsemé des griffes de votre chat.')

  suite = input()
  print('Il est temps d’aider votre mère à l’auberge.')
  suite = input()

  #Choix 2
  print('Sortir ?')
  print('1.oui')
  print('2.Non les humains me font peur ')
  peur = None
  while peur not in [1, 2]:
    try:
      peur = int(input())
    except ValueError:
      print("Vous devez faire un choix")
      pass
  sortir(peur)
  
  suite = input()
  print('Vous baillez fortement et passez à la salle de bain pour vous rafraîchir le visage')
  suite = input()
  print('Il faut faire bonne impression devant les clients tout de même.')
  suite = input()
  print('Vous descendez enfin, et, allez dans la grande salle saluer votre mère et les clients')
  suite = input()
  print('Mère : Oh, mon enfant, cet homme vient de s’installer au village.')
  suite = input()
  print('Homme : Bonjour, moi c’est Gaston, charpentier, enchanté de vous connaître. Et vous ?')
  suite = input()
  print('Moi, je suis…')
  
  #Choix Sexe et Nom
  print("(Entrer votre nom)")
  nom = input()

  print("Vous êtes...")
  print("1.Une Femme")
  print("2.Un Homme")
  print("3.Autre")
  sexe  = None
  while sexe not in [1, 2, 3]:
    try:
      sexe = int(input())
    except ValueError:
      print("Vous devez faire un choix")
      pass
  monBrave = nomSexe(nom,sexe) 

  print("Suite à cet échange, vous allez en cuisine et commencez à aider les employés de votre mère.")
  suite = input()
  print("Mais soudain, un cri stridant se fait entendre,")
  suite = input()
  print("vous accourez alors dans la grande salle,")
  suite = input()
  print("pour y trouver votre mère gisante sur le sol.")
  suite = input()
  print("Un couteau planté en elle")
  suite = input()


  #Choix 3
  print('Vous paniquez :')
  print('1.Accourir auprès de votre mère et questionner les clients')
  print('2.Courir à l’extérieur pour voir si quelqu’un s’enfuit')
  choix3 = None
  while choix3 not in [1, 2]:
    try:
      choix3 = int(input())
    except ValueError:
      print("Vous devez faire un choix")
      pass

  if choix3 == 2:
    print("Vous regardez partout, mais ne trouvez personne dans la rue.")
    suite = input()
    print("Retourner à l’intérieur de l’auberge.")
    suite = input()

  print("Vous : Qui a fait ça !")
  suite = input()
  print("Vous : Ma pauvre mère…")
  suite = input()
  print("Vous regardez l’assemblée autour de vous ")
  suite = input()
  print("Vous : Que savez-vous ?")
  suite = input()
  print("Les clients se regardent, confus ; personne ne semble avoir observé la scène.")
  suite = input()
  print("Une femme dit avoir vu un homme trappu habillé de noir ")
  suite = input()
  print("Un colporteur est certain de l’avoir vu avec une cape")
  suite = input()
  print("Un homme se dégage de la foule et s’exclame :", monBrave , ", si vous désirez le fin mot de cette histoire,") 
  print("afin de rendre justice à votre triste mère…")
  suite = input()
  print("…Je vous conseille de rendre visite au vieux magicien magique, qui habite au") 
  print("Nord du Royaume. Il saura percevoir la vérité…")
  suite = input()

  #Choix de vie
  print("Que décidez-vous ?")
  print("1.Fermer l’auberge et aller chercher voir ce vieux magicien.")
  print("2.Continuer de faire tourner l’auberge, pour continuer l’œuvre de votre mère")
  cVie = None
  while cVie not in [1, 2]:
    try:
      cVie = int(input())
    except ValueError:
      print("Vous devez faire un choix")
      pass
  choixDeVie(cVie)

  print("Pour partir à l’aventure, il faut se préparer.")
  suite = input()
  print("Après que les médecins aient pris en charge le corps de votre mère,")
  suite = input()
  print("vous montez à l’étage, et vous vous préparez à partir.")
  suite = input()
  print("Vous prenez votre grand sac à dos et y mettez de la nourriture,")
  suite = input()
  print("une lampe-torche, un sac de couchage, des chaussettes de rechange et de l’eau ")
  suite = input()
  print("Il vous reste une petite place, mais vous ne savez pas quel choix faire.")
  suite = input()

  #ObjetDepart
  print("Qu’est-ce que vous y mettez ? (1 seul choix)")
  print("1.Une loupe")
  print("2.Un couteau suisse")
  print("3.Un pull")
  objetDepart = None
  while objetDepart not in [1, 2, 3]:
    try:
      objetDepart = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass

  inventaire = choixObjetDepart(objetDepart)

  print("Maintenant que vous êtes fin prêt, vous dites au-revoir à la maison de votre enfance et la fermez à clé.")
  suite = input()
  print("Votre recherche peut enfin commencer, mais… Par quel côté aller en premier ?")

  #ChoixDirection

  print("Quel chemin prendre ?")
  print("1.Aller à gauche")
  print("2.Aller en face")
  print("3.Aller à droite")
  direction  = None
  while direction not in [1, 2, 3]:
    try:
      direction = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass

  choixDirection(direction)

  #Entrée Magasin

  print("Le magasin général est petit et vieux, mais il suffit amplement aux habitants du village pour se fournir en denrées alimentaires")
  print("et autres outils de bricolage.")
  suite = input()
  print("Le reste se trouve au marché sur la grand place.")
  suite = input()
  print("Le commerçant est devant son comptoir, à lire son journal.")
  suite = input()
  print("Commerçant: Oh", monBrave, " ! J’ai eu vent de ce qu’il est arrivé à votre mère. C’est affreux… Que me vaut votre visite ? ")
  suite = input()
  print("Vous: Je pars à la recherche de l’assaillant de ma mère. Je cherche de quoi me défendre")
  suite = input()
  print("Commerçant: Et bien, c’est une aventure risquée que vous entreprenez là !…")
  suite = input()
  print("Commerçant: … Mais j’ai ce qu’il vous faut… ")
  suite = input()
  print("Commerçant: Faites votre choix… Je vous fait une ristourne pour votre premier achat, votre cause est noble… ")
  suite = input()
  argent = 100
  print("Vous disposez de",argent,"pièces")
  print("Vous choisissez:")
  print("1.Un arc/arbalète (150 pièces)")
  print("2.Une hache (100 pièces)")
  print("3.Un bâton (25 pièces)")
  print("4.Un marteau (20 pièces)")
  armement  = None
  while armement not in [1, 2, 3, 4]:
    try:
      armement = int(input())
    except ValueError:
      print("Vous devez faire un choix")
      pass
  argent, arme = choixArme(armement,argent)
  print("Vous disposez maintenant de", arme, "et il vous reste", argent , "pièces")

  suite = input()
  print("Ce fut un plaisir de commercer avec vous ! Je vous souhaite beaucoup de chance dans votre quête !")
  suite = input()
  print("Vous: Merci… ")
  suite = input()
  print("Vous sortez du magasin")
  suite = input()
  print("Il est temps de partir maintenant… ")
  suite = input()
  print("Vous vous rendez à gauche")
  suite = input()
  print("Vous arrivez rapidement aux portes de village.")
  suite = input()
  print("Vous n’êtes jamais réellement allé loin d’ici, et vous savez que de nombreux monstres rôdent à l’extérieur,")
  suite = input()
  print("mais il vous faut faire face afin de réussir à rendre justice pour votre mère…")
  suite = input()

  return inventaire, argent, arme, monBrave, nom

#Combat foret 
def fightLevel1(vieTotale, forceMin, forceMax, argent):
    argentGagne = None
    vieRestante = vieTotale

    monsters = ["rat", "sanglier", "troll", "blaireau", "serpent", "crapeau", "feu follet"]
    monstersLifeChoice = [10, 15, 15, 20, 25, 30]
    monsterLife = secrets.choice(monstersLifeChoice)

    print("Vous vous êtes trop enfoncés dans la forêt.")
    suite = input()
    print("Vous arrivez face à un", secrets.choice(monsters), "et un", secrets.choice(monsters), ".")
    print("\n", "-" * 50, "\n")
    suite = input()

    while vieRestante >= 0 or monsterLife > 0:
        yourAttack = randint(forceMin, forceMax)
        monsterAttack = randint(2, 10)

        print("Vous avez", vieRestante, "points de vie")
        suite = input()
        print("Les monstres ont", monsterLife, "points de vie.")
        suite = input()

        if vieRestante > 0:
            print("Vous frappez les monstres et leur enlevez",
                  yourAttack, "points de vie.")
            monsterLife = monsterLife - yourAttack
            suite = input()

        if monsterLife <= 0:
            argentGagne = randint(5, 15)
            print("\n", "-" * 50, "\n")
            print("Les monstres sont morts !")
            print("Vous gagnez", argentGagne, "pièces.")
            print("\n", "-" * 50, "\n")
            argent = argent + argentGagne
            return vieRestante, argent
        elif vieRestante <= 0:
            print("Vous tombez à terre, exténué.")
            suite = input()
            print("...")
            suite = input()
            print("Un marchand itinérant vous a trouvé là et vous a ramené au village.")
            suite = input()
            print("Vous vous retrouvez au magasin général.")
            magasin()
            return vieRestante, argent
        else:
            print("Les monstres vous frappent et vous enlèvent",
                  monsterAttack, "points de vie.")
        vieRestante = vieRestante - monsterAttack
        suite = input()

# 2eme partie du jeu
#Magasin
def magasin(inventaire, argent, arme, monBrave, nom, vieTotale, lieuvisite):
  print("Vous retournez au magasin général")
  suite = input()
  print("Ah, te revoilà", nom, "y a t-il eu de l'avancement dans ta quête ?")
  suite = input()
  print("Je viens de recevoir un nouvel arrivage! Approche viens jeter un oeil")
  suite = input()
  print("Vous disposez de ",argent,"pièces")
  print("Vous choisissez:")
  print("1.Un arc/arbalète (150 pièces)")
  print("2.Une hache (100 pièces)")
  print("3.Un bâton (25 pièces)")
  print("4.Un marteau (20 pièces)")
  print("5.Une pomme (5 pièces)")
  print("6.Une baguette de pain frais (10 pièces)")
  print("7.Une tomme de fromage de chèvre (15 pièces)")
  print("8.Des baies sauvages (5 pièces)")
  print("9.Ne rien acheter")

  if "village" in lieuvisite:
    print("10.Une arbalète 100 pièces")
  if "moulin" in lieuvisite:
    print("11.Une épée 125 pièces")
  if "pont" in lieuvisite:
    print("12.Une lance 130 pièces")
  if "pont" in lieuvisite:
    print("13.Une masse 165 pièces")

  choixMagasin  = None
  while choixMagasin not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
    try:
      choixMagasin = int(input())
    except ValueError:
      print("Vous devez faire un choix")
      pass
  acheter (choixMagasin,inventaire, argent, arme, monBrave, nom, vieTotale)
  choixDirection2(inventaire, argent, arme, monBrave, nom, vieTotale)
  return inventaire, argent, arme, monBrave, nom, vieTotale,lieuvisite

def acheter(choixMagasin,inventaire, argent, arme, monBrave, nom, vieTotale):
  if choixMagasin == 1 and argent >= 150:
    arme = "arc"
    return argent-150, arme, vieTotale
  elif choixMagasin == 2 and argent >= 100:
    arme = "hache"
    print("Vous avez maintenant une hache")
    return  argent-100, arme, vieTotale
  elif choixMagasin == 3 and argent >= 25:
    arme = "bâton"
    print("Vous avez maintenant un bâton")
    return argent-25 , arme, vieTotale
  elif choixMagasin == 4 and argent >= 20:
    arme = "marteau"
    print("Vous avez maintenant un marteau")
    return argent-20, arme, vieTotale
  elif choixMagasin == 5 and argent >= 5:
    print("Vous manger la pomme et gagnez 5 points de vie")
    vieTotale+5
    print("Vous avez",vieTotale,"points de vie")
    return argent-5, vieTotale, arme
  elif choixMagasin == 6 and argent >= 10:
    print("Vous manger le pain et gagnez 10 points de vie")
    vieTotale+10
    print("Vous avez",vieTotale,"points de vie")
    return argent-10, vieTotale, arme
  elif choixMagasin == 7 and argent >= 15:
    print("Vous manger le fromage et gagnez 15 points de vie")
    vieTotale+15
    print("Vous avez",vieTotale,"points de vie")
    return argent-15, vieTotale, arme
  elif choixMagasin == 8 and argent >= 5:
    print("Vous manger quelques baies et gagnez 5 points de vie")
    vieTotale+10
    print("Vous avez",vieTotale,"points de vie")
    return argent-10, vieTotale, arme
  elif choixMagasin == 9:
    print("Vous continuez votre aventure")
    choixDirection2(inventaire, argent, arme, monBrave, nom, vieTotale)
  elif choixMagasin == 10 and argent >= 100:
    arme = "arbalète"
    print("Vous avez maintenant une arbalète")
    return argent-100, vieTotale, arme
  elif choixMagasin == 11 and argent >= 125:
    arme = "epee"
    print("Vous avez maintenant une épée")
    return argent-125, vieTotale, arme
  elif choixMagasin == 12 and argent >= 130:
    arme = "lance"
    print("Vous avez maintenant une lance")
    return argent-130, vieTotale, arme
  elif choixMagasin == 13 and argent >= 165:
    inventaire.append("masse")
    print("Vous avez maintenant une masse")
    return argent-165, vieTotale, arme
  else:
    print("Vous n'avez pas assez d'argent pour cela, refaites un choix:")
    print("Vous disposez de ",argent,"pièces")
    print("Vous choisissez:")
    print("1.Un arc/arbalète (150 pièces)")
    print("2.Une hache (100 pièces)")
    print("3.Un bâton (25 pièces)")
    print("4.Un marteau (20 pièces)")
    print("5.Une pomme (5 pièces)")
    print("6.Une baguette de pain frais (10 pièces)")
    print("7.Une tomme de fromage de chèvre (15 pièces)")
    print("8.Des baies sauvages")
    print("9.Ne rien acheter")
    if "village" in lieuvisite:
      print("10.Une arbalète 100 pièces")
    if "moulin" in lieuvisite:
      print("11.Une épée 125 pièces")
    if "pont" in lieuvisite:
      print("12.Une lance 130 pièces")
    if "pont" in lieuvisite:
      print("13.Une masse 165 pièces")

    choixMagasin  = None
    while choixMagasin not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
      try:
        choixMagasin = int(input())
      except ValueError:
        print("Vous devez faire un choix")
      pass
    argent, arme, vieTotale = acheter (choixMagasin,inventaire, argent, arme, monBrave, nom, vieTotale)

def choixDirection2(inventaire, argent, arme, monBrave, nom, vieTotale):
  suite = input()
  print("Où voulez vous aller ?")
  print("1. La forêt")
  if "foret" in lieuvisite:
    print("2. Le village abandonné")
  if "village" in lieuvisite:
    print("3. Le moulin")
  if "moulin" in lieuvisite:
    print("4. Le pont")
  if "pont" in lieuvisite:
    print("5. L'entrée de la ville")
  if "entree" in lieuvisite:
    print("6. Faire le tour de la forteresse")
    print("7. Chercher le magicien")
  if "entreechateau" in lieuvisite:
    print("8. L'Entrée chateau")
    print("9. Le centre-ville de Ciadas")
  if "centreville" in lieuvisite:
    print("10. La taverne")
  

  destination  = None
  while destination not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    try:
      destination = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  if destination == 1:
    foret(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
  if destination == 2:
    villageAbandonne(inventaire, argent, arme, monBrave, nom, vieTotale)
  if destination == 3:
    moulin(inventaire, argent, arme, monBrave, nom, vieTotale)
  if destination == 4:
    pont(inventaire, argent, arme, monBrave, nom, vieTotale)
  if destination == 5:
    EntreeCiadas(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )
  if destination == 6:
    forteresseCiadas(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
  if destination == 7:
    magicien(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
  if destination == 8:
    entreeChateau(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
  if destination == 9:
    centrevilleCiadas(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite)
  if destination == 10:
    taverneCiadas(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
  
#Retour en arrière, direction le magasin
def tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite ):
  if rebrousser == 2:
    print_slow("Vous rebroussez chemin et retournez au magasin")
    suite = input()
    magasin (inventaire, argent, arme, monBrave, nom, vieTotale, lieuvisite)
    
#Chap 1 : Foret
def foret(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax):
  lieuvisite.append("foret")

  #niv 1
  print("Vous commencez votre aventure et suivez votre prodigieux sens de l’orientation,")
  suite = input()
  print("vous dirigeant jusqu’à une grande forêt.")
  suite = input()
  print("Que faire ?")
  print("1.Entrer dans la forêt")
  print("2.Rebrousser chemin")
  rebrousser  = None
  while rebrousser not in [1, 2]:
    try:
      rebrousser = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )

  vieTotale, argent = fightLevel1(vieTotale, forceMin, forceMax, argent)

  #niv2
  suite = input()
  print("Cette forêt est sombre et pleine de mystères…")
  suite = input()
  print("Les oiseaux volent…")
  suite = input()
  print("Que faire ?")
  print("1.Continuer")
  print("2.Rebrousser chemin")
  rebrousser  = None
  while rebrousser not in [1, 2]:
    try:
      rebrousser = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )

  vieTotale, argent = fightLevel1(vieTotale, forceMin, forceMax, argent)
  
  #niv3
  suite = input()
  print("Vous trouvez un bâton couvert de mousse")
  suite = input()
  if "couteau" in inventaire:
    print_slow("Vous : Quelques petits coups de couteau...")
    suite = input()
    print_slow("Vous : TADAM ! Un pieu en bois")
    inventaire.append("Pieu")
    suite = input()
  else :
    print("Vous le jettez")
    suite = input()
  print("Que faire ?")
  print("1.Continuer")
  print("2.Rebrousser chemin")
  rebrousser  = None
  while rebrousser not in [1, 2]:
    try:
      rebrousser = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )

  vieTotale, argent = fightLevel1(vieTotale, forceMin, forceMax, argent)

  #niv4
  suite = input()
  print("Vous arrivez à l’orée d’une clairière, qui possède un magnifique lac. Dans l’eau, une femme profite de la chaleur du soleil sur son corps.")
  suite = input()
  print("Vous vous avancez vers la femme")
  suite = input()
  print_slow("Femme: Bonjour mon enfant. Veux-tu que je te lise ton avenir ?")

  print("1.Oui")
  print("2.Non")
  avenir  = None
  while avenir not in [1, 2]:
    try:
      avenir = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  if avenir == 1:
    print_slow("Vous: Vous me semblez bien sage, que pouvez-vous me dire sur mon futur ?")
    suite = input()
    print_slow("Femme: Je vois...")
    suite = input()
    print_slow("Femme: dans l'eau claire...")
    suite = input()
    print_slow("Femme: un avenir incertain...")
    suite = input()
    print("Cela ne vous est pas très utile...")
    suite = input()
  
  print("3[0;37;40m Que faire ?")
  print("1.Continuer")
  print("2.Rebrousser chemin")
  rebrousser  = None
  while rebrousser not in [1, 2]:
    try:
      rebrousser = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )

  vieTotale, argent = fightLevel1(vieTotale, forceMin, forceMax, argent)
  
  #niv5
  suite = input()
  print("Vous vous enfoncez dans la forêt")
  suite = input()
  if "loupe" in inventaire:
    print("En examinant les arbres vous trouvez des baies comestibles")
    inventaire.append("baie")
    suite = input()
  print("Vous croisez un écureuil et sortez de la forêt")
  suite = input()
  print("Il vous reste", vieTotale, "points de vie.")
  print("Vous avez", argent, "pièces.")

  return inventaire, argent, arme, monBrave, nom, vieTotale, argent

#Chap 2 : Village
def villageAbandonne(inventaire, argent, arme, monBrave, nom, vieTotale):
  lieuvisite.append("village")
  print("Vous continuez votre aventure, et vos pas vous emmènent à l’orée d’un vieux village.")
  suite = input()
  print("Que faire ?")
  print("1.Entrer dans le village")
  print("2.Passer son chemin")
  rebrousser  = None
  while rebrousser not in [1, 2]:
    try:
      rebrousser = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )

  
  print("Vous entrez dans le village, en ruine. Il reste à peine une ou deux bâtisses qui tiennent debout…")
  suite = input()
  print("Vous avancez et vous tombez nez à nez avec un vieux puit en pierres vermoulues")
  suite = input()
  print("Vous...")
  print("1.Ramassez une pierre et la lancez dans le puit")
  print("2.Laissez ce vieux puit tranquille")
  puit = None
  while puit not in [1, 2]:
    try:
      puit = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  if puit == 1:
    print("Vous vous baissez pour ramasserr une pierre et vous la laissez tomber dans le puit")
    suite = input()
    print("Elle se cogne contre les parrois du puit et vous entendez l'écho de sa chute pendant un long moment...")
    suite = input()
    print("Finalement au bout de 5-6 seconde vous entendez enfin un faible bruit d'eau")
    suite = input()
    print("Qui aurait cru que ce puit soit si profond !? Comment faisient les villageois pour puiser leur eau ?")
  suite = input() 
  print("Que faire ?")
  print("1.Continuer dans le village")
  print("2.Renoncer à l'exploration")
  rebrousser  = None
  while rebrousser not in [1, 2]:
    try:
      rebrousser = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )

  print("Vous continuez votre avancée dans ce qui était surement un village plein de vie autrefois")
  suite = input()
  print("Vous passez devant un vieil arbre, surement le dernier résident de ce village...")
  suite = input()
  print("Vous vous rapprochez... Cet arbre a du en voir des choses, des mariages, des fêtes de villages, des tempêtes...")
  if "couteau" in inventaire:
    print("Vous pouvez, avec votre couteau, inscrire quelque chose sur le tronc de cet arbre. Temoinage de votre passage ")
    suite = input()
    print("Vous gravez...")
    gravure = input()
    print("Voilà vous avez laissé une trace de votre passage...Les prochaines personnes assez courageuse pour entrer dans cette ville trouveront ce message:", gravure)
  elif "loupe" in inventaire:
    print("Vous balladez votre main sur le tronc de l'arbre et vous remarquez des petites griffures")
    suite = input()
    print("Avec votre loupe, vous examinez de plus près ces petites entailles")
    suite = input()
    print("Vous percevez, gravé dans le bois un petit coeur avec l'inscription Al + St")
    suite = input()
    print("Vous: Des amoureux prennant cet arbre pour temoin de leur amour... Je me demande ce qu'ils sont devenus...")
 
  suite = input()
  print("Vous marchez tel un fantôme dans ce lieu abandonné")
  suite = input()
  print("Vous arrivez devant une maison abandonée. Ses tuiles manquantes laissent apparaitre son squelette de bois. Tout les carreaux de ses fenêtres sont explosés et le verre est répandu sur le sol")
  suite = input()
  print("Ses murs sont infestés de mousse verdatres et tachés de mille et unes traces grisâtres. Les volets en morceaux claquent à chaque coup de vent")
  suite = input()
  print("La porte ou enfin ce qu'il en reste est ouverte")
  print("Que faire ?")
  print("1.Entrer")
  print("2.Renoncer à l'exploration")
  rebrousser  = None
  while rebrousser not in [1, 2]:
    try:
      rebrousser = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )

  print("Vous entrez dans la maison, une forte odeur de sous-bois se dégage de l'interieur")
  suite = input()
  print("Le plancher grince sous vos pas. Vous essayez de vous frayer un chemin parmis les meubles en décompositions renversés sur sol")
  suite = input()
  print("Le plafond de la maison est devenu la résidence d'une colonie d'araignée ou chaque fissure fait office d'appartement privé")
  suite = input()
  print("Vous sentez un courant d'air dans votre nuque")
  suite = input()
  print("Vous: Ah, c'est surement le vent...C'est pas très bien isolé ici")
  suite = input()
  print("Vous traversez ce qui devait être auparavant une entrée. Ses murs sont remplis de vielles photos de famille jaunies.")
  suite = input()
  print("Vous vous rapprochez des portraits. Sous ceux-ci se trouve une vieille commode, il ne lui reste qu'un seul tiroir debout qui semble tenir tout l'ensemble... ensemble")
  suite = input()
  print("Ouvrir le tiroir ?")
  print("1.Oui")
  print("2.Non")
  tiroir= None
  while tiroir not in [1, 2]:
    try:
      tiroir = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  if tiroir == 1:
    print("Vous essayer d'ouvrir le tiroir mais il n'a pas l'air de vouloir bouger")
    suite = input()
    print("Les pieds solidement encrés sur le plancher sale vous tirez avec de plus en plus de force.")
    suite = input()
    print("Le tiroir commence à bouger dans un crissement aigu")
    suite = input()
    print("Vous y metter tout ce qu'il vous reste de force et le tiroir fini par ceder et se décrocher de la commode. Vous tombez par-terre et entendez des craquement de bois")
    suite = input()
    print("La commode ne pouvant se tenir toute seule s'écroule. Le tiroir encore dans les mains vous vérifiez le contenu...")
    suite = input()
    print("Quelques mites, beaucoup de poussière et un petit objet doré...")
    suite = input()
    print("Une vieille montre en or ! On doit pouvoir l'échanger contre quelques pièces")
    suite = input()
    print("Vous gagnez 25 pièces")
    argent +25

  print("Vous vous détrournez des photos et vous dirigez vers la suite de la maison. Malheuresement un trou béant vous sépare de ce qui ressemble à un salon. Vous ne pourrez surment pas aller dans une autre pièce. ")
  suite = input()
  print("Vous sortez de la maison.")
  suite = input()
  print("Vous continuez votre exploration du village en vous enfonçant de plus en plus")
  suite = input()
  print("Vous vous arrivez devant le vieux clocher. En entrant, une vieille statue du Christ est posée là.")
  suite = input()
  print("Il y a des bancs renversés et des livres de prières sur le sol. Tous les vitraux sont brisés et laisse passer par leur trous la lumière non flitrée du soleil")
  suite = input()
  print("Devant vous se dresse une vieille échelle en bois. Elle semble mener au clocher")
  suite = input()
  print("Voulez vous vous risquer à l'emprunter ? ")
  print("1.Oui")
  print("2.Non")
  renoncer = None
  rebrousser  = None
  while rebrousser not in [1, 2]:
    try:
      rebrousser = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite)
  
  print("Vous atteignez le sommet du clocher")
  suite = input()
  print("Vous avez une vue imprenable sur l'ensemble de la contrée")
  suite = input()
  if "pull" not in inventaire:
    print("Il fait froid dans cette vieille bâtisse… Vous auriez dû prendre un pull...")
    suite = input()
  print("Vous redescendez")
  suite = input()
  print("En chemin, vous êtes agressé par une araignée...Vous perdrez 5 points de vie")
  vieTotale -5
  print("Vous sortez du clocher")

  return inventaire, argent, arme, monBrave, nom, vieTotale

#Chap 3 : Moulin
def moulin(inventaire, argent, arme, monBrave, nom, vieTotale):
  lieuvisite.append("moulin")
  print("Vous continuez votre aventure, et traversant à travers un pré recouvert de fleurs,vous tombez sur un champ de blé au fond duquel se trouve un moulin.")
  suite = input()
  print("Vous traversez le champ de blé, en y arrachant un épi au passage")
  print("Vous arrivez au moulin")
  suite = input()
  print("Vous...")
  print("1.Aller voir si quelqu’un se trouve ici")
  print("2.Rebroussez chemin. Je ne connais pas la personne qui vit ici c'est peut être Xavier Dupont de Ligonnès")
  rebrousser  = None
  while rebrousser not in [1, 2]:
    try:
      rebrousser = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )

  print("Aucune réponse...")
  suite = input()
  print("Vous...")
  print("1.Insistez")
  print("2.Ne vous acharnez pas. Il ne doit y avoir personne ici")
  rebrousser  = None
  while rebrousser not in [1, 2]:
    try:
      rebrousser = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )

  print("Vous percevez une faible voix venant de l'intérieur")
  suite = input()
  print("Voix d'homme: Que se passe-t-il ici !? ")
  suite = input()
  print("Lui demander...")
  print("1.D'ouvrir la porte")
  print("2.Lui demander des informations à travers la porte")
  porte = None
  while porte not in [1, 2]:
    try:
      porte = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass

  if porte == 1:
    print("Vous: Monsieur, ouvrez moi la porte, je suis un jeune aventurier qui a besoin d'aide et je demande votre hospitalité")
  elif porte == 2 :
    print("Vous: Monsieur, je suis un jeune aventurier en quête de la vérité, vous avez peut-être des informations qui pourrait m'intérésser")
  suite = input()
  print("Voix d'homme: Ah ça non ! Les aventuriers, je ne les aide plus ! J’en ai trop vu de ma vie ! Hors de ma vue !")
  suite = input()
  print("Vous: Mais Monsieur, j'ai peut-être quelque chose qui pourrait vous intéréssez...")
  suite = input()
  print("Lui proposer...")
  print("1.De l'argent")
  print("2.Abandonner et rebrousser chemin")
  if "baie" in inventaire:
    print("3.Des baies")

  soudoyer = None
  while soudoyer not in [1, 2, 3]:
    try:
      soudoyer= int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  if soudoyer == 1:
    print("Vous: Peut-être que tout pourrait s'arranger avec un petit billet")
    suite = input()
    print("Voix d'homme: Oh", monBrave,"ça va te couter cher. Je ne suis pas si facile à amadouer")
    suite = input()
    print("Voix d'homme: Je te donnerai ce que tu veux si tu peux me donner 200 pièces")
    suite = input()
    if argent < 200:
      print ("Vous n'avez pas assez d'argent ")
      rebrousser = 2
      tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )

    elif argent >= 200:
      print ("Vous avez ",argent," pièces")
      print ("1. Lui donnez 200 pièces")
      print ("2. Ne lui donnez rien.")
      amadouer = None
      while amadouer not in [1, 2]:
        try:
          amadouer = int(input())
        except ValueError:
          print("Vous devez faire un choix")
        pass
      if amadouer == 1:
        finMoulin(inventaire, argent, arme, monBrave, nom, vieTotale)

  elif soudoyer == 2 :
    rebrousser = 2
    tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )
  
  elif "baie" in inventaire and soudoyer == 3:
    finMoulin(inventaire, argent, arme, monBrave, nom, vieTotale)

def finMoulin(inventaire, argent, arme, monBrave, nom, vieTotale):
  print("3. J’ai un cadeau pour vous monsieur. Laissez-moi vous l’offrir s’il vous plait…")
  suite = input()
  print ("L’homme ouvre alors la porte, intrigué")
  suite = input()
  print ("Vieux meunier: Oh ! Cela fait si longtemps que je n’ai pas eu de cadeaux ! Entrez", monBrave, "venez me raconter vos aventures et vous réchauffer !")
  suite = input()
  print ("Après avoir vous êtres installé près du feu, vous racontez votre histoire au vieux meunier.")
  suite = input()
  print("Vieux meunier: Je suis désolé de ce qui vous arrive et je vous demande pardon pour mon accueil peu chaleureux. Tenez du pain pour me faire pardonner de mon comportement")
  inventaire.append("pain")
  suite = input()
  print("Vous en mangez un morceau et regagnez 10 points de vie")
  vieTotale +10
  suite = input()
  print("Vieux meunier: C’est une grande aventure que vous entreprenez-là… J’ai peut être connaissance de quelqu’un qui pourra vous aider.")
  suite = input()
  print("Vous: Ah oui !? Qui donc ?")
  suite = input()
  print("Vieux meunier: Mon vieil ami le gardien du pont. Il voit tous les jours des dizaines d’individus différents passer. Il aura peut-être vu quelque chose de suspect. Allez le voir de ma part.")
  suite = input()
  print("Après une bonne nuit de sommeil, vous sortez du moulin...")
  suite = input()
  print("Sur le retour, vous croisez des rats et perdez 2 pv")
  vieTotale -2
  return inventaire, monBrave, vieTotale

#Chap 4 : Pont
def pont(inventaire, argent, arme, monBrave, nom, vieTotale):
 print("Vous continuez votre aventure, et vous tombez rapidement sur un ravin énorme")
 suite = input()
 print("Impossible de le traverser. Mais à votre droite, vous voyez un pont suspendu. Vous vous apprrochez")
 suite = input()
 print("Soudain, un vieil homme...de petite taille jaillit de sous le pont. ")
 suite = input()
 print("Homme étrange: Vous ne passerez pas, manant !")
 suite = input()
 print("Vous: Mais… J’ai besoin de passer pour continuer mon aventure")
 suite = input()
 print("Homme étrange: Je n’en ai que faire. Pour passer, il faut réussir mon énigme !")
 suite = input()
 print("Vous: Quelle est cette énigme ?")
 suite = input()
 print("Homme étrange: Eh bien, c’est très simple, mais à la fois très compliqué. Personne ne m’a battu jusqu’à maintenant : qu’est ce qui a 4 pattes le matin, 2 le midi, et 3 le soir ?")
 suite = input()
 print("Vous...")
 print("1.Essayez de lui soutirer des informations")
 print("2.Essayez de répondre à son énigme")
 print("3.Rebroussez chemin")
 devinette = None
 while devinette not in [1, 2, 3]:
   try:
     devinette = int(input())
   except ValueError:
     print("Vous devez faire un choix")
   pass
 
 enigme(devinette,inventaire, argent, arme, monBrave, nom, vieTotale)
 return inventaire, argent, arme, monBrave, nom, vieTotale,lieuvisite
 
def enigme (devinette,inventaire, argent, arme, monBrave, nom, vieTotale):
 if devinette == 1:
   print("Vous: Je ne cherche pas à passer, je cherche juste des informations. Pouvez-vous répondre à mes questions ?")
   suite = input()
   print("Homme étrange: Je ne réponds pas aux questions des gens qui ne réponde pas à MA question")
   suite = input()
   print("Homme étrange: Je ne réponds pas aux questions des gens qui ne réponde pas à MA question")
   suite = input()
   print("Vous...")
   print("1.Essayez de lui soutirer des informations")
   print("2.Essayez de répondre à son énigme")
   print("3.Rebroussez chemin")
   devinette = None
   while devinette not in [1, 2, 3]:
     try:
       devinette = int(input())
     except ValueError:
       print("Vous devez faire un choix")
     pass
   enigme(devinette,inventaire, argent, arme, monBrave, nom, vieTotale)
   return inventaire, argent, arme, monBrave, nom, vieTotale,lieuvisite
 
 elif devinette == 2:
   print("Vous: Je relève le défi, je vais répondre à votre enigme... ")
   suite = input()
   print("Homme étrange: Tu te crois bien intelligent")
   suite = input()
   suite = input()
   reponse = input("Vous: La réponse est..." ).lower()
   if reponse == "homme" or reponse == "l'homme" or reponse == "humain" or reponse == "l'humain":
     print("Et bien… C’est plutôt surprenant… Mais bon, tout le monde réussit de toute façon. Vous pouvez passer !")
     continuer(inventaire, argent, arme, monBrave, nom, vieTotale)
 
   else:
     print("Je vous avais dit que c’était compliqué… Revenez quand vous aurez la solution.")
     suite = input()
     print("Vous retournez au magasin")
     magasin(inventaire, argent, arme, monBrave, nom, vieTotale, lieuvisite)
 
 elif devinette == 3:
   print("Vous: Je ne fais pas confiance à cet homme... passons notre chemin")
   rebrousser = 2
   tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )

def continuer(inventaire, argent, arme, monBrave, nom, vieTotale):
  suite = input()
  if "pain" in inventaire:
    print("Vous: Merci ! Mais attendez, je me suis embarqué dans une aventure, et j’ai rencontré votre ami le vieux meunier.")
    suite = input()
    print("Vous: Il m’a dit que vous m’aideriez… Avez-vous vu passer des personnes louches récemment ?")
    suite = input()
    print("Homme étrange: Des personnes louches… Peut être bien. J’ai récemment vu passer une troupe de troubadours… ")
    suite = input()
    print("Homme étrange: Ceux-là sont très bizarres… Mais j’ai aussi vu passer un grand homme, très mystérieux, qui avait une longue cape noire et un chapeau pointu.")
    suite = input()
    print("Homme étrange: Il s’en est allé très rapidement après avoir voulu me donner de l’argent car il ne trouvait pas la réponse à mon énigme.")
    suite = input()
    print("Vous: Je vois… Merci de votre aide !")
    suite = input()
    print("Vous continuez votre chemin")
    suite = input()
  elif "pain" not in inventaire:
    print("Vous: Merci beaucoup !")
    suite = input()
  lieuvisite.append("pont")
  EntreeCiadas(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite)

#3e partie du jeu
def EntreeCiadas(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite):
    lieuvisite.append("entree")
    # niv 1

    print("Vous arrivez à l'orée de la grande ville de Ciadas,")
    suite = input()
    print("domaine du roi Chomelus, qui règne sur la contrée de Tambarin.")
    suite = input()
    print("Que faire ?")
    print("1. Entrer dans la ville")
    print("2. Rebrousser chemin")
    rebrousser = None
    while rebrousser not in [1, 2]:
        try:
            rebrousser = int(input())
        except ValueError:
            print("Vous devez faire un choix")
        pass
    tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite)

    print("Les gardes vous barrent la route")
    suite = input()
    print("Garde 1: Halte-là, déclinez votre identité !")
    suite = input()
    print(
        "Vous: Je suis",nom,"enfant de la défunte tavernière de la ville de Qululu")
    suite = input()
    print("Garde 2: Je suis désolé pour votre mère...")
    suite = input()
    print("Garde 2: Malheureusement nous ne pouvons vous laisser entrer.")
    suite = input()
    print("Garde 1: Aujourd'hui est un jour très spécial pour le seigneur, ")
    suite = input()
    print("Garde 1: Seul les habitants et les pointures du royaume sont autorisés à entrer.")
    suite = input()
    print("Il va vous falloir trouver un autre moyen d'entrer dans le royaume...")
    print("1. Faire le tour de la forteresse")
    print("2. Rebrousser chemin")
    print("3. Aller chercher de l'aide ailleurs")
    rebrousse = None
    while rebrousse not in [1, 2, 3]:
        try:
            rebrousse = int(input())
        except ValueError:
            print("Vous devez faire un choix")
        pass
    tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite)
    if rebrousse == 1:
      forteresseCiadas(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
    elif rebrousse == 3:
      magicien(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
    suite = input()

####################################
####################################
####################################


def forteresseCiadas(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax):
    lieuvisite.append("forteresse")
    print("Vous: Voyons si on peut trouver une autre entrée...")
    suite = input()
    print("Vous faites le tour de la forteresse...")
    suite = input()
    print("...")
    suite = input()
    print("Vous trouvez une brèche dans la pierre...")
    suite = input()
    print("Peut-être qu'avec un objet assez lourd...")
    if "masse" in inventaire:
        print("Vous: Vous sortez votre masse et démolissez les briques une à une...")
        suite = input()
        print("Vous: Yes ! Une brèche ! Cette masse m'a été bien utile.")
        suite = input()
        print("Vous entrez dans la ville...")
        suite = input()
        entreeChateau(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
    suite = input()
    print("Malheureusement vous n'avez rien de tel sur vous.")
    suite = input()
    print("Vous continuez de faire le tour de la forteresse,")
    suite = input()
    print("mais vous ne trouvez aucune faille.")
    suite = input()
    print("...")
    suite = input()
    print("Vous êtes revenu à l'entrée.")
    suite = input()
    print("Vous: Cette forteresse est décidemment bien solide...")
    suite = input()
    print("Que faire ?")
    print("1. Aller chercher de l'aide ailleurs")
    print("2. Rebrousser chemin")
    rebrousser = None
    while rebrousser not in [1, 2]:
        try:
            rebrousser = int(input())
        except ValueError:
            print("Vous devez faire un choix")
        pass

    tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )
    magicien(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)  

####################################
####################################
####################################


def magicien(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax):
    print("Vous continuez votre aventure.")
    suite = input()
    print("Vous: Peut-être qu'en trouvant ce vieux magicien...")
    suite = input()
    print("...")
    suite = input()
    print("Vous pas vous emmènent à une grande rivière.")
    suite = input()
    print("Un petit châlet se distingue au bord de l'eau.")
    suite = input()
    print("...")
    suite = input()
    print("Vous vous approchez.")
    suite = input()
    print("Un vieil homme pêche dans la rivière.")
    suite = input()
    print("Vous: Bonjour pêcheur ! Auriez-vous eu vent d'en vieux magicien,")
    suite = input()
    print("Vous: qui logerait dans la région ?")
    suite = input()
    print("Le vieil homme vous regarde, circonspect.")
    suite = input()
    print("Pêcheur: Il n'y a plus eu de magicien depuis bien longtemps dans ce pays...")
    suite = input()
    print("Pêcheur: ... Mais il y a bien un vieux fermier qui est adapte de sciences ésotériques plus loin...")
    suite = input()
    print("Allez vers le Sud et vous le trouverez")
    suite = input()
    print("...")
    suite = input()
    print("Vous remerciez le vieux pêcheur et reprenez votre route.")
    suite = input()
    print("...")
    suite = input()
    print("Vous arrivez rapidement à une vieille ferme.")
    suite = input()
    print("De la fumée sort de la cheminée.")
    suite = input()
    print("...")
    suite = input()
    print("Vous vous rapprochez et toquez à l'entrée.")
    suite = input()
    print("...")
    suite = input()
    print("Un homme vous ouvre,")
    suite = input()
    print("Il a une vieille barbe grisonnante de laquelle il s'échappe de la poudre.")
    suite = input()
    print("Fermier: Oui, jeune homme ? Que me vaut votre visite ?")
    suite = input()
    print("Vous lui racontez l'objet de votre quête.")
    suite = input()
    print("Fermier: Je vois... Je suis désolé pour vous, mais malheureusement, je ne suis pas votre homme.")
    suite = input()
    print("Vous êtes prêt à lui hurler 'Menteur' !")
    suite = input()
    print("Mais derrière lui, on entend soudain un grand BOUM ;")
    suite = input()
    print("Des bulles et des pailettes s'échappent bientôt de la cheminée, et retombent en flocons...")
    suite = input()
    print("Fermier: ...")
    suite = input()
    print("Vous: ...")
    suite = input()
    print("Magicien: Bon, j'accepte de vous aider,")
    suite = input()
    print("Magicien: Mais à une condition !")
    suite = input()
    print("Vous attendez, inquiet de savoir ce qu'un tel homme peut vouloir.")
    suite = input()
    print("Magicien: ... Battez-moi au pierre-feuille-ciseaux !")
    suite = input()
    print("Vous: ...")
    suite = input()
    print("Que faire ?")
    print("1. Accepter le duel")
    print("2. Vous fumez, vieil homme !")
    suite = input()
    choix = None
    while choix not in [1, 2]:
        try:
            choix = int(input())
            if choix == 1:
                chifumi(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
            elif choix == 2:
                suite = input()
                print("Magicien: Bon... Je vais vous aider de toute façon, alors...")
                suite = input()
                print("Magicien: Mais refuser de jouer avec un vieil homme comme moi...")
                suite = input()
                print("Magicien: C'est vraiment ingrat.")
        except ValueError:
            print("Vous devez faire un choix")
        pass
    suite = input()
    print("Il vous ouvre la porte.")
    suite = input()
    print("Vous entrez à l'intérieur de la ferme.")
    suite = input()
    print("De nombreux objets tous plus bizarres les uns que les autres jonchent le sol.")
    suite = input()
    print("Au fond, vous remarquez une grande table avec une boule de cristal posée en évidence en son milieu.")
    suite = input()
    print("Vous butez sur une pile de livre posée sur le tapis et tombez à terre.")
    suite = input()
    print("Vous entendez un feulement près de vous.")
    suite = input()
    print("Le temps de vous relevez, et vous voyez le magicien avec un chat noir dans le bras.")
    suite = input()
    print("Magicien: Ne faites pas attention, ce n'est que Sarouminet, mon fidèle compagnon.")
    suite = input()
    print("Magicien: Dit bonjour, mon minet.")
    suite = input()
    print("Le chat ne fait que vous feuler dessus.")
    suite = input()
    print("Magicien: ... Bon, venez avec moi.")
    suite = input()
    print("Vous le suivez jusqu'à la grande table.")
    suite = input()
    print("Il commence à faire d'obscurs mouvements en direction de la boule de cristal, qui se trouble peu à peu.")
    suite = input()
    print("Vous remarquez sur le côté de la table un livre : 'Mémoires de Gandilf le Gris'.")
    suite = input()
    print("Magicien: Hé ! Occupez-vous de la boule de cristal, plutôt. C'est là que se trouve votre réponse.")
    suite = input()
    print("Vous vous concentrez comme demandé sur la boule de cristal.")
    suite = input()
    print("Magicien: Je vois...")
    suite = input()
    print("Magicien: ...")
    suite = input()
    print("Magicien: Le roi...")
    suite = input()
    print("Magicien: A ses côtés... Un homme...")
    suite = input()
    print("Magicien:  Une longue cape...")
    suite = input()
    print("Vous: Oui ! C'est ça !")
    suite = input()
    print("Magicien: Chut ! Ne me coupez pas !")
    suite = input()
    print("Vous: ...")
    suite = input()
    print("Magicien: Il a... Un titre...")
    suite = input()
    print("Magicien: Le Pape !")
    suite = input()
    print("Vous: Le Pape ?")
    suite = input()
    print("Magicien: Oui ! Le Pape Françis ! C'est lui, votre homme !")
    suite = input()
    print("Vous: Mais... C'est incensé ! Pourquoi ferait-il cela à ma pauvre mère ?")
    suite = input()
    print("Vous: ... Je ne peux pas voir les pensées des gens, malheureusement... Cependant...")
    suite = input()
    print("Il se lève et se penche vers une malle. il en sort une drôle de bague.")
    suite = input()
    print("Magicien: Tenez. Ca pourra vous aider. C'est mon anneau magique.")
    inventaire.append("anneau")
    suite = input()
    print("Magicien: Avec cela, vous passerez les portes de la ville sans aucun souci !")
    suite = input()
    print("Magicien: Trouvez cet homme, et apprenez la vérité !")
    suite = input()
    print("Vous: Euh, et bien... Merci... Je...")
    suite = input()
    print("Il vous met à la porte et vous crie 'bonne aventure'.")
    suite = input()
    print("...")
    suite = input()
    print("Vous: Et bien... Maintenant je sais où chercher...")
    suite = input()
    print("Il est grand temps de finir cette aventure...")
    suite = input()
    print("Que faire ?")
    print("1. Se rendre à Ciadas")
    print("2. Rebrousser chemin")
    rebrousser = None
    while rebrousser not in [1, 2]:
        try:
            rebrousser = int(input())
        except ValueError:
            print("Vous devez faire un choix")
        pass
    tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )

    print("Vous retournez sur vos pas.")
    suite = input()
    print("Après une longue marche, vous arrivez enfin aux portes de la ville")
    suite = input()
    print("Vous mettez l'anneau donné par le magicien.")
    suite = input()
    print("Vous vous approchez de l'entrée...")
    suite = input()
    print("Les gardes s'endorment sur place...")
    suite = input()
    print("Vous: Messieurs...")
    suite = input()
    print("Ils se réveillent brutalement, et écarquillent les yeux en vous voyant.")
    suite = input()
    print("Garde 1: Oh, monseigneur !")
    suite = input()
    print("Garde 2: Votre éminence...")
    suite = input()
    print("Vous: Je viens pour la cérémonie...")
    suite = input()
    print("Garde 2: Bien évidemment !")
    suite = input()
    print("Garde 1: Entrez donc !")
    suite = input()
    print("Vous passez les portes de la ville.")
    suite = input()
    print("Après avoir tourné dans une ruelle, vous enlevez l'anneau, pour rester incognito.")
    suite = input()
    print("Vous: Ce vieux fou n'était donc pas si fou que cela...")
    suite = input()

    entreeChateau(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)

####################################
####################################
####################################


def chifumi(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax):
    print("Magicien: Je ne m'attendais pas à ce que vous acceptiez... Mais soit !")
    suite = input()
    print("Magicien: Battons-nous !")
    suite = input()
    print("Magicien: Nous jouerons cette victoire en trois points gagnants !")
    suite = input()

    manche = 1

    pointsOrdi = 0
    pointsJoueur = 0

    while pointsOrdi < 3 and pointsJoueur < 3:
        print("Manche: ", manche)
        print("Choisissez votre coup:")
        print("1: Pierre")
        print("2: Feuille")
        print("3: Ciseau")

        choixCoupJoueur = None

        while choixCoupJoueur not in [1, 2, 3]:
            try:
                choixCoupJoueur = int(input("Entrez votre choix: "))
                if choixCoupJoueur == 1:
                    print("Vous choisissez pierre.")
                    suite = input()
                elif choixCoupJoueur == 2:
                    print("Vous choisissez feuille.")
                    suite = input()
                elif choixCoupJoueur == 3:
                    print("Vous choisissez ciseaux.")
                    suite = input()
            except ValueError:
                print("Vous devez entrer un chiffre entre 1 et 3.")

        choixCoupOrdi = randint(1, 3)
        if choixCoupOrdi == 1:
            print("Le magicien magique joue pierre.")
            suite = input()
        elif choixCoupOrdi == 2:
            print("Le magicien magique joue feuille.")
            suite = input()
        else:
            print("Le magicien magique joue ciseau.")
            suite = input()

        if choixCoupOrdi == choixCoupJoueur:
            print("Egalité !")
            suite = input()
            print("Personne ne gagne.")
            suite = input()

        elif choixCoupOrdi == 1 and choixCoupJoueur == 2:
            print("Vous avez gagné cette manche.")
            suite = input()
            pointsJoueur += 1
            print("Vous avez", pointsJoueur, "point(s).")
            suite = input()

        elif choixCoupOrdi == 2 and choixCoupJoueur == 3:
            print("Vous avez gagné cette manche.")
            pointsJoueur += 1
            print("Vous avez", pointsJoueur, "point(s).")
            suite = input()

        elif choixCoupOrdi == 3 and choixCoupJoueur == 1:
            print("Vous avez gagné cette manche.")
            pointsJoueur += 1
            print("Vous avez", pointsJoueur, "points.")
            suite = input()

        else:
            print("Vous avez perdu cette manche.")
            suite = input()
            pointsOrdi += 1
            print("Le magicien magique a", pointsOrdi, "points.")
            suite = input()

        manche += 1

    if pointsOrdi > pointsJoueur:
        print("Le magicien a gagné la partie.")
        suite = input()
        print("Magicien: Oh, oh ! Je ne suis donc pas si rouillé que ça !")
        suite = input()
    else:
        print("Vous avez gagné la partie.")
        suite = input()
        print("Magicien: C'est bien dommage... Nous aurons notre revanche !")
        suite = input()

####################################
####################################
####################################


def salleDuTrone(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax):
    print("Vous voici enfin arrivé à l'intérieur du château.")
    suite = input()
    print("La salle du trône est comble.")
    suite = input()
    print("Vous vous faufilez à travers les nobles et les servants,")
    suite = input()
    print("de sorte à avoir une vue d'ensemble de la salle.")
    suite = input()
    print("Vous: Mais où peut donc bien être ce Pape ?")
    suite = input()
    print("... ?")
    suite = input()
    print("...")
    suite = input()
    print("La cérémonie commence...")
    suite = input()
    print("Le roi de Tambarin arrive sur son trône.")
    suite = input()
    print("Un homme lit un long papier, ")
    suite = input()
    print("Il explique la présence des convives en ce jour.")
    suite = input()
    print("Le roi serait apparemment en recherche d'une prétendante...")
    suite = input()
    print("C'est donc pour cela qu'il a fait convier la majorité des seigneurs des pays voisins...")
    suite = input()
    print("Mais vous n'avez pas le temps pour cela.")
    suite = input()
    print("Vous avez remarqué le Pape, caché dans un coin derrière le trône du seigneur.")
    suite = input()
    print("...")
    suite = input()
    print("Il s'éclipse.")
    suite = input()
    print("Vous vous frayez un chemin à travers l'assemblée, suivant le Pape.")
    suite = input()
    print("A pas de loup, vous le chassez à travers les couloirs du château.")
    suite = input()
    print("Il s'arrête au milieu d'une pièce, ")
    suite = input()
    print("Tire un flambeau, ")
    suite = input()
    print("... Et la grande bibliothèque se déplace.")
    suite = input()
    print("...")
    suite = input()
    print("Il s'engouffre dans le passage secret.")
    suite = input()
    print("Vous le suivez.")
    suite = input()
    print("Vous arrivez tous les deux dans une grande pièce sombre.")
    suite = input()
    print("Il se retourne.")
    suite = input()
    print("Pape: Qui êtes vous ?!")
    suite = input()
    print("Vous: Je suis",nom, monBrave,"fils de Lasung, la gérante du...")
    suite = input()
    print("Pape: Oui, oui... Je vois... Et que me vaut votre visite ?")
    suite = input()
    print("Vous: Vous l'avez tuée !!!")
    suite = input()
    print("Pape: Vous ne comprenez pas...")
    suite = input()
    print("Pape: Elle le voulait.")
    suite = input()
    print("Pape: C'était pour la bonne cause...")
    suite = input()
    print("Pape: La prophétie va enfin se réaliser.")
    suite = input()
    print("Vous: De quoi parlez-vous ?! Ma mère n'aurait jamais voulu mourir de la sorte !")
    suite = input()
    print("Vous lui foncez dessus.")
    fightFinal(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)

####################################
####################################
####################################

def fightFinal(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax):
  vieRestante = vieTotale
  monsterLife = 150

  print("Le Pape dégaine son sceptre et riposte.")
  suite = input()
  print("\n", "-" * 50, "\n")
  suite = input()

  while vieRestante >= 0 or monsterLife > 0:
    yourAttack = randint(forceMin, forceMax)
    monsterAttack = randint(5, 15)

    print("Vous avez", vieRestante, "points de vie")
    suite = input()
    print("Le Pape a", monsterLife, "points de vie.")
    suite = input()

    if vieRestante > 0:
      print("Vous frappez le Pape et lui enlevez",yourAttack, "points de vie.")
      monsterLife = monsterLife - yourAttack
      suite = input()

    if monsterLife <= 0:
      print("\n", "-" * 50, "\n")
      print("Le Pape tombe à terre, exténué.")
      suite = input()
      print("Pape Françis: Vous m'avez eu...")
      print("\n", "-" * 50, "\n")
      suite = input()
      print("Vous: Dites-moi pourquoi avez vous fait cela à ma mère !")
      suite = input()
      print("Pape Françis: Je...")
      suite = input()
      print("Pape Françis: C'était... L'élue...")
      suite = input()
      print("Pape Françis: Elle le voulait...")
      suite = input()
      print("Pape Françis: Allez... Voir... Le puit...")
      suite = input()
      print("Pape Françis: Village...")
      suite = input()
      print("Pape Françis: Et vous saurez...")
      suite = input()
      print("\n", "-" * 50, "\n")
      print("\n", "-" * 50, "\n")
      print("\n", "-" * 50, "\n")
      print("A suivre...")
      print("\n", "-" * 50, "\n")
      print("\n", "-" * 50, "\n")
      print("\n", "-" * 50, "\n")
      print('')
      print("Merci d'avoir testé notre jeu !")
      print('')
      return vieRestante
      return gameOver()
    elif vieRestante <= 0:
      print("Vous tombez à terre, exténué !")
      suite = input()
      print("Le Pape vous jette par dessus une fenêtre.")
      suite = input()
      print("Vous êtes ramené à l'entrée de la ville.")
      EntreeCiadas()
      return vieRestante
    else:
      print("Le Pape vous attaque et vous enlève",monsterAttack, "points de vie.")
      vieRestante = vieRestante - monsterAttack
      suite = input()

####################################
####################################
####################################

def entreeChateau(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax):
  #######################
  #    Entree chateau   #
  #######################
  lieuvisite.append("entreechateau")
  print("Maintenant que vous êtes dans la ville, il vous faut réussir à accéder au château.")
  suite = input()
  print("Vous remontez les rues de la ville jusqu'à arriver aux portes du château.")
  suite = input()
  print("Des gardes sont postés à l'entrée.")
  suite = input()
  if "anneau" in inventaire:
    print("Vous: Il serait plus judicieux de remettre l'anneau pour réussir à passer...")
    suite = input()
    print("Vous remettez l'anneau à votre doigt, et avancez jusqu'aux portes.")
    suite = input()
    print("les gardes vous laissent passer.")
    suite = input()
    salleDuTrone(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
  else:
    print("Vous vous avancez, mais la route vous est bien vite barrée.")
    suite = input()
    print("Garde 1: Halte-là mon brave. Seuls les nobles peuvent accéder à la salle du trône.")
    suite = input()
    print("Garde 2: Nous devons assurer la bonne tenue du sacre...")
    suite = input()
    print("...")
    suite = input()
    print("Vous allez devoir trouver un autre moyen pour passer l'entrée du château...")
    suite = input()
    centrevilleCiadas(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite)

#######################
#     Centre-ville    #
#######################  
def centrevilleCiadas(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite):
  lieuvisite.append("centreville")
  print("Vous redescendez vers le centre-ville.")
  suite = input()
  print("Vous: Il y aura bien quelque chose qui pourra me servir...")
  suite = input()
  print("...")
  suite = input()
  print("Vous vous baladez au hasard dans la ville.")
  suite = input()
  print("...")
  suite = input()

  #######################
  #        Tissus       #
  #######################
  print("Vous arrivez rapidement devant un marchand de tissus")
  suite = input()
  print("1. Y entrer")
  print("2. Rebrousser chemin")
  print("3. Continuer sa route")
  rebrousse = None
  while rebrousse not in [1, 2, 3]:
    try:
      rebrousse = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  if rebrousse == 1:
    print("Vous entrez dans le commerce.")
    suite = input()
    print("Vous saluez le marchand.")
    suite = input()
    print("Vous remarquez une belle étoffe en velours.")
    suite = input()
    print("Cela pourrait vous être utile...")
    suite = input()
    print("Voulez vous acheter cette étoffe ?")
    acheter = None
    while acheter not in [1, 2]:
      try:
        print("1. Acheter l'étoffe pour 100 pièces")
        print("2. Ne pas acheter")
        print("")
        acheter = int(input("Acheter cet objet pour 100 pièces ?"))
      except ValueError:
        print("Vous devez faire un choix")
      pass
      if acheter == 1:
        if argent >= 100:
          print("Vous avez acheté l'étoffe au marchand")
          inventaire.append("cape")
          argent = argent - 100
          suite = input()
        else:
          print("")
          print("Vous n'avez pas assez pour acheter cette étoffe.")
      elif acheter == 2:
        print("Vous: On va chercher autre chose...")
        suite = input()
      tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )
      if rebrousse == 3:
        print("Vous: On va chercher autre chose...")
        suite = input()
  print("...")
  suite = input()

  #######################
  #        Forge        #
  #######################
  print("Vous continuez votre balade et arrivez devant une forge.")
  suite = input()
  print("1. Y entrer")
  print("2. Rebrousser chemin")
  print("3. Continuer sa route")
  rebrousse = None
  while rebrousse not in [1, 2, 3]:
    try:
      rebrousse = int(input())
      if rebrousse == 1:
        print("Vous entrez dans le commerce.")
        suite = input()
        print("Vous entendez le tintement du métal frappé par le forgeron.")
        suite = input()
        print("Vous remarquez une grande épée dont le fourreau en cuir est orné de pierres.")
        suite = input()
        print("Cela pourrait vous être utile...")
        suite = input()
        print("Voulez vous acheter cette épée ?")
        acheter = None
        while acheter not in [1, 2]:
          try:
            print("1. Acheter l'épée pour 150 pièces")
            print("2. Ne pas acheter")
            print("")
            acheter = int(input("Acheter cet objet pour 150 pièces ?"))
            if acheter == 1:
              if argent >= 150:
                print("Vous avez acheté l'épée au forgeron")
                inventaire.append("epee")
                argent = argent - 150
                suite = input()
              else:
                print("")
                print("Vous n'avez pas assez pour acheter cette épée.")
            elif acheter == 2:
              print("Vous: On va chercher autre chose...")
              suite = input()
          except ValueError:
            print("Vous devez faire un choix")
          pass
      tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )
      if rebrousse == 3:
        print("Vous: On va chercher autre chose...")
        suite = input()
    except ValueError:
      print("Vous devez faire un choix")
    pass
  print("...")
  suite = input()

  #######################
  #        Eglise       #
  #######################
  print("Vous continuez votre balade et arrivez devant une église.")
  suite = input()
  print("1. Y entrer")
  print("2. Rebrousser chemin")
  print("3. Continuer sa route")
  rebrousse = None
  while rebrousse not in [1, 2, 3]:
    try:
      rebrousse = int(input())
      if rebrousse == 1:
        print("Vous entrez dans l'Eglise.")
        suite = input()
        print("...")
        suite = input()
        print("Vous priez pour votre mère.")
        suite = input()
        print("En sortant, vous remarquez une annonce : ")
        suite = input()
        print("'Nos moines copistes rédigeront toute lettre pour la modique somme de 50 pièces !'")
        suite = input()
        print("C'est cher... Mais vous pourriez obtenir votre entrée pour le château...")
        suite = input()
        print("Même si pour cela vous devez donner 50 pièces au tueur de votre mère...")
        acheter = None
        while acheter not in [1, 2]:
          try:
            print("1. Se faire rédiger une invitation par un moine copiste")
            print("2. Ne pas se faire rédiger l'invitation")
            print("")
            acheter = int(input("Acheter l'invitation pour 50 pièces ?"))
            if acheter == 1:
              if argent >= 50:
                print("Le moine a rédigé votre invitation")
                inventaire.append("invitation")
                argent = argent - 50
                suite = input()
              else:
                print("")
                print("Vous n'avez pas assez pour acheter cette invitation.")
            elif acheter == 2:
              print("Vous: On va chercher autre chose...")
              suite = input()
          except ValueError:
            print("Vous devez faire un choix")
          pass
      tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )
      if rebrousse == 3:
        print("Vous: On va chercher autre chose...")
        suite = input()
    except ValueError:
      print("Vous devez faire un choix")
    pass
    print("...")
    suite = input()

    #######################
    #       Taverne       #
    #######################
    print("Vous vous retrouvez devant la taverne.")
    suite = input()
    print("1. Se rendre à l'entrée du château")
    print("2. Rebrousser chemin")
    print("3. Entrer dans la taverne")
    rebrousse = None
    while rebrousse not in [1, 2, 3]:
      try:
        rebrousse = int(input())
        if rebrousse == 1:
          retourChateauCiadas(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
        tuRebrousse1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite )
        if rebrousse == 3:
          taverneCiadas(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
      except ValueError:
        print("Vous devez faire un choix")
      pass

####################################
####################################
####################################

def taverneCiadas(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax):
  print("Vous entrez dans la taverne.")
  suite = input()
  print("Les gens y parlent fort et l'alcool coule à flot")
  suite = input()
  print("Vous achetez une bière pour 10 pièces.")
  argent = argent - 10
  suite = input()
  print("...")
  suite = input()
  print("Après être bien alcoolisé, vous vous bagarrez avec deux individus et finissez jeté dehors.")
  suite = input()
  print("les gardes ont été appelés et vous finissez au cachot.")
  #######################
  #        Cachot       #
  #######################
  suite = input()
  print("...")
  suite = input()
  print("Vous vous réveillez lentement de votre transe.")
  suite = input()
  print("Vous avez très mal au crâne...")
  suite = input()
  print("Vous entendez un bruit bizarre de l'autre côté de la pièce...")
  suite = input()
  print("Un vieil homme bizarre est assis là, une patate à la main.")
  suite = input()
  print("1. S'évader")
  print("2. Lui parler")
  choix = None
  while choix not in [1, 2]:
      try:
        choix = int(input())
        if choix == 1:
          if "couteau" in inventaire:
            print("Vous crochetez la serrure.")
            suite = input()
            print("...")
            suite = input()
            print("Vous voilà hors de la cellule !")
            suite = input()
            print("Il est enfin temps pour vous de vous rendre à cette cérémonie...")
            suite = input()
            salleDuTrone(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
          else:
            print("Vous essayez de crocheter la serrure... En vain.")
            suite = input()
            print("...")
            suite = input()
            print("Vous feriez mieux de parler au vieil homme plutôt que de rester là...")
            suite = input()
            print("Vous vous approchez du vieil homme...")
            suite = input()
            print("Homme à la patate: Schneubeugleu !?")
            suite = input()
            print("Vous: ?!")
            suite = input()
            print("Vous ne comprenez rien à son charabia.")
            suite = input()
            print("Homme à la patate: “coudoussère, Holretemps, frappincechame drepintalisse !!!")
            suite = input()
            print("Soudain, il vous frappe à la tête avec sa patate, qui est aussi dure que la pierre...")
            suite = input()
            print("Vous tombez dans un profond sommeil...")
            suite = input()
            print("A votre réveil, la porte du cachot est ouverte...")
            suite = input()
            print("Le vieux fou n'est plus là...")
            suite = input()
            print("... Mais vous n'avez plus de ceinture.")
            suite = input()
            print("Vous vous levez précipitemment et vous échappez.")
            suite = input()
            salleDuTrone(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
        if choix == 2 :
            print("Vous vous approchez du vieil homme...")
            suite = input()
            print("Homme à la patate: Schneubeugleu !?")
            suite = input()
            print("Vous: ?!")
            suite = input()
            print("Vous ne comprenez rien à son charabia.")
            suite = input()
            print("Homme à la patate: “coudoussère, Holretemps, frappincechame drepintalisse !!!")
            suite = input()
            print("Soudain, il vous frappe à la tête avec sa patate, qui est aussi dure que la pierre...")
            suite = input()
            print("Vous tombez dans un profond sommeil...")
            suite = input()
            print("A votre réveil, la porte du cachot est ouverte...")
            suite = input()
            print("Le vieux fou n'est plus là...")
            suite = input()
            print("... Mais vous n'avez plus de ceinture.")
            suite = input()
            print("Vous vous levez précipitemment et vous échappez.")
            suite = input()
            salleDuTrone(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
      except ValueError:
        print("Vous devez faire un choix")
      pass

def retourChateauCiadas(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax):
          print("Vous retournez à l'entrée du château")
          suite = input()
          if "cape" or "epee" or "invitation" in inventaire:
            print("Vos précieux achats vous permettront peut-être d'accéder à la salle du trône...")
            suite = input()
            print("...")
            suite = input()
            print("Avec vos précieuses acquisitions, vous réussissez à passer sans peine devant les gardes !")
            salleDuTrone(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
          else:
            print("...")
            suite = input()
            print("Malheureusement les gardes ne vous laissent toujours pas passer...")
            suite = input()
            print("Que faire ?")
            print("1. Chercher de l'aide ailleurs")
            print("2. Rebrousser chemin")
            print("3. Se rendre à la taverne")
            rebrousse = None
            while rebrousse not in [1, 2, 3]:
              try:
                rebrousse = int(input())
                if rebrousse == 1:
                  magicien(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
                tuRebrrousses1(rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax, lieuvisite)
                if rebrousse == 3:
                  taverneCiadas(inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
              except ValueError:
                print("Vous devez faire un choix")
              pass


#Début de l'aventure
#Run the game different parts of the game
def Aventure(inventaire, argent, arme, monBrave, nom, vieTotale): 
  print ("Commencer l'aventure !")
  suite = input()
  foret (inventaire, argent, arme, monBrave, nom, vieTotale, forceMin, forceMax)
  villageAbandonne(inventaire, argent, arme, monBrave, nom, vieTotale)
  moulin(inventaire, argent, arme, monBrave, nom, vieTotale)
  pont(inventaire, argent, arme, monBrave, nom, vieTotale)
  print("fin")
  
  
def gameOver():
  return("FIN")
#Run the game
def Jeu():
  inventaire, argent, arme, monBrave, nom = Intro()
  Aventure(inventaire, argent, arme, monBrave, nom, vieTotale)

Jeu()



