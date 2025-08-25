import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def draw_cat_plot():
    # Load data
    df = pd.read_csv('medical_examination.csv')

    # Data preprocessing
    df['overweight'] = (df['weight'] / (df['height']/100)**2 > 25).astype(int)
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
    df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

    # Create a DataFrame for the cat plot
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Draw the catplot
    g = sns.catplot(data=df_cat, kind='bar', x='variable', y='total', hue='value', col='cardio')
    g.set_axis_labels('Variable', 'Total')
    g.set_titles('Cardio = {col_name}')
    plt.show()
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def draw_heat_map():
    # Load data
    df = pd.read_csv('medical_examination.csv')

    # Data preprocessing
    df = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate correlation matrix
    corr = df.corr()

    # Generate a mask for the upper triangle
    mask = corr.where(pd.np.triu(pd.np.ones(corr.shape), k=1).astype(bool))

    # Set up the matplotlib figure
    plt.figure(figsize=(10, 8))

    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', center=0, linewidths=0.5)

    plt.show()
