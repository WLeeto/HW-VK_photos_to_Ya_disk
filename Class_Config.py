import configparser
import os


class Config:
    '''
    Класс создает ini фаил из представленных токенов вк и читает его
    '''
    def __init__(self, path='Tokens/settings.ini'):
        with open('Tokens/token_vk.txt') as token_file:
            vk_token = token_file.read()
        self.vk_token = vk_token

        with open('Tokens/token_ya_disk.txt') as token_file:
            ya_token = token_file.read()
        self.ya_token = ya_token

        self.path = path

    def createConfig(self):
        """
        Create a config file
        """
        config = configparser.ConfigParser()
        config.add_section("Tokens")
        config.set("Tokens", "VK", "Yandex")
        config.set("Tokens", "VK", self.vk_token)
        config.set("Tokens", "Yandex", self.ya_token)

        with open(self.path, "w") as config_file:
            config.write(config_file)

    def get_token(self, type):
        """
        Read config
        """
        if not os.path.exists(self.path):
            self.createConfig()

        config = configparser.ConfigParser()
        config.read(self.path)

        return config.get("Tokens", type)


if __name__ == "__main__":
    config = Config()
    config.createConfig()
    print(config.get_token('yandex'))
