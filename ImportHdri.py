import unreal
import os
path = "E:\OneDrive - Technicolor\HDRI_WITH_hdriS"

tasks = []
def buildImportTask(destination_path,filename,destination_name):

        task = unreal.AssetImportTask()
        task.set_editor_property('automated',True)
        task.set_editor_property('destination_name', destination_name)
        task.set_editor_property('destination_path', destination_path)
        task.set_editor_property('filename',filename)
        task.set_editor_property('replace_existing', False)
        task.set_editor_property('save', False)
        return task

def execute(tasks):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)

# buildImportTask
for i in os.listdir(path):
        f = os.path.join(path, i)
        if(os.path.isfile(f)):
            continue
        for k in os.listdir(f):
            if(k.endswith(".hdr")):
                print(k)
                fullpath = os.path.join(f, k)
                task = buildImportTask('/Game/pmm/HDRIs/',fullpath,i)
                tasks.append(task)
execute(tasks)

