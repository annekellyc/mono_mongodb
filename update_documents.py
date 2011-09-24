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

import time
import generator
import constants
import datetime

def update(db, documents):
    try:
        start = time.clock()
        for document in documents:
            db.posts.update({"author": document['author']}, {                    
                              "author": "Updated post! " + str(document['author']) ,
                              "text": generator.generate_word(constants.number_of_letters),
                              "tags": ["mongodb", "python", "pymongo"],
                              "date": datetime.datetime.utcnow(),
                              "category": {
                                "name": generator.generate_word(constants.number_of_letters),
                                "description": generator.generate_word(constants.number_of_letters)
                              }
                            })
        elapsed = (time.clock() - start)   
        print "--> " + str(len(documents)) + " updated document(s). " + "Time: " + str(elapsed)
    except Exception:
        print "--> Erro ao atualizar o(s) documento(s)."         


