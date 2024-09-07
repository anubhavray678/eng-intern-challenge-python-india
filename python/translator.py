
import sys

# Corrected Braille-to-English dictionary with unique entries
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", ".....O": "capital", "......O": "number",  # Correct special indicators
    ".O.....": "1", ".O.O...": "2", ".OO....": "3", ".OO.O..": "4", ".O..O..": "5",
    ".OOO...": "6", ".OOOO..": "7", ".O.OO..": "8", "..OO...": "9", "..OOO..": "0"
}

# English-to-Braille dictionary
english_to_braille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", "1": ".O.....", "2": "OOO.O.", "3": ".OO....", "4": ".O.OOO",
    "5": ".O..O..", "6": ".OOO...", "7": ".OOOO..", "8": ".O.OO..", "9": "..OO...",
    "0": "..OOO..", " ": "........", "capital": ".....O", "number": "......O"
}

def detect_input_type(input_str):
    # Check if the input contains only Braille characters
    if all(c in ['O', '.', ' '] for c in input_str):
        return "braille"
    else:
        return "english"

def braille_to_text(braille_str):
    words = braille_str.split(' ')
    result = []
    capital_next = False
    number_next = False

    for word in words:
        chars = [word[i:i+6] for i in range(0, len(word), 6)]
        word_result = ""

        for char in chars:
            if char == ".....O":
                capital_next = True
                continue
            if char == "......O":
                number_next = True
                continue

            # Debugging: print each Braille character and its mapping
            if char not in braille_to_english:
                
                word_result += "?"  # Handle unknown Braille patterns
                continue

            if capital_next:
                word_result += braille_to_english[char].upper()
                capital_next = False
            elif number_next:
                word_result += braille_to_english[char]
                number_next = False
            else:
                word_result += braille_to_english[char]

        result.append(word_result)

    return ' '.join(result)

def text_to_braille(text_str):
    result = []

    for char in text_str:
        if char.isupper():
            result.append(english_to_braille["capital"])
            result.append(english_to_braille[char.lower()])
        elif char.isdigit():
            result.append(english_to_braille["number"])
            result.append(english_to_braille[char])
        elif char == ' ':
            result.append(english_to_braille[" "])
        else:
            result.append(english_to_braille.get(char, "?"))  # Handle unknown characters

    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        print("Please provide input to translate.")
        return

    input_str = " ".join(sys.argv[1:])  # concatenate all arguments with spaces
    input_type = detect_input_type(input_str)

    if input_type == "braille":
        print(braille_to_text(input_str))
    else:
        print(text_to_braille(input_str))

if __name__ == "__main__":
    main()
