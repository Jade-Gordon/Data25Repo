# Control flow examples

"""
Managing film certifications
if age is under 12 years -> U, PG, and 12 films are available
if age is under 15 years -> U, PG, 12, and 15 films are available
if age is 18+ years -> all films are available
"""
customer_age = 18

if customer_age <= 12:
    print('U, PG, and 12 films are available')
elif customer_age <= 15:
    print('U, PG, 12, and 15 films are available')
else:
    print('All films are available')

"""
Chatbot greetings
Between 05:00-12:00 -> "Good morning"
Between 12:00-18:00 -> "Good afternoon"
Between 18:00-00:00 -> "Good evening"
"""

time_of_day = 6

if time_of_day > 5 and time_of_day < 12:
    print('Good morning')
elif time_of_day > 12 and time_of_day < 18:
    print('Good afternoon')
else:
    print('Good evening')

# Nested if statement
x = 44

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
else:
    print("Not above 10")