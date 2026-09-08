
heart_rate_samples = {
"J. Alvarez": [72, 75, 78],
"M. Chen": [80, 82],
"R. Okafor": [65, 68, 70, 66],
"S. Patel": [90, 95, 92, 88, 91],
"T. Nguyen": [77, 79],
"L. Kowalski": [68, 70, 69],
"D. Osei": [98, 101, 95, 99],
"A. Whitfield": [74, 76, 75, 73],
}


#created a list to assign the patients a number
patient_number = list(enumerate(heart_rate_samples.keys(), start=0))
print(patient_number)

def get_patient_name(number):
    number = int(input("Enter patient number: "))
    return patient_number[number]
print(get_patient_name(patient_number))



data_type = input("Which data type? 1. All Data, 2. Max, 3. Min")
if data_type == "1":
        heart_rate = input("0: [72, 75, 78], 1: [80, 82], 2: [65, 68, 70, 66], 3: [90, 95, 92, 88, 91], 4: [77, 79], 5:[68, 70, 69], 6: [98, 101, 95, 99], 7: [74, 76, 75, 73]")
if data_type == "2":
        heart_rate = input("0: [78], 1: [82], 2: [70], 3: [95], 4:[79], 5: [70], 6: [101], 7: [76]")
if data_type == "3":
        heart_rate = input("0: [72], 1: [80], 2: [65], 3: [88], 4: [77], 5:[68], 6: [95], 7: [73] ")
else:
    print("MISSING!")













