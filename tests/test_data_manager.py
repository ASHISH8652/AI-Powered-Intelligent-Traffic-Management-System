from traffic_ai.integration import DataManager


def test_data():

    DataManager.update_vehicle_count(3500)

    DataManager.update_density("Medium")

    DataManager.update_prediction(3720)

    data = DataManager.get_data()

    print(data)


if __name__ == "__main__":

    test_data()