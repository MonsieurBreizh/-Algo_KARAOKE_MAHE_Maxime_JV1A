class Player:
    def __init__(self,pseudo):
        self.pseudo = pseudo
        self.listescore = [0,0,0,0,0]
        self.listeChanson = [0,1,2,3,4]

    def getChanson(self):
        return self.listeChanson
    
    def getScore(self):
        return self.listescore

    def getPseudo(self):
        return self.pseudo

    def getTotal(self):
        return self.listescore

    def nouveauScore(self):
        if (Score > self.listescore[]):

    def getlisteChanson(self):
        return self.listeChanson

    
game = True
choixChanson = -1
nomPlayer = input("Quel est ton prénom s'il te plaît ?")
player = Player(nomPlayer)
print("Bonjour et bienvenue dans ce karaoké" + player.getPseudo())
while game
    print("Que voulez-vous chanter ?")
    print("1 - " + str(Player.getlisteChanson(1)) + " - " + Player.getScore(1))
    print("2 - " + str(Player.getlisteChanson(1)) + " - " + Player.getScore(2))
    print("3 - " + str(Player.getlisteChanson(1)) + " - " + Player.getScore(3))
    print("4 - " + str(Player.getlisteChanson(1)) + " - " + Player.getScore(4))
    print("5 - " + str(Player.getlisteChanson(1)) + " - " + Player.getScore(5))
