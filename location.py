import postcodes_io_api

class location:

    def __init__(self, postcode):
        api  = postcodes_io_api.Api(debug_http=True)
        data = api.get_postcode(postcode)
        
        self.postcode = data['result']['postcode']
        self.eastings = data['result']['eastings']     
        self.northings = data['result']['northings']   
        self.longitude = data['result']['longitude']    
        self.latitude = data['result']['latitude']  
        self.electoral_region = data['result']['european_electoral_region']          
        self.primary_care_trust = data['result']['primary_care_trust'] 
        self.region = data['result']['region']  
        self.lsoa = data['result']['lsoa'] 
        self.msoa = data['result']['msoa'] 
        self.parliamentary_constituency = data['result']['parliamentary_constituency'] 
        self.ward = data['result']['ward'] 
        self.parish = data['result']['parish'] 
        self.country = data['result']['country']       
        self.ccg = data['result']['ccg']   


