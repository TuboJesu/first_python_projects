
total_scores = 0

def answer_verification(theory_answer, current_keywords_and_points):
    global total_scores

    score = 0
    temp_answer_store = []

    for keyword in theory_answer:
        answer_verification_list = []
        if keyword in current_keywords_and_points:
            if keyword not in temp_answer_store:
                points = current_keywords_and_points[keyword]
                temp_answer_store.append(keyword)
                answer_verification_list.append(keyword)
                score += points

    for first_index in range(len(theory_answer)):
            for next_index in range(first_index + 1, len(theory_answer) + 1):
                phrase =  " ".join(theory_answer[first_index:next_index])          
                if phrase in current_keywords_and_points and phrase not in temp_answer_store:  
                    points = current_keywords_and_points[phrase]
                    score += points
    
    total_scores += score

    print(f" Your current answer has been graded and it scored {score}")
    return ""

def main_operation():
    question_and_keywords= {
        "1. Explain the process of photosynthesis": {"photosynthesis": 2, "light energy": 1, "chemical energy": 1, "chloroplasts": 2, "chlorophyll": 1, "carbon dioxide": 1, "water": 1, "glucose": 1, "oxygen": 1, "atp": 1},

        "2. What is the water cycle?": {"water cycle": 1, "evaporation": 2, "condensation": 2, "precipitation": 2, "oceans": 1, "atmosphere": 1, "transpiration": 1, "runoff": 2},

        "3. Explain photosynthesis in plants": {"photosynthesis": 2, "sunlight": 2, "chemical energy": 2, "chlorophyll": 2, "carbon dioxide": 1, "water": 1, "glucose": 1, "oxygen": 1},

        "4. What are tectonic plates?": {"tectonic plates": 1, "lithosphere": 2, "earthquakes": 1, "volcanic activity": 2, "mountain formation": 1, "continental drift": 2},

        "5. Describe the process of cellular respiration": {"cellular respiration": 1, "glucose": 2, "energy": 1, "atp": 2, "mitochondria": 2, "oxygen": 1, "nutrients": 1}
    }


    print('''

    Welcome to the exam wizard where you will have 5 theory questions to answer, and remember that there are points allocated for each keyword found in your answer!!!

    ''')

    print()

    for question, keywords in question_and_keywords.items():
        print(question)
        current_k_and_w = keywords
        user_answer = input("Enter your answer to the question: ").lower().replace(",", "")
        cleaned_answer = user_answer.replace(".", "").split()
        print(answer_verification(cleaned_answer, current_k_and_w))

    print(f"Exam completed and your total scores is {total_scores}")

main_operation()