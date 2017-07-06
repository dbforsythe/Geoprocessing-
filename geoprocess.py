import arcpy
arcpy.env.workspace = "C:\Users\dforsythe\Documents\ArcGIS\Default.gdb"
arcpy.env.overwriteOutput = True
#Create new table
arcpy.CreateTable_managment("C:\Users\dforsythe\Documents\ArcGIS\Default.gdb","Buffer_Distance",)
#Add new fields
arcpy.AddField_management("Buffer_Distance", "ROUTE_TYPE","TEXT")
arcpy.AddField_management("Buffer_Distance", "DISTANCE","SHORT")
rows = arcpy.InsertCursor("Buffer_Distance")
row = rows.newRow()
row.ROUTE_TYPE = "Primary"
row.DISTANCE = 2000
rows.insertRow(row)
del rows
del row











##FCList = arcpy.ListFeatureClasses()
##for FC in FCList:
 ##   desc = arcpy.Describe(FC)
 ##   print FC + ":"
 ##   print desc.spatialReference.name, "\n"

    


