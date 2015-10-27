from data_structures.NMapJobsStructure import NMapJobsStructure
import sys


class FileParserReader:
    """ 
    This is file reader class, reads and parses the file :)
    """
    file = ''
    name = "NoName"
    lines = []
    
    def __init__(self,name):
        self.name = name

        
    def read_lines(self):
        try:
            self.file = open(self.name, "r")
            for line in self.file:
                self.lines.append(line.rstrip('\n'))
        except IOError as e:
            print("I/O error ")
            exit(-1)
        except ValueError:
            print("Could not convert data to an integer.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
   

    def getListOfJobs(self):
        jobsList = []
        for line in self.lines:
            tmp = NMapJobsStructure(line,line,line,line)
            jobsList.append(tmp)
        return jobsList
    
    
    
    def print_lines(self):
        for line in self.lines:
            print(line)