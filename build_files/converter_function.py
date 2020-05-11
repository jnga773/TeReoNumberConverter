# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:35:26 2020

@author: Jacob
"""

def TeReoNumberConverter(input_number_str):
    """
    Reads an input integer from the console (less than 10 million) and converts
    the digits into Te Reo Māori.
    """
    # Read numerical input from console
    input_number_int = int(input_number_str)
    input_number_str = str(input_number_int)
    input_number_fill = input_number_str.zfill(12)
    # List of tens
    tens_str = [" rau piriona", " tekau piriona", " piriona",
                " rau miriona"," tekau miriona", " miriona",
                " rau mano", " tekau mano", " mano",
                " rau", " tekau", "mā"]
    # List of numbers from 0-9
    digits_str = ["kore", "kotahi", "rua", "toru", "whā", "rima", "ono",
                  "whitu", "waru", "iwa", "tekau"]

    # If input is less than 10, just print the number. Otherwise, go through
    # the long method
    if input_number_int <= 10:
        # If the ones digit is 1, print "tahi" instead of "kotahi"
        if input_number_int == 1:
            output = "tahi"
        else:
            output = str(digits_str[input_number_int])
    else:
        # Turn input string into list
        input_number_str_list = list(input_number_fill)
        # Create list where each element is int(input_number_str_list[i])
        nums_list = []
        # Create list where each element is the word for int(input_number_str_list[i])
        str_list = []
        for i in input_number_str_list:
            nums_list.append(int(i))
            if int(i) != 0:
                str_list.append(digits_str[int(i)])
            else:
                str_list.append("")
        # Create a list for the placeholders to be printed
        out_tens = []
        # Cycle through elements in nums_list. If element is 0, append "" to out_tens,
        # otherwise, append the tens placeholder
        for element, number in enumerate(nums_list):
            if number == 0:
                out_tens.append("")
            else:
                out_tens.append(tens_str[element])
        # Cycle through str_list to see if commas are needed
        commas = []
        for element, number in enumerate(nums_list[:-1]):
            if number == 0:
                # No number so comma is not needed
                commas.append("")
            else:
                # Cycle through the rest of the list (excluding the ones column)
                # and check if there is any non-zero between current number
                # and the ones column
                check = False
                for i in nums_list[element+1:-1]:
                    if i == 0:
                        # The element is 0 so set check = True. Comma not needed
                        check = True
                    else:
                        check = False
                        break
                if check is True:
                    commas.append("")
                else:
                    commas.append(", ")
        del check
        # Append "" for tens (no comma needed)
        # commas.append("")
        # If the ones column is 0, mā not needed, otherwise append mā
        if nums_list[-1] == 0:
            commas.append("")
        else:
            commas.append(" mā ")
        # Split output_string into different components for each tens
        output = ""
        for element, number in enumerate(nums_list[:-2]):
            if number != 0:
                output += "{}{}{}".format(str_list[element], out_tens[element], commas[element])
            else:
                output += ""
        # Tens
        if nums_list[-2] != 0:
            # If the tens digit is 1, print nothing, instead of "kotahi tekau"
            if nums_list[-2] == 1:
                output += "tekau"
            else:
                output += "{}{}".format(str_list[-2], out_tens[-2])
        else:
            output += ""
        # Ones
        if nums_list[-1] != 0:
            # If the ones digit is 1, print "tahi" instead of "kotahi"
            if nums_list[-1] == 1:
                output += "{}tahi".format(commas[-1])
            else:
                output += "{}{}".format(commas[-1], str_list[-1])
    # Return output
    return output

def main():
     # Read numerical input from console
    while True:
        input_number_str = input("Input whole number (less than 1 trillion): ")
        try:
            input_number_int = int(input_number_str)
            del input_number_int
            break
        except ValueError:
            print("Not a whole number. Please try again")
    output = TeReoNumberConverter(input_number_str)
    print("In Te Reo Māori, {} is: {}!".format(input_number_str, output))
    
if __name__ == "__main__":
    main()