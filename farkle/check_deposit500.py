#funktion check_insättning som kollar så första värdet som sparas är minst 500

# vi ska ta in vilken spelare det är, 
#kolla om den spelaren har 0 på bank-kontot
#om den har det så kan den bara spara om omgångens poäng är minst 500
#returnerar True eller False. 
#om den är False måste man fortsätta kolla denna funktion varje gång till den är True


#bank ska vara variabeln för dictionaryn
#tempscore ska vara poäng under pågående tur
#hussein och basma har currentplayer eftersom de skriver vems tur det är
def check_deposit500(current_player, bank, tempscore):
    if bank.get(current_player) == 0:
        if tempscore >= 500:
            #saveBank: funktion som hussein och Basma gjort
            saveBank()
            return True
        else:
            #print("throw more dices or end turn and get zero points") 
            return False
