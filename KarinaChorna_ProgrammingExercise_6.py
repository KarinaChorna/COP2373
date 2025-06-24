# Karina Chorna
# Programming Exercise 6
# The purpose of this code is to determine if the phone number, SSN, and zip code the user entered are valid.

import re

# check if phone number is valid
def is_valid_phone(phone):
    pattern = re.compile(r'^(\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}$')
    return bool(pattern.match(phone))

# check if social security number is valid
def is_valid_ssn(ssn):
    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    return bool(pattern.match(ssn))

# check if zip code is valid
def is_valid_zip(zip_code):
    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    return bool(pattern.match(zip_code))

# prompt user to enter their information
def main():
    print("Please enter the following information:")

    phone = input("Phone Number: ")
    ssn = input("Social Security Number (SSN): ")
    zip_code = input("ZIP Code: ")

    # display the results
    print("\n--- Validation Results ---")
    print(f"Phone Number Is Valid: {'Yes' if is_valid_phone(phone) else 'No'}")
    print(f"SSN Is Valid: {'Yes' if is_valid_ssn(ssn) else 'No'}")
    print(f"ZIP Code Is Valid: {'Yes' if is_valid_zip(zip_code) else 'No'}")


if __name__ == "__main__":
    main()
