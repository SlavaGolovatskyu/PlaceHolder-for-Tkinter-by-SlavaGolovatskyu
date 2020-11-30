from tkinter import *

"""
При создания класса тоисть
PlaceHold = PlaceHolder(arg1, arg2, arg3) нужно передать все строки тоисть 3 строки и больше.
"""

class PlaceHolder:
	def __init__(self, arg1, arg2, arg3 = None, arg4 = None):
		super().__init__()

		self.MainDict = {
			1: arg1,  # Строка которую вы хотите впихнуть в первый Entry
			2: arg2,  # Строка которую вы хотите впихнуть во второй Entry и т.д
			3: arg3,
			4: arg4
		}

	""" number это цифра Entry сперва биндите Entry на клик. После чего этой функцие передаете номер Entry
	    Допустим enter.bind('<Button-1>', giveNumber)
	    def giveNumber(event):
	        DeletePlaceHolder(1, 2) 1 аргумент это номер Entry 2 аргумент количество всех Entry's
	        3, 4 аргументы обьязательны это переменые самих Entry's Тоисть создали вы например такую переменую:
	        enter = Entry() в 3 аргумент данной функции передаете эту переменую и следующие
	НА ДАННЫЙ МОМЕНТ ФУНКЦИЯ РАБОТАЕТ НОРМАЛЬНО ВСЕГОЛИШ С 3 АРГУМЕНТАМИ 4 и больше неработают. 
	"""
	def DeletePlaceHolder(self, number, CountEnter, enter, enter_2, enter_3 = None, enter_4 = None):
		numb = 1 if number == 1 else number
		if numb != 1:
			numb = 2 if number == 2 else 3
		# if numb == 3:
		#	numb = 3 if number == 3 else 4

		array = [i for i in range(1, CountEnter + 1) if i != numb]

		MainEnter = enter if numb == 1 else 2
		if MainEnter == 2:
			MainEnter = enter_2 if numb == 2 else enter_3
		# if MainEnter == 3:
		#	MainEnter = enter_3 if numb == 3 else enter_4

		SecondEnter = enter if array[0] == 1 else enter_2

		ThreeEnter = None

		if CountEnter == 2:
			array.append(numb)
			DictForCheck = {
				array[0]: SecondEnter.get(),
				array[1]: MainEnter.get()
			}
			if self.MainDict[array[0]] == DictForCheck[array[0]] and self.MainDict[array[1]] == DictForCheck[array[1]]:
				MainEnter.delete(0, END)
			else:
				if self.MainDict[array[0]] != DictForCheck[array[0]] and not DictForCheck[array[0]]:
					SecondEnter.insert(0, self.MainDict[array[0]])
					MainEnter.delete(0, END)

				if self.MainDict[array[1]] != DictForCheck[array[1]] and not DictForCheck[array[1]]:
					MainEnter.insert(0,  self.MainDict[array[1]])
					SecondEnter.delete(0, END)

				MainEnter.delete(0, END)
		else:
			ThreeEnter = enter_2 if array[1] == 2 else enter_3
			DictForCheck = {
				array[0]: SecondEnter.get(),
				array[1]: ThreeEnter.get()
			}
			if self.MainDict[array[0]] == DictForCheck[array[0]] and self.MainDict[array[1]] == DictForCheck[array[1]]:
				MainEnter.delete(0, END)
			else:
				if self.MainDict[array[0]] != DictForCheck[array[0]] and not DictForCheck[array[0]]:
					SecondEnter.insert(0, self.MainDict[array[0]])
					MainEnter.delete(0, END)

				if self.MainDict[array[1]] != DictForCheck[array[1]] and not DictForCheck[array[1]]:
					ThreeEnter.insert(0, self.MainDict[array[1]])
					MainEnter.delete(0, END)

				if (self.MainDict[array[0]] != DictForCheck[array[0]] and not DictForCheck[array[0]] and not
					DictForCheck[array[1]] and self.MainDict[array[1]] != DictForCheck[array[1]]):

					ThreeEnter.insert(0, self.MainDict[array[1]])
					SecondEnter.insert(0, self.MainDict[array[0]])
					MainEnter.delete(0, END)
				MainEnter.delete(0, END)
