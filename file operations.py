
#Working with CSV

import csv
data = open("example.csv",encoding="utf-8")
csv_data = csv.reader(data)
datalines = list(csv_data)

datalines[:3]

for line in datalines[:5]:
    print(line)

print(len(datalines))

all_lines = []
for i in datalines[1:15]:
    all_lines.append(i)
print(all_lines)

output_file = open('output_file','w',newline='')
csv_write = csv.writer(output_file,delimiter = ',')

csv_write.writerow(['a','b','c'])
csv_write.writerows([['1','2','3'],['4','5','6']])
output_file.close()

f = open('output_file','a',newline='')
csv_write = csv.writer(f)
csv_write.writerow(['new','new','new'])
f.close()

print("-----------------------------------------------------------------------------------------")

#Working with PDF

import PyPDF2

f = open("Working_Business_Proposal.pdf",'rb')
pdf_reader = PyPDF2.PdfReader(f)

print(len(pdf_reader.pages))

page_one = pdf_reader.pages[0]
page_one_text = page_one.extract_text()
page_one_text
f.close()

print(page_one)
print(page_one_text)


f = open("Working_Business_Proposal.pdf",'rb')
pdf_reader = PyPDF2.PdfReader(f)
first_page = pdf_reader.pages[0]

pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(first_page)

pdf_output = open('output_pdf.pdf','wb')
pdf_writer.write(pdf_output)
f.close()

print(first_page)

f = open("Working_Business_Proposal.pdf",'rb')

#List of every pages text, index will be page number
pdf_text = []
pdf_reader = PyPDF2.PdfReader(f)

for i in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[i]
    pdf_text.append(page.extract_text())
    print(page)

pdf_text
print(pdf_text)

import csv
import re

import requests
data = open('sample.csv',encoding='utf-8')
csv_data = csv.reader(data)
print(csv_data)
datalines = list(csv_data)
#print(datalines)

url = str(datalines).startswith("https:")
#url = re.findall("https://[a-z]",str(datalines))
#url = re.findall(r'https://',datalines)
print(url)


#Extract Phone number from pdf
import PyPDF2
import re

f = open("Find_the_Phone_Number.pdf",'rb')
pdf_reader = PyPDF2.PdfReader(f)
#print(len(pdf_reader.pages))

page = pdf_reader.pages[13]
page_text = page.extract_text()
#print(page_text)

phone_number = re.findall(r'[0-9]+.[0-9]+.[0-9]+',page_text)
print(phone_number)
