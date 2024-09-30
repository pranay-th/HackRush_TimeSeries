import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os

DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://neondb_owner:Ijov0mkf6Ohl@ep-damp-dust-a11bi2qp-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require')
engine = create_engine(DATABASE_URL)

def get_data_from_db():
    query = "SELECT df.date, df.time, r.name as region, d.name as disease, COUNT(*) as frequency FROM disease_frequency df JOIN region r ON df.regionId = r.id JOIN disease d ON df.diseaseId = d.id GROUP BY df.date, df.time, r.name, d.name ORDER BY df.date, df.time"
    df = pd.read_sql(query, engine)
    return df

def plot_time_series_for_region():
    df = get_data_from_db()

    regions = ['Kolkata', 'Delhi', 'Pune']
    for region in regions:
        region_df = df[df['region'] == region]
        
        plt.figure(figsize=(14, 8))
        sns.set_style("darkgrid")
        sns.lineplot(x='date', y='frequency', data=region_df, linewidth=2, marker='o', label=region)
        
        region_df['Rolling_Avg'] = region_df['frequency'].rolling(window=7).mean()
        sns.lineplot(x='date', y='Rolling_Avg', data=region_df, color='red', label='7-day Rolling Average')
        
        plt.title(f'Time Series of Disease Frequency for {region}', fontsize=20)
        plt.xlabel('Date', fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        plt.savefig(f'static/{region}_time_series.png')
    
    # Return the file path for one of the images (e.g., Kolkata)
    return 'static/Kolkata_time_series.png'
