def score(scores):
    nscores = set(scores)
    nscores.remove(max(nscores))
    return max(nscores)

n = int(input("Enter the No.of Participants: "))

scores = list(map(int , input("Enter the scores seperated by spaces:").split()))

if len(scores)!=n:
    print("No of Scores entered does not match the No of Participants.")
else:
    ascore = score(scores)
    print("The runner up score is: ",ascore)