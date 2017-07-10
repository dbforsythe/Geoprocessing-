import arcpy
arcpy.env.workspace = 'c:/data'
# Print to the Interactive window all the feature datasets in the
#   workspaces that start with the letter c or f.
datasets1 = list(set(arcpy.ListDatasets("c*", "Feature")) |
                 set(arcpy.ListDatasets("f*", "Feature")))
print(datasets1)

#   workspaces that start with the letters except c
datasets2 = list(set(arcpy.ListDatasets("*", "Feature")) -
                 set(arcpy.ListDatasets("c*", "Feature")))
print(datasets2)

#   workspaces that contain both the letter c and f
datasets3 = list(set(arcpy.ListDatasets("*c*", "Feature")) &
                 set(arcpy.ListDatasets("*f*", "Feature")))
print(datasets3)
