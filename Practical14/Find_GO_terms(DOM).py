from xml.dom.minidom import parse 
import xml.dom.minidom
import xlsxwriter
import pandas as pd

# read file
file = pd.read_xml('go_obo.xml')
tree = xml.dom.minidom.parse(file)
root = tree.documentElement
terms = root.getElementsByTagName('term')

# Create an Excel workbook
workbook = xlsxwriter.Workbook('autophagosome.xlsx')
# create a worksheet
worksheet = workbook.add_worksheet()
# Sets the header row of the worksheet
worksheet.write(0, 0, 'GO id')
worksheet.write(0, 1, 'Term name')
worksheet.write(0, 2, 'Definition string')
worksheet.write(0, 3, 'Number of childNodes')

# Define a line number variable, starting with 1
row = 1
for term in terms:
 # Gets the defstr attribute
 defstr = term.getAttribute('defstr')
 # Check if defstr contains 'autophagosome'
 if 'autophagosome' in defstr:
 # Gets the id and name attributes
  id = term.getAttribute('id')
  name = term.getAttribute('name')
 # Get all the is_a elements
  is_a_list = term.getElementsByTagName('is_a')
 # Calculate the number of child nodes
  counter = len(is_a_list)
 # Write id, name, defstr, and counter to the corresponding columns of the worksheet
  worksheet.write(row, 0, id)
  worksheet.write(row, 1, name)
  worksheet.write(row, 2, defstr)
  worksheet.write(row, 3, counter)
 # Increase the row number by one, ready for the next line of writing
  row += 1

file.close()
workbook.close()
