def create_record(name, telephone, address):
    """"Create Record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record


userOne = create_record("Vasya", "+7484234234", "Moscow")
userTwo = create_record("Petya", "+7484543534234", "SaintP")

print(userOne)
print(userTwo)


def give_award(medal, *persons):
    """Give Medal To Persons"""
    for person in persons:
        print("TOVARISH: " + person.title() + " nagrazhdayetsya medalyu " + medal)


give_award("Za Berlin", "vasya", "petya")