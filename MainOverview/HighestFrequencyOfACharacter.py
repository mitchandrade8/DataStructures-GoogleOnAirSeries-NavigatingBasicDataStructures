
'''
    What type of data structure should we use we finding a value?
    or mapping a value?
'''

def find_highest_frequency(input_str):
    # initialize a dictionary to store character frequencies
    char_map = {}

    # Count frequency of each character in the given string
    for char in input_str:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map = 1
    
    # Initialize variables to track the character with the highest frequency
    max_frequency = -1
    letter_with_highest_frequency = None

    # Find the character with the highest frequency
    for char, frequency in char_map.items():
        if frequency > max_frequency:
            max_frequency = frequency
            letter_with_highest_frequency = char
    
    return letter_with_highest_frequency

def main():
    # Example 
    input_str1 = "hello world, let us see if python can track and display the most common letter in this string"

    # Call the function
    result = find_highest_frequency(input_str1)
    print("The character with the highest frequency in this string is: ", result)

main()
