import random

pokedex = []
pokemons_mato = ["Pidgey","Scizor","Caterpie","Weedle","Pinsir","Pikachu","Bubasaur","Torterra","Snorlex","Chimchar"]
pokemons_caverna = ["Rattata","Zubat","Eevee","Ditto","Tauros","Fuecoco","Axew","Slugma","Chansey","Darumaka"]

print("Olá, sou o professor Carvalho, um pesquisador Pokémon.")

nome_jogador = input("Antes de começarmos nossa jornada, qual é o seu nome: ")

print(f"Ótimo, então você é {nome_jogador}!! Prepare-se para embarcar em uma aventura emocionante no mundo dos Pokémon!")

opcao = 0

while opcao != 4:
    
    porcentagem_de_captura_mato = 0.5
    porcentagem_de_captura_caverna = 0.35
    chance_caverna = random.random()
    chance_mato = random.random()
    
    caverna_aleatorio = random.choice(pokemons_caverna)
    mato_aleatorio = random.choice(pokemons_mato)

    
    print("\n\nO que você deseja fazer?\n1. Entrar na caverna\n2. Entrar no mato\n3. Listar pokémon da pokédex\n4. Sair")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao > 4 or opcao < 0:
        print("\n\nErro, selecione entre 1 e 4\n\n")
        continue  
    elif opcao == 4:
        print("Estarei te esperando para continuar sua jornada Pokémon!!")
        break
    
    elif opcao == 1:
        print(f"Você entrou na caverna e encontrou um {caverna_aleatorio}!")
        if caverna_aleatorio in pokedex:
            print('você já tem esse pokemon, não poderá capturar!')
            continue
        
        opcao_caverna = int(input("Deseja tentar capturar este pokémon?(sim digite 1, nao digite 2): "))
        
        if opcao_caverna == 2:
            continue
        elif opcao_caverna == 1:
            if chance_caverna <= porcentagem_de_captura_caverna:
                    print(f"Você capturou o pokemon")
                    pokedex.append(caverna_aleatorio)
            else:
                tentativa = int(input(f"Você não capturou, mas tem mais 3 tentativas, deseja tentar? (sim digite 1 e nao digite 2): "))
                
                if tentativa == 2:
                    break
                elif tentativa == 1:
                    for c in range(0,3):            
                        porcentagem_de_captura_caverna = 0.35
                        chance_caverna = random.random()
                        
                        if chance_caverna <= porcentagem_de_captura_caverna:
                            print(f"Você capturou o pokémon") 
                            pokedex.append(caverna_aleatorio)
                            break 
                        else:
                            print("Você nao capturou")                                                 
    if opcao == 2:
        print(f"Você entrou no mato e encontrou um {mato_aleatorio}")
        if caverna_aleatorio in pokedex:
            print('você já tem esse pokemon, não poderá capturar!')
            continue
        opcao_mato = int(input("Deseja tentar capturar este pokémon?(sim digite 1, nao digite 2): "))
        if opcao_mato == 2:
            continue
    
        elif opcao_mato == 1:
            if chance_mato <= porcentagem_de_captura_mato:
                    print(f"Você capturou o pokemon")
                    pokedex.append(mato_aleatorio)
            else:
                tentativa = int(input("Você não capturou, mas tem mais 3 tentativas, deseja tentar?(sim digite 1 e nao digite 2): "))
                if tentativa == 2:
                    break
                elif tentativa == 1:
                    for c in range(0,3):            
                        porcentagem_de_captura_mato = 0.5
                        chance_mato = random.random()
                        
                        if chance_mato <= porcentagem_de_captura_mato:
                            print(f"Você capturou o pokémon") 
                            pokedex.append(mato_aleatorio)
                            break 
                        else:
                            print("Você nao capturou") 
    
    elif opcao == 3:
        print(f"\nPokémon na sua Pokédex: {pokedex}")