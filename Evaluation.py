import numpy as np
import json

try:
    from keras.layers import Dense
    from keras.models import model_from_json, Sequential

    class PlaceNNet:
        def __init__(self, load=False):
            if load:
                with open("./temp/place_config.json", 'r') as f:
                    self.model = model_from_json(json.load(f))
                self.model.load_weights("./temp/place_weights_curr.h5")
            else:
                self.model = Sequential([
                    Dense(128, input_dim=64, activation="relu"),
                    Dense(128, activation="relu"),
                    Dense(128, activation="relu"),
                    Dense(128, activation="relu"),
                    Dense(128, activation="relu"),
                    Dense(64, activation="tanh")
                ])
                with open("./temp/place_config.json", 'w') as f:
                    json.dump(self.model.to_json(), f)
            self.model.compile(loss="mse", optimizer="adam")

    class MoveNNet:
        def __init__(self, load=False):
            if load:
                with open("./temp/move_config.json", 'r') as f:
                    self.model = model_from_json(json.load(f))
                self.model.load_weights("./temp/move_weights_curr.h5")
            else:
                self.model = Sequential([
                    Dense(1024, input_dim=64, activation="relu"),
                    Dense(1024, activation="relu"),
                    Dense(1024, activation="relu"),
                    Dense(1024, activation="relu"),
                    Dense(1024, activation="relu"),
                    Dense(512, activation="tanh")
                ])
                with open("./temp/move_config.json", 'w') as f:
                    json.dump(self.model.to_json(), f)
            self.model.compile(loss="mse", optimizer="adam")
except ModuleNotFoundError:
    class PlaceNNet:
        pass

    class MoveNNet:
        pass


class Evaluation:
    def __init__(self, load=False):
        self.place = PlaceNNet(load)
        self.move = MoveNNet(load)

    def predict(self, board):
        if board.placing:
            return self.place.model.predict(board.canonical)
        return self.move.model.predict(board.canonical)

    def save(self, key, suffix):
        self.place.model.save_weights(f"./temp/place_weights_{suffix}.h5")
        self.move.model.save_weights(f"./temp/move_weights_{suffix}.h5")

    def train(self, board, vv):
        if board.placing:
            self.place.model.fit(board.canonical, vv)
        else:
            self.move.model.fit(board.canonical, vv)
