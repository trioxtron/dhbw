import random

class Neuron():
    def __init__(self):
        self.w1 = random.random()
        self.w2 = random.random()
        self.b = random.random()


    def learn(self, clouds, temp_drop, expected_output):
        error = self.predict(clouds, temp_drop) - expected_output

        self.w1 -= 0.01 * error * clouds
        self.w2 -= 0.01 * error * temp_drop
        self.b -= 0.01 * error 

    def predict(self, clouds, temp_drop):
        # Calculate the output of the neuron
        output = (self.w1 * clouds + self.w2 * temp_drop) + self.b
        # Apply the activation function (step function)
        return 1 if output > 0.5 else 0


def main():
    neuron = Neuron()

    training_data = [
        (1, 1, 1),  # Cloudy and temp drop, will rain
        (1, 0, 0),  # Not cloudy and temp drop, will not rain
        (0, 1, 0),  # Cloudy and temp drop, will rain
        (0, 0, 0),  # Not cloudy and temp drop, will not rain
    ]
    # Train the neuron with the training data
    for _ in range(10000):
        for clouds, temp_drop, expected_output in training_data:
            neuron.learn(clouds, temp_drop, expected_output)

    # Test the neuron with new data
    for _ in range(10):
        test_clouds = 1  # Example cloudiness
        test_temp_drop = 1  # Example temperature drop
        will_rain = neuron.predict(test_clouds, test_temp_drop)
        
        if will_rain:
            print("It will rain.")


if __name__ == "__main__":
    main()
