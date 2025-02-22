import random

# Taulukko, joka sisältää inspiroivia lainauksia
quotes = [
    "Don't watch the clock, do what it does. Stop thinking about how you are going to fail and start thinking about what you need to do right now!",
    "The only way to do great work is to love what you do.",
    "The biggest risk is not taking any risk.",
    "The best way to predict your future is to create it.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "You miss 100% of the shots you don't take.",
    "Believe you can and you're halfway there.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Success is walking from failure to failure with no loss of enthusiasm.",
    "Keep your eyes on the stars, and your feet on the ground.",
    "I have not failed. I've just found 10,000 ways that won't work.",
    "Do something today that your future self will thank you for.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "Keep going. Keep going. Keep going.",
    "The world needs people who are not afraid to take risks, who are not afraid to take the road less traveled.",
    "Do not let what you cannot do interfere with what you can do.",
    "In order to succeed, your desire for success should be greater than your fear of failure.",
    "The biggest adventure you can take is to live the life of your dreams.",
    "The biggest mistake you can make is to believe that you are working for somebody else when in fact, you are working for yourself.",
    "The best way to get started is to quit talking and begin doing.",
    "Do not let yesterday take up too much of today.",
    "The best revenge is massive success.",
    "The best way to get approval is not to need it.",
    "The biggest mistake you can make is to believe that you are working for somebody else when in fact, you are working for yourself.",
    "The biggest risk is not taking any risk.",
    "The best way to predict your future is to create it."
]

def main():
    response = input("Wanna hear a fortune? (yes/no): ")
    if response.lower() == 'yes' or response.lower() == 'y':
        random_index = random.randint(0, len(quotes) - 1)
        print(quotes[random_index])
    elif response.lower() == 'no' or response.lower() == 'n':
        print("Too bad, you filthy monkey!")
    else:
        print("Invalid response. Please try again.")

if __name__ == "__main__":
    main()
