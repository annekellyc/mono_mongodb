#=======================================================================
# Anne Kelly Da Costa Geraldo
# Monografia 
# Pos Graduacao em Engenharia de Software
#=======================================================================

#!/bin/env/ python 

import random

#=======================================================================
# Function to create letters randomly
#=======================================================================
def generate_word(number_of_letters):
    concatenating_letter = []
    for r in xrange(number_of_letters):
        letter = chr(random.randint(97,122)) 
        concatenating_letter.append(letter)
    return ''.join(concatenating_letter)



