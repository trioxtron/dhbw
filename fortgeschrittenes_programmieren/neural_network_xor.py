import random
import math
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

class Neuron():
    def __init__(self):
        self.w1 = random.uniform(-1, 1)
        self.w2 = random.uniform(-1, 1)
        self.b = random.uniform(-1, 1)

        self.last_input = (0, 0)
        self.last_raw_output = 0
        self.last_output = 0


    def predict(self, x1, x2):
        # Calculate the output of the neuron
        output = (self.w1 * x1 + self.w2 * x2) + self.b
        activated = sigmoid(output)

        self.last_input = (x1, x2)
        self.last_raw_output = output
        self.last_output = activated

        return activated


    def update_weights(self, error, learning_rate=0.1):
        x1, x2 = self.last_input
        self.w1 -= learning_rate * error * x1
        self.w2 -= learning_rate * error * x2

        self.b -= learning_rate * error


class Network():
    def __init__(self):
        self.hidden = [Neuron(), Neuron()]
        self.output = Neuron() 


    def predict(self, x1, x2):
        hidden_x1 = self.hidden[0].predict(x1, x2)
        hidden_x2 = self.hidden[1].predict(x1, x2)

        return 1 if self.output.predict(hidden_x1, hidden_x2) > 0.5 else 0


    def train(self, x1, x2, target, lr=0.1):
        hidden_x1 = self.hidden[0].predict(x1, x2)
        hidden_x2 = self.hidden[1].predict(x1, x2)
        output = self.output.predict(hidden_x1, hidden_x2)

        error = output - target
        d_out = error * sigmoid_derivative(self.output.last_raw_output)

        self.output.update_weights(lr, d_out)

        dh1 = d_out * self.output.w1 * sigmoid_derivative(self.hidden[0].last_raw_output)
        dh2 = d_out * self.output.w2 * sigmoid_derivative(self.hidden[1].last_raw_output)

        self.hidden[0].update_weights(dh1, lr)
        self.hidden[1].update_weights(dh2, lr)

        return error**2

def main():
    net = Network()
    training_data = [
        (1, 1, 0),
        (1, 0, 1),
        (0, 1, 1),
        (0, 0, 0)
    ]

    losses = []

    for epoch in range(10000):
        loss = 0
        for x1, x2, target in training_data:
            loss += net.train(x1, x2, target)

        print(f"Epoch: {epoch} – Loss: {loss}")
        losses.append(loss)

    plt.plot(losses)
    plt.xlabel("Epoch")
    plt.ylabel("Total Squared Error")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
        

    for x1, x2, _ in training_data:
        print(f"Input: ({x1}, {x2}) – Predicted: {net.predict(x1, x2):.4f}")


if __name__ == "__main__":
    main()
