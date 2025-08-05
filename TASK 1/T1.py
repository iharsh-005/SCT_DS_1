import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('gender_distribution.csv')
plt.figure(figsize=(8, 6))
bars = plt.bar(
    data['Gender'], 
    data['Population (in Millions)'], 
    color=['#1E90FF', '#FF69B4', '#8A2BE2'],
    edgecolor='black',
    width=0.5
)
plt.title("Population Distribution by Gender", fontsize=16, weight='bold')
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Population (in Millions)", fontsize=12)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 5,
        f'{height}',
        ha='center',
        fontsize=11
    )

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("gender_distribution_chart.png", dpi=300)
plt.show()