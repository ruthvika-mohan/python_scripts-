# Import required modules
# Glob module finds all the pathnames matching a specified pattern
# Pandas required to do merge operation
# chdir() method in Python used to change the current working directory to specified path.
from os import chdir
from glob import glob 
import pandas as pdlib

# Move to the path that holds our CSV files
csv_file_path = 'C:\folder_containing_csv_files'
chdir(csv_file_path)

# List all CSV files in the working directory 
list_of_files = [file for file in glob('*.csv')]
print(list_of_files)

 

"""
 Function:
  Produce a single CSV after combining all files
"""
def produceOneCSV(list_of_files,file_out):
   # Consolidate all CSV files into one object
   result_obj = pdlib.concat([pdlib.read_csv(file,header = 0,encoding  = 'cp1252') for file in list_of_files],ignore_index = True)
   # Convert the above object into a csv file and export
   result_obj.to_csv(file_out)

file_out = "MergedOutput.csv"
produceOneCSV(list_of_files,file_out)