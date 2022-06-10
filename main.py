from random import randint, choice


def randCardNumber():
    result = str(randint(1, 9))
    for i in range(15):
        result += str(randint(0, 9))
    return str(result)


def getRandDateTime():
    datetime = "2022:05:" + str(randint(5, 15)) + ":"
    datetime += str(randint(8, 22)) + ":" + choice(["00", "15", "30", "45"]) + ":00"
    return datetime


def getRandPhoneNum():
    return str(randint(1000000000, 9999999999))


if __name__ == "__main__":
    with open("seats.txt", "w") as seats:
        for i in range(1, 11):
            for j in range(1, 11):
                seats.write("(1, " + str(i) + ", " + str(j) + "),\n")

        for i in range(1, 13):
            for j in range(1, 11):
                seats.write("(2, " + str(i) + ", " + str(j) + "),\n")

        for i in range(1, 11):
            for j in range(1, 16):
                seats.write("(3, " + str(i) + ", " + str(j) + "),\n")

    with open("customers.txt", "w") as customers:
        customers.write("('Oliver Smith', " + randCardNumber() + "),\n")
        customers.write("('Charlotte Johnson', " + randCardNumber() + "),\n")
        customers.write("('Declan Williams', " + randCardNumber() + "),\n")
        customers.write("('Aurora Brown', " + randCardNumber() + "),\n")
        customers.write("('Willow Jones', " + randCardNumber() + "),\n")
        customers.write("('Theodore Garcia', " + randCardNumber() + "),\n")
        customers.write("('Ezra Miller', " + randCardNumber() + "),\n")
        customers.write("('Rowan Davis', " + randCardNumber() + "),\n")
        customers.write("('Violet Rodriguez', " + randCardNumber() + "),\n")
        customers.write("('Jasper Martinez', " + randCardNumber() + "),\n")
        customers.write("('Hazel Hernandez', " + randCardNumber() + "),\n")
        customers.write("('James Lopez', " + randCardNumber() + "),\n")
        customers.write("('Silas Gonzales', " + randCardNumber() + "),\n")
        customers.write("('Luna Wilson', " + randCardNumber() + "),\n")
        customers.write("('Quinn Anderson', " + randCardNumber() + "),\n")
        customers.write("('Liam Thomas', " + randCardNumber() + "),\n")
        customers.write("('Asher Thomas', " + randCardNumber() + "),\n")
        customers.write("('Aria Taylor', " + randCardNumber() + "),\n")
        customers.write("('Kai Moore', " + randCardNumber() + "),\n")
        customers.write("('Finn Jackson', " + randCardNumber() + "),\n")
        customers.write("('Owen Martin', " + randCardNumber() + "),\n")

    with open("prices.txt", "w") as prices:
        for i in range(12):
            prices.write(str(randint(5, 15)) + "." + str(randint(0, 99)) + "\n")

    with open("showing.txt", "w") as showing:
        for i in range(20):
            showing.write("(" + str(randint(1, 13)) + ", " + str(randint(1, 4)) + ", '" + getRandDateTime() + "'),\n")

    with open("employees.txt", "w") as employees:
        employees.write("('Ethan Lee', " + getRandPhoneNum() + ", 30, NULL),\n")
        employees.write("('Isla Perez', " + getRandPhoneNum() + ", 20, 1),\n")
        employees.write("('Luca Thompson', " + getRandPhoneNum() + ", 20, 1),\n")
        employees.write("('Alexander White', " + getRandPhoneNum() + ", 10, 2),\n")
        employees.write("('Ivy Harris', " + getRandPhoneNum() + ", 10, 2),\n")
        employees.write("('Sage Sanchez', " + getRandPhoneNum() + ", 10, 2),\n")
        employees.write("('Felix Clark', " + getRandPhoneNum() + ", 10, 2),\n")
        employees.write("('Freya Ramirez', " + getRandPhoneNum() + ", 10, 3),\n")
        employees.write("('Harper Lewis', " + getRandPhoneNum() + ", 10, 3),\n")
        employees.write("('Henry Robinson', " + getRandPhoneNum() + ", 10, 3),\n")
        employees.write("('Nora Walker', " + getRandPhoneNum() + ", 10, 3),\n")

    with open("bookings.txt", "w") as bookings:
        for i in range(1, 21):
            for j in range(randint(1, 3)):
                bookings.write("(" + str(i) + ", " + str(randint(1, 20)) + ", " + str(randint(1, 370)) + "),\n")