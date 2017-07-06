import arcpy
#workspace
from arcpy import env
env.worspace = "C://FilePath//"
#Process and List the Feature Classes
fclist = arcpy.ListFeatureClasses()
#Print feature class list
print fclist
#Process and describe the park clip
desc = arcpy.Describe("parks_Clip.shp")
print "Parks_Clip is a " + desc.shapeType
#Parks shape is a polygon

#Describe the facilities_buffer
desc1= arcpy.Describe("facilities_Buffer.shp")
#Print the facilities Buffer Shapetype
print "Facilities_buffer is a "+ desc1.shapeType
