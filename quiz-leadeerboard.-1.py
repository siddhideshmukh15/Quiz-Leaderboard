leaderboard=[]
questions={
    "what is capital of india?":
    "Delhi",
    "Which language are we learning?":
    "python",
    "How many days are in week?":"7"

}
while True:
    print("=== Quiz Leaderboard ===")
    print("1. Play Quiz")
    print("2. View Leaderboard")
    print("3. View Top Scorer")
    print("4.Exit")
    choice=input("Enter your choice:")

    if choice=="1":
        name=input("Enter player name:")
        score=0
        for question,answer in questions.items():
            user_name=input(question+"")
            if user_name.lower()==answer.lower():
                print("Correct")
                score+=1
            else:
                print("Wrong answer! Answer:",answer)
        leaderboard.append({"name":name,"score":score})
        print("Your score:",score,"/",len(questions))

    elif choice=="2":
        leaderboard.sort(key=lambda x:x["score"],reverse=True)

        if not leaderboard:
            print("No scores available!")
        else:
            print("\n===== Leaderboard=====")
            for i,player in enumerate(leaderboard,1):
                print(i,player["name"],"-",player["score"])

    elif choice=="3":
        if not leaderboard:
            print("No score available!")
        else:
            top_player=max(leaderboard,key=lambda x:x["score"])

            print("\n Top scorer:",top_player["name"])
            print("Score:",top_player["score"])

    elif choice=="4":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice!")

    
    
