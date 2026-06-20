def format_numbers(phone_number: str) -> str:
    numbers = list(filter(str.isdigit, phone_number))[1:]
    return "+7({}{}{}){}{}{}-{}{}-{}{}".format(*numbers)

phone_number = input()

refined=format_numbers(phone_number)    

print(refined)

