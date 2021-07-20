import pandas as pd

years_start = 25
years_end = 85

df = pd.read_csv('data/heart.csv')
df = df[df.trtbps >= 140]

bins = [i for i in range(years_start, years_end + 1, 10)]
labels = ['25-34', '35-44', '45-54', '55-64', '65-74', '75-84']

df['age_group'] = pd.cut(x=df['age'], bins=bins, labels=labels, right=False)

plot_data = df.groupby('age_group').mean()['thalachh']
plot = plot_data.plot(kind='bar', xlabel='Age', ylabel='Heartbeat',
                      title='Average heartbeat by age groups', figsize=(8, 5)).get_figure()
plot.savefig('heartbeat.jpeg', bbox_inches='tight')
