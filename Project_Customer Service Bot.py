# Project: Customer Chat Bot

# Greeting - Thanks for contacting Tiny Space!

def greeting():
    name = input("Thanks for contacting Tiny Space! May I have your name? ").capitalize()
    print(f"Thanks, {name}!")
    return

# Inquiry Categories:
# Store Location and Hours
# Order Status: Elliot
# Issue with Order: Chrissa
# Design Services: Ramon
# Other: Trinity

def select_category():
    category = input("""Please select from one of the categories
below using the numbers 1 - 5.

[1] Store Hours & Locations 
[2] Status of Order
[3] Issue with Order
[4] Design Services
[5] Other """)

    if category == '1':
        store_location_hours()
        return

    if category == '2':
        order_status()
        return

    if category == '3':
        order_issue()
        return

    if category == '4':
        design_services()
        return

    if category == '5':
        other()
        return

    if category not in ['1', '2', '3', '4', '5']:
        select_category()


# Please select from one of the categories listed below using the numbers 1 - 5.
# If customer selects anthing other than 1 - 5, then bot returns customers to inquiry categories


# Store Location & Hours:
# 2300 Riverdale Lane, Boston, MA 02101
# Store Hours: Monday-Saturday from 10am. to 6pm.
# May I help you with anything else? If yes, then return to inquiry categories; else, "Thanks for contacting Tiny Space!"

def store_location_hours():
    location = "2300 Riverdale Lane, Boston, MA 02101"
    hours = "Monday - Saturday from 10AM to 6PM"
    print(f"Tiny Space is located at {location}. The store is open {hours}.")

    additional_question = input("May I help you with anything else? [Yes/No] ").lower()
    if additional_question == 'yes':
        select_category()
    elif additional_question == 'no':
        print("Thanks for contacting Tiny Space!")
    return

# Order Status

def order_status():
    print("Sure, I can help you with that. ")
    full_name = input("May I have the full name on the order? ")
    order_number = input("May I have the order number? ")
    transfer_Elliot()
    return

# Order Issues

def order_issue():
    print("I'm sorry that you're experiencing issues with your order. ")
    full_name = input("May I have the full name on the order? ")
    order_number = input("May I have the order number? ")
    issue = input("Could you please describe the issue with your order?   ")
    transfer_Chrissa()
    return

# Design Services

def design_services():
    print("I can definitely help you out with your design questions.")
    transfer_Ramon()
    return

# Other Inquiries

def other():
    transfer_Trinity()
    return

# Defining the Transfer Functions

def transfer_Elliot():
    print("Awesome! I'm checking the status of the order now.")
    return

def transfer_Chrissa():
    print("Thanks for providing that information. I'm looking into this now.")
    return

def transfer_Ramon():
    design_question = input("Tell me how I may be of assistance.  ")
    return

def transfer_Trinity():
    other_inquiry = input("No problem, please describe to me how I may be of assistance. ")
    return

# Call the functions to start the chat bot

greeting()
select_category()
