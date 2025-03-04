import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_regression

# Linear Regression Model
class LinearRegressionModel(nn.Module):
    def __init__(self, input_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, 1)
    
    def forward(self, x):
        return self.linear(x)

# Two-Layer Neural Network
class TwoLayerNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(TwoLayerNN, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, x):
        x = F.relu(self.fc1(x))
        return self.fc2(x)

# Generating Regression Data
X, y = make_regression(n_samples=1000, n_features=5, noise=0.1)
y = y.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Training Linear Regression Model
lr_model = LinearRegressionModel(input_dim=5).to(device)
optimizer = optim.SGD(lr_model.parameters(), lr=0.01)
criterion = nn.MSELoss()

X_train_torch = torch.tensor(X_train, dtype=torch.float32).to(device)
y_train_torch = torch.tensor(y_train, dtype=torch.float32).to(device)

for epoch in range(100):
    optimizer.zero_grad()
    predictions = lr_model(X_train_torch)
    loss = criterion(predictions, y_train_torch)
    loss.backward()
    optimizer.step()
    if epoch % 10 == 0:
        print(f'Epoch {epoch}: Loss = {loss.item()}')

print("Linear Regression Model Trained!")

# Training Two-Layer Neural Network
nn_model = TwoLayerNN(input_dim=5, hidden_dim=10, output_dim=1).to(device)
nn_optimizer = optim.Adam(nn_model.parameters(), lr=0.01)

for epoch in range(100):
    nn_optimizer.zero_grad()
    predictions = nn_model(X_train_torch)
    loss = criterion(predictions, y_train_torch)
    loss.backward()
    nn_optimizer.step()
    if epoch % 10 == 0:
        print(f'Epoch {epoch}: NN Loss = {loss.item()}')

print("Two-Layer Neural Network Trained!")

# Contoh data baru untuk prediksi
new_data = torch.tensor([[0.5, -1.2, 0.3, 0.8, -0.5]], dtype=torch.float32)

# Prediksi dengan model linear regression
lr_model.eval()
predicted_value = lr_model(new_data)
print(f"Prediksi Linear Regression: {predicted_value.item()}")

# Prediksi dengan Two-Layer Neural Network
nn_model.eval()
predicted_nn_value = nn_model(new_data)
print(f"Prediksi Neural Network: {predicted_nn_value.item()}")
