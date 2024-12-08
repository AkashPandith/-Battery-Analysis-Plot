import pandas as pd
import plotly.express as px
dataset_path = r"C:\Users\akash\Desktop\Battery Data Analysis\cleaned_dataset\metadata.csv"
df = pd.read_csv(dataset_path)
columns = ['uid', 'Re', 'Rct']
subset_data = df[columns].dropna()

plot_re = px.line(subset_data, x='uid', y='Re',
                 title='Electrolyte Resistance (Re) vs Cycle Count',
                 labels={'cycle_count': 'Cycle Count', 'Re': 'Electrolyte Resistance (Ohms)'})
plot_re.show()

plot_rct = px.line(subset_data, x='uid', y='Rct',
                  title='Charge Transfer Resistance (Rct) vs Cycle Count',
                  labels={'cycle_count': 'Cycle Count', 'Rct': 'Charge Transfer Resistance (Ohms)'})
plot_rct.show()

