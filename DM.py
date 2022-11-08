#   ಠ   #

    #Constantes
    
reponse = "O"


    #Variables 
    
n = int(input('Veuillez rentrer la valeur de n : '))
x = 0


    #Programme

while reponse == "O" :
    
    while n < 1 :
        print ("Vous devez entrer un nombre entier strictement positif !")
        n = int(input('Veuillez rentrer la valeur de n : '))

            
    for i in range (n) : 
                
        x = 0.1*x + 0.7
        
    print("-----------------------------------\n"
            "La probabilité de résussite du service au service n°" , i + 1 , "sera de :" ,(round(x, n)) , "\n"
            "-----------------------------------")
            
    reponse = input('Voulez-vous recommencez (O)ui ou (N)on ? : ')
    if reponse == "O" :
        n = int(input('Veuillez rentrer la valeur de n : '))
    else :
        break
