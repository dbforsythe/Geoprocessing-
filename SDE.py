import arcpy
import os

# SDE workspace to be used
admin_workspace = "Database Connections/tenone@sde.sde"

analyze_contents = []

for dirpath, workspaces, datatypes in arcpy.da.Walk(
        admin_workspace,
        followlinks=True,
        datatype=['Table', 'FeatureClass', 'RasterDataset']):

    # Create full path, and add tables, feature classes, raster datasets
    analyze_contents += [
        os.path.join(dirpath, datatype) for datatype in datatypes]

    # create full path, add the feature datasets of the .sde file
    analyze_contents += [
        os.path.join(dirpath, workspace) for workspace in workspaces]

# Execute Analyze Datasets on the complete list
arcpy.AnalyzeDatasets_management(admin_workspace,
                                 "SYSTEM",
                                 analyze_contents,
                                 "ANALYZE_BASE",
                                 "ANALYZE_DELTA",
                                 "ANALYZE_ARCHIVE")
