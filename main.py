import xlwings as xw
import test_helper as th

# Stores details of all Lambeth postcodes.
postcode_list = []
th.store_postcodes(postcode_list)

# Open the xls containing the test results.
wb = xw.Book('data/testdata2.xlsx')

# Reference the results sheet.
sht = wb.sheets['data']

if sht.range('I1').value != 'Area':
    sht.range('I:I').insert()
    sht.range('K:K').insert()
    sht.range('K:K').number_format = '0.0'

    sht.range('I1').value = 'Area'
    sht.range('K1').value = 'Age'
    sht.range('O1').value = 'Outcome'

row_number = 2
postcode_col = 8
DoB_col = 10
age_col = 11
ward_col = 9
test_col = 14
outcome_col = 15

while True:
    office = sht.range(row_number, 1).value

    # Stop once each row in the test spreadsheet has been processed.
    if office is None:
        break

    date_birth = th.calculate_age(sht.range(row_number, DoB_col).value)
    test_code = sht.range(row_number, test_col).value

    # Determine each system user's age.
    postcode = th.get_postcode_from_file(sht.range(row_number, postcode_col).value)
    sht.range(row_number, age_col).value = date_birth

    # Determine the ward from which the booking was made.
    ward = th.get_ward_from_postcode(postcode, postcode_list)
    sht.range(row_number, ward_col).value = ward
    sht.range(row_number, outcome_col).value = th.get_test_outcome_from_code(test_code)

    row_number += 1
