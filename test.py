from model import SimpleCNN
import torch

def test_model():
    model = SimpleCNN()
    x = torch.randn(1, 1, 28, 28)
    output = model(x)

    assert output.shape == (1, 10)
    print("Model test passed!")

if __name__ == "__main__":
    test_model()
