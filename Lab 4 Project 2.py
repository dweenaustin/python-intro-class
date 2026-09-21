import requests

# A Census API URL always has the shape:
# http://api.census.gov/data/{year}/{dataset}?get={variables}&for={geography}
YEAR = 2022
DATASET = "acs/acs5"
URL = f"https://api.census.gov/data/{YEAR}/{DATASET}"
API_KEY = "895e54d8e20447c1d81311b17fcd5697d917c604"

#ask user for state FIPS code
print("Census Population Lookup")
print("________________________")
print("Examples: "
      "12 = Florida, "
      "13 = Georgia, "
      "15 = Hawaii, "
      "53 = Washington")

state_code = input("Enter state FIPS code: ").strip()

# ask user to input variable(s)
print("Variable Examples:")
print("B01003_001E = Total Population")
print("B01001_002E = Male Population")
print("B01001_026E = Female Population")
print("NAME = State Name")
print("-------------------------------")

variables = input("Enter variable(s): ").strip()


# build API request
params = {
    "get": variables,
    "for": f"state:{state_code}",
    "key": API_KEY,
}

#send request
response = requests.get(URL, params=params)

# process response
data = response.json()

header = data[0]
row = data[1]

# display results
print("Results")
for i in range(0, len(row)):
    print(f"{header[i]}: {row[i]}")

