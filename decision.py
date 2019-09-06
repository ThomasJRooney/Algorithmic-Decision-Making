#input decisions such that the probability of occurance add to 100

def decision():
    option = input("Enter option: ")
    probability = int(input("Probability /100: "))
    reward = int(input("Reward /100: "))
    risk = int(input("Risk /100:"))
    score = (risk / reward) * (probability / 100)
    return(score)

def best_decision(optionScores):
    highestScore = 0
    for i in range(len(optionscores)):
        if(optionScores[i] > highestScore):
            highestScore = optionScores[i]
    return(highestScore)

def main():
    decisions = []
    decision = decision()
    while(decision != 0):
        decisions.append(decision)
        decision = decision()
    print(best_decision(decsions))

if __name__ == '__main__':
    main()
