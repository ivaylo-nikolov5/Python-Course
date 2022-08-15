def start_spring(**kwargs):
    result = ""
    objects = {}
    for object, type_ in kwargs.items():
        if type_ not in objects:
            objects[type_] = []
        objects[type_].append(object)

    objects = dict(sorted(objects.items(), key=lambda x:(-len(x[1]), x[0])))

    for type_, object in objects.items():
        result += f"{type_}: \n"
        object = sorted(object)
        for obj in object:
            result += f"-{obj}\n"

    return result

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

