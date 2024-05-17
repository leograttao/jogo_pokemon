import random

pokebolas = 3
pokedex = []
pokemons_mato = ["Pidgey","Scizor","Caterpie","Weedle","Pinsir","Pikachu","Bubasaur","Torterra","Snorlex","Chimchar"]
pokemons_caverna = ["Rattata","Zubat","Eevee","Ditto","Tauros","Fuecoco","Axew","Slugma","Chansey","Darumaka"]
pokemon_incial = ["Charmander","Squirtle","Bulbasaur"]

def sorteio_pokemon(lista_pokemon):
    pokemon_aleatorio = random.choice(lista_pokemon)

    return pokemon_aleatorio

def introducao(): 
    print("Olá, sou o professor Carvalho, um pesquisador Pokémon.")
    nome_jogador = input("Antes de começarmos nossa jornada, qual é o seu nome: ")
    print(f"Ótimo, então você é {nome_jogador}!! Prepare-se para embarcar em uma aventura emocionante no mundo dos Pokémon!\n")
    print("0-charmander\n1-squirtle\n2-Bulbasaur\n")

def menu_principal():
    print("\n\nO que você deseja fazer?\n1. Entrar na caverna\n2. Entrar no mato\n3. Listar pokémon da pokédex\n4. Sair")

introducao()
escolha_incial = int(input("Digite o número do seu pokémon inicial para começar sua jornada pokémon: "))
pokedex.append(pokemon_incial[escolha_incial])
print(f"\nParabéns, vc escolheu o {pokemon_incial[escolha_incial]} como seu primeiro pokémon!!\n")


opcao = 0

while opcao != 4:
    
    porcentagem_de_captura_mato = 0.5
    porcentagem_de_captura_caverna = 0.35
    chance_caverna = random.random()
    chance_mato = random.random()


    menu_principal()

    opcao = int(input("Escolha uma opção: "))
    
    if opcao > 4 or opcao < 0:
        print("\n\nErro, selecione entre 1 e 4\n\n")
        continue
    elif pokebolas <= 0:
        print("Suas pokebolas acabaram, reinicie o jogo para jogar novamente!!!")
        break  
    elif opcao == 4:
        print("Estarei te esperando para continuar sua jornada Pokémon!!")
        break
    
    elif opcao == 1:
        chance_pokebolas = random.randint(0,2)
        pokebolas += chance_pokebolas
        print("-"*30)
        print(f"Você encontrou {chance_pokebolas} pokebolas")
        print(f"Pokebolas: {pokebolas}")
        print(f"Você entrou na caverna e encontrou um {sorteio_pokemon(pokemons_caverna)}!\n")
        if sorteio_pokemon(pokemons_caverna) in pokedex:
            print('você já tem esse pokemon, não poderá capturar!')
            continue
        
        opcao_caverna = input("Deseja tentar capturar este pokémon, irá gastar uma pokebola?(s/n): ")
        
        if opcao_caverna == "n" or opcao_caverna == "não" or opcao_caverna == "nao":
            continue
        elif opcao_caverna == "s" or opcao_caverna == "sim":
            if chance_caverna <= porcentagem_de_captura_caverna:
                    print(f"Você capturou o pokemon")
                    pokedex.append(sorteio_pokemon(pokemons_caverna))
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
                            pokedex.append(sorteio_pokemon(pokemons_caverna))
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
                            if  pokebolas <= 0:
                                print("Suas pokebolas acabaram!!")
                                break
                            elif tentativa2 == "s" or tentativa2 == "sim": 
                                pokebolas -= 1 
                                continue                                        
    if opcao == 2:
        chance_pokebolas = random.randint(0,2)
        pokebolas += chance_pokebolas
        print("-"*30)
        print(f"Você encontrou {chance_pokebolas} pokebolas")
        print(f"Pokebolas: {pokebolas}")
        print(f"Você entrou no mato e encontrou um {sorteio_pokemon(pokemons_mato)}\n")
        if sorteio_pokemon(pokemons_mato) in pokedex:
            print('você já tem esse pokemon, não poderá capturar!')
            continue
        opcao_mato = input("Deseja tentar capturar este pokémon, irá gastar uma pokebola?(s/n): ")
        if opcao_mato == "n" or opcao_mato == "não" or opcao_mato == "nao":
            continue
    
        elif opcao_mato == "s" or opcao_mato == "sim":
            if chance_mato <= porcentagem_de_captura_mato:
                    print(f"Você capturou o pokemon")
                    pokedex.append(sorteio_pokemon(pokemons_mato))
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
                            pokedex.append(sorteio_pokemon(pokemons_mato))
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
                                pokebolas -= 1
                                continue
    
    elif opcao == 3:
        print(f"\nPokémon na sua Pokédex: {pokedex}")