# Use the following 5 profiles to construct a script that does the following:
# Encrypts the data using symmetrical encryption from the AnonyMate anonymizer function upon user request
# Allows the user to query any of the following profile specifics:
# Name
# DoB
# Sex
# Blood Type ('blood_group')

from decimal import Decimal
import datetime


profiles = [{'job': 'Agricultural engineer',
             'company': 'Phillips-Johnson',
             'ssn': '055-51-3629',
             'residence': '1107 Brian Coves\nSouth Jessica, UT 66862',
             'current_location': (Decimal('-81.6575675'), Decimal('111.794874')),
             'blood_group': 'B+',
             'website': ['https://hurley.com/', 'http://www.baker.info/', 'http://silva-jones.com/', 'https://www.mathews.com/'],
             'username': 'nnelson',
             'name': 'Oscar Newman',
             'sex': 'M',
             'address': '2574 Scott Manors\nPort Aprilfort, MI 13337',
             'mail': 'wgraham@hotmail.com',
             'birthdate': datetime.date(1927, 1, 19)},

            {'job': 'Engineer, civil (consulting)',
             'company': 'Guzman Inc',
             'ssn': '457-09-3674',
             'residence': '8014 Lambert Ways Apt. 285\nSouth Briannaside, KS 13217',
             'current_location': (Decimal('61.686331'), Decimal('-42.036583')),
             'blood_group': 'A-',
             'website': ['http://gregory-martin.org/', 'http://tanner.org/', 'https://www.carr.org/'],
             'username': 'lking',
             'name': 'Jeremy Wilson',
             'sex': 'M',
             'address': '9375 Thomas Alley Suite 536\nNorth Darren, AZ 22956',
             'mail': 'hdeleon@hotmail.com',
             'birthdate': datetime.date(1996, 10, 12)},

            {'job': 'Information officer',
             'company': 'Green Inc',
             'ssn': '230-42-2169',
             'residence': 'Unit 6625 Box 0858\nDPO AE 52466',
             'current_location': (Decimal('-78.802646'), Decimal('-47.996111')),
             'blood_group': 'A-',
             'website': ['https://www.watkins.com/', 'http://johnson.org/'],
             'username': 'timothycastro',
             'name': 'Kenneth Rhodes',
             'sex': 'M',
             'address': '7994 Pearson Square\nHannahmouth, FM 16699',
             'mail': 'sonya72@hotmail.com',
             'birthdate': datetime.date(2003, 6, 15)},

            {'job': 'Contracting civil engineer',
             'company': 'Smith-Williamson',
             'ssn': '796-76-1297',
             'residence': '0041 Brittany Mountains\nNorth Harryshire, MN 69202',
             'current_location': (Decimal('66.422320'), Decimal('107.124001')),
             'blood_group': 'AB+',
             'website': ['http://www.nolan.com/'],
             'username': 'debraphillips',
             'name': 'Nicole Richardson',
             'sex': 'F', 'address': '303 Wong Trafficway Suite 883\nLake Kiara, MN 78039',
             'mail': 'andrew33@gmail.com',
             'birthdate': datetime.date(2003, 9, 7)},

            {'job': 'Engineer, technical sales',
             'company': 'Moody-Meza',
             'ssn': '574-63-6422',
             'residence': '74438 Moore Fall\nSouth Andrew, GA 64257',
             'current_location': (Decimal('38.089195'), Decimal('35.459581')),
             'blood_group': 'A+',
             'website': ['https://brooks-moore.com/'],
             'username': 'xlewis',
             'name': 'Gary Gamble',
             'sex': 'M',
             'address': '9929 Henderson Branch Suite 961\nLake Mary, AL 36478',
             'mail': 'ambercordova@yahoo.com',
             'birthdate': datetime.date(1968, 8, 19)}]


from faker import Faker
from anonymate.anonymizer import Anonymizer

fake = Faker()
anonymizer = Anonymizer

# Assign profile number
def get_profile_number(profiles_number):

    profiles_number = 1

    for name in profiles:
        if profiles_number == profiles_number:
            return name

        profiles_number = profiles_number + 1

profiles_number = int(input("Enter profile number (1-5): "))



# Retrieving specific patient data
def print_specific_data(*args):
    profiles_number = args[0]
    profile_specifics = args[1]

    patient_data = get_profile_number(profiles_number)

    if profile_specifics == 1:
        print("name:", patient_data['name'])

    elif profile_specifics == 2:
        print("birthdate:", patient_data['birthdate'])

    elif profile_specifics == 3:
        print("sex:", patient_data['sex'])

    elif profile_specifics == 4:
        print("blood_group:", patient_data['blood_group'])

    else:
        print("Error: Invalid Selection")



print("Profile specifics:")
print("1:name")
print("2:birthdate")
print("3:sex")
print("4:blood_group")

profile_specifics = int(input("Enter profile specifics (1-4): "))

print_specific_data(profiles_number, profile_specifics)



