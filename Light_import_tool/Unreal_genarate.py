import unreal
import json

unreal.log("Start")
json_file = open(".\Light_location.txt",'r')
lights = json.load(json_file)
json_file.close()
print(lights["spotlights"])
print(type(lights["spotlights"][0]['location']))
def convertLocation(location):
    x = location[0]     
    y = location[1]        
    z = location[2]   
    return x,y,z    

def spawn_point_lights(pointlight):
    light_class = unreal.PointLight()
    # light_class.intensity = 10.0
    tx,ty,tz = convertLocation(pointlight['location'])
    light_location = unreal.Vector(tx,ty,tz)
    # unreal.EditorLevelLibrary.spawn_actor_from_class(light_class, light_location)
    light = unreal.EditorLevelLibrary.spawn_actor_from_object(light_class, light_location)
    light.set_actor_label(pointlight['title'])
    lightComponent = light.point_light_component
    lightComponent.set_editor_property("intensity", pointlight['intensity'])
    lightComponent.set_editor_property("mobility", unreal.ComponentMobility.MOVABLE)
    print(lightComponent.get_editor_property("mobility"))

def spawn_spot_lights(spotlight):
    light_class = unreal.SpotLight()
    # light_class.intensity = 10.0
    tx,ty,tz = convertLocation(spotlight['location'])
    light_location = unreal.Vector(tx,ty,tz)
    # unreal.EditorLevelLibrary.spawn_actor_from_class(light_class, light_location)
    light = unreal.EditorLevelLibrary.spawn_actor_from_object(light_class, light_location)
    light.set_actor_label(spotlight['title'])
    lightComponent = light.spot_light_component
    lightComponent.set_editor_property("intensity", spotlight['intensity'])
    lightComponent.set_editor_property("mobility", unreal.ComponentMobility.MOVABLE)
    print(lightComponent.get_editor_property("mobility"))

def spawn_rect_lights(Rectlight):
    light_class = unreal.RectLight()
    # light_class.intensity = 10.0
    tx,ty,tz = convertLocation(Rectlight['location'])
    light_location = unreal.Vector(tx,ty,tz)
    # unreal.EditorLevelLibrary.spawn_actor_from_class(light_class, light_location)
    light = unreal.EditorLevelLibrary.spawn_actor_from_object(light_class, light_location)
    light.set_actor_label(Rectlight['title'])
    lightComponent = light.rect_light_component
    lightComponent.set_editor_property("intensity", Rectlight['intensity'])
    lightComponent.set_editor_property("mobility", unreal.ComponentMobility.MOVABLE)
    print(lightComponent.get_editor_property("mobility"))



for i in lights["pointlights"]:
    spawn_point_lights(i)
for i in lights["spotlights"]:
    spawn_spot_lights(i)
for i in lights["rectlights"]:
    spawn_rect_lights(i)


