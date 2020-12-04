import os
import random
import time


# нарисованная сетка для игры
def table(list_table):
	os.system("cls")    # очистка терменала для windows

	print("---Играем в крестики нолики---\n\n")
	print(f"\t {list_table[0]} | {list_table[1]} | {list_table[2]}\n"
		  f"\t{11*'-'}\n"
		  f"\t {list_table[3]} | {list_table[4]} | {list_table[5]}\n"
		  f"\t{11*'-'}\n"
		  f"\t {list_table[6]} | {list_table[7]} | {list_table[8]}\n"
		  f"\n")


# для повторного входа в игру
def more():
	while True:
		more_game = input("Хотите еще сыграть? (y/n): ")

		if more_game.lower() == "y":
			game()

		elif more_game.lower() == "n":
			print("Всего хороршего!")
			exit()

		else:
			print("Непонятный ввод")


# алгоритм игры
def alg(list_game, list_table, player, symbol_player):
	# удаление введенного числа из списка "list_game"
	list_game.remove(player)
	# определение индекса введенного числа в списке "list_table"
	ind = list_table.index(player)
	# замена введенного числа по его индексу в списке "list_table"
	list_table[ind] = (symbol_player)

	if len(list_game) == 0:
		table(list_table)
		print ("Пау - пау - пау... Ничья!")
		return more()

	# проверка комбинации победы по диагонали
	if symbol_player in str(list_table[0]) and symbol_player in str(list_table[4]) and symbol_player in str(list_table[8])\
	or symbol_player in str(list_table[2]) and symbol_player in str(list_table[4]) and symbol_player in str(list_table[6]):
		table(list_table)
		print(f"Игра окончена, победил {symbol_player}")
		return more()

	else:
		# проверка комбинации победы по горизонтали
		for i in range(0, 7, 3):
			if symbol_player in str(list_table[i]) and symbol_player in str(list_table[i + 1])\
			and symbol_player in str(list_table[i + 2]):
				table(list_table)
				print(f"Игра окончена, победил {symbol_player}")
				return more()

		# проветка комбинации победы по вертикали
		for i in range(3):    # проветка комбинации победы по вертикали
			if symbol_player in str(list_table[i]) and symbol_player in str(list_table[i + 3])\
				and symbol_player in str(list_table[i + 6]):
				table(list_table)
				print(f"Игра окончена, победил {symbol_player}")
				return more()


# ход пользователем с проверкой правитьного ввода
def move_player(list_game, symbol_player):
	while True:
		move = input(f"Выберете куда ставим {symbol_player}: ")
		if not move.isdigit():
			print("Не верный ввод..")
			continue
		if int(move) not in list_game or int(move) < 1 and int(move) > 9:
			print("Сюда ставить нельзя..")
			continue
		return int(move)


# присвоение х и у для каждого игрока
def appropriation_x_y():
	while True:
		symbol = input("Выбирите себе Х или О: ")

		if symbol.lower() == "x":
			symbol_player_1 = "X"
			symbol_player_2 = "O"

		elif symbol.lower() == "o":
			symbol_player_1 = "O"
			symbol_player_2 = "X"

		else:
			print("Не верный ввод...")
			continue
		return symbol_player_1, symbol_player_2


# игра
def game():
	# список для выбора постановки знака ii, а так же для определения ничьей
	list_game = [i for i in range(1, 10)]
	# список для сетки (стола) игры
	list_table = list_game.copy()

	print("Начинае играть в Крестики-Нолики\n")

	# присвоение <х> и <у> игрокам
	symbol_player_1, symbol_player_2 = appropriation_x_y()

	# ход игры
	while True:
		table(list_table)
		# ход игрока
		player_1 = move_player(list_game, symbol_player_1)
		alg(list_game, list_table, player_1, symbol_player_1)
		table(list_table)
		time.sleep(random.randint(1, 3))
		# ход ии
		move_ii = random.choice(list_game)
		alg(list_game, list_table, move_ii, symbol_player_2)


game()
