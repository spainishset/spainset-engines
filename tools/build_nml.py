#!/usr/bin/env python3

print("Generating nml files...")

import codecs
from string import Template

output = []

data = [{'id': '040_verraco'}, {'id': '030_perruca'}]

steamEngineTemplate = Template(codecs.open('src/steam/template_item.tnml', 'r', 'utf-8').read())

for engineData in data:
  print("Templating: " + engineData['id'])
  output.append(steamEngineTemplate.safe_substitute(engineData))

  outputFilename = 'engineData['id'] +'_item.pnml'
  print("Generatin Writing the file : " + outputFilename)

  outputFile = codecs.open(outputFilename, 'w', 'utf-8')
  outputFile.write('\n'.join(output))
  outputFile.close()

