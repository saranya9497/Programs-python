import numpy as np
import pandas as pd

# Generate random data
num_rows = 10
data = {
    "ID": np.arange(1, num_rows + 1),
    "Age": np.random.randint(18, 60, num_rows),
    "Salary": np.random.randint(30000, 100000, num_rows),
}

# Create DataFrame
df = pd.DataFrame(data)
print(df)
