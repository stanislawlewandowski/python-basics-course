likesAmount = 5
ShareAmount = 5
if likesAmount >= 500 and ShareAmount >= 100:
    print('Price drops 10%')
elif likesAmount < 500 and ShareAmount < 100:
    print("There is not much likes and shares left! Come on!")
elif likesAmount < 500:
    print('There is not much likes left! Come on!')
elif ShareAmount < 100:
    print('There is not much Shares left! Come on!')
