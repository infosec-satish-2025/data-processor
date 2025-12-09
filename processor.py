import pandas as pd
import numpy as np
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class DataProcessor:
    def __init__(self):
        self.database_url = os.getenv('DATABASE_URL')
        self.redis_url = os.getenv('REDIS_URL')
        
    def process_data(self, data_source):
        """Process data from various sources"""
        print(f"Processing data from {data_source}")
        
        # Simulate data processing
        df = pd.DataFrame({
            'timestamp': pd.date_range(start='2024-01-01', periods=100, freq='H'),
            'value': np.random.randn(100),
            'category': np.random.choice(['A', 'B', 'C'], 100)
        })
        
        # Clean data
        df = self.clean_data(df)
        
        # Validate data
        if self.validate_data(df):
            print("Data validation passed")
            return df
        else:
            print("Data validation failed")
            return None
    
    def clean_data(self, df):
        """Clean and prepare data"""
        # Remove duplicates
        df = df.drop_duplicates()
        
        # Handle missing values
        df = df.fillna(method='ffill')
        
        # Remove outliers
        df = df[np.abs(df['value'] - df['value'].mean()) <= (3 * df['value'].std())]
        
        return df
    
    def validate_data(self, df):
        """Validate data quality"""
        if df.empty:
            return False
        
        if df.isnull().sum().sum() > 0:
            return False
        
        return True
    
    def export_data(self, df, format='csv'):
        """Export processed data"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'processed_data_{timestamp}.{format}'
        
        if format == 'csv':
            df.to_csv(filename, index=False)
        elif format == 'json':
            df.to_json(filename, orient='records')
        elif format == 'parquet':
            df.to_parquet(filename, index=False)
        
        print(f"Data exported to {filename}")
        return filename

if __name__ == '__main__':
    processor = DataProcessor()
    data = processor.process_data('api_source')
    
    if data is not None:
        processor.export_data(data, format='csv')
