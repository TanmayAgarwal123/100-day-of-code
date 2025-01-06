import datetime

def calculate_age_in_weeks(birth_date):
    today = datetime.date.today()
    age_in_days = (today - birth_date).days
    age_in_weeks = age_in_days // 7
    return age_in_weeks

def main():
    print("Enter your date of birth (in YYYY-MM-DD format):")
    birth_date_input = input()
    
    try:
        birth_year, birth_month, birth_day = map(int, birth_date_input.split('-'))
        birth_date = datetime.date(birth_year, birth_month, birth_day)
        age_in_weeks = calculate_age_in_weeks(birth_date)
        print(f"You are approximately {age_in_weeks} weeks old.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")

if __name__ == "__main__":
    main()
