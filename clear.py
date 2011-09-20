#=======================================================================
# Anne Kelly Da Costa Geraldo
# Monografia 
# Pos Graduacao em Engenharia de Software
#=======================================================================


#!/bin/env/ python 

#=======================================================================
# Function to clear all posts before insert new documents 
#=======================================================================
def drop_posts(db):
    db.posts.drop()


