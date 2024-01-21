from datetime import date, datetime, timedelta


# import datetime

def get_birthdays_per_week(users):
    def date_next_monday():
        res_date = date.today()
        one_day = timedelta(days=1)

        for i in range(8):
            if res_date.weekday() != 0:
                res_date += one_day
            else:
                break

        return res_date

    if not users:
        print("_" * 25)
        print("The list of users is empty")
        return {}

    date_monday = date_next_monday()

    today = date.today()
    one_weeks_interval = timedelta(weeks=1)
    date_next_week = today + one_weeks_interval

    print("_" * 25)
    print(today)
    print(date_next_week)
    print(users)

    res_dict = {}
    count = 0

    for user in users:

        birthday = user.get("birthday")
        name = user.get("name")

        birthday_this_year = birthday.replace(year=today.year)

        if today.year != date_next_week.year and birthday_this_year.month == 1:
            birthday_this_year = birthday.replace(year=today.year + 1)

        if birthday_this_year < today:
            count += 1

            if len(users) == count:
                print("Everyone's birthday has already passed this year")
                return {}

        if today <= birthday_this_year <= date_next_week:
            str_weekday = birthday_this_year.strftime('%A')

            if str_weekday not in res_dict:
                res_dict[str_weekday] = []

            res_dict[str_weekday].append(name)

        if birthday_this_year < date_monday:

            if "Saturday" in res_dict:
                if "Monday" not in res_dict:
                    res_dict["Monday"] = []

                res_dict["Monday"].extend(res_dict.get("Saturday"))
                res_dict.pop("Saturday")

            if "Sunday" in res_dict:
                if "Monday" not in res_dict:
                    res_dict["Monday"] = []

                res_dict["Monday"].extend(res_dict.get("Sunday"))
                res_dict.pop("Sunday")

    print(f">>>>>>Result: {res_dict}<<<<<<")
    return res_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        # {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
        # {"name": "Test 20", "birthday": datetime(2000, 1, 20).date()},
        # {"name": "Test 21", "birthday": datetime(2000, 1, 21).date()},
        # {"name": "Test 22", "birthday": datetime(2000, 1, 22).date()},
        # {"name": "Test 23", "birthday": datetime(2000, 1, 23).date()},
        # {"name": "Test 24", "birthday": datetime(2000, 1, 24).date()},
        # {"name": "Test 25", "birthday": datetime(2000, 1, 25).date()},
        # {"name": "Test 26", "birthday": datetime(2000, 1, 26).date()},
        # {"name": "Test 27", "birthday": datetime(2000, 1, 27).date()},
        # {"name": "Test 28", "birthday": datetime(2000, 1, 28).date()},
        # {"name": "Test 29", "birthday": datetime(2000, 1, 29).date()},
        # {"name": "Test 30", "birthday": datetime(2000, 1, 30).date()},
        # {"name": "Test 31", "birthday": datetime(2000, 1, 31).date()},
    ]

    result = get_birthdays_per_week(users)
    # print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print("Test: ")
        print(f"{day_name}: {', '.join(names)}")
