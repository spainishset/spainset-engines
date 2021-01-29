#!/usr/bin/env python3
OUTPUT_PATH = "generated/"


def parseArguments():
  "Parse command line arguments and get the type of engine that will be parsed"
  import argparse

  parser = argparse.ArgumentParser(prog='build_nml', description='Build NML files from Velocity templates.')
  parser.add_argument("engine", choices=['steam', 'diesel', 'electric'])
  args = parser.parse_args()
  return args.engine

def stringToNumber(strValue):
  "Tries to convert a string to a number (integer or float)"
  try:
    return int(strValue)
  except ValueError:
    try:
      return float(strValue)
    except ValueError:
      return strValue

def readCSVFile(filename):
  "Reads a CSV file and returns a dictionary with the values"
  import csv

  with open(filename, newline='') as csvfile:
    csvReader = csv.DictReader(csvfile)
    output=[]
    for row in csvReader:
      for key in row.keys():
        row[key] = stringToNumber(row[key])
      output.append(row)
    return output

def writeOutputFile(filename, data):
  "Writes a file"
  import codecs # Easy I/O

  outputFile = codecs.open(filename, 'w', 'utf-8')
  outputFile.write(data)
  outputFile.close()

def parseTemplate(template, data, engine, outputFilename):
  "Parses a Airspeed template and generates an output file"
  templateOutput = template.merge(data)

  print(f"Generating file : {outputFilename}")
  writeOutputFile(OUTPUT_PATH + engine + "/" + outputFilename, templateOutput)


def main():
  engine = parseArguments()
  print("Generating nml files for " + engine)

  import codecs # Easy I/O
  import airspeed # Tamplete engine compatible with Java Velocity


  data = readCSVFile(f'src/{engine}/specs.csv')
  #print(data)

  # Generate all the vehicle files from CSV data
  itemTemplate = airspeed.Template(codecs.open(f'src/{engine}/template_item.vm', 'r', 'utf-8').read())
  graphicsTemplate = airspeed.Template(codecs.open(f'src/{engine}/template_graphics.vm', 'r', 'utf-8').read())

  ids=[]
  for engineData in data:
    print(f"Templating item file for: {engineData['id']}")
    outputItemFilename = f"{engineData['id']}_item.pnml"
    parseTemplate(itemTemplate, engineData, engine, outputItemFilename);

    print(f"Templating graphics file for: {engineData['id']}")
    outputGraphicsFilename = f"{engineData['id']}_graphics.pnml"
    parseTemplate(graphicsTemplate, engineData, engine, outputGraphicsFilename);

    ids.append(engineData['id'])

  # Generate the include all pnml file
  includeAllTemplate = airspeed.Template(codecs.open(f'src/{engine}/template_include.vm', 'r', 'utf-8').read())
  print(f"Templating file {engine}/template_include.vm")
  parseTemplate(includeAllTemplate, {'ids': ids}, engine, 'include_all.pnml');


if __name__ == "__main__":
  main()
