#!/usr/bin/env python

# Usage:
#   -i --input=     The input file
#   -o --output=    The output file (optional)
#   -h --help       Usage information
#
# Requirements:
#   Redland librdf python interface <http://librdf.org/docs/python.html>
#   Debian users cann install these bindings with "apt-get install python-librdf"
#
# Copyright:    (c) 2014 AKSW <http://aksw.org/>
# License:      GNU General Public License (GPL) <http://opensource.org/licenses/gpl-license.php>
# Author:       Natanael Arndt <http://aksw.org/NatanaelArndt>

import os
import sys
import getopt
import re
import RDF

args, opts = getopt.getopt(sys.argv[1:], "b:i:o:h", ["baseUri=", "input=", "output=", "help"])

def help():
    sys.stderr.write("""
Usage:
  -b --baseUri=   The base URI to use for the export model
  -i --input=     The path of the input directory
  -o --output=    The output file (optional)
  -h --help       Usage information

""")

def addFiles (model, baseUri, inputPath):
    for root, subFolders, files in os.walk(inputPath):
        rootUri = root[len(inputPath)+1:]
        sys.stderr.write("rootUri: " + rootUri + "\n")
        files = [f for f in files if not f[0] == '.']
        subFolders[:] = [d for d in subFolders if not d[0] == '.']
        for fileName in files:
            f = open(os.path.join(root, fileName), 'r')
            if (len(rootUri) > 0):
                fileUri = RDF.Uri(baseUri + rootUri + "/" + fileName)
            else:
                fileUri = RDF.Uri(baseUri + fileName)
            sys.stderr.write("Add Resource: " + fileUri.__str__() + "\n")
            markdownString = f.read()
            model.append(RDF.Statement(fileUri, RDF.Uri("http://ns.ontowiki.net/SysOnt/Site/content"), RDF.Node(markdownString, datatype=RDF.Uri("http://ns.ontowiki.net/SysOnt/Markdown"))))
            model.append(RDF.Statement(fileUri, RDF.Uri("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), RDF.Uri("http://xmlns.com/foaf/0.1/Document")))
            model.append(RDF.Statement(fileUri, RDF.Uri("http://www.w3.org/2000/01/rdf-schema#label"), fileName))

outputUri = None
inputPath = None
baseUri   = None
for opt, arg in args:
    if opt in ("-i", "--input"):
        inputPath = arg
    elif opt in ("-o", "--output"):
        outputUri = arg
    elif opt in ("-b", "--baseUri"):
        baseUri = arg
    elif opt in ("-h", "--help"):
        help()
        sys.exit(0)

sys.stderr.write("Input: " + inputPath + "\n")

model = RDF.Model()

addFiles(model, baseUri, inputPath)

ttlSerializer = RDF.Serializer(name="turtle")
ttlSerializer.set_namespace("rdfs", "http://www.w3.org/2000/01/rdf-schema#")
ttlSerializer.set_namespace("foaf", "http://xmlns.com/foaf/0.1/")
ttlSerializer.set_namespace("sysont", "http://ns.ontowiki.net/SysOnt/")
ttlSerializer.set_namespace("site", "http://ns.ontowiki.net/SysOnt/Site/")
string = ttlSerializer.serialize_model_to_string(model, baseUri)

if (outputUri):
    outFile = open(outputUri, "w")
else:
    outFile = sys.stdout
outFile.write(string)

sys.stderr.write("done\n")
