import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', header=0, index_col='date', parse_dates=True)

# Clean data
df = df.drop(df[(df['value'] > df['value'].quantile(0.975)) | (df['value'] < df['value'].quantile(0.025))].index)

def draw_line_plot():
    # Draw line plot
    fig = df.plot(y='value', kind='line', figsize=(12,4), color='r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['day'] = df.index.day
    df_bar['month'] = df.index.month_name()
    df_bar['year'] = df.index.year

    avg_views = df_bar.groupby(['year', 'month'])['value'].mean()
    avg_views = avg_views.reset_index()
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    avg_views['month'] = pd.Categorical(avg_views['month'], categories=month_order, ordered=True)
    avg_views = avg_views.sort_values(by='month')
    avg_views = pd.pivot_table(data=avg_views, index='year', columns='month', values='value')
 
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    avg_views.plot(kind='bar', ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    plt.legend(title='Month')
 
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Year-wise box plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0]).get_figure()
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise box plot (Seasonality)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=month_order).get_figure()
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
