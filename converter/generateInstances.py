import ufoProcessor
from mojo.UI import PutFile, GetFile
import os

"""
    Open a .sp3 or .designspace document and generate the instances.
    No reporting, no editing, no debugging. 
"""

def convertSuperpolatorToDesignSpace(path):
    # this a superpolator path and needs to be converted first
    newPathName = path.replace(".sp3", "_converted.designspace")
    newPathName = PutFile(message="Save this Superpolator document as Designspace:", fileName=os.path.basename(newPathName))
    if newPathName:
        ufoProcessor.sp3.sp3_to_designspace(path, newPathName)
    return newPathName

def generateInstances():
    path = GetFile("Open a Desingspace or Superpolator file to generate:", fileTypes=['sp3', 'designspace'])
    if path is None:
        return
    if os.path.splitext(path)[-1] == ".sp3":
        path = convertSuperpolatorToDesignSpace(path)
        if path is None:
            return
    ufoProcessor.build(path)
    
generateInstances()
print('done')

