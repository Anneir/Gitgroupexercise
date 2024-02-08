def main():
    while True:
        start_or_not = input("Do you wanna start the game? (Yes/No)")

        correct_amount = 0
        print("Answer the following questions:")

        if start_or_not == "Yes":
            q1 = int(input("105 + 40 = ?"))
            if q1 == 145:
                correct_amount += 1
            q2 = int(input("30 + 83 = ?"))
            if q2 == 113:
                correct_amount += 1
            q3 = input("Onko Filippiineillä lämmin? (Kyllä/Ei)")
            if q3 == "Kyllä":
                correct_amount += 1

            
