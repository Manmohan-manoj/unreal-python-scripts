from fileinput import filename
import os
import unreal as ue
editLib = ue.EditorAssetLibrary()
editUtil = ue.EditorUtilityLibrary()
AssetTooldHelp = ue.AssetToolsHelpers()
root = r""

assetname = "enLivingRoom"
def importTexture(assetname):
    texturepath = os.path.join(root,assetname,r"\texture")
    dir_list = os.listdir(texturepath)
    for i in dir_list:
        subpath = os.path.join(texturepath,i)
        subdirlist = os.listdir(subpath)
        lastfolder = subdirlist[-1]
        lastpath = os.path.join(subpath,lastfolder)
        print(lastpath)
        ueDir = "Game/Lookdev/"+assetname+"/"+subpath+"_"+lastfolder
        if editLib.does_directory_exist(ueDir):
            continue
            print( ueDir.split('/')[-1]," - up to date")
        editLib.make_directory(ueDir)
        texture_import_tasks = []
        files_in_lastpath = [f for f in os.listdir(lastpath) if os.path.isfile(f)]
        for file in files_in_lastpath:
            texture_import_task = buildImportTast(file,ueDir)
            texture_import_tasks.append(texture_import_task)
            #test
        print(lastpath," importing to ",ueDir)
        # executeImportTask(texture_import_tasks)

def buildImportTast(filenname, destination_path):
    task = ue.AssetImportTask()
    task.set_editor_properties('automated',True)
    task.set_editor_properties('destination_name','')
    task.set_editor_properties('destination_path',destination_path)
    task.set_editor_properties('filename',filename)
    task.set_editor_properties('replace_existing',False)
    task.set_editor_properties('save',False)
    return task
def executeImportTask(tasks):
    AssetTooldHelp.get_asset_tools().import_asset_tasks(tasks)