from sys import exit

# Box Game: the point of this game is to test my abilities with if statements and loops
# functions will be used to isolate the tasks that need to be accomplished

def which_box():
	print "Pick: box 1 (it's big) or box 2 (it's small)"
	decision = raw_input("> ")
	if "1" in decision:
		toiletries()
	elif "2" in decision:
		free_gift()
	else: 
		dead("Try again!")

def toiletries():
	print "This is my store! I sell..."
	print "Toiletries! What do you need?"
	while True:
		decision = raw_input("> ")

		if "soap" in decision:
			cost = 1.50
			how_many(cost)
		elif "toothpaste" in decision or "paste" in decision:
			cost = 4.0
			how_many(cost)
		elif "shaving cream" in decision:
			cost = 3.0
			how_many(cost)
		else:
			print "Don't have it! Ask again!"

def how_many(cost):
	print "How many would you like? 1 or 2?"
	decision = raw_input("> ")

	if decision == "1":
		print "Okay, that will be $%.2f. " % cost
		total_cost = cost
		decision = 0
		cash_credit(total_cost)
	elif decision == "2":
		total_cost = 2*cost
		print "Okay, that will be $%.2f. " % total_cost
		cash_credit(total_cost)
	else: 
		dead("Get out of my store I said I only have 2!")

def cash_credit(total_cost):
	print "Will that be Cash or Credit?"
	decision = raw_input("> ")

	if "cash" in decision:
		print "what bill are you paying with?"
		bill = raw_input("> ")

		if bill == "1":
			payment = int(bill)
		elif bill == "5":
			payment = int(bill)
		elif bill == "10":
			payment = int(bill)
		elif bill == "20":
			payment = int(bill)
		else:
			dead("I can't accept that - leave!")
	elif "credit" in decision:
		print "All finished! Enjoy your purchase!"
		exit()
	else: 
		dead("Wrong answer. Leave. ")

	change(total_cost, payment)

def change(total_cost, payment):
	cash_change = payment-total_cost
	if cash_change >= 0:
		print "Your change is $%.2f. Thanks for shopping!" % cash_change
		exit()
	else:
		dead("Not enough - sorry!")

def free_gift():
	print "You open the box..."
	print "A free gift! Would you like the sandwich or money?"
	decision = raw_input("> ")

	if decision == "money":
		print "spend it in my store!"
		toiletries()
	elif decision == "sandwich":
		print "Yum!"
		exit()
	else:
		dead("I don't have that. Bye!")

def dead(why):
	print why
	exit(0)

def start():
	print """
	Welcome to box game!
	There are two boxes in front of you."""
	which_box()



start()
