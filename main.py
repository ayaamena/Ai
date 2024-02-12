print("Welcome to the Pulmonary Embolism Preliminary Screening")
print("Please answer the following questions with 'yes' or 'no'.")

questions = [
    "Do you experience sudden shortness of breath?",
    "Do you feel chest pain that worsens with a deep breath or cough?",
    "Do you cough up blood?",
    "Do you feel lightheaded or dizzy?",
    "Do you experience rapid pulse?",
    "Do you have a cough, possibly with bloody mucus?",
    "Do you have swelling or pain in one leg?",
    "Do you have excessive sweating?",
    "Do you have fever?",
    "Do you feel a sense of anxiety or nervousness?",
    "Do you have blue lips or nails?",
    "Do you experience sharp or stabbing chest pain?",
    "Do you have a history of blood clots?",
    "Do you have a history of recent surgery or prolonged immobility?",
    "Do you have a history of cancer?",
]

yes_answers = 0

for question in questions:
    answer = input(question + " ").lower()
    if answer == 'yes':
        yes_answers += 1

if yes_answers >= 5:
    print("Based on your answers, it's recommended to seek medical attention immediately.")
else:
    print("Based on your answers, you may not be at high risk, but consulting a healthcare professional is advisable.")