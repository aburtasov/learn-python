def create_record(name,telephone,address):
    """Create Record"""
    
    record = {
        'name':name,
        'phone':telephone,
        'address': address
    }
    return record

user1 = create_record("Vasya","+79122434234","Canada")
user2 = create_record("Petya","+7923122421","USA")

print(user1)
print(user2)

#------------------------------------------------------
def give_award(medal,*persons):
    """Give Medals to persons"""
    for person in persons:
        print("Tovarish " + person.title() + " nagrazhdaetsa medal " + medal)


give_award("Za Berlin", "Vasya", "Petya")
give_award("Za London", "Vasya", "Petya")