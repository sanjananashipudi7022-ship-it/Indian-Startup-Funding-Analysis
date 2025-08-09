import pandas as pd
df=pd.read_csv('/content/startup_funding.csv')
display(df.head())
display(df.info())

if 'date' in df.columns:
            trend_data = df.groupby(df['date'].dt.year)['amount_in_usd'].sum().reset_index()
            plt.figure(figsize=(8, 5))
            sns.lineplot(data=trend_data, x='date', y='amount_in_usd', marker='o')
            plt.title("Funding Trends Over Time")
            plt.xlabel("Year")
            plt.ylabel("Total Funding (USD)")
            plt.tight_layout()
            plt.show(block=False)
            plt.pause(0.1)

if 'Industry Vertical' in df.columns: # Changed 'industry_vertical' to 'Industry Vertical' based on df.columns output
            plt.figure(figsize=(8, 5))
            top_sectors = df['Industry Vertical'].value_counts().head(5) # Changed 'industry_vertical' to 'Industry Vertical'
            sns.barplot(x=top_sectors.values, y=top_sectors.index)
            plt.title("Top 5 Sectors by Startup Count")
            plt.xlabel("Number of Startups")
            plt.ylabel("Sector")
            plt.tight_layout()
            plt.show(block=False)
            plt.pause(0.1)


        # Top startups
if 'Startup Name' in df.columns: # Changed 'startup_name' to 'Startup Name' based on df.columns output and fixed indentation
            plt.figure(figsize=(8, 5))
            top_startups = df['Startup Name'].value_counts().head(5) # Changed 'startup_name' to 'Startup Name'
            sns.barplot(x=top_startups.values, y=top_startups.index)
            plt.title("Top 5 Startups by Funding Count")
            plt.xlabel("Number of Fundings")
            plt.ylabel("Startup")
            plt.tight_layout()
            plt.show(block=False)
            plt.pause(0.1)

if 'investors_name' in df.columns:
            plt.figure(figsize=(8, 5))
            top_investors = df['investors_name'].value_counts().head(5)
            sns.barplot(x=top_investors.values, y=top_investors.index)
            plt.title("Top 5 Active Investors")
            plt.xlabel("Number of Investments")
            plt.ylabel("Investor")
            plt.tight_layout()
            plt.show(block=False)
            plt.pause(0.1)

if 'InvestmentnType' in df.columns:
    inv_type_dist = df['InvestmentnType'].value_counts()
    print("\nInvestment Type Distribution:")
    print(inv_type_dist)

funding_trend = df.groupby(df['Date dd/mm/yyyy'].dt.to_period('M'))['Amount in USD'].sum()
funding_trend.plot(kind='line', figsize=(12,6), marker='o')
plt.title("Funding Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Total Funding (USD)")
plt.show()