# The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

# Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

# Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.

def tickets(people):
    amountOf25 = 0;
    amountOf50 = 0;
    amountOf100 = 0;
    for person in people:
        if person == 25:
            amountOf25 += 1
            continue
        if person == 50 and amountOf25 >= 1:
            amountOf50 += 1
            amountOf25 -= 1
            continue
        if person == 100 and amountOf25 >= 1 and amountOf50 >= 1:
            amountOf100 += 1
            amountOf25 -= 1
            amountOf50 -= 1
            continue
        if person == 100 and amountOf25 >= 3:
            amountOf25 -= 3
            continue
        return "NO"
    return "YES"
