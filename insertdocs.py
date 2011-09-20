#=======================================================================
# Anne Kelly Da Costa Geraldo
# Monografia 
# Pos Graduacao em Engenharia de Software
#=======================================================================

#!/bin/env/ python 

import clear
import connectionmongodb
import generator
import constant
import datetime

#=======================================================================
# Connection with MongoDB
#=======================================================================
db = connectionmongodb.create_connection()

#=======================================================================
# Function to clear all posts before insert new documents 
#=======================================================================
def initialize_finalize():
    clear.drop_posts(db)

#=======================================================================
# Function to insert new documents 
#=======================================================================
def insert_documents():
    for p in xrange(constant.number_of_docs):
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
        posts = db.posts
        posts.insert(post)
    return posts
    
#=======================================================================
# Call the function insert_documents
#=======================================================================
try:
    initialize_finalize()
    insert_documents()
    initialize_finalize()
    msg = "--> " + str(constant.number_of_docs) + " documento(s) inserido(s)."
    print msg    
except Exception:
    print "--> Erro ao inserir o(s) documento(s)."

