from Class_interface import Interface


if __name__ == "__main__":

    with open('Tokens/token_vk.txt') as token_file:
        token_vk = token_file.read()

    with open('Tokens/token_ya_disk.txt') as token_file:
        token_ya = token_file.read()

    interface = Interface(token_vk=token_vk, token_ya=token_ya)
    interface.greetings()
    interface.help()
    command = input('Введите команду: ')
    if command == "Ya":
        interface.Ya_command()
    elif command == "G":
        interface.G_command()
    elif command == "H":
        interface.H_command()
    elif command == "L":
        interface.L_command()
    else:
        print('Неизвестная команда')

# 273339906

# 14191653
