#input decisions such that the probability of occurance add to 100

def decision():
    score = 0
    option = input("Enter option: ")
    if(option != ""):
        probability = int(input("Probability /100: "))
        reward = int(input("Reward /100: "))
        risk = int(input("Risk /100: "))
        score = int((risk / reward) * probability * 1000)
    return(score)

def best_decision(optionScores):
    highestScore = 0
    for i in range(len(optionScores)):
        if(optionScores[i] > highestScore):
            highestScore = optionScores[i]
    return(highestScore)

def main():
    d = input("What do you want to make a decision about(health, wealth, wisdom, love)? ")
    if(d == "health"):
        hd = input("What subset of health do you wanna make a decision about? ")
    elif(d=="wealth"):
        wed = input("What subset of wealth do you wanna make a decision about(career, personal, investments)? ")
        if(wed == "career"):
            careers = []
            thiscareer = career_decision()
            while(thiscareer[0] != ""):
                careers.append(thiscareer)
                thiscareer = career_decision()
            print(best_career_decision(careers))
        elif(wed == "personal"):
            careers = []
            thiscareer = career_decision()
            while(thiscareer[0] != ""):
                careers.append(thiscareer)
                thiscareer = career_decision()
            print(best_career_decision(careers))
        elif(wed == "investments"):
            careers = []
            thiscareer = career_decision()
            while(thiscareer[0] != ""):
                careers.append(thiscareer)
                thiscareer = career_decision()
            print(best_career_decision(careers))
        else:
            print("error")
    elif(d=="wisdom"):
        print("")
    elif(d=="love"):
        print("")
    else:
        print("error")
    decisions = []
    thisdecision = decision()
    while(thisdecision != 0):
        decisions.append(thisdecision)
        thisdecision = decision()

    print(best_decision(decisions))

if __name__ == "__main__":
    main()
