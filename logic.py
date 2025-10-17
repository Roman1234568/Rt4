from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.hp = randint(75, 125)
        self.power = randint(10, 25)
        self.img = self.get_img()
        self.name = self.get_name()
        self.level = 1
        self.feed_count = 0

        Pokemon.pokemons[pokemon_trainer] = self

    def feed(self):
        self.feed_count += 1
        if self.feed_count >= 10:
            self.level += 1
            self.feed_count = 0
            return f"Поздравляю! {self.name} достиг уровня {self.level}!"
        return f"{self.name} покормлен. Еда: {self.feed_count}/10 до след. уровня"
    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Pikachu"
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    
    def get_wiki_url(self):
        pokemon_name = self.name.capitalize()
        wiki_url = f"https://pokemon.fandom.com/wiki/{pokemon_name}"
        return wiki_url


    
    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}\nУровень: {self.level} hp: {self.hp} power: {self.power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    def show_wiki(self):
        return self.get_wiki_url()
    
    def attack(self, enemy):
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

