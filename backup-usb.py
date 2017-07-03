import os.path
import argparse

def parseArguments():
  parser = argparse.ArgumentParser(description='Backup Materia from USB.')
  parser.add_argument('source', help='source to backup')
  parser.add_argument('destination', help='destination to backup')
  return parser.parse_args()

all_files={}

if __name__ == "__main__":
  args  =  parseArguments()
  src = args.source
  dest =  args.destination

  if os.path.exists(src) == False:
    print(src,'Not exists')
     
  

