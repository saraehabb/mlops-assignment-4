from model import SimpleCNN
import torch

def train():
    model = SimpleCNN()
    x = torch.randn(1, 1, 28, 28)
    output = model(x)
    print("Training step successful. Output shape:", output.shape)

if __name__ == "__main__":
    train()
