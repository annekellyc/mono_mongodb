# Copyright 2011 Anne Kelly <annekellyc@gmail.com>
#
# This file is part of mono_mongodb.
#
# mono_mongodb is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License as published by the 
# Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version.
#
# mono_mongodb is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License 
# for more details.
#
# You should have received a copy of the GNU General Public License along 
# with mono_mongodb. If not, see http://www.gnu.org/licenses/.


#!/bin/env/ python 

import random

# Function to create letters randomly
def generate_word(number_of_letters):
    concatenating_letter = []
    for r in xrange(number_of_letters):
        letter = chr(random.randint(97,122)) 
        concatenating_letter.append(letter)
    return ''.join(concatenating_letter)

def generate_post(number_of_posts):
    posts = []
    for p in xrange(number_of_posts):
        post = [{                    
          "author": generator.generate_word(constant.number_of_letters),
          "text": generator.generate_word(constant.number_of_letters),
          "tags": ["mongodb", "python", "pymongo"],
          "date": datetime.datetime.utcnow(),
          "category": {
            "name": generator.generate_word(constant.number_of_letters),
            "description": generator.generate_word(constant.number_of_letters)
          }
        }]        
        posts.append(post)

    return posts
