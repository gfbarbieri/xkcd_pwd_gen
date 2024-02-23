#!/usr/bin/env python

###############################################################################
# IMPORTS 
###############################################################################

import math
from xkcd_pwd_gen.main import calc_passphrase_entropy

###############################################################################
# TESTS 
###############################################################################

def test_entropy_with_known_values():
    """
    Test the entropy calculation with known values.

    This test verifies that the entropy calculation function works as expected
    by comparing the output against manually calculated entropy values.
    Ensuring accurate entropy calculation is crucial for the security of the
    passphrase, as it directly relates to how resistant the passphrase is
    against brute-force attacks.
    """

    # Assume a word list of 2048 words and 2 digits, typical values for a
    # secure passphrase.
    word_count = 4
    digit_count = 2

    expected_entropy = (
        word_count * math.log2(2048) +
        digit_count * math.log2(10)
    )
    
    # Calculate entropy using the function.
    calculated_entropy = calc_passphrase_entropy(word_count, digit_count)
    
    # Assert that the calculated entropy matches the expected value.
    assert (
        math.isclose(calculated_entropy, expected_entropy, rel_tol=1e-9),
        "Entropy calculation should match expected value for known input sizes."
    )

def test_entropy_increasing_with_word_count():
    """
    Test that entropy increases as the number of words increases.

    This test checks that adding more words to the passphrase increases its
    entropy, which is expected as each additional word adds more complexity and
    randomness to the passphrase. Increasing the passphrase's entropy enhances
    its security by making it harder to guess or brute-force.
    """

    # Keep the number of digits constant to isolate the variable being tested.
    digit_count = 2  
    lower_word_count = 4
    higher_word_count = 6

    # Calculate entropy using the function.
    lower_entropy = calc_passphrase_entropy(lower_word_count, digit_count)
    higher_entropy = calc_passphrase_entropy(higher_word_count, digit_count)

    # Assert that entropy is higher when more words are used.
    assert (
        higher_entropy > lower_entropy,
        "Entropy should increase with the number of words in the passphrase."
    )

def test_entropy_increasing_with_digit_count():
    """
    Test that entropy increases as the number of digits increases.

    Similar to adding more words, increasing the number of digits in the
    passphrase should also increase its entropy. This test ensures that the
    entropy calculation correctly accounts for the additional complexity
    introduced by including more digits, thereby enhancing the security of the
    generated passphrase.
    """

    # Keep the word count constant to focus on the effect of increasing digits.
    word_count = 4
    lower_digit_count = 2
    higher_digit_count = 4

    # Calculate entropy using the function.
    lower_entropy = calc_passphrase_entropy(word_count, lower_digit_count)
    higher_entropy = calc_passphrase_entropy(word_count, higher_digit_count)

    # Assert that entropy is higher with more digits.
    assert (
        higher_entropy > lower_entropy,
        "Entropy should increase with the number of digits in the passphrase."
    )
