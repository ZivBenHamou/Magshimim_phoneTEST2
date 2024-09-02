def letter_combinations(digits):
    # Mapping of digits to letters based on the telephone keypad
    phone_mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    # If the input is empty, return an empty list
    if not digits:
        return []

    # Recursive function to generate all possible combinations
    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return

        possible_letters = phone_mapping[digits[index]]

        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])

    return combinations

# Input from the user
user_input = input("Enter digits (2-9): ")
result = letter_combinations(user_input)
print("The possible combinations are:", result)
