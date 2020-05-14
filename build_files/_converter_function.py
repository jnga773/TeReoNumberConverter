# -*- coding: utf-8 -*-
"""
Created on Thu May 14 14:11:25 2020

@author: Jacob
"""

def _ones_translator(_input_element, place="more than ten"):
    """
    Takes a single-digit number as an input and converts it into a string
    corresponding to the Te Reo Māori word for that number.
    """
    Te_Reo_Numbers = ["kore", "tahi", "rua", "toru",
                      "whā", "rima", "ono", "whitu",
                      "waru", "iwa", "tekau"]
    if place == "more than ten":
        Te_Reo_Numbers[0] = ""
        Te_Reo_Numbers[1] = "kotahi"
        # Add spacing for tens placeholder
        for i in range(len(Te_Reo_Numbers[1:])):
            Te_Reo_Numbers[i] = Te_Reo_Numbers[i] + " "
    if place == "ten":
        Te_Reo_Numbers[1] = ""
    if place == "ones":
        Te_Reo_Numbers[1] = "tahi"
    return Te_Reo_Numbers[_input_element]        

def _hundreds_translator(_input_int, hundreds_check=False):
    """
    Splits number into three-column list.:
        [[hundreds], [tens], [columns]],
    and converts number into Te Reo Māori.
    """
    # Pad _input_int with zeros if < 100
    _input_str = str(_input_int).zfill(3)
    # Turn string into a list
    _input_list = list(_input_str)
    # turn each element back into an integer
    for i in range(len(_input_list)):
        _input_list[i] = int(_input_list[i])
    # Cycle through _input_list and convert each number into Te Reo, adding to
    # output string
    _hundreds_translator_output = ""
    if _input_list[0] != 0:
        # Hundreds column
        _hundreds_translator_output += "{}rau".format(_ones_translator(_input_list[0]))
    if _input_list[1] != 0:
        # Check if tens column is one. If so, then set just_ten to True
        if _input_list[1] == 1:
            place = "ten"
        else:
            place = "more than ten"
        # Tens column
        if _input_list[0] == 0:
            # No hundreds so don't space
            _hundreds_translator_output += "{}tekau".format(_ones_translator(_input_list[1], place))
        else:
            # Include space
            _hundreds_translator_output += ", {}tekau".format(_ones_translator(_input_list[1], place))
    if _input_list[2] != 0:
        # Check if this set of numbers is for the hundreds/tens/ones column
        if hundreds_check is True:
            place = "ones"
        else:
            place = "more than ten"
        # Ones column
        if _input_list[0] == 0 and _input_list[1] == 0:
            # Only a ones column so don't need "mā" in front of ones
            _hundreds_translator_output += "{}".format(_ones_translator(_input_list[2], place))
        else:
            # either a hundred or a ten so add "mā"
            _hundreds_translator_output += " mā {}".format(_ones_translator(_input_list[2], place))
    return _hundreds_translator_output

def TeReoNumberConverter(input_number_str):
    """
    Reads an input integer from the console (less than 10 million) and converts
    the digits into Te Reo Māori.
    """
    # Read numerical input from console
    input_number_int = int(input_number_str)
    input_number_str = str(input_number_int)
    # Pad string with zeros up to a billion
    input_number_str = input_number_str.zfill(10)
    # Special case if input is zero
    if input_number_int == 0:
        output_str = "kore"
    else:
        # Split input number into 4 columns of three numbers:
        #   billions, millions, thousands, hundreds/tens/ones.
        # Billions
        billions_str = input_number_str[0]
        billions_int = int(billions_str)
        # Millions
        millions_str = "".join([input_number_str[1], input_number_str[2], input_number_str[3]])
        millions_int = int(millions_str)
        # Thousands
        thousands_str = "".join([input_number_str[4], input_number_str[5], input_number_str[6]])
        thousands_int = int(thousands_str)
        # Hundreds/tens/ones
        hundreds_str = "".join([input_number_str[7], input_number_str[8], input_number_str[9]])
        hundreds_int = int(hundreds_str)
        # Go through each column and, if the number is not zero, update output_str
        output_str = ""
        if billions_int != 0:
            output_str += "{}piriona".format(_hundreds_translator(billions_int))
        if millions_int != 0:
            if billions_int == 0:
                # No billion number, so don't need comma
                output_str += "{}miriona".format(_hundreds_translator(millions_int))
            else:
                # Need comma
                output_str += ", {}miriona".format(_hundreds_translator(millions_int))
        if thousands_int != 0:
            if billions_int == 0 and millions_int == 0:
                # No billion or million number, so don't need comma
                output_str += "{}mano".format(_hundreds_translator(thousands_int))
            else:
                # Need comma
                output_str += ", {}mano".format(_hundreds_translator(thousands_int))
        if hundreds_int != 0:
           if billions_int == 0 and millions_int == 0 and thousands_int == 0:
               # No billion, million or thousand number, so don't need comma
               output_str += "{}".format(_hundreds_translator(hundreds_int, hundreds_check=True))
           elif hundreds_int < 10:
               # No comma, just add mā
               output_str += " mā {}".format(_hundreds_translator(hundreds_int, hundreds_check=True))
           else:
               # Need comma
               output_str += ", {}".format(_hundreds_translator(hundreds_int, hundreds_check=True))
    # Return output
    return output_str
    
        
def main():
    """
    Read numerical input from console
    """
    while True:
        input_number_str = input("Input whole number (less than 1 trillion): ")
        try:
            input_number_int = int(input_number_str)
            break
        except ValueError:
            print("Not a whole number. Please try again")
    output = TeReoNumberConverter(input_number_str)
    print("In Te Reo Māori, {:,d} is: {}!".format(input_number_int, output))

if __name__ == "__main__":
    main()