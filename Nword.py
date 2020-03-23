def intro():
    print("\n/////////////////////////////Created by Natfuss///////////////////////////////////")
    print(r"::::::::::::::::::::::::::::::::::::::/8\::::::::::::::::::::::::::::::::::::::::::::")
    print(r"///////////////Entrez toutes les informations en minuscules\\\\\\\\\\\\\\\\\\\\\\\\\\")
    print("--------------------------------------------------------------------------------------")
    return interactive()


def interactive():

    "On demande toutes les infos et on les entres dans le dico (profil) :"

    profil = {}

    prenom = input("\n>Prenom : ")
    while len(prenom) == 0 or prenom == '' or prenom == ' ': # On empeche l'utilistateur
        print("\n>Vous devez entrer un prenom.")              # de ne pas mettre de prenom
        prenom = input("\n>Prenom : ")

    nom = input(">Nom : ")
    surnom = input(">Surnom : ")

    profil['prenom'] = str(prenom)
    if len(nom) != 0:
        profil['nom'] = str(nom)
    if len(surnom) != 0:
        profil['surnom'] = str(surnom)


    date_naissance = input(">Date de naissance (xx/xx/xxxx) : ")
    if len(date_naissance) != 0:
        profil['date_naissance'] = str(date_naissance)

    prenom_bis = input("\n>Prenom d'un Frere ou d'une Soeur (ou autre) : ")
    surnom_bis = input(">Surnom du Frere ou de la Soeur (ou autre) : ")
    date_naissance_bis = input(">Date de naissance du Frere ou de la Soeur (xx/xx/xxxx) : ")

    if len(prenom_bis) != 0:
        profil['prenom_bis'] = str(prenom_bis)
    if len(surnom_bis) != 0:
        profil['surnom_bis'] = str(surnom_bis)
    if len(date_naissance_bis) != 0:
        profil['date_naissance_bis'] = str(date_naissance_bis)

    autre = input("\n>Autre info (une info a la fois) : ")
    sup = 1
    while len(autre) != 0:
        profil[sup] = autre
        autre = input("\n>Autre info : ")
        sup +=1

    return bd_mix(profil)

def bd_mix(profil):

    if 'date_naissance' in profil.keys():

    	bdj = profil['date_naissance'][0:2]
    	profil['jour'] = str(bdj)

    	bdm = profil['date_naissance'][2:4]
    	profil['mois'] = str(bdm)

    	bdy_xxxx = profil['date_naissance'][4:9]
    	profil['y_xxxx'] = str(bdy_xxxx)

    	bdy_xxx = profil['date_naissance'][5:9]
    	profil['y_xxx'] = str(bdy_xxx)

    	bdy_xx = profil['date_naissance'][6:9]
    	profil['y_xx'] = str(bdy_xx)

    "On s'occupe maintenant de la deuxieme partie (bis)"

    if 'date_naissance_bis' in profil.keys():

    	bdj_bis = profil['date_naissance_bis'][0:2]
    	profil['jour_bis'] = str(bdj_bis)

    	bdm_bis = profil['date_naissance_bis'][2:4]
    	profil['mois_bis'] = str(bdm_bis)

    	bdy_xxxx_bis = profil['date_naissance_bis'][4:9]
    	profil['y_xxxx_bis'] = str(bdy_xxxx_bis)

    	bdy_xxx_bis = profil['date_naissance_bis'][5:9]
    	profil['y_xxx_bis'] = str(bdy_xxx_bis)

    	bdy_xx_bis = profil['date_naissance_bis'][6:9]
    	profil['y_xx_bis'] = str(bdy_xx_bis)

    return mix(profil)

def mix(profil):

    char = [
    r'#', '@', '%', '&', '!',
    '*', ',', '=', '+','$',
    '~', '_', '-', '?', '£'
    ]
    numb = ['0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9', '10'
    ]
    nom_fichier = input("\n\t[+] Entrez le nom du fichier : ")
    with open(nom_fichier, 'w') as word: # On ouvre un fichier en mode ecriture

        "a 2"
        for a1 in profil.values():
            for b1 in profil.values():
                mix_a_2 = a1+b1                           # On creer un mix d'une addition de toutes les valeures
                mix_a_2_up = mix_a_2[0:].title()          # On met la premiere lettre en majuscule
                mix_a_2_maj = mix_a_2.upper()             # On met tout en majuscule
                word.write(f"{mix_a_2}\n")     # et on le met dans le fichier
                word.write(f"{mix_a_2_up}\n")
                word.write(f"{mix_a_2_maj}\n")
        "a 3"
        for a2 in profil.values():
            for b2 in profil.values():
                for c2 in profil.values():
                    mix_a_3 = a2+b2+c2                # Idem mais avec une addition de toutes les valeures 3 fois
                    mix_a_3_up = mix_a_3[0:].title()
                    mix_a_3_maj = mix_a_3.upper()
                    word.write(f"{mix_a_3}\n")
                    word.write(f"{mix_a_3_up}\n")
                    word.write(f"{mix_a_3_maj}\n")
        "a 4"
        for a3 in profil.values():
            for b3 in profil.values():
                for c3 in profil.values():
                    for d3 in profil.values():
                        mix_a_4 = a3+b3+c3+d3      # Idem mais avec une addition de toutes les valeures 4 fois
                        mix_a_4_up = mix_a_4[0:].title()
                        mix_a_4_maj = mix_a_4.upper()
                        word.write(f"{mix_a_4}\n")
                        word.write(f"{mix_a_4_up}\n")
                        word.write(f"{mix_a_4_maj}\n")
        "char simple"
        for a1 in profil.values():
            for b1 in char:
                spe_char = a1+b1                # On associe a chaque valeures un char
                spe_char_up = spe_char[0:].title()
                spe_char_maj = spe_char.upper()
                word.write(f"{spe_char}\n")
                word.write(f"{spe_char_up}\n")
                word.write(f"{spe_char_maj}\n")
        "char intermediaire"
        for a2 in char:
            for b2 in char:
                char_mix = a2 + b2
                for c2 in profil.values():
                    inter_mix = c2 + char_mix # On associe les char entre eux puis au valeures du profil
                    inter_mix_up = inter_mix[0:].title()
                    inter_mix_maj = inter_mix.upper()
                    word.write(f"{inter_mix}\n")
                    word.write(f"{inter_mix_up}\n")
                    word.write(f"{inter_mix_maj}\n")
        "char difficile"
        for a3 in char:
            for b3 in char:
                char_mix = a3 + b3
                for c3 in profil.values():
                    for d1 in profil.values():
                        val_mix = c3+d1
                        mix_ = val_mix + char_mix
                        mix_0 = c3+a3+d1+b3
                        mix_1 = c3+a3+d1
                        mix_up = mix_[0:].title()
                        mix_0up = mix_0[0:].title()
                        mix_1up = mix_1[0:].title()
                        mix_maj = mix_.upper()
                        mix_0maj = mix_0.upper()
                        mix_1maj = mix_1.upper()
                        word.write(f"{mix_}\n")
                        word.write(f"{mix_0}\n")
                        word.write(f"{mix_1}\n")
                        word.write(f"{mix_up}\n")
                        word.write(f"{mix_0up}\n")
                        word.write(f"{mix_1up}\n")
                        word.write(f"{mix_maj}\n")
                        word.write(f"{mix_0maj}\n")
                        word.write(f"{mix_1maj}\n")
        "numb simple"
        for e1 in profil.values():
            for f1 in numb:
                spe_numb = a1+b1
                spe_numb_up = spe_numb[0:].title()
                spe_numb_maj = spe_numb.upper()
                word.write(f"{spe_numb}\n")
                word.write(f"{spe_numb_up}\n")
                word.write(f"{spe_numb_maj}\n")
        "numb intermediaire"
        for e2 in numb:
            for f2 in numb:
                numb_mix = e2 + f2
                for g2 in profil.values():
                    inter_mix1 = g2 + numb_mix
                    inter_mix1_up = inter_mix1[0:].title()
                    inter_mix1_maj = inter_mix1.upper()
                    word.write(f"{inter_mix1}\n")
                    word.write(f"{inter_mix1_up}\n")
                    word.write(f"{inter_mix1_maj}\n")
        "numb difficile"
        for e3 in numb:
            for f3 in numb:
                numb_mix1 = e3 + f3
                for g3 in profil.values():
                    for h1 in profil.values():
                        val_mix1 = g3+h1
                        mix_2 = val_mix1 + numb_mix1
                        mix_3 = g3+e3+h1+f3
                        mix_4 = g3+e3+h1
                        mix_2up = mix_2[0:].title()
                        mix_3up = mix_3[0:].title()
                        mix_4up = mix_4[0:].title()
                        mix_2maj = mix_2.upper()
                        mix_3maj = mix_3.upper()
                        mix_4maj = mix_4.upper()
                        word.write(f"{mix_2}\n")
                        word.write(f"{mix_3}\n")
                        word.write(f"{mix_4}\n")
                        word.write(f"{mix_2up}\n")
                        word.write(f"{mix_3up}\n")
                        word.write(f"{mix_4up}\n")
                        word.write(f"{mix_2maj}\n")
                        word.write(f"{mix_3maj}\n")
                        word.write(f"{mix_4maj}\n")



    return '\n\t>Toutes les informations ont été envoyé dans le fichier choisi, Bonne Chance...'



print(intro())
