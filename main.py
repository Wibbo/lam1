import postcodes_io_api
import xlwings as xw
from location import location
from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))



# Open the xls containing the test results.
wb = xw.Book('testdata.xlsx')

# Reference the results sheet.
sht = wb.sheets['291220_1852']

if sht.range('I1').value != 'Area':
    sht.range('I:I').insert()
    sht.range('K:K').insert()
    sht.range('K:K').number_format = '0.0'

    sht.range('I1').value = 'Area'
    sht.range('K1').value = 'Age'


row_number = 2
postcode_col = 8
DoB_col = 10
age_col = 11

while True:
    postcode = sht.range(row_number, postcode_col).value
    date_birth = sht.range(row_number, DoB_col).value
    
    if postcode != None:
        location_data = location(postcode)
    sht.range(row_number, age_col).value = calculate_age(date_birth)
    row_number += 1

    if postcode == None:
        break

    #print(postcode, date_birth)






# =(TODAY()-I2)/365

# Read each row into a test_person class.



#print(location_data.country)
#print(location_data.ward)

