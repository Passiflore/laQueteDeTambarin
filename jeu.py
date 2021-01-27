vieTotale = 100
charisme = 10
force = 20
argent = 100
inventaire =[]
lieuvisite =[]

#Global imports
from random import *
# import secrets

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
   choix1 = int(input())

def sortir(peur):
  if peur == 2: 
    print("Reprends toi, il est grand temps d'affronter le monde. C'est la même chose tous les jours et ça ne changera jamais")

def nomSexe(nom,sexe):
  monBrave = "mon brave"
  # if nom == "Triceratops":
  #   vie = vie + 10
  #   print("Votre vie est de",vie)
  # if nom == "Boubou":
  #   print("Bonus de crâne chauve")
  #   charisme = charisme + 20
  #   print("Votre charisme est de", charisme)
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
    return GameOver

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
      while revenir not in [1, 2, 3]:
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
def fightLevel1(vieTotale):
  vieRestante = vieTotale
  youAlive = True
  forceMin = 5
  forceMax = 15

  monsters = ["rat", "sanglier", "troll", "blaireau", "serpent", "crapeau", "feu follet"]
  monstersLifeChoice = [10, 15, 15, 20, 25, 30]
  monsterLife = secrets.choice(monstersLifeChoice)

  print("Vous vous êtes trop enfoncés dans la forêt.")
  suite = input()
  print("Vous arrivez face à un", secrets.choice(monsters), "et un", secrets.choice(monsters),".")
  print("\n", "-" * 50, "\n")

  while vieRestante >= 0 and monsterLife > 0 :
    yourAttack = randint(forceMin, forceMax)
    monsterAttack = randint(2, 10)

    suite = input()
    print("Vous avez", vieRestante, "points de vie")
    suite = input()
    print("Les monstres ont", monsterLife, "points de vie.")
    suite = input()
    print("Vous frappez les monstres et leur enlevez", yourAttack, "points de vie.")
    monsterLife = monsterLife - yourAttack
    suite = input()

    if monsterLife <= 0 :
      monsterAlive = False
      print("\n", "-" * 50, "\n")
      print("Les monstres sont morts !")
      suite = input()
      print("Vouz continuez votre route...")
      return vieRestante
    elif vieRestante <= 0 :
      youAlive = False
      print("Vous êtes mort !")
      suite = input()
      print("Un passant vous a retrouvé et vous a ramené au village.")
      suite = input()
      print("Vous vous retrouvez au magasin général.")
      magasin()
      return vieRestante
    else : print("Les monstres vous frappent et vous enlèvent", monsterAttack, "points de vie.")
    vieRestante = vieRestante - monsterAttack
    suite = input()

# 2eme partie du jeu
def magasin(inventaire, argent, arme, monBrave, nom, vieTotale):
  print("Vous retournez au magasin général")
  print("Ah, te revoilà", nom, "y a t-il eu de l'avancement dans ta quête ?")

def tuRebrousse1 (rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale):
  if rebrousser == 2:
    print_slow("Vous : Les forêts ça fait toujours peur, c'est inquiétant, il serait plus judicieux de rebrousser chemin...")
    suite = input()
    magasin (inventaire, argent, arme, monBrave, nom)
    foret (inventaire, argent, arme, monBrave, nom, vieTotale)

def foret(inventaire, argent, arme, monBrave, nom, vieTotale):

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
  tuRebrousse1 (rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale)

  vieTotale = fightLevel1(vieTotale)

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
  tuRebrousse1 (rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale)

  vieTotale = fightLevel1(vieTotale)
  
  #niv3
  suite = input()
  print("Vous trouvez un bâton couvert de mousse")
  suite = input()
  if "couteau" in inventaire:
    print_slow("Vous : Quelques petits coups de couteau...")
    suite = input()
    print_slow("Vous : TADAM ! Un pieu en bois")
    inventaire.append("Pieu")
  else :
    print("Vous le jettez")
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
  tuRebrousse1 (rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale)

  vieTotale = fightLevel1(vieTotale)

  #niv4
  suite = input()
  print("Vous arrivez à l’orée d’une clairière, qui possède un magnifique lac. Dans l’eau, une femme profite de la chaleur du soleil sur son corps.")
  suite = input()
  print("Parler à la femme")
  suite = input()
  print_slow("\033[1;32;40m Femme: Bonjour mon enfant. Veux-tu que je te lise ton avenir ?\n\033[m")

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
    print_slow("\033[1;37;40m Vous: Vous me semblez bien sage, que pouvez-vous me dire sur mon futur ?\033[m")
    suite = input()
    print_slow("\033[1;32;40m Femme: Je vois...\033[m")
    suite = input()
    print_slow("\033[1;32;40m Femme: dans l'eau claire...\033[m")
    suite = input()
    print_slow("\033[1;32;40m Femme: un avenir incertain...\033[m")
    suite = input()
    print("\033[1;33;40m Cela ne vous est pas très utile...\n\033[m")
  
  print("\033[0;37;40m Que faire ?\033[m")
  print("1.Continuer")
  print("2.Rebrousser chemin")
  rebrousser  = None
  while rebrousser not in [1, 2]:
    try:
      rebrousser = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  tuRebrousse1 (rebrousser,inventaire, argent, arme, monBrave, nom, vieTotale)

  vieTotale = fightLevel1(vieTotale)
  
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
  print("Il vous reste", vieTotale, "points de vie")

  return inventaire, argent, arme, monBrave, nom, vieTotale
  

def tuRebrousse2 (renoncer,inventaire, argent, arme, monBrave, nom, vieTotale):
  if renoncer == 2:
    print("Vous: Il doit être hanté depuis un moment… j’ai peur des fantômes")
    magasin(inventaire, argent, arme, monBrave, nom, vieTotale)
    moulin(inventaire, argent, arme, monBrave, nom, vieTotale)


def villageAbandonne(inventaire, argent, arme, monBrave, nom, vieTotale):
  print("Vous continuez votre aventure, et vos pas vous emmènent à l’orée d’un vieux village.")
  suite = input()
  print("Que faire ?")
  print("1.Entrer dans le village")
  print("2.Passer son chemin")
  renoncer = None
  while renoncer not in [1, 2]:
    try:
      renoncer = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  tuRebrousse2 (renoncer,inventaire, argent, arme, monBrave, nom, vieTotale)
  
  suite = input()
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
  print("Que faire ?")
  print("1.Continuer dans le village")
  print("2.Renoncer à l'exploration")
  renoncer = None
  while renoncer not in [1, 2]:
    try:
      renoncer = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
  tuRebrousse2 (renoncer,inventaire, argent, arme, monBrave, nom, vieTotale)

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
  renoncer = None
  while renoncer not in [1, 2]:
    try:
      renoncer = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
    tuRebrousse2 (renoncer,inventaire, argent, arme, monBrave, nom, vieTotale)

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
  while renoncer not in [1, 2]:
    try:
      renoncer = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
    tuRebrousse2 (renoncer,inventaire, argent, arme, monBrave, nom, vieTotale)
  
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


def tuRebrousse3 (abandonner,inventaire, argent, arme, monBrave, nom, vieTotale):
  if abandonner == 2:
    print("Cet endroit à l'air sent le piège... Je préfère ne pas m'y risquer")
    magasin(inventaire, argent, arme, monBrave, nom, vieTotale)
    pont(inventaire, argent, arme, monBrave, nom, vieTotale)


def moulin(inventaire, argent, arme, monBrave, nom, vieTotale):
  print("Vous continuez votre aventure, et traversant à travers un pré recouvert de fleurs,vous tombez sur un champ de blé au fond duquel se trouve un moulin.")
  suite = input()
  print("Vous traversez le champ de blé, en y arrachant un épi au passage")
  vieTotale = fightLevel1(vieTotale)
  print("Vous arrivez au moulin")
  suite = input()
  print("Vous...")
  print("1.Aller voir si quelqu’un se trouve ici")
  print("2.Rebroussez chemin. Je ne connais pas la personne qui vit ici c'est peut être Xavier Dupont de Ligonnès")
  abandonner = None
  while abandonner not in [1, 2]:
    try:
      abandonner = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
    tuRebrousse3 (abandonner,inventaire, argent, arme, monBrave, nom, vieTotale)

  print("Aucune réponse...")
  suite = input()
  print("Vous...")
  print("1.Insistez")
  print("2.Ne vous acharnez pas. Il ne doit y avoir personne ici")
  abandonner = None
  while abandonner not in [1, 2]:
    try:
      abandonner = int(input())
    except ValueError:
      print("Vous devez faire un choix")
    pass
    tuRebrousse3 (abandonner,inventaire, argent, arme, monBrave, nom, vieTotale)

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
      print ("Vous n'avez pas assez d'argent")
      soudoyer = 2
    elif argent >= 200:
      print ("Vous...")
      print ("1. Lui donnez 200 pièces")
      print ("2. Ne lui donnez rien.")
      amadouer = None
    while amadouer not in [1, 2]:
      try:
        amadouer = int(input())
      except ValueError:
        print("Vous devez faire un choix")
      pass

  elif soudoyer == 2 or amadouer == 2:
    abandonner = 2
    tuRebrousse3 (abandonner,inventaire, argent, arme, monBrave, nom, vieTotale)
  
  elif "baie" in inventaire and soudoyer == 3 or amadouer == 1:
    print("3. J’ai un cadeau pour vous monsieur. Laissez-moi vous l’offrir s’il vous plait…")
    suite = input()
    print ("L’homme ouvre alors la porte, intrigué")
    suite = input()
    print ("Vieux meunier: Oh ! Cela fait si longtemps que je n’ai pas eu de cadeaux ! Entrez", monbrave, "venez me raconter vos aventures et vous réchauffer !")
    suite = input()
    print ("Après avoir vous êtres installé près du feu, vous racontez votre histoire au vieux meunier.")
    suite = input()
    print("Vieux meunier: Je suis désolé de ce qui vous arrive et je vous demande pardon pour mon accueil peu chaleureux. Tenez du pain pour me faire pardonner de mon comportement")
    inventaire.append("pain")
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
  return inventaire, argent, arme, monBrave, nom, vieTotale


#Début de l'aventure
#Run the game different parts of the game
def Aventure(inventaire, argent, arme, monBrave, nom): 
  print ("Commencer l'aventure !")
  suite = input()
  foret (inventaire, argent, arme, monBrave, nom, vieTotale)
  villageAbandonne(inventaire, argent, arme, monBrave, nom, vieTotale)
  moulin(inventaire, argent, arme, monBrave, nom, vieTotale)
  pont(inventaire, argent, arme, monBrave, nom, vieTotale)

#Run the game
def Jeu():
  inventaire, argent, arme, monBrave, nom = Intro()
  Aventure(inventaire, argent, arme, monBrave, nom)

Jeu()



