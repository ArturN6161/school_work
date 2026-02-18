# class Planet:
#     def __init__(self, name, mass, orbit_radius):
#         self.name = name
#         self.mass = mass
#         self.orbit_radius = orbit_radius
#         self.satellites = []
#
#     def add_moon(self, satellite):
#         self.satellites.append(satellite)
#
#     def display_info(self):
#         print(f'Планета {self.name}, с массой {self.mass}. '
#               f'Имеет орбиту {self.orbit_radius} и спутники:')
#         print(self.satellites)
#
#     def __repr__(self):
#         return f'{self.name}'
#
#
# class Moon:
#     def __init__(self, name, mass, radius, planet):
#         self.name = name
#         self.mass = mass
#         self.radius = radius
#         self.planet = planet
#
#     def __repr__(self):
#         return (f'Спутник {self.name} с массой {self.mass} и радиусом '
#                 f'{self.radius}. Вращается вокруг планеты {self.planet}')
#
#
# earth = Planet(name="Земля", mass=5.972e24, orbit_radius=149.6e6)
# moon = Moon(name="Луна", mass=7.35e22, radius=1737.1, planet=earth)
# earth.add_moon(moon)
# earth.display_info()


# class Player:
#     def __init__(self, name, points):
#         self.name = name
#         self.__points = points
#
#     def __repr__(self):
#         return f'У игрока {self.name}, {self.info_points} очков'
#
#     @property
#     def info_points(self):
#         return self.__points
#
#     @info_points.setter
#     def info_points(self, points):
#         self.__points += points
#
#
# class Tournament:
#     def __init__(self):
#         self.players = []
#
#
#     def add_player(self, player):
#         self.players.append(player)
#
#     def show_leaderboard(self):
#         list_leaders = list(self.players)
#         list_leaders.sort(key=lambda x: x.info_points, reverse=True)
#         print("--- Таблица лидеров ---")
#         for i in list_leaders:
#             print(i)
#
# player1 = Player(name="Alice", points=10)
# player2 = Player(name="Bob", points=20)
# tournament = Tournament()
# tournament.add_player(player1)
# tournament.add_player(player2)
# tournament.show_leaderboard()
# print(player1.info_points)
# player1.info_points = 30
# print(player1.info_points)
# tournament.show_leaderboard()