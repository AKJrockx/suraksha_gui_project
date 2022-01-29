import random
from tkinter import *
from pygame import mixer
from datetime import time
from time import sleep

mixer.init()

counter = 0
running = True


# Global stop function to stop the clock
def stop():
	global running
	running = False


# Global alarm system to play the alarm sound *********** Currently not working and not used *******************
def alarm_system():
	mixer.music.load('alarm_sound.mp3')
	mixer.music.play()
	sleep(3)
	mixer.music.stop()


# ----------------------------------------------------Fire App --------------------------------------------------------#

def fire_app():
	floor_number = random.randint(1, 20)
	room_number = (floor_number * 100) + random.randint(1, 9)
	global running, counter
	running = True
	counter = 0
	fire_window = Toplevel(window)
	fire_window.title("Fire App")
	fire_window.config(padx=15, pady=20)
	Button(
		fire_window,
		image=fire_logo,
		command=lambda: [stop(), ]
	).grid(row=0, column=0, columnspan=2)

	Label(fire_window, text="Fire Alert", font=("Monetarist", 50, "bold")).grid(row=1, column=0, columnspan=2)

	Label(
		fire_window,
		text=f"Floor No. {floor_number} \nRoom No. {room_number}",
		font=("Monetarist", 15)
	).grid(row=2, column=0, columnspan=2)

	Label(
		fire_window,
		text="An alert has been send to all the residents",
		font=("Monetarist", 15)
	).grid(row=3, column=0, columnspan=2)

	Label(fire_window, text="Fire brigade has been called", font=("Monetarist", 15)).grid(row=4, column=0, columnspan=2)
	timer_label = Label(fire_window, text="00:00", fg="red")
	timer_label.grid(row=5, column=0, columnspan=2)

	def fire_count_app():
		if running:
			global counter

			seconds = counter % 60
			minutes = (counter // 60) % 60

			dt = time(second=seconds, minute=minutes)
			string = dt.isoformat(timespec='auto')
			timer_label.config(text=string)

			counter += 1
			window.after(1000, fire_count_app)

	fire_count_app()


# ----------------------------------------------------Theft App -------------------------------------------------------#

def theft_yes_action():
	yes_window = Toplevel(window)
	yes_window.title("Calling...")
	yes_window.config(padx=45, pady=155)
	Label(yes_window, text="Calling... \n100", font=("Monetarist", 50, "bold")).grid(row=0, column=0)

	Label(
		yes_window,
		text="your address has been sent \nto the police, they will be arriving \nvery soon",
		font=("Monetarist", 15, "italic")
	).grid(row=1, column=0)


def theft_app():
	theft_window = Toplevel(window)
	theft_window.title("Theft App")
	theft_window.config(padx=40, pady=40)
	Button(theft_window, image=theft_logo).grid(row=0, column=0, columnspan=2)

	Label(theft_window, text="Theft Alert", font=("Monetarist", 50, "bold")).grid(row=1, column=0, columnspan=2)
	Label(
		theft_window,
		text="\nThe gate has been opened by an \nanonymous person",
		font=("Monetarist", 15)
	).grid(row=2, column=0, columnspan=2)

	Label(
		theft_window,
		text="Do you want to call the police?\n",
		font=("Monetarist", 15)
	).grid(row=3, column=0, columnspan=2)

	Button(
		theft_window,
		image=yes_img,
		command=lambda: [theft_yes_action(), theft_window.destroy()]
	).grid(row=4, column=0)

	Button(theft_window, image=no_img, command=theft_window.destroy).grid(row=4, column=1)


# ----------------------------------------------------Temp App --------------------------------------------------------#

def temp_yes_action():
	yes_window = Toplevel(window)
	yes_window.title("Opening...")
	yes_window.config(padx=35, pady=175)
	Label(yes_window, text="Opening... \n", font=("Monetarist", 50, "bold")).grid(row=0, column=0)
	Label(yes_window, text="The gate has been opened", font=("Monetarist", 15, "italic")).grid(row=1, column=0)


def temp_no_action():
	no_window = Toplevel(window)
	no_window.title("Mic")
	no_window.config(padx=35, pady=175)
	Label(no_window, text="Mic \n", font=("Monetarist", 50, "bold")).grid(row=0, column=0)
	Label(no_window, text="The gate has been opened", font=("Monetarist", 15, "italic")).grid(row=1, column=0)


def temp_app():
	temp = random.randint(85, 105)
	person = random.choice(['him', 'her'])
	temp_window = Toplevel(window)
	temp_window.title("Temp App")
	temp_window.config(padx=35, pady=40)
	Button(temp_window, image=temp_logo).grid(row=0, column=0, columnspan=2)

	Label(temp_window, text="Temp Alert", font=("Monetarist", 50, "bold")).grid(row=1, column=0, columnspan=2)

	Label(
		temp_window,
		text=f"\nThe person's temperature is\n{temp}°F",
		font=("Monetarist", 15)
	).grid(row=2, column=0, columnspan=2)

	Label(
		temp_window,
		text=f"Do you want {person} to enter?\n",
		font=("Monetarist", 15)
	).grid(row=3, column=0, columnspan=2)

	Button(temp_window, image=yes_img, command=lambda: [temp_window.destroy(), temp_yes_action()]).grid(row=4, column=0)
	Button(temp_window, image=no_img, command=lambda: [temp_window.destroy()]).grid(row=4, column=1)


# ----------------------------------------------------Voltage App -----------------------------------------------------#

def voltage_app():
	global running, counter
	running = True
	counter = 0

	volt = random.choice(['High', 'Low'])
	voltage_window = Toplevel(window)
	voltage_window.title("Voltage App")
	voltage_window.config(padx=35, pady=45)
	Button(voltage_window, image=voltage_logo, command=stop).grid(row=0, column=0, columnspan=2)
	Label(voltage_window, text=f"{volt} Volt", font=("Monetarist", 50, "bold")).grid(row=1, column=0, columnspan=2)
	Label(voltage_window, text="Since,", font=("Monetarist", 15)).grid(row=2, column=0, columnspan=2)
	timer_label = Label(voltage_window, text="00:00", font=("Monetarist", 15))
	timer_label.grid(row=3, column=0, columnspan=2)

	Label(
		voltage_window,
		text="\n\nHeavy appliance has been shut down\n to prevent damage !!",
		font=("Monetarist", 15)
	).grid(row=4, column=0, columnspan=2)

	def voltage_count_app():
		if running:
			global counter

			seconds = counter % 60
			minutes = (counter // 60) % 60

			dt = time(second=seconds, minute=minutes)
			string = dt.isoformat(timespec='auto')
			timer_label.config(text=string)

			counter += 1
			window.after(1000, voltage_count_app)

	voltage_count_app()


# ----------------------------------------------------Leakage App -----------------------------------------------------#

def leakage_yes_action():
	yes_window = Toplevel(window)
	yes_window.title("Calling...")
	yes_window.config(padx=55, pady=155)
	Label(yes_window, text="Calling... \nPlumber", font=("Monetarist", 50, "bold")).grid(row=0, column=0)

	Label(
		yes_window,
		text="your address has been sent \nto the plumber, he/she will be \narriving very soon",
		font=("Monetarist", 15, "italic")
	).grid(row=1, column=0)


def random_floors():
	floor_number = random.randint(1, 20)
	room_number = floor_number * 100 + random.randint(1, 9)
	return room_number


def leakage_app():
	leakage_window = Toplevel(window)
	leakage_window.title("Leakage App")
	leakage_window.config(padx=10, pady=15)
	Button(leakage_window, image=leakage_logo).grid(row=0, column=0, columnspan=2)
	Label(leakage_window, text="Leakage Alert", font=("Monetarist", 50, "bold")).grid(row=1, column=0, columnspan=2)

	Label(
		leakage_window,
		text="Leakage has been detected \non multiple floors: ",
		font=("Monetarist", 15)
	).grid(row=2, column=0, columnspan=2)

	Label(
		leakage_window,
		text=f"{random_floors(), random_floors(), random_floors(), random_floors()}\n\n",
		font=("Monetarist", 15)
	).grid(row=3, column=0, columnspan=2)

	Label(leakage_window, text="Want to call plumber?", font=("Monetarist", 20)).grid(row=7, column=0, columnspan=2)

	Button(
		leakage_window,
		image=yes_img,
		command=lambda: [leakage_window.destroy(), leakage_yes_action()]
	).grid(row=8, column=0)
	Button(leakage_window, image=no_img, command=lambda: [leakage_window.destroy()]).grid(row=8, column=1)


# -----------------------------------------------------Medic App ------------------------------------------------------#

def medic_app():
	medic_window = Toplevel(window)
	medic_window.title("Medic App")
	medic_window.config(padx=30, pady=30)
	Button(medic_window, image=medic_logo).grid(row=0, column=0, columnspan=2)
	Label(medic_window, text="Medic Alert", font=("Monetarist", 50, "bold")).grid(row=1, column=0, columnspan=2)

	Label(
		medic_window,
		text="Medic AI detected medical situation\n",
		font=("Monetarist", 15)
	).grid(row=2, column=0, columnspan=2)

	Label(
		medic_window,
		text="Message has been sent to \nhospital and neighbours\n\n",
		font=("Monetarist", 15)
	).grid(row=3, column=0, columnspan=2)
	Label(medic_window, text="Calling ambulance", font=("Monetarist", 20, "bold")).grid(row=4, column=0, columnspan=2)


# -------------------------------------------------------Crime App ----------------------------------------------------#

def crime_yes_action():
	yes_window = Toplevel(window)
	yes_window.title("Calling...")
	yes_window.config(padx=45, pady=155)
	Label(yes_window, text="Calling... \n100", font=("Monetarist", 50, "bold")).grid(row=0, column=0)

	Label(
		yes_window,
		text="your address has been sent \nto the police, they will be arriving \nvery soon",
		font=("Monetarist", 15, "italic")
	).grid(row=1, column=0)


def crime_app():
	crime_window = Toplevel(window)
	crime_window.title("Crime App")
	crime_window.config(padx=25, pady=40)
	Button(crime_window, image=crime_logo).grid(row=0, column=0, columnspan=2)

	Label(crime_window, text="Crime Alert", font=("Monetarist", 50, "bold")).grid(row=1, column=0, columnspan=2)

	Label(
		crime_window,
		text="Camera AI detected unidentified \nperson accessing of your parked vehicle",
		font=("Monetarist", 15)
	).grid(row=2, column=0, columnspan=2)

	Label(
		crime_window,
		text="Do you want to call the police?\n",
		font=("Monetarist", 15)
	).grid(row=3, column=0, columnspan=2)

	Button(
		crime_window,
		image=yes_img,
		command=lambda: [crime_yes_action(), crime_window.destroy()]
	).grid(row=4, column=0)

	Button(crime_window, image=no_img, command=crime_window.destroy).grid(row=4, column=1)


# -------------------------------------------------------Gas App ------------------------------------------------------#

def gas_app():
	gas_window = Toplevel(window)
	gas_window.title("Gas App")
	gas_window.config(padx=50, pady=30)
	Button(gas_window, image=gas_logo).grid(row=0, column=0, columnspan=2)
	Label(gas_window, text="Gas Alert", font=("Monetarist", 50, "bold")).grid(row=1, column=0, columnspan=2)

	Label(
		gas_window,
		text="Gas leakage detected!!!",
		font=("Monetarist", 15)
	).grid(row=2, column=0, columnspan=2)

	Label(
		gas_window,
		text="STATUS: \nElectricity and gas connections \nhave been shut down",
		font=("Monetarist", 15)
	).grid(row=3, column=0, columnspan=2)

	Label(
		gas_window,
		text="Neighbours have been informed",
		font=("Monetarist", 15)
	).grid(row=4, column=0, columnspan=2)


# ----------------------------------------------------Home Page UI ----------------------------------------------------#

window = Tk()
window.title("Security App")
window.config(padx=20, pady=30, background="black")

# Creating the display label
label = Label(text="Suraksha\n\n", fg="white", bg="black", font=("Monetarist", 50, "bold"))
label.grid(row=0, column=0, columnspan=2)

# Creating all the images for logos
fire_logo = PhotoImage(file="images/fire_logo.png")
theft_logo = PhotoImage(file="images/theft_logo.png")
temp_logo = PhotoImage(file="images/temp_logo.png")
voltage_logo = PhotoImage(file="images/voltage_logo.png")
leakage_logo = PhotoImage(file="images/leakage_logo.png")
medic_logo = PhotoImage(file="images/medic_logo.png")
crime_logo = PhotoImage(file="images/crime_logo.png")
gas_logo = PhotoImage(file="images/gas_logo.png")

# Yes and No button images
yes_img = PhotoImage(file="images/yes_button.png")
no_img = PhotoImage(file="images/no_button.png")

# Creating the buttons
fire_img = PhotoImage(file="images/fire_button.png")
fire_button = Button(image=fire_img, highlightbackground="black", command=fire_app)
fire_button.grid(row=1, column=0)

theft_img = PhotoImage(file="images/theft_button.png")
theft_button = Button(image=theft_img, highlightbackground="black", command=theft_app)
theft_button.grid(row=1, column=1)

temp_img = PhotoImage(file="images/temp_button.png")
temp_button = Button(image=temp_img, highlightbackground="black", command=temp_app)
temp_button.grid(row=2, column=0)

voltage_img = PhotoImage(file="images/voltage_button.png")
voltage_button = Button(image=voltage_img, highlightbackground="black", command=voltage_app)
voltage_button.grid(row=2, column=1)

leakage_img = PhotoImage(file="images/leakage_button.png")
leakage_button = Button(image=leakage_img, highlightbackground="black", command=leakage_app)
leakage_button.grid(row=3, column=0)

medic_img = PhotoImage(file="images/medic_button.png")
medic_button = Button(image=medic_img, highlightbackground="black", command=medic_app)
medic_button.grid(row=3, column=1)

crime_img = PhotoImage(file="images/crime_button.png")
crime_button = Button(image=crime_img, highlightbackground="black", command=crime_app)
crime_button.grid(row=4, column=0)

gas_img = PhotoImage(file="images/gas_button.png")
gas_button = Button(image=gas_img, highlightbackground="black", command=gas_app)
gas_button.grid(row=4, column=1)

window.mainloop()
