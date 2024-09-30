import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv(r'C:\HackRush\r1.xlsx')  # Replace 'your_data.csv' with the actual filename

# Ensure 'Day' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Create the enhanced time series plot
plt.figure(figsize=(14, 8))
sns.set_style("darkgrid")
sns.set_palette("deep")

# Main line plot
ax = sns.lineplot(x='Date', y='Count', data=df, linewidth=2, marker='o')

# Add a rolling average line
df['Rolling_Avg'] = df['Count'].rolling(window=7).mean()  # 7-day rolling average
sns.lineplot(x='Date', y='Rolling_Avg', data=df, color='red', label='7-day Rolling Average')

# Customize the plot
plt.title('Time Series of Count over Days', fontsize=20)
plt.xlabel('Day', fontsize=14)
plt.ylabel('Count', fontsize=14)

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Add annotations for max and min points
max_point = df.loc[df['Count'].idxmax()]
min_point = df.loc[df['Count'].idxmin()]

ax.annotate(f'Max: {max_point["Count"]}', 
            xy=(max_point['Date'], max_point['Count']),
            xytext=(10, 10), textcoords='offset points',
            arrowprops=dict(arrowstyle='->'))

ax.annotate(f'Min: {min_point["Count"]}', 
            xy=(min_point['Date'], min_point['Count']),
            xytext=(10, -10), textcoords='offset points',
            arrowprops=dict(arrowstyle='->'))

# Add a trend line
sns.regplot(x=df.index, y='Count', data=df, scatter=False, color='green', label='Trend')

# Enhance the legend
plt.legend(title='Legend', title_fontsize='13', fontsize='11')

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()

# Note: If you need additional columns for more advanced analysis, consider adding:
# - 'Category': to group data and use different colors for each category
# - 'Confidence': to show confidence intervals around the main line
# - 'Event': to mark significant events on the timeline

