#!/usr/bin/env python

###############################################################################
# IMPORTS 
###############################################################################

import math
import secrets
import sys
from word_list import wordlist

###############################################################################
# CALCULATE ENTROPY 
###############################################################################

def calc_passphrase_entropy(word_count, digit_count):
    """
    Calculate passphrase entropy.
    """

    word_entropy_bits = word_count * math.log2(len(wordlist))
    digits_entropy_bits = digit_count * math.log2(10)

    passphrase_entropy_bits = word_entropy_bits + digits_entropy_bits

    return passphrase_entropy_bits

###############################################################################
# MAIN: PASSWORD GENERATOR 
###############################################################################

def main(_):
    """
    Generate a random passphrase consisting of some common words and a
    few digits.
    """

    word_count = 4
    digit_count = 2
    
    # Choose random words from the word list.
    random_words = []
    for _ in range(word_count):
        random_index = secrets.randbelow(len(wordlist))
        random_words.append(wordlist[random_index])

    # Choose random digits.
    random_digits = []
    for _ in range(digit_count):
        random_digits.append(str(secrets.randbelow(10)))

    # Display the random passphrase.
    random_passphrase = ' '.join(random_words + random_digits)
    print(random_passphrase, flush=True)

    # Display the amount of entropy in the passphrase.
    passphrase_entropy_bits = calc_passphrase_entropy(
        word_count=word_count, digit_count=digit_count
    )
    print(passphrase_entropy_bits, flush=True)

    return 0

# Check if the script was run from the command line.
if __name__ == "__main__":
    return_code = main(sys.argv[1:])
    sys.exit(return_code)
