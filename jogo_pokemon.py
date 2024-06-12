import random
import time

rodada = 0
turno = 0
pokebolas = 20
pokedex = []
insignas = []

#batalha [nome],[vida],[dano],[vida inicial]
psyduck =["psyduck" ,60, 22, 60]
froakie = ["froakie", 60, 17, 60]
greninja = ["greninja", 75, 32, 75]
Feraligatr= ["Feraligatr", 132, 29, 132]
Swampert = ["Swampert", 120, 32, 120]
kyogre= ["kyogre" ,400, 50, 400]
Magby = ["Magby", 64, 20, 64]
Chimchar = ["Chimchar", 62, 17, 62]
Magmar = ["Magmar", 67, 25, 67]
Blaziken = ["Blaziken", 140, 37, 140]
Magmortar = ["Magmortar", 160, 38, 160]
moltres = ["moltres", 400, 57, 400]
Articuno = ["Articuno", 520, 40, 520]
Zapdos = ["Zapdos", 380, 49, 380]
Ho_Oh = ["Ho-Oh", 400, 50, 400 ]
Regirock = ["Regirock", 700, 20, 700]
Mewtwo = ["Mewtwo", 500, 58, 500]
Pidgey = ["Pidgey",60, 30,60]
Scizor = ["Scizor",130, 30,130]
Caterpie = ["Caterpie",50,20,50]
Weedle = ["Weedle",50,25,50]
Pinsir = ["Pinsir",120,25,120]
Pikachu = ["Pikachu",70,35,70]
Torterra = ["Torterra",180,20,180]
Snorlex = ["Snorlex",150,20,150]
Chimchar = ["Chimchar",60,25,60] 
Rattata = ["Rattata",40,30,40]
Zubat = ["Zubat",50,20,50]
Eevee = ["Eevee",70,20,70]
Haunter = ["Haunter",70,40,70]
Tauros = ["Tauros",120,20,120]
Fuecoco = ["Fuecoco",80,20,80]
Axew = ["Axew",60,20,60]
Slugma = ["Slugma",70,30,70]
Chansey = ["Chansey",110,30,110]
Darumaka = ["Darumaka",80,30,80]
Charizard = ["Charizard",120,30,120]
Blastoise = ["Blastoise",120,30,120]
Venusaur = ["Venusaur",120,30,120]

pokemons_mato = [Pidgey,Scizor,Caterpie,Weedle,Pinsir,Pikachu,Torterra,Snorlex,Chimchar,Blastoise,Venusaur]
pokemons_caverna = [Rattata,Zubat,Eevee,Haunter,Tauros,Fuecoco,Axew,Slugma,Chansey,Darumaka,Charizard]
pokemon_incial = [Charizard,Blastoise,Venusaur]
pokemon_agua= [psyduck,froakie, greninja, Feraligatr, Swampert, kyogre ]
pokemon_fogo = [Magby, Chimchar, Magmar, Blaziken, Magmortar, moltres ]
pokemon_lendario = [Articuno,Zapdos, Ho_Oh,  Regirock , Mewtwo ]

def batalha(pokemon1, pokemon2):
    print(f"\nBatalha entre {pokemon1[0]} e {pokemon2[0]} começa!\n")
    
    turno = 0
    while esta_vivo(pokemon1) and esta_vivo(pokemon2):
        turno += 1
        print(f"Turno {turno}:")
        time.sleep(2.5)

        dano = atacar(pokemon1, pokemon2)
        print(f"{pokemon1[0]} ataca {pokemon2[0]} causando {dano} de dano. Vida de {pokemon2[0]}: {pokemon2[1]}")
        
        if not esta_vivo(pokemon2):
            print(f"{pokemon2[0]} foi derrotado! {pokemon1[0]} vence a batalha!")
            break

        dano = atacar(pokemon2, pokemon1)
        print(f"{pokemon2[0]} ataca {pokemon1[0]} causando {dano} de dano. Vida de {pokemon1[0]}: {pokemon1[1]}")

        if not esta_vivo(pokemon1):
            print(f"{pokemon1[0]} foi derrotado! {pokemon2[0]} vence a batalha!")
            break

def atacar(atacante, defensor):
    dano = random.randint(0, atacante[2])
    defensor[1] -= dano
    return dano

def esta_vivo(pokemon):
    return pokemon[1] > 0

def restaurar_vida(pokemon):
    pokemon[1] = pokemon[3]

def sorteio_pokemon(lista_pokemon): 
    return random.choice(lista_pokemon)

def introducao(): 
    print("Olá, sou o professor Carvalho, um pesquisador Pokémon.")
    nome_jogador = input("Antes de começarmos nossa jornada, qual é o seu nome: ")
    print(f"Ótimo, então você é {nome_jogador}!! Prepare-se para embarcar em uma aventura emocionante no mundo dos Pokémon!\n")
    print("0-Charizard\n1-Blastoise\n2-Venusaur\n")

def menu_principal():
    print("\n\nO que você deseja fazer?\n1. Entrar na caverna\n2. Entrar no mato\n3. Ginásio Pokemon\n4. Listar pokémon da pokédex\n5. Ver insignas\n6. Sair")

introducao()
escolha_incial = int(input("Digite o número do seu pokémon inicial para começar sua jornada pokémon: "))
pokedex.append(pokemon_incial[escolha_incial])
print(f"Parabéns, vc escolheu o {pokemon_incial[escolha_incial][0]} como seu primeiro pokémon!!\n")

opcao = 0

while opcao != 6:
    
    porcentagem_de_captura_mato = 0.5
    porcentagem_de_captura_caverna = 0.35
    chance_caverna = random.random()
    chance_mato = random.random()
    porcentagem_de_captura_ginasio = 0.5
    chance_ginasio = random.random()


    menu_principal()

    opcao = int(input("Escolha uma opção: "))
    if insignas == "insigna lendaria":
        print("Parabéns, você acaba de se tornar o maior treinador pokemon do mundo!!!\n")
        print("Nos despedimos aqui mestre, não é um adeus, é um até logo!!")
        break
    elif opcao > 6 or opcao < 0:
        print("\n\nErro, selecione entre 1 e 5\n\n")
        continue
    elif pokebolas <= 0:
        print("Suas pokebolas acabaram, reinicie o jogo para jogar novamente!!!")
        break  
    elif opcao == 6:
        print("Estarei te esperando para continuar sua jornada Pokémon!!")
        break
    
    elif opcao == 1:
        chance_pokebolas = random.randint(0,2)
        pokebolas += chance_pokebolas
        pokemon_sorteado_caverna = sorteio_pokemon(pokemons_caverna)
        print("-"*30)
        print(f"Você encontrou {chance_pokebolas} pokebolas")
        print(f"Pokebolas: {pokebolas}")
        print(f"Você entrou na caverna e encontrou um {pokemon_sorteado_caverna[0]}!\n")
        ja_tem_pokemon = False
        for pokemon in pokedex:
            if pokemon[0] == pokemon_sorteado_caverna[0]:
                ja_tem_pokemon = True
                break
        
        if ja_tem_pokemon:
            print("Você já tem esse Pokémon, não poderá capturar!")
            continue

        batalha_caverna = input("Deseja batalhar contra esse pokemon e caso vença, poderá tentar capturar ele?(s/n): ")
        
        if batalha_caverna == "n" or batalha_caverna == "não" or batalha_caverna == "nao":
            continue
        elif batalha_caverna == "s" or batalha_caverna == "sim":
            print("[nome/vida/dano/vida/inicial]")
            print(f"Pokedex: {pokedex}")
            
            escolha_pokemon = int(input("Qual pokemon vc quer da sua pokedex para batalhar(digite o número da posição dele na pokedex): "))
            pokemon_escolhido = pokedex[escolha_pokemon - 1]

            batalha(pokemon_escolhido,pokemon_sorteado_caverna)

        if pokemon_escolhido[1] <= 0:
            print("Seu pokemon foi derrotado, lute melhor na próxima vez!!")
            restaurar_vida(pokemon_sorteado_caverna)
            restaurar_vida(pokemon_escolhido)
            turno = 0
            continue
        elif pokemon_sorteado_caverna[1] <= 0:
            print("Parabéns, você derrotou o pokemon!!\n")
            restaurar_vida(pokemon_sorteado_caverna)
            restaurar_vida(pokemon_escolhido)
            turno = 0
        
            opcao_caverna = input("Agora que venceu o pokemon, deseja tentar captura-lo? irá gastar uma pokebola(s/n): ")
        
            if opcao_caverna == "n" or opcao_caverna == "não" or opcao_caverna == "nao":
                continue
            elif opcao_caverna == "s" or opcao_caverna == "sim":
                if chance_caverna <= porcentagem_de_captura_caverna:
                    print(f"Você capturou o pokemon")
                    pokedex.append(pokemon_sorteado_caverna)
                    pokebolas -= 1
                else:
                    pokebolas -= 1
                    if pokebolas <= 0:
                        print("Suas pokebolas acabaram!!")
                        break
                    tentativa = input(f"Você não capturou, mas tem mais {pokebolas} pokebolas, deseja tentar e gastar suas pokebolas?(s/n): ")
                    if tentativa == "n" or tentativa == "não" or tentativa == "nao":
                        continue
                    elif tentativa == "s" or tentativa == "sim":
                        for c in range(pokebolas):            
                            porcentagem_de_captura_caverna = 0.35
                            chance_caverna = random.random()
                        
                            if chance_caverna <= porcentagem_de_captura_caverna:
                                print(f"Você capturou o pokémon") 
                                pokedex.append(pokemon_sorteado_caverna)
                                pokebolas -= 1
                                break 
                            else:
                                print("Você nao capturou") 
                                pokebolas -= 1
                                if  pokebolas <= 0:
                                    print("Suas pokebolas acabaram!!")
                                    break
                                tentativa2 = input(f"Você tem mais {pokebolas} pokebolas, deseja tentar novamente e gastar suas pokebolas?(s/n): ") 
                                if tentativa2 == "n" or tentativa2 == "não" or tentativa2 == "nao":
                                    break                                         
                                elif  pokebolas <= 0:
                                    print("Suas pokebolas acabaram!!")
                                    break
                                elif tentativa2 == "s" or tentativa2 == "sim": 
                                    continue                                        
    if opcao == 2:
        chance_pokebolas = random.randint(0,2)
        pokebolas += chance_pokebolas
        pokemon_sorteado_mato = sorteio_pokemon(pokemons_mato)
        print("-"*30)
        print(f"Você encontrou {chance_pokebolas} pokebolas")
        print(f"Pokebolas: {pokebolas}")
        print(f"Você entrou no mato e encontrou um {pokemon_sorteado_mato[0]}\n")
        ja_tem_pokemons = False
        for pokemons in pokedex:
            if pokemons[0] == pokemon_sorteado_mato[0]:
                ja_tem_pokemons = True
                break
        
        if ja_tem_pokemons:
            print("Você já tem esse Pokémon, não poderá capturar!")
            continue

        batalha_mato = input("Deseja batalhar contra esse pokemon e caso vença, poderá tentar capturar ele?(s/n): ")
        
        if batalha_mato == "n" or batalha_mato == "não" or batalha_mato == "nao":
            continue
        elif batalha_mato == "s" or batalha_mato == "sim":
            print("[nome/vida/dano/vida/inicial]")
            print(f"Pokedex: {pokedex}")
            
            escolha_pokemon2 = int(input("Qual pokemon vc quer da sua pokedex para batalhar(digite o número da posição dele na pokedex): "))
            pokemon_escolhido2 = pokedex[escolha_pokemon2 - 1]

            batalha(pokemon_escolhido2,pokemon_sorteado_mato)

        if pokemon_escolhido2[1] <= 0:
            print("Seu pokemon foi derrotado, lute melhor na próxima vez!!")
            restaurar_vida(pokemon_sorteado_mato)
            restaurar_vida(pokemon_escolhido2)
            turno = 0
            continue
        elif pokemon_sorteado_mato[1] <= 0:
            print("Parabéns, você derrotou o pokemon!!\n")
            restaurar_vida(pokemon_sorteado_mato)
            restaurar_vida(pokemon_escolhido2)
            turno = 0
            opcao_mato = input("Agora que venceu o pokemon, deseja tentar captura-lo? irá gastar uma pokebola(s/n): ")
        
            if opcao_mato == "n" or opcao_mato == "não" or opcao_mato == "nao":
                continue
    
            elif opcao_mato == "s" or opcao_mato == "sim":
                if chance_mato <= porcentagem_de_captura_mato:
                    print(f"Você capturou o pokemon")
                    pokedex.append(pokemon_sorteado_mato)
                    pokebolas -= 1
                else:
                    pokebolas -= 1
                    if pokebolas <= 0:
                        print("Suas pokebolas acabaram!!")
                        break
                    tentativa = input(f"Você não capturou, mas tem mais {pokebolas} pokebolas, deseja tentar e gastar suas pokebolas?(s/n): ")
                    if tentativa == "n" or tentativa == "não" or tentativa == "nao":
                        continue
                    elif tentativa == "s" or tentativa == "sim":
                        for c in range(pokebolas):            
                            porcentagem_de_captura_mato = 0.5
                            chance_mato = random.random()
                        
                            if chance_mato <= porcentagem_de_captura_mato:
                                print(f"Você capturou o pokémon") 
                                pokedex.append(pokemon_sorteado_mato)
                                pokebolas -= 1
                                break 
                            else:
                                print("Você nao capturou")
                                if  pokebolas <= 0:
                                    print("Suas pokebolas acabaram!!")
                                    break
                                pokebolas -= 1
                                tentativa3 = input(f"Você tem mais {pokebolas} pokebolas, deseja tentar novamente e gastar suas pokebolas?(s/n): ")
                                if tentativa3 == "n" or tentativa3 == "não" or tentativa3 == "nao":
                                    break
                                elif pokebolas <= 0:
                                    print("Suas pokebolas acabaram!!")
                                    break
                                elif tentativa3 == "s" or tentativa3 == "sim":
                                    continue
    elif opcao == 3:
        print(f"Bem-vindo ao ginásio Pokémon, liga competitiva dos melhores treinadores de todo o mundo!!!\n")
        print(f"Escolha um dos 3 ginásios para batalhar, caso vença, irá ganhar a insigna do elemento do ginásio e poderá tentar capturar o pokémon boss:\n1. Ginásio de Fogo\n2. Ginásio de Água\n3. Ginásio lendário")
        print("\nContendo as duas insignas, poderá batalhar no ginásio lendário!!!!")
        ginasio = int(input("Escolha o número do ginásio que deseja ir: "))

        if ginasio > 3 or ginasio <= 0:
            print("\n\nErro, selecione entre 1 e 3\n\n")
            continue
        elif ginasio == 1:
            print("\nVocê entrou no ginásio de fogo, terá que enfrentar 5 pokémons e 1 pokémon lendário!! ")
            print(f"Os pokémons de cada rodada são: ")
            for n in range(6):
                print(f"Rodada{n+1}: {pokemon_fogo[n]}")
            batalha_ginasio = input("Deseja batalhar contra esses pokemons?(s/n): ")
            if batalha_ginasio == "n" or batalha_ginasio == "não" or batalha_ginasio == "nao":
                continue
            elif batalha_ginasio == "s" or batalha_ginasio == "sim":
                print("[nome/vida/dano/vida/inicial]")
                print(f"Pokedex: {pokedex}")
            
                escolha_pokemon_ginasio = int(input("\nQual pokemon vc quer da sua pokedex para batalhar(digite o número da posição dele na pokedex): "))
                pokemon_escolhido_ginasio = pokedex[escolha_pokemon_ginasio - 1]
                
                m = 0
                while m < 7:
                    print(f"\nRodada {m+1}:\n")
                    batalha(pokemon_escolhido_ginasio,pokemon_fogo[m])
                    if pokemon_escolhido_ginasio[1] <= 0:
                        tentativa_ginasio = input("Seu pokemon foi derrotado, deseja escolher outro pokemon da sua pokedex para batalhar?(s/n) ")
                        if tentativa_ginasio == "n" or tentativa_ginasio == "não" or tentativa_ginasio == "nao":
                            m=0
                            turno = 0
                            for pokemon_p in pokedex:
                                restaurar_vida(pokemon_p)
                            for pokemon_f in pokemon_fogo:
                                restaurar_vida(pokemon_f)
                            break
                        elif tentativa_ginasio == "s" or tentativa_ginasio == "sim":
                            print("[nome/vida/dano/vida/inicial]")
                            print(f"Pokedex: {pokedex}")
            
                            escolha_pokemon_ginasio = int(input("Qual pokemon vc quer da sua pokedex para continuar a batalha, verifique se ele tem vida(digite o número da posição dele na pokedex): "))
                            pokemon_escolhido_ginasio = pokedex[escolha_pokemon_ginasio - 1]
                            if pokemon_escolhido_ginasio[1] > 0:
                                turno = 0
                                continue
                            else:
                                print("Pokémon sem vida.")
                                for pokemon_po in pokedex:
                                    restaurar_vida(pokemon_po)
                                for pokemon_fo in pokemon_fogo:
                                    restaurar_vida(pokemon_fo)
                                    m=0
                                turno = 0
                                break
                    elif pokemon_fogo[m][1] <= 0:
                        print("Parabéns, você derrotou o pokemon, irá para a próxima rodada!!")
                        m += 1
                        turno = 0
                        time.sleep(2)
                        if pokemon_fogo[5][1] <= 0:
                            print(f"Parabéns, você venceu o ginásio e ganhou a insigna de fogo!!\n")
                            insignas.append("insigna de fogo")
                            m = 0
                            for pokemon_pok in pokedex:
                                restaurar_vida(pokemon_pok)
                            restaurar_vida(pokemon_fogo[5])
                            opcao_ginasio = input(f"Agora que venceu o ginásio, deseja tentar captura o {pokemon_fogo[5][0]} ? irá gastar uma pokebola(s/n): ")       
                            if opcao_ginasio == "n" or opcao_ginasio == "não" or opcao_ginasio == "nao":
                                break
                            elif opcao_ginasio == "s" or opcao_ginasio == "sim":
                                turno = 0
                                if chance_ginasio <= porcentagem_de_captura_ginasio:
                                    print(f"Você capturou o pokemon")
                                    pokedex.append(pokemon_fogo[5])
                                    pokebolas -= 1
                                    break
                                else:
                                    pokebolas -= 1
                                    if pokebolas <= 0:
                                        print("Suas pokebolas acabaram!!")
                                        break
                                    tentativa_ginasio = input(f"Você não capturou, mas tem mais {pokebolas} pokebolas, deseja tentar e gastar suas pokebolas?(s/n): ")
                                    if tentativa_ginasio == "n" or tentativa_ginasio == "não" or tentativa_ginasio == "nao":
                                        break
                                    elif tentativa_ginasio == "s" or tentativa_ginasio == "sim":
                                        for c in range(pokebolas):            
                                            porcentagem_de_captura_ginasio = 0.5
                                            chance_ginasio = random.random()
                        
                                            if chance_ginasio <= porcentagem_de_captura_ginasio:
                                                print(f"Você capturou o pokémon") 
                                                pokedex.append(pokemon_fogo[5])
                                                pokebolas -= 1
                                                break 
                                            else:
                                                print("Você nao capturou")
                                                if  pokebolas <= 0:
                                                    print("Suas pokebolas acabaram!!")
                                                    break
                                                pokebolas -= 1
                                                tentativa3_ginasio = input(f"Você tem mais {pokebolas} pokebolas, deseja tentar novamente e gastar suas pokebolas?(s/n): ")
                                                if tentativa3_ginasio == "n" or tentativa3_ginasio == "não" or tentativa3_ginasio == "nao":
                                                    break
                                                elif pokebolas <= 0:
                                                    print("Suas pokebolas acabaram!!")
                                                    break
                                                elif tentativa3_ginasio == "s" or tentativa3_ginasio == "sim":
                                                    continue
        elif ginasio == 2:
            print("\nVocê entrou no ginásio de água, terá que enfrentar 5 pokémons e 1 pokémon lendário!! ")
            print(f"Os pokémons de cada rodada são: ")
            for a in range(6):
                print(f"Rodada{a+1}: {pokemon_agua[a]}")
            batalha_ginasio2 = input("Deseja batalhar contra esses pokemons?(s/n): ")
            if batalha_ginasio2 == "n" or batalha_ginasio2 == "não" or batalha_ginasio2 == "nao":
                continue
            elif batalha_ginasio2 == "s" or batalha_ginasio2 == "sim":
                print("[nome/vida/dano/vida/inicial]")
                print(f"Pokedex: {pokedex}")
            
                escolha_pokemon_ginasio2 = int(input("\nQual pokemon vc quer da sua pokedex para batalhar(digite o número da posição dele na pokedex): "))
                pokemon_escolhido_ginasio2 = pokedex[escolha_pokemon_ginasio2 - 1]
                
                m = 0
                while m < 7:
                    print(f"\nRodada {m+1}:\n")
                    batalha(pokemon_escolhido_ginasio2,pokemon_agua[m])
                    if pokemon_escolhido_ginasio2[1] <= 0:
                        tentativa_ginasio2 = input("Seu pokemon foi derrotado, deseja escolher outro pokemon da sua pokedex para batalhar?(s/n) ")
                        if tentativa_ginasio2 == "n" or tentativa_ginasio2 == "não" or tentativa_ginasio2 == "nao":
                            m=0
                            turno = 0
                            for pokemon_poked in pokedex:
                                restaurar_vida(pokemon_poked)
                            for pokemon_ag in pokemon_agua:
                                restaurar_vida(pokemon_ag)
                            break
                        elif tentativa_ginasio2 == "s" or tentativa_ginasio2 == "sim":
                            print("[nome/vida/dano/vida/inicial]")
                            print(f"Pokedex: {pokedex}")
            
                            escolha_pokemon_ginasio2 = int(input("Qual pokemon vc quer da sua pokedex para continuar a batalha, verifique se ele tem vida(digite o número da posição dele na pokedex): "))
                            pokemon_escolhido_ginasio2 = pokedex[escolha_pokemon_ginasio2 - 1]
                            if pokemon_escolhido_ginasio2[1] > 0:
                                turno = 0
                                continue
                            else:
                                print("Pokémon sem vida.")
                                for pokemon_poke in pokedex:
                                    restaurar_vida(pokemon_poke)
                                for pokemon_a in pokemon_agua:
                                    restaurar_vida(pokemon_a)
                                    m=0
                                turno = 0
                                break
                    elif pokemon_agua[m][1] <= 0:
                        print("Parabéns, você derrotou o pokemon, irá para a próxima rodada!!")
                        m += 1
                        turno = 0
                        time.sleep(2)
                        if pokemon_agua[5][1] <= 0:
                            print(f"Parabéns, você venceu o ginásio e ganhou a insigna de água!!\n")
                            insignas.append("insigna de agua")
                            m = 0
                            for pokemon_poked in pokedex:
                                restaurar_vida(pokemon_poked)
                            restaurar_vida(pokemon_agua[5])
                            opcao_ginasio2 = input(f"Agora que venceu o ginásio, deseja tentar captura o {pokemon_agua[5][0]} ? irá gastar uma pokebola(s/n): ")       
                            if opcao_ginasio2 == "n" or opcao_ginasio2 == "não" or opcao_ginasio2 == "nao":
                                break
                            elif opcao_ginasio2 == "s" or opcao_ginasio2 == "sim":
                                turno = 0
                                if chance_ginasio <= porcentagem_de_captura_ginasio:
                                    print(f"Você capturou o pokemon")
                                    pokedex.append(pokemon_agua[5])
                                    pokebolas -= 1
                                else:
                                    pokebolas -= 1
                                    if pokebolas <= 0:
                                        print("Suas pokebolas acabaram!!")
                                        break
                                    tentativa_ginasio2 = input(f"Você não capturou, mas tem mais {pokebolas} pokebolas, deseja tentar e gastar suas pokebolas?(s/n): ")
                                    if tentativa_ginasio2 == "n" or tentativa_ginasio2 == "não" or tentativa_ginasio2 == "nao":
                                        break
                                    elif tentativa_ginasio2 == "s" or tentativa_ginasio2 == "sim":
                                        for c in range(pokebolas):            
                                            porcentagem_de_captura_ginasio = 0.5
                                            chance_ginasio = random.random()
                            
                                            if chance_ginasio <= porcentagem_de_captura_ginasio:
                                                print(f"Você capturou o pokémon") 
                                                pokedex.append(pokemon_agua[5])
                                                pokebolas -= 1
                                                break 
                                            else:
                                                print("Você nao capturou")
                                                if  pokebolas <= 0:
                                                    print("Suas pokebolas acabaram!!")
                                                    break
                                                pokebolas -= 1
                                                tentativa3_ginasio2 = input(f"Você tem mais {pokebolas} pokebolas, deseja tentar novamente e gastar suas pokebolas?(s/n): ")
                                                if tentativa3_ginasio2 == "n" or tentativa3_ginasio2 == "não" or tentativa3_ginasio2 == "nao":
                                                    break
                                                elif pokebolas <= 0:
                                                    print("Suas pokebolas acabaram!!")
                                                    break
                                                elif tentativa3_ginasio2 == "s" or tentativa3_ginasio2 == "sim":
                                                    continue
        elif ginasio == 3:
            if 'Insignia de fogo' not in insignas or 'Insignia de agua' not in insignas:
                print("Você precisa das insígnias de fogo e de água para entrar no ginásio lendário.")
                continue
            
            print("\nVocê entrou no ginásio lendário, terá que enfrentar 5 pokémons lendário para conseguir a maior insigna do mundo, a INSIGNA LENDÁRIA!!! ")
            print(f"Os pokémons de cada rodada são: ")

            for a in range(5):
                print(f"Rodada{a+1}: {pokemon_lendario[a]}")
            batalha_ginasio3 = input("Deseja batalhar contra esses pokemons?(s/n): ")
            if batalha_ginasio3 == "n" or batalha_ginasio3 == "não" or batalha_ginasio3 == "nao":
                continue
            elif batalha_ginasio3 == "s" or batalha_ginasio3 == "sim":
                print("[nome/vida/dano/vida/inicial]")
                print(f"Pokedex: {pokedex}")
            
                escolha_pokemon_ginasio3 = int(input("\nQual pokemon vc quer da sua pokedex para batalhar(digite o número da posição dele na pokedex): "))
                pokemon_escolhido_ginasio3 = pokedex[escolha_pokemon_ginasio3 - 1]
                
                m = 0
                while m < 6:
                    print(f"\nRodada {m+1}:\n")
                    batalha(pokemon_escolhido_ginasio3,pokemon_lendario[m])
                    if pokemon_escolhido_ginasio3[1] <= 0:
                        tentativa_ginasio3 = input("Seu pokemon foi derrotado, deseja escolher outro pokemon da sua pokedex para batalhar?(s/n) ")
                        if tentativa_ginasio3 == "n" or tentativa_ginasio3 == "não" or tentativa_ginasio3 == "nao":
                            m=0
                            turno = 0
                            for pokemon_pokedee in pokedex:
                                restaurar_vida(pokemon_pokedee)
                            for pokemon_l in pokemon_lendario:
                                restaurar_vida(pokemon_l)
                            break
                        elif tentativa_ginasio3 == "s" or tentativa_ginasio3 == "sim":
                            print("[nome/vida/dano/vida/inicial]")
                            print(f"Pokedex: {pokedex}")
            
                            escolha_pokemon_ginasio3 = int(input("Qual pokemon vc quer da sua pokedex para continuar a batalha, verifique se ele tem vida(digite o número da posição dele na pokedex): "))
                            pokemon_escolhido_ginasio3 = pokedex[escolha_pokemon_ginasio3 - 1]
                            if pokemon_escolhido_ginasio3[1] > 0:
                                turno = 0
                                continue
                            else:
                                print("Pokémon sem vida.")
                                for pokemon_pokedeee in pokedex:
                                    restaurar_vida(pokemon_pokedeee)
                                for pokemon_le in pokemon_lendario:
                                    restaurar_vida(pokemon_le)
                                    m=0
                                turno = 0
                                break
                    elif pokemon_lendario[m][1] <= 0:
                        print("Parabéns, você derrotou o pokemon, irá para a próxima rodada!!")
                        m += 1
                        turno = 0
                        time.sleep(2)
                        if pokemon_lendario[4][1] <= 0:
                            print(f"Parabéns, você venceu o ginásio e ganhou a insigna lendária!!\n")
                            insignas.append("insigna lendaria")
                            m = 0
                            for pokemon_pokedeeee in pokedex:
                                restaurar_vida(pokemon_pokedeeee)
                            restaurar_vida(pokemon_lendario[5])
                            opcao_ginasio3 = input(f"Agora que venceu o ginásio, deseja tentar captura o {pokemon_lendario[5][0]} ? irá gastar uma pokebola(s/n): ")       
                            if opcao_ginasio3 == "n" or opcao_ginasio3 == "não" or opcao_ginasio3 == "nao":
                                break
                            elif opcao_ginasio3 == "s" or opcao_ginasio3 == "sim":
                                turno = 0
                                if chance_ginasio <= porcentagem_de_captura_ginasio:
                                    print(f"Você capturou o pokemon")
                                    pokedex.append(pokemon_lendario[5])
                                    pokebolas -= 1
                                else:
                                    pokebolas -= 1
                                    if pokebolas <= 0:
                                        print("Suas pokebolas acabaram!!")
                                        break
                                    tentativa_ginasio3 = input(f"Você não capturou, mas tem mais {pokebolas} pokebolas, deseja tentar e gastar suas pokebolas?(s/n): ")
                                    if tentativa_ginasio3 == "n" or tentativa_ginasio3 == "não" or tentativa_ginasio3 == "nao":
                                        break
                                    elif tentativa_ginasio3 == "s" or tentativa_ginasio3 == "sim":
                                        for po in range(pokebolas):            
                                            porcentagem_de_captura_ginasio = 0.5
                                            chance_ginasio = random.random()
                            
                                            if chance_ginasio <= porcentagem_de_captura_ginasio:
                                                print(f"Você capturou o pokémon") 
                                                pokedex.append(pokemon_lendario[5])
                                                pokebolas -= 1
                                                break 
                                            else:
                                                print("Você nao capturou")
                                                if  pokebolas <= 0:
                                                    print("Suas pokebolas acabaram!!")
                                                    break
                                                pokebolas -= 1
                                                tentativa3_ginasio3 = input(f"Você tem mais {pokebolas} pokebolas, deseja tentar novamente e gastar suas pokebolas?(s/n): ")
                                                if tentativa3_ginasio3 == "n" or tentativa3_ginasio3 == "não" or tentativa3_ginasio3 == "nao":
                                                    break
                                                elif pokebolas <= 0:
                                                    print("Suas pokebolas acabaram!!")
                                                    break
                                                elif tentativa3_ginasio3 == "s" or tentativa3_ginasio3 == "sim":
                                                    continue                                
    elif opcao == 4:
        print("[nome/vida/dano/vida inicial]")
        print(f"\nPokémon na sua Pokédex: {pokedex}")
    elif opcao == 5:
        print("\n--- Insígnias ---")
        for insignia in insignas:
            print(insignia)
        print("---------------\n")