class NMapJobsStructure:
    """ This is the Nmap jobs structure class. Stores the nmap jobs """
    id = ''
    parameters = ''
    periodic = ''
    time = ''
    
    def __init__(self, id, parameters, periodic, time ):
        self.id = id
        self.parameters = parameters
        self.periodic = periodic
        self.time = time
        
        
    def print_structure(self):
        print("id: ", self.id, " parameters: ", self.parameters, " periodic: ", self.periodic, " time: ", self.time)

        

