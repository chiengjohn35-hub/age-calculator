#using functions to check age with current year and birth year

#check year of birth
def year_of_birth(n):
    enter = int(input("enter the year of birth :"))
    if not enter.is_integer():
        raise ValueError("Please enter a valid number or digit!")
    if enter:
        age = n - enter
        print(f"Your are {age} years old")
        return enter

def main():
    while True:
        try:
            current_year = int(input("enter the current year:"))
            current_year = year_of_birth(current_year)
            break
        except ValueError:
            print("Please enter a valid number or digit!")

if __name__ == '__main__':
    main()