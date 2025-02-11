
score = 0


questions = ["1. What is the full meaning of ECOWAS", 
                "2. SQI is which type of school?", 
                "3. Who is the president of Nigeria?", 
                "4. Python is a ____ language?", 
                "5. How many states do we have in Nigeria?"]


options = ["a. Economic Community of West African States \nb. Economic Common Wealth And Sales \nc. Economic Common Wealth of West African States",
            "a. Business School \nb. Coding School \nc. Army School", 
            "a. President Muhammad Buhari \nb. Prof. Yemi Osinbajo \nc. Bola Ahmed Tiubu",
            "a. progamming language \nb. igbo language \nc. traditional language",
            "a. 36 \n b. 37 \n c. 38"]

answer = ["c", "b", "c", "a", "a"]


for i, question in enumerate(questions):
    print(question)
    print(options[i])

    user_answer = input("Choose the answer (a - c): ").lower().strip()

    if user_answer == answer[i]:
        print("You are correct!")
        score += 10
    
    else:
        print("Wrong answer!")
    





print(f"Your total Score = {str(score)}")

