from traffic_ai.prediction.model_loader import ModelLoader


loader = ModelLoader()

loader.load()

print(loader.get_metadata())

print(loader.get_features())