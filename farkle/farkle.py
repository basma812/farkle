import random
class Farkle:
     rollNum = 6
     player = None
     thisRound = []
     bank = []

     def __init__(self):
          self.rollNum = 6
          self.player = None
          self.thisRound = []
          self.bank = []

     # welcome_msg
     print("Welcome to Farkle")


     def roll_dice(self):
     #Gets a randomly generated roll.
		rolled = []
		for i in range(self.rollNum):
			rolled.append(random.randint(1,6))
		return rolled

     def reroll(self):
		self.bank = [] #taking the numbers from score 
		self.thisRound = [] #
		self.rollNum = 6;
     
     #took it from Samuel's code
     def bank(self):
      = bankmodule.create_bank()
     print(bank)

# def play(dice, players):



# def score(dice, players):

#   Calculate a Farkle score using the traditional scoring method, which is:
#     4 1s:     2,000 points
#     3 1s:     1,000 points
#     Single 1: 100 points
#     Single 5: 50 points
#     Triple of any non-1 number:    100 x number showing
#     Quadruple of any non-1 number: Double the triple score
#     """
# Notes:
#     - Doubles score nothing (unless a 1 or a 5) as above
#     - All scoring dice must be rolled in a single turn (i.e. they
#     are not additive over turns)
#     - Rolling all 6 will be two sets and scored accordingly
#         [4] + [2]
#         [3] + [3]
#         [2] + [2] + [2]
#
# Examples:
#     1,1,1,5,5,5 ==> 1500 (1000 for 1s + 250 for 3 5s)
#     1,1,1,1,6,6 ==> 2000 (2000 for 4 1s)
#     5,3,6,5,3,3 ==> 400 (300 for 3 3s + 100 for 2 5s)
#     1,2,2,3,3,5 ==> 150 (100 for a 1 and 50 for a 5)


# kanske def rounds(players):
