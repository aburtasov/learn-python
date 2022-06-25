def days_to_units(number_of_days,units):
    if units == "hours":
       return f"{number_of_days} days are {number_of_days * 24} {units}"
    elif units == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} {units}"
    else:
        return "unsupported unit"
  
    
def validate_and_exec(days_and_unit_dictionary):
    
    try:
        
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            print(days_to_units(user_input_number,days_and_unit_dictionary["unit"]))
        elif user_input_number == 0:
             print("you entered a zero!")
        else:
            print("negative number!")
        
    except ValueError:
        print("input is not a valid!")
        
        
user_input_message = "Enter a number!:\n"