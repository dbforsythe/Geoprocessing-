#import arcpy and os
import arcpy
import os
#input feauture class to buffer
inFCs = "C://File Path/"
#output workspace
outWS = "C://File Path/"
#Buffer distance
dist = 1000
#Split input feature classes into seperate feature clases
inFC = inFCs.split(";")
#loop through each feature class and create buffers.
for inFC in inFCSs:
    #get the name of the output feature class.
    (filePath,fileName) = os.path.split(inFC)
    dotInd = fileName.find(".")
    if dotInd <> -1:
        newFC = fileName[0:dotInd]
        outFC = newFC + "_buffer"
        else:
            outFC = filename + "_buffer"
            #create the buffer feature class.
            arcpy.Buffer_analysis(inFC,outWS + "\\" + outFC,str(dist)+" Feet")
