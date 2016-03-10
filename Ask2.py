table = ['0','0','0','0','0','0','0','0','0']
tableY = ['0','1','2','3','4','5','6','7','8']
table2=['0','0','0','0','0','0','0','0','0']
table3=['0','0','0','0','0','0','0','0','0']
print "Ο πίνακας ειναι:"
for i in range(3):
    for j in range(3):
        print table[i*3+j],
    print
print "Οι θέσεις του πίνακα ειναι οι εξής"
for i in range(3):
    for j in range(3):
        print tableY[i*3+j],
    print
print "BB = Big Black\nMB = Medium Black\nSB = Small Black\nBR = Big Red\nMR = Medium Red\nSR = Small Red\n"
SB = 1
MB = 2
BB = 3
SR = 1
MR = 2
BR = 3
k1=2
k2=2
k3=2
k4=2
k5=2
k6=2
ProtosGuros=1
Niki = False
Draw = False
boolean = False
while Niki == False:    
    print "Player Black Round"
    k = True
    answer = "m"
    
    Z=0
    y='0'
    while answer != "k" and answer !="t":
        boolean = False
        answer = raw_input("Θέλεις να κινήσεις ή να τοποθετήσεις κάποιο πιόνι;(k/t):")
    if ProtosGuros == 0:
        if answer == 'k':
            
              while y == '0':
                x = 9
                logiko = False
                while logiko == False:
                    x = int(raw_input("Διάλεξε ποιό πιόνι θες να κινήσεις (0-8):"))
                    if x <= 8 or x >= 0:
                        logiko = True
                y = table[x]
                y1 = y
                if y == '0':
                    print "Ξαναδιάλεξε θέση"
              if y == 'BB' or y == 'MB' or y == 'SB':
                     
                     while M==0:
                        answer = int(raw_input("Διάλεξε τη θέση που θες να πας:"))
                        n = table[answer]
                         
                        if y == 'BB': 
                            if n == 'BB':
                                print "Αδύνατο"
                            if n == 'BR':
                                print "Αδύνατο"
                            elif n == '0':
                                table[x] = n
                                table[answer] = y
                                M = 1
                                for i in range(3):
                                    for j in range(3):
                                        print table[i*3+j],
                                    print
                                break
                            elif n == 'MR':
                                table[x] = "0"
                                table[answer] = y
                                M = 1
                                for i in range(3):
                                    for j in range(3):
                                        print table[i*3+j],
                                    print
                                break
                            elif n == 'MB':
                                table[x] = "0"
                                table[answer] = y
                                M = 1
                                for i in range(3):
                                    for j in range(3):
                                        print table[i*3+j],
                                    print
                                break
                            elif n == 'SR':
                                table[x] = "0"
                                table[answer] = y
                                M = 1
                                for i in range(3):
                                    for j in range(3):
                                        print table[i*3+j],
                                    print
                                break
                            elif n == 'SB':
                                table[x] = "0"
                                table[answer] = y
                                M = 1
                                for i in range(3):
                                    for j in range(3):
                                        print table[i*3+j],
                                    print
                                break           
                        elif y == 'MB':
                            if n == '0':
                                table[x] = "0"
                                table[answer] = y
                                M=1
                                Z=1
                                for i in range(3):
                                    for j in range(3):
                                        print table[i*3+j],
                                    print
                            elif n == "SR":
                                 table[x] = "0"
                                 table[answer] = y
                                 M=1
                                 Z=1
                                 for i in range(3):
                                     for j in range(3):
                                         print table[i*3+j],
                                     print
                            elif n == "SB":
                                  table[x] = "0"
                                  table[answer] = y
                                  M=1
                                  Z=1
                                  for i in range(3):
                                     for j in range(3):
                                         print table[i*3+j],
                                     print
                            if n == 'BB':
                                print "Αδύνατο"
                            if n == 'BR':
                                print "Αδύνατο"
                            if n == 'MR':
                                print "Αδύνατο"
                            if n == 'MB':
                                print "Αδύνατο"
                        elif n=="0":
                            print "Διάλεξε αλλο"
                        else:
                            if n == '0':
                                table[x] = n
                                table[answer] = y
                                M = 1
                                Z=1
                            for i in range(3):
                                for j in range(3):
                                    print table[i*3+j],
                                print
                            
                            else:
                                print "Αδύνατο"
    elif answer =='k':
        print "Πρεπεί να έχεις πιόνια στο ταμπλό για να κουνήσεις.Τοποθέτησε πρώτα."
        boolean = True
    if answer == 't' or boolean ==True:
        p = 0
        M = 1
        while p==0:
            pioni = 4
            while pioni!=3 and pioni!=2 and pioni!=1:
                print "Έχεις:\n", k3, "Μεγάλα(3)"
                print  k2, "Μεσσαία(2)"
                print  k1, "Μικρά(1)"
                pioni = input("Διάλεξε πιόνι")
                
                if pioni == 3 and k3>0:
                    k3 = k3-1
                    M = 0
                    p=1
                elif pioni == 2 and k2>0:
                    k2 = k2-1
                    M = 0
                    p=1
                elif pioni == 1 and k1>0:
                    k1 = k1-1
                    M = 0
                    p=1
                elif k3 == 0 and k2 == 0 and k1 == 0:
                    Draw = True
                    p=1
                
                while M==0:
                    answer = 9
                    while answer > 8 or answer <0 :
                        answer = input("Διάλεξε τη θέση που θες να πας:")
                    n = table[answer]
                    if pioni == 3: 
                        if n == 'BB':
                            print "Αδύνατο"
                        elif n == 'RB':
                            print "Αδύνατο"
                        else:
                            
                            table[answer] = 'BB'
                            for i in range(3):
                                for j in range(3):
                                    print table[i*3+j],
                                print
                            break
                    
                    elif pioni == 2:
                            if n == 'BB':
                                print "Αδύνατο"
                            elif n == 'BR':
                                print "Αδύνατο"
                            elif n == 'MR':
                                print "Αδύνατο"
                            elif n == 'MB':
                                print "Αδύνατο"
                            else:
                                
                                table[answer] = 'MB'
                                
                                for i in range(3):
                                    for j in range(3):
                                        print table[i*3+j],
                                    print
                                break
                    elif pioni == 1:
                            if n != '0':
                                print "Αδύνατο" 
                            
                            elif n =='0':
                                
                                table[answer] = 'SB'
                                
                                for i in range(3):
                                    for j in range(3):
                                        print table[i*3+j],
                                    print
                                break    
    if (table[0] == "BB" or table[0] =="MB" or table[0]=="SB") and (table[1] == "BB" or table[1] == "MB" or table[1] =="SB") and (table[2]=="BB" or table[2]=="MB" or table[2] == "SB"):
        Niki = True
        
    elif (table[0] == "BB" or table[0] =="MB" or table[0]=="SB") and (table[4] == "BB" or table[4] == "MB" or table[4] =="SB") and (table[8]=="BB" or table[8]=="MB" or table[8] == "SB"):
        Niki = True
        
    elif (table[0] == "BB" or table[0] =="MB" or table[0]=="SB") and (table[3] == "BB" or table[3] == "MB" or table[3] =="SB") and (table[6]=="BB" or table[6]=="MB" or table[6] == "SB"):
        Niki = True
        
    elif (table[1] == "BB" or table[1] =="MB" or table[1]=="SB") and (table[4] == "BB" or table[4] == "MB" or table[4] =="SB") and (table[7]=="BB" or table[7]=="MB" or table[7] == "SB"):
        Niki = True
        
    elif (table[2] == "BB" or table[2] =="MB" or table[2]=="SB") and (table[5] == "BB" or table[5] == "MB" or table[5] =="SB") and (table[8]=="BB" or table[8]=="MB" or table[8] == "SB"):
        Niki = True
        
    elif (table[3] == "BB" or table[3] =="MB" or table[3]=="SB") and (table[4] == "BB" or table[4] == "MB" or table[4] =="SB") and (table[5]=="BB" or table[5]=="MB" or table[5] == "SB"):
        Niki = True
        
    elif (table[6] == "BB" or table[6] =="MB" or table[6]=="SB") and (table[7] == "BB" or table[7] == "MB" or table[7] =="SB") and (table[8]=="BB" or table[8]=="MB" or table[8] == "SB"):
        Niki = True
        
    elif (table[6] == "BB" or table[6] =="MB" or table[6]=="SB") and (table[4] == "BB" or table[4] == "MB" or table[4] =="SB") and (table[2]=="BB" or table[2]=="MB" or table[2] == "SB"):
        Niki = True
        
    if Niki == True:
        print "Black Player Wins"
    elif Draw == True:
        print "Draw"
    
    
    
    
    
    
    if Niki == False and Draw == False:
        print "Player Red Round"
        k = True
        answer = "m"
        M = 0
        Z=0
        y='0'
        while answer != "k" and answer !="t":
            boolean = False
            answer = raw_input("Θέλεις να κινήσεις ή να τοποθετήσεις κάποιο πιόνι;(k/t):")
        if ProtosGuros == 0:
            if answer == 'k':
                
                  while y == '0':
                    x = 9
                    logiko = False
                    while logiko == False:
                        x = int(raw_input("Διάλεξε ποιό πιόνι θες να κινήσεις (0-8):"))
                        if x <= 8 or x >= 0:
                            logiko = True
                    y = table[x]
                    y1 = y
                    if y == '0':
                        print "Ξαναδιάλεξε θέση"
                  if y == "BR" or y == "MR" or y == "SR":
                         
                         while M==0:
                            answer = int(raw_input("Διάλεξε τη θέση που θες να πας:"))
                            n = table[answer]
                             
                            if y == 'BR': 
                                if n == 'BB':
                                    print "Αδύνατο"
                                if n == 'BR':
                                    print "Αδύνατο"
                                elif n == '0':
                                    table[x] = "0"
                                    table[answer] = y
                                    M = 1
                                    for i in range(3):
                                        for j in range(3):
                                            print table[i*3+j],
                                        print
                                    break
                                elif n == 'MR':
                                    table[x] = "0"
                                    table[answer] = y
                                    M = 1
                                    for i in range(3):
                                        for j in range(3):
                                            print table[i*3+j],
                                        print
                                    break
                                elif n == 'MB':
                                    table[x] = "0"
                                    table[answer] = y
                                    M = 1
                                    for i in range(3):
                                        for j in range(3):
                                            print table[i*3+j],
                                        print
                                    break
                                elif n == 'SR':
                                    table[x] = "0"
                                    table[answer] = y
                                    M = 1
                                    for i in range(3):
                                        for j in range(3):
                                            print table[i*3+j],
                                        print
                                    break
                                elif n == 'SB':
                                    table[x] = "0"
                                    table[answer] = y
                                    M = 1
                                    for i in range(3):
                                        for j in range(3):
                                            print table[i*3+j],
                                        print
                                    break           
                            elif y == 'MR':
                                if n == '0':
                                    table[x] = "0"
                                    table[answer] = y
                                    M=1
                                    Z=1
                                    for i in range(3):
                                        for j in range(3):
                                            print table[i*3+j],
                                        print
                                elif n == "SR":
                                     table[x] = "0"
                                     table[answer] = y
                                     M=1
                                     Z=1
                                     for i in range(3):
                                         for j in range(3):
                                             print table[i*3+j],
                                         print
                                elif n == "SB":
                                      table[x] = "0"
                                      table[answer] = y
                                      M=1
                                      Z=1
                                      for i in range(3):
                                         for j in range(3):
                                             print table[i*3+j],
                                         print
                                if n == 'BB':
                                    print "Αδύνατο"
                                if n == 'BR':
                                    print "Αδύνατο"
                                if n == 'MR':
                                    print "Αδύνατο"
                                if n == 'MB':
                                    print "Αδύνατο"
                            elif n=="0":
                                print "Διάλεξε αλλο"
                            else:
                                if n == '0':
                                    table[x] = "0"
                                    table[answer] = y
                                    M = 1
                                    Z=1
                                for i in range(3):
                                    for j in range(3):
                                        print table[i*3+j],
                                    print
                                
                                else:
                                    print "Αδύνατο"
        elif answer =='k':
            print "Πρεπεί να έχεις πιόνια στο ταμπλό για να κουνήσεις.Τοποθέτησε πρώτα."
            boolean = True 
        if answer == 't' or boolean ==True:
                p = 0
                while p==0:
                    pioni = 4
                    while pioni!=3 and pioni!=2 and pioni!=1:
                        print "Έχεις:\n", k6, "Μεγάλα(3)"
                        print  k5, "Μεσσαία(2)"
                        print  k4, "Μικρά(1)"
                        pioni = input("Διάλεξε πιόνι")
                        
                        if pioni == 3 and k6>0:
                            k6 = k6-1
                            M = 0
                            p=1
                        elif pioni == 2 and k5>0:
                            k5 = k5-1
                            M = 0
                            p=1
                        elif pioni == 1 and k4>0:
                            k4 = k4-1
                            M = 0
                            p=1
                        elif k6 == 0 and k5 == 0 and k4 == 0:
                            Draw = True
                            p=1
                        
                        while M==0:
                            answer = 9
                            while answer > 8 or answer <0 :
                                answer = input("Διάλεξε τη θέση που θες να πας:")
                            n = table[answer]
                            if pioni == 3: 
                                if n == 'BB':
                                    print "Αδύνατο"
                                elif n == 'BR':
                                    print "Αδύνατο"
                                else:
                                    
                                    table[answer] = 'BR'
                                    for i in range(3):
                                        for j in range(3):
                                            print table[i*3+j],
                                        print
                                    break
                            
                            elif pioni == 2:
                                    if n == 'BB':
                                        print "Αδύνατο"
                                    elif n == 'BR':
                                        print "Αδύνατο"
                                    elif n == 'MR':
                                        print "Αδύνατο"
                                    elif n == 'MB':
                                        print "Αδύνατο"
                                    else:
                                        
                                        table[answer] = 'MR'
                                        
                                        for i in range(3):
                                            for j in range(3):
                                                print table[i*3+j],
                                            print
                                        break
                            elif pioni == 1:
                                    if n != '0':
                                        print "Αδύνατο" 
                                    
                                    elif n =='0':
                                        
                                        table[answer] = 'SR'
                                        
                                        for i in range(3):
                                            for j in range(3):
                                                print table[i*3+j],
                                            print
                                        break    
                       
        print "Τέλος γύρου"            
        if ProtosGuros == 1:
            ProtosGuros = 0
        if (table[0] == "BR" or table[0] =="MR" or table[0]=="SR") and (table[1] == "BR" or table[1] == "MR" or table[1] =="SR") and (table[2]=="BR" or table[2]=="MR" or table[2] == "SR"):
            Niki = True
                
        elif (table[0] == "BR" or table[0] =="MR" or table[0]=="SR") and (table[4] == "BR" or table[4] == "MR" or table[4] =="SR") and (table[8]=="BR" or table[8]=="MR" or table[8] == "SR"):
            Niki = True
                
        elif (table[0] == "BR" or table[0] =="MR" or table[0]=="SR") and (table[3] == "BR" or table[3] == "MR" or table[3] =="SR") and (table[6]=="BR" or table[6]=="MR" or table[6] == "SR"):
            Niki = True
                
        elif (table[1] == "BR" or table[1] =="MR" or table[1]=="SR") and (table[4] == "BR" or table[4] == "MR" or table[4] =="SR") and (table[7]=="BR" or table[7]=="MR" or table[7] == "SR"):
            Niki = True
                
        elif (table[2] == "BR" or table[2] =="MR" or table[2]=="SR") and (table[5] == "BR" or table[5] == "MR" or table[5] =="SR") and (table[8]=="BR" or table[8]=="MR" or table[8] == "SR"):
            Niki = True
                
        elif (table[3] == "BR" or table[3] =="MR" or table[3]=="SR") and (table[4] == "BR" or table[4] == "MR" or table[4] =="SR") and (table[5]=="BR" or table[5]=="MR" or table[5] == "SR"):
            Niki = True
                
        elif (table[6] == "BR" or table[6] =="MR" or table[6]=="SR") and (table[7] == "BR" or table[7] == "MR" or table[7] =="SR") and (table[8]=="BR" or table[8]=="MR" or table[8] == "SR"):
            Niki = True
                
        elif (table[6] == "BR" or table[6] =="MR" or table[6]=="SR") and (table[4] == "BR" or table[4] == "MR" or table[4] =="SR") and (table[2]=="BR" or table[2]=="MR" or table[2] == "SR"):
            Niki = True
                
        if Niki == True:
            print "Red Player Wins"
        elif Draw == True:
            print "Draw"
