
### **🐍 script.py**
```python
import numpy as np
from sklearn.linear_model import LinearRegression

scores = list(map(int, input("Enter past test scores (comma-separated): ").split(",")))
X = np.arange(len(scores)).reshape(-1, 1)
y = np.array(scores)

model = LinearRegression().fit(X, y)
next_score = model.predict([[len(scores)]])

print(f"📈 Predicted Next Test Score: {next_score[0]:.2f}")
