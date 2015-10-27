from structures.NMapJobsStructure import NMapJobsStructure

class AgentNMap:
    """ This is the AgentNmap class. The agent manipulates the nmap call """
    name = ''
    jobs = []

    
    def __init__(self, name ):
        self.name = name        
       
    
    def setJobs(self, jobs):
        for job in jobs:
            self.jobs.append(job)
    
    
    def print_agent(self):
        print("Name ", self.name)
        for job in self.jobs:
            job.print_structure()
        
        
        
        
        

        

