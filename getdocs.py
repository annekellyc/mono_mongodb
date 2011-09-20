#=======================================================================
# Anne Kelly Da Costa Geraldo
# Monografia 
# Pos Graduacao em Engenharia de Software
#=======================================================================

#!/bin/env/ python 

import clear
import connectionmongodb
import insertdocs

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
# Function to select all documents
#=======================================================================
def get_documents(doc):
    for post in doc.find():        
        print post    
   
#=======================================================================
# Call the function get_documents
#=======================================================================
try:
    initialize_finalize()
    documents = insertdocs.insert_documents()
    print "--> Documents:"
    get_documents(documents)
    initialize_finalize()
except Exception:
    print "--> Erro ao recuperar o(s) documento(s)!"




