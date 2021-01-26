#!/usr/bin/env python3
OUTPUT_PATH = "generated/"

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

def parseTemplate(template, data, outputFilename):
  "Parses a Airspeed template and generates an output file"
  templateOutput = template.merge(data)

  print("Generating file : " + outputFilename)
  writeOutputFile(OUTPUT_PATH + outputFilename, templateOutput)


def main():
  print("Generating nml files...")

  import codecs # Easy I/O
  import airspeed # Tamplete engine compatible with Java Velocity


  data = readCSVFile('src/steam/data.csv')
  #print(data)

  # Generate all the vehicle files from CSV data
  itemTemplate = airspeed.Template(codecs.open('src/steam/template_item.vm', 'r', 'utf-8').read())
  graphicsTemplate = airspeed.Template(codecs.open('src/steam/template_graphics.vm', 'r', 'utf-8').read())

  ids=[]
  for engineData in data:
    print("Templating item file for: " + engineData['id'])
    outputItemFilename = engineData['id'] +'_item.pnml'
    parseTemplate(itemTemplate, engineData, outputItemFilename);

    print("Templating graphics file for: " + engineData['id'])
    outputGraphicsFilename = engineData['id'] +'_graphics.pnml'
    parseTemplate(graphicsTemplate, engineData, outputGraphicsFilename);

    ids.append(engineData['id'])

  # Generate the include all pnml file
  includeAllTemplate = airspeed.Template(codecs.open('src/steam/template_include.vm', 'r', 'utf-8').read())
  print("Templating file steam/template_include.vm")
  parseTemplate(includeAllTemplate, {'ids': ids}, 'include_all.pnml');


if __name__ == "__main__":
  main()
