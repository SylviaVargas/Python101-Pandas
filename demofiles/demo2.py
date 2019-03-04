# An example of the process of data analysis using Python 3
#  Get Data,  Prepare data, Analyze Data, Present Data.

#http://pandas.pydata.org/pandas-docs/version/0.20/10min.html
import pandas
import sys
from  matplotlib import pyplot
from numpy import arange

print ('---- Beginning of Data Acquisition ------')
ifile="degrees-that-pay-back.csv"

degreesFile = pandas.read_csv(ifile)

print ('---- End of Data Acquisition ------')
#------------------------------------------------------


print ('---- Beginning of Transformation -------')
# Transform data
print ("# of records in file: %d" % len(degreesFile))
print ( " Fields in file %s" % ifile)
print (degreesFile.dtypes) # View the fields and datatypes.