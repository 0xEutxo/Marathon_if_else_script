marathon = 24

while True:
    response = input("Did you complete the 24 mile marathon? yes or no >> ")
    
    if response == 'yes' :
        print("Congrats! ")
        response = int(input("How long did it take you to finish in hours? "))
        if response > 0 :
            response = round(response * 60 / marathon, 2)
            print("Your pace was " + str(response) + " minute per mile.")
            break
        else :
            break
    else :
        print("Better luck next time!")
        break

    