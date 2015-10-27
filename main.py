from agent.agent import AgentNMap
from file.file_parser_reader import FileParserReader


def main():
    agent = AgentNMap("First Agent")
    
    
    fileParserReader = FileParserReader("./file/test.csv")
    fileParserReader.read_lines()
    agent.setJobs(fileParserReader.getListOfJobs())

    agent.print_agent()
    
    
if __name__ == "__main__":
    main()
