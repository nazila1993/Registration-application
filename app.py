import yaml
import verifier
with open ("questionnaire.yaml", "r")as f:
    question = yaml.load(f)

answers= {}
go_on = "do you want to continue with the voter registration?"
for q in [i for i in question]:
    c = 0
    while c < 3:
        c +=1
        ans = input(q.get("text"))
        if getattr(verifier, q.get("Verification"))(ans):
            answers[q.get("number")] = ans
            if input(go_on).strip().lower().startswith("n"):
                exit()
            else:
                break
        if c < 3:
            print("Wrong, Try again!")
        else:
            exit()

temp = """
Thanks for registering to vote. Here is the information we received:
name (first last): {} {}
age : {}
U.S. citizen: {}
state : {}
zipcode : {}
Thanks for trying the voter resgistration application.
"""
if int(answers.get(3)) >= 18 and answers.get(4).strip().lower().startswith("y"):
    print(temp.format(*answers.values()))
else:
    print ("You are not aligible")

with open ("data.csv", "a")as f:
    f.write("\n", ", ".join(answers.values()))



