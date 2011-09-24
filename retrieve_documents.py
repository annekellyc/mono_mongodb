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

# Function to retrieve documents 
def retrieve(db, documents):
    try:
        start = time.clock()
        for document in documents:
            db.posts.find_one({ 'author': document['author'] })
            #print "Text: " + document['text'] + " ",
        elapsed = (time.clock() - start)    
        print "--> " + str(len(documents)) + " retrieved document(s). " + "Time: " + str(elapsed)
    except Exception:
        print "--> Erro ao recuperar o(s) documento(s)."

        


