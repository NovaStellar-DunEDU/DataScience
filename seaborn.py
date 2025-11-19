import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = pd.read_csv('tips.csv')
sns.set_theme()

fig, axes = plt.subplots(1,2, figsize=(18,5))

sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", ax=axes[0])
axes[0].set_title("Scatter Plot: Total Bill vs Tip")

sns.lineplot(data=tips, x="size", y="total_bill", estimator="mean", ax=axes[1])

plt.tight_layout()
plt.show()