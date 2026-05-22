import random
def fortune(modo: int, mensagem = "") -> str:
    match(modo):
        case 1:
            with open("Saved.txt", "r") as file:
                if (mensagem + '\n') in file.readlines():
                    return f'\"{mensagem}\" já existe na lista de recados!'
            with open("Saved.txt", "a") as file:
                file.write(mensagem + "\n")
            return f'\"{mensagem}\" adicionada à lista de mensagens'
        case 2:
            with open("Saved.txt", "r") as file:
                notes = file.readlines()
            return f'Sua fortuna:\n{notes[random.randint(0, len(notes) - 1)]}'
        case _:
            return "Erro de instrução."
        
if __name__ == "__main__":            
    while(True):
        modo = int(input("O que deseja?\n1 - Deixar mensagem\n2 - Abrir biscoito da sorte\n3 - Sair\n>>"))
        match(modo):
            case 1:
                print(fortune(modo, input("Digite sua mensagem\n>>")))
            case 2:
                print(fortune(2))
                break
            case 3:
                break
            case _:
                print("Comando não encontrado!\n")
