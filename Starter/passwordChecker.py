password = input("Enter password: ")


def strength(password):
    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for p in password:
        if p.isdigit():
            digit = True
    result["digit"] = digit

    upperCase = False
    for p in password:
        if p.isupper():
            upperCase = True
    result["upperCase"] = upperCase

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"


print(strength(password))
