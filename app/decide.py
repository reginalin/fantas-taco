import random 

def randomDecision():
	decisions = [
				"Heck yeah", 
				"Nah, maybe later", 
				"YESSS", 
				"go for it!",
				"You know you want to :)",
				"What are you still doing here? Go get a taco!",
				"to food or not to food...taco is the question."
				]
	return decisions[random.randint(0, len(decisions) - 1)]
	