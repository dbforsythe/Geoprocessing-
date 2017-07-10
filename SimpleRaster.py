import arcpy
import os

workspace = "c:/data"
rasters = []

for dirpath, dirnames, filenames in arcpy.da.Walk(
        workspace, topdown=True, datatype="RasterDataset"):
    # Disregard any folder named 'back_up' in creating list 
    #  of rasters
    if "back_up" in dirnames:
        dirnames.remove('back_up')
    for filename in filenames:
        rasters.append(os.path.join(dirpath, filename))
