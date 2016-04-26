###############################################
# Exercícios do site Codecombat.com           # 
# Autor: Rodrigo Vieira Peres                 #
# Data: 24/04/2016                            #
#                                             #
# Site: http://www.rodrigoperes.tk/           #
#                                             #
# Arquivo: Lv11 - Cupboards of Kithgard.py    #
###############################################

"""Break open the Cupboard. Under 7 statements. You can perform any action before a while-true loop"""


# There may be something around to help you!

# First, move to the Cupboard.
self.moveUp()
self.moveRight(2)
self.moveDown(2)
# Then, attack the "Cupboard" inside a while-true loop.
while True:
    self.attack("Cupboard")