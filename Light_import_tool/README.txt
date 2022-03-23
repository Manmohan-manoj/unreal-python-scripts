Light rigs from other software to unreal

The light importer is an unreal engine python script for sharing light rigs from other DCCs to unreal.
The appropriate scripts for the DCCs will be used to export light information as JSON. The tool uses that JSON file to spawn lights in unreal. 

Currently, the script takes transforms and intensity values. In the future, I hope to calculate the value corrections needed to achieve the closest result in Unreal.

Light_location.txt is the location data exported from maya.
Unreal_genarate.py is the main python script that does the importing.
LightRigTool.uasset is a Utility widget for the tool in unreal engine.

