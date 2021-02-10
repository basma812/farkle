def trissCheck(dice_List):
    # dice_List = [5, 6, 5, 6, 6, 5]
    playerPointstogive = 0
    threeOfkind = 0
    tempPlayerpoints = 0
    
    
    
    dice_List.sort()
      
    if dice_List[0] == dice_List[2] or dice_List[1] == dice_List[3] or dice_List[2] == dice_List[4] or dice_List[3] == dice_List[5]:
        threeOfkind = 1
    if threeOfkind == 1:         
        if dice_List[0] == dice_List[2] and dice_List[0] == 1 or dice_List[1] == dice_List[3] and dice_List[1] == 1 or dice_List[2] == dice_List[4]  and dice_List[4] == 1 or dice_List[3] == dice_List[5] and dice_List[5] == 1: 
            tempPlayerpoints += 1000
            threeOfkind += 1
        if dice_List[0] == dice_List[2] and dice_List[0] == 2 or dice_List[1] == dice_List[3] and dice_List[1] == 2 or dice_List[2] == dice_List[4]  and dice_List[4] == 2 or dice_List[3] == dice_List[5] and dice_List[5] == 2: 
            tempPlayerpoints += 200      
            threeOfkind += 1
        if dice_List[0] == dice_List[2] and dice_List[0] == 3 or dice_List[1] == dice_List[3] and dice_List[1] == 3 or dice_List[2] == dice_List[4]  and dice_List[4] == 3 or dice_List[3] == dice_List[5] and dice_List[5] == 3:
            tempPlayerpoints += 300      
            threeOfkind += 1
        if dice_List[0] == dice_List[2] and dice_List[0] == 4 or dice_List[1] == dice_List[3] and dice_List[1] == 4 or dice_List[2] == dice_List[4]  and dice_List[4] == 4 or dice_List[3] == dice_List[5] and dice_List[5] == 4:
            tempPlayerpoints += 400  
            threeOfkind += 1
        if dice_List[0] == dice_List[2] and dice_List[0] == 5 or dice_List[1] == dice_List[3] and dice_List[1] == 5 or dice_List[2] == dice_List[4]  and dice_List[4] == 5 or dice_List[3] == dice_List[5] and dice_List[5] == 5:
            tempPlayerpoints += 500     
            threeOfkind += 1
        if dice_List[0] == dice_List[2] and dice_List[0] == 6 or dice_List[1] == dice_List[3] and dice_List[1] == 6 or dice_List[2] == dice_List[4]  and dice_List[4] == 6 or dice_List[3] == dice_List[5] and dice_List[5] == 6:
            tempPlayerpoints += 600
            threeOfkind += 1
        if threeOfkind == 3:
            tempPlayerpoints = 0
            tempPlayerpoints = 2500
            playerPointstogive += tempPlayerpoints
    print(playerPointstogive)   

           
    
