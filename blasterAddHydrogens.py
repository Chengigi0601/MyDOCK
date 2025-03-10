##Here is a problem I got in the blasterAddHydrogens.py document, but I am not sure I will got the same problem in the future , there is a error in line 134 so I initialized the value of linecount
   134    linecount = 0  
   135    for linecount, line in enumerate(outFile):
   136      pass  # throw away data
   137    if linecount == 0: 
   138      print "\tfile " + os.path.join(workingDir, chargedReceptorFullH)
   139      print "\tis empty, check input files"
   140      sys.exit(1)
