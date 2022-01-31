import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder, RobustScaler, MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

data = pd.read_csv("scope_2_1.csv")
plt.figure(figsize=(12, 6))
plt.title("Volate")

plt.plot(data["second"], data["Volt"])
plt.show()
