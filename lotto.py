import tkinter 
from tkinter import ttk , simpledialog
import tkinter.messagebox
import time
import random

HIGHEST_NUMBER_POSSIBLE = 100
AMOUNT_OF_NUMBER_ITEMS = 5

WINNING_NUMBERS = [1,2,3,4,5]
RANDOMLY_GENERATED_NUMBERS = [random.randint(1,HIGHEST_NUMBER_POSSIBLE) for num in range(AMOUNT_OF_NUMBER_ITEMS)]

class Admin:

	def __init__(self):
		winning_numbers = []
		for i in range(AMOUNT_OF_NUMBER_ITEMS):
			if i == 0:
				num = tkinter.simpledialog.askinteger("Admin", "Enter 1st Number")
				winning_numbers.append(num)
			elif i == 1:
				num = tkinter.simpledialog.askinteger("Admin", "Enter 2nd Number")
				winning_numbers.append(num)
			elif i == 2:
				num = tkinter.simpledialog.askinteger("Admin", "Enter 3rd Number")
				winning_numbers.append(num)	
			else:
				num = tkinter.simpledialog.askinteger("Admin", "Enter " + str(i + 1) + "th" + " Number")
				winning_numbers.append(num)	

		self.done_display = tkinter.messagebox.showinfo("Complete", "The Winning Numbers Have Been Changed")	

		change_winning_numbers(winning_numbers)	
		tkinter.mainloop()
			

class Homescreen:

	def __init__(self):
		self.main_window = tkinter.Tk()
		self.top_frame = tkinter.Frame(self.main_window)
		self.middle_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)
		self.last_frame = tkinter.Frame(self.main_window)
		self.admin_bttn = tkinter.Button(self.main_window, text='Admin', command=self.admin_bttn_clicked)
		self.intro_prompt_lbl = tkinter.Label(self.top_frame, text='\n\nWelcome to the City Tech Lotto!\n' + \
		'Here you have an opportunity to win $1 for free.\n If you lose, you can try again but you have to pay $20\n\n\n\n')
		self.option_prompt_lbl = tkinter.Label(self.middle_frame, text='You have two options.\n You can either input your own numbers manually,\n or have them randomly generated for you.' +
			'\nPlease select whichever you prefer.\nThen click \'Ok\'')
		
		self.radio_var = tkinter.IntVar()
		self.radio_var.set(1)
		#Creating manual & random radio button with int_var set to 1 and 0 respectively
		self.manualbttn = tkinter.Radiobutton(self.bottom_frame, \
												text='Manual', variable=self.radio_var, \
												value=1)
		self.randombttn = tkinter.Radiobutton(self.bottom_frame, \
												text='Random', variable=self.radio_var, \
												value=0)
		self.ok_bttn = tkinter.Button(self.last_frame, \
									text='Ok', command=self.get_choice)
		self.quit_bttn = tkinter.Button(self.last_frame, \
										text='Quit', command=self.main_window.destroy)



		#Packing all of the elements
		self.admin_bttn.pack(side='top', anchor='e')
		self.manualbttn.pack(side='left')
		self.randombttn.pack(side='left')
		self.ok_bttn.pack(side='left')
		self.quit_bttn.pack(side='left')
		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()
		self.last_frame.pack()
		self.intro_prompt_lbl.pack(side='top')
		self.option_prompt_lbl.pack(side='top')
		tkinter.mainloop()



	def admin_bttn_clicked(self):
		self.password = tkinter.simpledialog.askstring("Password","Please enter password:")
		if self.password == 'alligatorsoup':
			admin_obj = Admin()
		else:
			invalid_password = tkinter.messagebox.showerror("Password Invalid", "\nAccess Denied" )

	def get_choice(self):
		self.main_window.destroy()
		self.get_choice = self.radio_var.get()
		if self.get_choice == 1:
			manual_window = ManuallyInputScreen()
		if self.get_choice == 0:
			random_window = RandomScreen()	
			



class ManuallyInputScreen:

	def __init__(self):
		self.manual_window = tkinter.Tk()
		self.top_frame = tkinter.Frame(self.manual_window)
		self.middle_frame = tkinter.Frame(self.manual_window)
		self.bottom_frame = tkinter.Frame(self.manual_window)
		self.lowest_frame = tkinter.Frame(self.manual_window)
		self.manual_prompt = tkinter.Label(self.top_frame,text='Enter 5 Numbers Separated By A Space: ')
		self.manual_entry = tkinter.Entry(self.top_frame, width=9)
		self.manual_submit_bttn = tkinter.Button(self.middle_frame, text='Submit', command=self.submit_and_check_manual)
		self.quit_bttn_manual_window = tkinter.Button(self.lowest_frame, text='Quit', command=self.manual_window.destroy)


		self.manual_prompt.pack(side='left')
		self.manual_entry.pack(side='left')
		self.manual_submit_bttn.pack(side='top')
		self.quit_bttn_manual_window.pack()
		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()
		self.lowest_frame.pack()
		


		tkinter.mainloop()

	def submit_and_check_manual(self):
		self.check_lbl = tkinter.Label(self.bottom_frame, text='\n...Checking Numbers...\n')
		self.check_lbl.after(1500, self.check_manual)
		self.check_lbl.pack(side='top')


	def check_manual(self):
		self.lowestframe = tkinter.Frame(self.manual_window)
		self.lowestframe.pack()
		self.check_lbl.destroy()
		try: 
			numbers_input = [int(x) for x in self.manual_entry.get().split(' ')]

			if len(numbers_input) == AMOUNT_OF_NUMBER_ITEMS:
				if sorted(numbers_input) == WINNING_NUMBERS:
					self.win_lbl = tkinter.Label(self.middle_frame, text='\n...YOU WIN!...\n')
					self.win_lbl.pack(side='top')
					self.manual_prompt.destroy()
					self.manual_entry.destroy()
					self.manual_submit_bttn.destroy()

				else:
					answer = tkinter.messagebox.askyesno("You Lost", "\tSorry, You Lose\n\nWould you like to try again? ")
					self.lose_lbl = tkinter.Label(self.middle_frame, text='\n...Better Luck Next Time!...\n')
					self.lose_lbl.pack(side='top')
					self.manual_prompt.destroy()
					self.manual_entry.destroy()
					self.manual_submit_bttn.destroy()
					if answer == True:
						self.manual_window.destroy()
						homescreen = Homescreen()
			else:
				tkinter.messagebox.showinfo("Error", "\tPlease Input " + str(AMOUNT_OF_NUMBER_ITEMS) +  " Numbers Only.\n\n Example:87 9 26 3 51")
						
		except ValueError:
			value_err_message = tkinter.messagebox.showinfo("Error", "\tPlease Input " + str(AMOUNT_OF_NUMBER_ITEMS) + " Numbers\nSeparated By A Single Space.\n\n Example:87 9 26 3 51")
					


class RandomScreen:

	def __init__(self):
		self.random_window = tkinter.Tk()
		self.top_frame = tkinter.Frame(self.random_window)
		self.middle_frame = tkinter.Frame(self.random_window)
		self.bottom_frame = tkinter.Frame(self.random_window)
		self.randomly_generating_lbl = tkinter.Label(self.top_frame, text='\n...Retrieving Your Random Numbers...\n')
		self.randomly_generating_lbl.after(1800, self.return_random_numbers)
		

		self.randomly_generating_lbl.pack(side='top')
		self.top_frame.pack()
		self.middle_frame.pack()
		self.bottom_frame.pack()
		tkinter.mainloop()


	def return_random_numbers(self):
		def get_random_number_sequence(listname):
			return(str(listname[0]) + ' ' + str(listname[1]) + ' ' + str(listname[2]) + ' '+ str(listname[3]) + ' and ' + str(listname[4]))	
		
		# randomly_generated_numbers = [random.randint(1,HIGHEST_NUMBER_POSSIBLE) for num in range(AMOUNT_OF_NUMBER_ITEMS)]
		number_sentence = 'Your random numbers are ' + get_random_number_sequence(RANDOMLY_GENERATED_NUMBERS)	
		self.randomly_generating_lbl.destroy()
		self.random_nums_lbl = tkinter.Label(self.top_frame, text=number_sentence)

		#Buttons to be displayed 'Randomize' should only show up after displaying the first set of random numbers as well as 'Submit'
		self.random_quit_bttn = tkinter.Button(self.bottom_frame, text='Quit', command=self.random_window.destroy)
		self.random_submit_bttn = tkinter.Button(self.bottom_frame, text='Submit', command=self.submit_random)
		self.regenerate_random = tkinter.Button(self.bottom_frame, text='Randomize', command= self.get_dif_random_nums)

		self.random_quit_bttn.pack(side='left')
		self.random_submit_bttn.pack(side='left')
		self.regenerate_random.pack(side='left')
		self.random_nums_lbl.pack()


	def submit_random(self):
		self.random_nums_lbl.destroy()
		self.check_lbl = tkinter.Label(self.top_frame, text='\n...Checking Numbers...\n')
		self.check_lbl.after(1500, self.check_random)
		self.check_lbl.pack(side='top')

	def check_random(self):
		self.check_lbl.destroy()
		if sorted(RANDOMLY_GENERATED_NUMBERS) == WINNING_NUMBERS:
			self.win_lbl = tkinter.Label(self.top_frame, text='\n...YOU WIN!...\n')
			self.win_lbl.pack(side='top')
		else:
			answer = tkinter.messagebox.askyesno("You Lost", "\tSorry, You Lose\n\nWould you like to try again? ")
			self.lose_lbl = tkinter.Label(self.top_frame, text='\n...Better Luck Next Time!...\n')
			self.regenerate_random.destroy()
			self.random_submit_bttn.destroy()

			self.lose_lbl.pack(side='top')
			
			if answer == True:
				self.random_window.destroy()
				homescreen = Homescreen()



	def get_dif_random_nums(self):
		self.random_nums_lbl.destroy()
		def get_random_number_sequence(listname):
			return(str(listname[0]) + ' ' + str(listname[1]) + ' ' + str(listname[2]) + ' '+ str(listname[3]) + ' and ' + str(listname[4]))	
		
		global RANDOMLY_GENERATED_NUMBERS
		RANDOMLY_GENERATED_NUMBERS = [random.randint(1,HIGHEST_NUMBER_POSSIBLE) for num in range(AMOUNT_OF_NUMBER_ITEMS)]
		self.randomly_generated_numbers = RANDOMLY_GENERATED_NUMBERS
		number_sentence = 'Your random numbers are ' + get_random_number_sequence(RANDOMLY_GENERATED_NUMBERS)
		self.random_nums_lbl = tkinter.Label(self.top_frame, text=number_sentence)
		self.random_nums_lbl.pack()

def change_winning_numbers(new_list):
			global WINNING_NUMBERS 
			WINNING_NUMBERS = new_list
	


homescreen = Homescreen()		
