#!/usr/bin/env python3
OUTPUT_PATH = "generated/"

def parseArguments():
  "Parse command line arguments and get the type of engine that will be parsed"
  import argparse

  parser = argparse.ArgumentParser(prog='build_nml', description='Build NML files from Velocity templates.')
  parser.add_argument("engine", choices=['steam', 'diesel', 'electric', 'emu', 'mmu'])
  parser.add_argument("-d","--debug", action='store_const', const=True, help="Enables the debug mode.")
  args = parser.parse_args()
  return [args.debug, args.engine]

def stringToNumber(strValue):
  "Tries to convert a string to a number (integer or float)"
  try:
    return int(strValue)
  except ValueError:
    try:
      return float(strValue)
    except ValueError:
      return strValue

def stringToList(strValue):
  "Detects if a string it's a list of values, and convert these values to a python list"
  strValue = strValue[1:-1] # Quitamos los corchetes
  strValues = strValue.split(',')
  values = []
  for strValue in strValues:
    values.append(stringToNumber(strValue.strip()))
  return values

def readCSVFile(filename):
  "Reads a CSV file and returns a dictionary with the values"
  import csv

  with open(filename, newline='') as csvfile:
    csvReader = csv.DictReader(csvfile)
    output=[]
    for row in csvReader:
      for key in row.keys():
        if row[key].startswith('[') and row[key].endswith(']'):
          row[key]= stringToList(row[key])
        else:
          row[key] = stringToNumber(row[key])
      output.append(row)
    return output

def writeOutputFile(filename, data):
  "Writes a file"
  import codecs # Easy I/O

  try:
    outputFile = codecs.open(filename, 'w', 'utf-8')
    outputFile.write(data)
  finally:
    outputFile.close()


class Loader:
  """Template loader for Airspeed"""

  def load_text(self, name):
    import codecs
    try:
      inputFile = codecs.open(name, 'r', 'utf-8')
      text = inputFile.read()
    finally:
      inputFile.close()
      return text

  def load_template(self, name):
    import codecs
    import airspeed
    try:
      inputFile = codecs.open(name, 'r', 'utf-8')
      text = inputFile.read()
    finally:
      inputFile.close()
      return airspeed.Template(text, name)

def parseTemplate(template, data, engine, outputFilename):
  "Parses a Airspeed template and generates an output file"
  import airspeed

  try:
    templateOutput = template.merge(data, loader=Loader())
  except airspeed.TemplateSyntaxError as ex:
    print(ex)

  print(f"Generating file : {outputFilename}")
  writeOutputFile(OUTPUT_PATH + engine + "/" + outputFilename, templateOutput)


def main():
  debug, engine = parseArguments()
  if debug:
    print("Debug mode activated")

  print("Generating nml files for " + engine)

  import codecs # Easy I/O
  import airspeed # Tamplete engine compatible with Java Velocity

  data = readCSVFile(f'src/{engine}/specs.csv')
  if debug:
    print(data)

  # Generate all the vehicle files from CSV data
  itemTemplate = airspeed.Template(codecs.open(f'src/{engine}/template_item.vm', 'r', 'utf-8').read())
  graphicsTemplate = airspeed.Template(codecs.open(f'src/{engine}/template_graphics.vm', 'r', 'utf-8').read())

  ids=[]
  for engineData in data:
    outputItemFilename = f"{engineData['id']}_item.pnml"
    parseTemplate(itemTemplate, engineData, engine, outputItemFilename);

    outputGraphicsFilename = f"{engineData['id']}_graphics.pnml"
    parseTemplate(graphicsTemplate, engineData, engine, outputGraphicsFilename);

    ids.append(engineData['id'])

  # Generate the include all pnml file
  includeAllTemplate = airspeed.Template(codecs.open(f'src/{engine}/template_include.vm', 'r', 'utf-8').read())
  parseTemplate(includeAllTemplate, {'ids': ids}, engine, 'include_all.pnml');


if __name__ == "__main__":
  main()
