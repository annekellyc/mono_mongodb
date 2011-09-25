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

import insert_documents
import delete_documents
import retrieve_documents
import update_documents
import connection
import generator
import clear
import sys

if len(sys.argv) <= 1 or len(sys.argv) != 2:
    print "--> Invalid input. Please type 'insert', 'retrieve', 'update' or 'delete' to run the program."
elif str(sys.argv[1]) != "insert"  and str(sys.argv[1]) != "retrieve" and str(sys.argv[1]) != "update" and str(sys.argv[1]) != "delete":
    print "--> Invalid input. Please type 'insert', 'retrieve', 'update' or 'delete' to run the program."
else:
    db = connection.create()
    
    print "\n--> Preparing test scenario. It may take a few minutes."
    scenario_01 = generator.generate_post(10)
    scenario_02 = generator.generate_post(100)
    scenario_03 = generator.generate_post(1000)
    scenario_04 = generator.generate_post(10000)
    #scenario_05 = generator.generate_post(100000)
    #scenario_06 = generator.generate_post(1000000)    
    scenario_list = [scenario_01, scenario_02, scenario_03, scenario_04]

    def init():
        clear.clear_table(db.posts)

    def finalize():
        clear.clear_table(db.posts)

    def execute_function(function, db):
        print "\n::: START RUNNING THE MONGODB TESTS WITH " + str(len(scenario_list)) + " SCENARIOS :::\n"               
       
        number_of_doc = 100 
        key_input = "Y"
        number_scenario = 1                 
        for scenario in scenario_list:   
            if (key_input == "Y" or key_input == "y"):
                print "\nSCENARIO " + str(number_scenario)
                init()                
                if function != insert_documents.insert:
                    insert_documents.insert(db, scenario)                                     
                function(db, scenario)                                        
                finalize()                                    
                if scenario == scenario_list[-1]:                    
                    break
                message = "--> Do you want to run the next scenario with " + str(number_of_doc) + " documents ([Y] / N)?: "
                key_input = raw_input(message)
                number_of_doc = number_of_doc * 10 
                number_scenario += 1   
            elif (key_input == "N" or key_input == "n"):
                print "\n--> Test finished.\n"
                break
            else:
                print "\n--> Invalid command.\n"               
                break
                    
    def execute_program():
        try:            
            param = str(sys.argv[1])       
            if param == "insert":            
                execute_function(insert_documents.insert, db)
            if param == "retrieve":            
                execute_function(retrieve_documents.retrieve, db)
            if param == "update":
                execute_function(update_documents.update, db)
            if param == "delete":
                execute_function(delete_documents.remove, db)
        except Exception:
            print "--> Error executing the program."

    execute_program()
            


