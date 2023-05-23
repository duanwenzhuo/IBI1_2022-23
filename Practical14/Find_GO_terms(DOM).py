from xml.dom.minidom import parse 
import xml.dom.minidom
import xlsxwriter
import os
import pandas as pd



# read file
os.chdir(r"C:\Users\86188\Downloads")
file = pd.read_xml(go_obo.xml)
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
  # Gets the defstr element
    defstr = term.getElementsByTagName('defstr')[0]
  # Check if defstr contains 'autophagosome'
    if 'autophagosome' in defstr.firstChild.data:
    # Gets the text content for id, name, and defstr
        id = term.getElementsByTagName('id')[0].firstChild.data
        name = term.getElementsByTagName('name')[0].firstChild.data
        defstr_text = defstr.firstChild.data
    # calculate the number of childnode
        counter = 0
        children = term.childNodes 
        for child in children:
            if child.nodeName == 'is_a':
                counter += 1
    # Write id, name, defstr_text, and counter to the corresponding columns of the worksheet
    worksheet.write(row, 0, id)
    worksheet.write(row, 1, name)
    worksheet.write(row, 2, defstr_text)
    worksheet.write(row, 3, counter)
    # 将行号加一，准备下一行的写入
    row += 1


file.close()
workbook.close()