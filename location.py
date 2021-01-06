class location:

    def __init__(self, postcode_data):
        self.postcode = postcode_data[0]
        self.latitude = postcode_data[2]
        self.longitude = postcode_data[3]
        self.easting = postcode_data[4]
        self.northing = postcode_data[5]
        self.grid_ref = postcode_data[6]
        self.ward = postcode_data[7]
        self.parish = postcode_data[8]
        self.country = postcode_data[12]
        self.lsoa_code = postcode_data[15]
        self.lsoa_name = postcode_data[16]
