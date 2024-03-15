from roboflow import Roboflow
rf = Roboflow(api_key="")
project = rf.workspace().project("car_logo_detect")
model = project.version(1).model


# infer on a local image
print(model.predict("222.png", confidence=40, overlap=30).json())
