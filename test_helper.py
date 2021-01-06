from location import location
import datetime
import csv


def calculate_age(date_of_birth):
    """Calculates how old someone is based on their date of birth.
    Args:
        [Datetime] born: The date on which a person was born.
    Returns:
        [Int]: The age of a person.
    """
    if date_of_birth is None:
        return 'Unknown'

    if isinstance(date_of_birth, str):
        d, m, y = date_of_birth.split('/')

        try:
            dob = datetime.datetime(int(y), int(m), int(d))
        except ValueError:
            return 'Invalid date'
    else:
        dob = date_of_birth

    today = datetime.date.today()

    year = dob.year
    age = today.year - year - ((today.month, today.day) < (dob.month, dob.day))

    if age > 90:
        return 'Unknown'
    else:
        return age


def store_postcodes(postcode_list):
    """Reads details of each postcode stored in the postcodes.csv
       file and stores them in a list of location objects.
    """
    row_count = 0

    with open('data/postcodes.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row_count > 0:
                postcode_list.append(location(row))

            row_count += 1


def get_postcode_from_file(raw_code):
    """Ensures the supplied postcode is correctly formatted.
    Args:
        raw_code: The postcode from the testing file.
    Returns: A correctly formatted postcode.
    """
    if raw_code is None:
        return "Unknown"

    raw_code = raw_code.replace(" ", "")
    code_length = len(raw_code)
    postfix = raw_code[code_length-3:]
    prefix = raw_code[:code_length-3]

    return prefix + " " + postfix


def get_ward_from_postcode(postcode, postcode_list):
    """Returns the ward name for the specified postcode.
    Args:
        postcode: The postcode from where the booking was made.
    Returns: Either the name of the Lambeth ward or Outside Lambeth.
    """
    ward = 'Outside Lambeth'

    for loc in postcode_list:
        if loc.postcode == postcode:
            ward = loc.ward
            break
    return ward


def get_test_outcome_from_code(test_code):

    if test_code is None:
        return 'Awaiting'

    test_code = test_code.lower()

    if test_code == 'zz89':
        return 'Negative'
    elif test_code == 'bb87':
        return 'Positive'
    elif test_code == 'dna':
        return 'Did not show'
    elif test_code == 'tt89':
        return 'Void'
    elif test_code == '':
        return 'Awaiting'
    else:
        return 'Unknown'
