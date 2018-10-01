import random 

decisions = [
			"Heck yeah", 
			"Nah, maybe later", 
			"YESSS", 
			"go for it!",
			"You know you want to :)",
			"What are you still doing here? Go get a taco!",
			"to food or not to food...taco is the question."
			]

def random_decision():
	return decisions[random.randint(0, len(decisions) - 1)]
	