
import arcpy
from arcpy import env

env.workspace = "C:\Users\dforsythe\Downloads\geodatabases\GeoDatabases\gdb2\GeoDatabase_2.gdb"

fcs = arcpy.ListFeatureClasses("A","polygon")
print "Here are the Feauture Classes Inside of gdb2:  "
print"     "
for x in fcs:
    print x



