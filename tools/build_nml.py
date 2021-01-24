#!/usr/bin/env python3

def readCSVFile(filename):
  import csv

  with open(filename, newline='') as csvfile:
    csvReader = csv.DictReader(csvfile)
    output=[]
    for row in csvReader:
      output.append(row)
    return output

def writeOutputFile(filename, data):
  outputFile = codecs.open(filename, 'w', 'utf-8')
  outputFile.write(data)
  outputFile.close()


print("Generating nml files...")

import codecs # Easy I/O
import airspeed # Tamplete engine compatible with Java Velocity


data = readCSVFile('src/steam/data.csv')
print(data)

itemTemplate = airspeed.Template(codecs.open('src/steam/template_item.tnml', 'r', 'utf-8').read())

for engineData in data:
  print("Templating: " + engineData['id'])
  outputItem = itemTemplate.merge(engineData)

  outputItemFilename = engineData['id'] +'_item.pnml'
  print("Generating file : " + outputItemFilename)

  writeOutputFile(outputItemFilename, outputItem)


