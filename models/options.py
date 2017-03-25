from enum import Enum
class ValidityOptions(Enum):
    start_with = 'start'
    exactly16 = '16'
    digits = 'IsDits'
    group4 = 'g4'
    separator = 'sparator'
    consecutive= 'consecutive'


'''
     It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
'''
