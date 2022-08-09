import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_REPLY = "I am happy because I don't waste my time on idiots "
R_QUIET = "My creator is a loner so am I"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
    random.randrange(4)]
    return response