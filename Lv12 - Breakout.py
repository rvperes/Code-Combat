###############################################
# Exercícios do site Codecombat.com           # 
# Autor: Rodrigo Vieira Peres                 #
# Data: 24/04/2016                            #
#                                             #
# Site: http://www.rodrigoperes.tk/           #
#                                             #
# Arquivo: Lv12 - Breakout.py                 #
###############################################

"""Free your friend. Escape the level. Under 7 statements. Free your friend by attacking the "Weak Door" so you have more time to break the 
stronger "Door" with a while-true loop."""


# Free your ally, then clear a path to escape!
self.moveRight(1)
self.attack("Weak Door")
self.moveRight(1)
self.moveDown(1)
while True:
    self.attack("Door")