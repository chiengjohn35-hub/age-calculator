#using functions to check age with current year and birth year

# #check year of birth
def validate_age(current_year, birth_year):
    if birth_year > current_year or birth_year <1900:
        print("INVALID YEAR!")
    return  current_year-birth_year


def main():
    while True:
        try:
            current_year = int(input("Enter the current year :"))
            birth_year = int(input("Enter your birth year :"))

            value = validate_age(current_year,birth_year)
            print(f"You are {value} years old")
            break
        except ValueError as  e:
            print(f"Error: {e}, please try again!.")

if __name__=="__main__":
    main()

