def main():
    age = int(input("How old are you: "))
    year = int(input("What year is it: "))
    year_turn_100 = calculate_year_turn_100(age, year)
    print(f"You will turn 100 in the year {year_turn_100}.")

def calculate_year_turn_100(age, year):
    return year + (100 - age)

main()
