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

import clear
import connectionmongodb
import insertdocs

# Connection with MongoDB
db = connectionmongodb.create_connection()

# Function to clear all posts before insert new documents 
def initialize_finalize():
    clear.drop_posts(db)

# Function to select all documents
def get_documents(doc):
    for post in doc.find():        
        print post    
   
# Call the function get_documents
try:
    initialize_finalize()
    documents = insertdocs.insert_documents()
    print "--> Documents:"
    get_documents(documents)
    initialize_finalize()
except Exception:
    print "--> Erro ao recuperar o(s) documento(s)!"
