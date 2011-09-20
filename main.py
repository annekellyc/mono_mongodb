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

import generator

import clear

db = connection.create()

scenario_01 = generator.generate_post(10)
scenario_02 = generator.generate_post(100)
scenario_03 = generator.generate_post(1000)

def run():

  init()

try:
  execute_insert_document_tests()
except Exception:
  print "--> Erro ao inserir o(s) documento(s)."

  execute_update_document_tests()
  execute_delete_document_tests()
  execute_update_document_tests()
  
  finalize()

def execute_insert_document_tests():
  # Executes the first scenario
  insert_documents.insert(db, scenario_01)

  # Executes the second scenario
  insert_documents.insert(db, scenario_02)

  # Executes the third scenario
  insert_documents.insert(db, scenario_03)

def execute_retrieve_document_tests():
  pass

def execute_update_document_tests():
  pass

def execute_delete_document_tests():
  pass

def init():
    clear.clear_table(db.posts)

def finalize():
    clear.clear_table(db.posts)
