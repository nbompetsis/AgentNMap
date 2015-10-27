from data_structures.NMapJobsStructure import NMapJobsStructure

class AgentNMap:
    """ This is the AgentNmap class. The agent manipulates the nmap call """
    name = ''
    jobs = []

    
    def __init__(self, name ):
        self.name = name        
       
    
    def setJobs(self, jobs):
        for job in jobs:
            self.jobs.append(job)
        #for job in jobs:
            #tmp = NMapJobsStructure(job,job,job,job)
            #tmp = (NMapJobsStructure) job
            #self.jobs.append(tmp)
    
    
    def print_agent(self):
        print("Name ", self.name)
        for job in self.jobs:
            job.print_structure()
        
        
        
        
        

        

