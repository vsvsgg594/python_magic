# Write a program that will ask the user the following question:
# Is Sydney the capital of Australia?

question=input("Is Sydney the capital of Australia? ")

if question.lower() == "y":
    print("That is correct, Sydney is the capital of Australia.")
elif question.lower() == "n":
    print("correct answers")
else:
    print("i dont know")
