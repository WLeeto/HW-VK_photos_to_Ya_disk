from Class_Interface import Interface
from Class_Config import Config


if __name__ == "__main__":
    config = Config()
    config.createConfig()
    token_vk = config.get_token('VK')
    token_ya = config.get_token('yandex')

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

# 231515574
# 14191653
