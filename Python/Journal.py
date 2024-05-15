def ask_questions():
    # Question 1
    while True:
        try:
            rating = int(input("How was your day? [1-5]: "))
            if 1 <= rating <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid integer.")

    # Questions 2-5
    good = input("What went well today?: ")
    not_well = input("What did not go well today?: ")
    learn = input("What did you learn today?: ")
    message = input("Any message to your future self?: ")

    # Printing the result
    print("\nSummary:")
    print(f"How was your day? [1-5]: {rating}")
    print(f"What went well today?: {good}")
    print(f"What did not go well today?: {not_well}")
    print(f"What did you learn today?: {learn}")
    print(f"Message to your future self?: {message}")

if __name__ == "__main__":
    ask_questions()
