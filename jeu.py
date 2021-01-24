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
    return print("Reprends toi, il est grand temps d'affronter le monde. C'est la même chose tous les jours et ça ne changera jamais")

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
    objet = "loupe"
    print("Excellent choix !")
    return objet
  elif objetDepart == 2: 
    print("Ça peut toujours vous dépanner et vous sauver de situations périlleuses")
    suite = input()
    objet = "couteau"
    print("Excellent choix !")
    return objet
  elif objetDepart == 3: 
    print("Vous aurez forcément froid… C’est ce que disent toutes les mamans.")
    tenue = "pull"
    suite = input()
    print("Excellent choix !")
    return objet

def choixDirection(direction):
  precedentDirection ="droite"
  while direction != 3:
    if direction == 1: 
      if precedentDirection =="face":
        print("Vous vous dirigez vers l’entrée de la ville.")
        print("Il vous manque peut être quelque chose avant d'affronter la ville")
      else: 
        print("Vous rencontrez des enfants qui jouent avec un papillon")
        suite = input()
        print("Qu’avez-vous vu passer ?")
        suite = input()
        print("Un monsieur a couru vers l’entrée de la ville, mais il est loin maintenant…")
        suite = input()
        if objet == "loupe":
          print("Inspecter le papillon : il a les pattes pleines de poussière…")
          suite = input()
        print("Rebrousser Chemin")
        precedentDirection ="gauche"
    elif direction == 2:
      precedentDirection =="face"
      print("Vous arrivez à l’entrée d’une maison. Vous toquez mais personne ne répond. La porte est entre-ouverte…")
      suite = input()
      print("Vous...")
      print("1.Entrez")
      print("2.Rebroussez chemin")
      rebrousse = int(input())
      if rebrousse == 1:
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
      elif rebrousse == 2:
        print("Vous rebroussez chemin et revenez à votre point de départ.")
    print("Quel chemin prendre ?")
    print("1.Aller à gauche")
    print("2.Aller en face")
    print("3.Aller à droite")
    direction = int(input())

def choixArme(armement):
  if armement == 1 and argent >= 150:
    arme = "arc"
    return argent-150, arme
  elif armement == 2 and argent >= 100:
    arme = "hache"
    return  argent-100, arme
    print("Vous a choisissez")
  elif armement == 3 and argent >= 25:
    arme = "bâton"
    return argent-100 , arme
  elif armement == 4 and argent >= 20:
    return argent-20, arme
  else:
    print("t'as pas assez d'argent pour cela refais un choix:")
    print("Vous choisissez:")
    print("1.Un arc/arbalète (150 pièces)")
    print("2.Une hache (100 pièces)")
    print("3.Un bâton (25 pièces)")
    print("4.Un marteau (20 pièces)")
    armement = int(input())
    choixArme(armement)

def Intro(): 
  #Commecer l'intro
  print('Mère : Hé ! Qu’est ce que tu fais encore là à roupiller viens m’aider plutôt. Les jeunes de nos jours…')
  print('(Appyuez sur ent. pour la suite)')
  suite = input()
  print('Vous ouvrez lentement les yeux, pour découvrir baignant dans la lumière du matin, le plafond en bois de chêne de votre chambre.')
  suite = input()
  print('Encore ensommeillé, vous percevez des odeurs de lait chaud, de miel, de confiture et de pain fraichement sorti du four.')
  print('Depuis la fenêtre, vous entendez l’agitation de la ville, le bruit des passants, le bourouha du marché et les résonnements du clocher.')
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
  choix1 = int(input())
  TutoChoix1(choix1)
  print('Une banale porte en bois. Le bas de porte est parsemé des griffes de votre chat.')

  suite = input()
  print('Il est temps d’aider votre mère à l’auberge.')
  suite = input()

  #Choix 2
  print('Sortir ?')
  print('1.oui')
  print('2.Non les humains me font peur ')
  peur = int(input())
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
  sexe = int(input())
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
  choix3 = int(input())

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
  cVie = int(input())

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
  argent = 100

  #ObjetDepart
  print("Qu’est-ce que vous y mettez ? (1 seul choix)")
  print("1.Une loupe")
  print("2.Un couteau suisse")
  print("3.Un pull")
  objetDepart = int(input())

  objet =  choixObjetDepart(objetDepart)

  print("Maintenant que vous êtes fin prêt, vous dites au-revoir à la maison de votre enfance et la fermez à clé.")
  suite = input()
  print("Votre recherche peut enfin commencer, mais… Par quel côté aller en premier ?")

  #ChoixDirection

  print("Quel chemin prendre ?")
  print("1.Aller à gauche")
  print("2.Aller en face")
  print("3.Aller à droite")
  direction = int(input())

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
  print("Vous disposez de",argent,"pièces")
  print("Vous choisissez:")
  print("1.Un arc/arbalète (150 pièces)")
  print("2.Une hache (100 pièces)")
  print("3.Un bâton (25 pièces)")
  print("4.Un marteau (20 pièces)")
  armement = int(input())

  argent, arme = choixArme(armement)
  print("Vous disposez maintenant de", arme, "et il vous reste", argent , "pièces")

  suite = input()
  print("Ce fut un plaisir de commercer avec vous ! Je vous souhaite beaucoup de chance dans votre quête !")
  suite = input()
  print("Vous: Merci… ")
  suite = input()
  print("Sortir du magasin général")
  suite = input()
  print("Il est temps de partir maintenant… ")
  suite = input()
  print("Se rendre à gauche")
  suite = input()
  print("Vous arrivez rapidement aux portes de village.")
  suite = input()
  print("Vous n’êtes jamais réellement allé loin d’ici, et vous savez que de nombreux monstres rôdent à l’extérieur,")
  suite = input()
  print("mais il vous faut faire face afin de réussir à rendre justice pour votre mère…")
  suite = input()

Intro()
