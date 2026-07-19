import pandas as pd
import matplotlib.pyplot as plt

#data loading
df = pd.read_csv(r"C:\internship\codalpha\data science\task2\Unemployment in India.csv")
print(df.head())
print("\n Columns:\n",df.columns)
print("\n Info:\n")
df.info()
#data cleaning

df.columns=df.columns.str.strip()
df["Date"]=pd.to_datetime(df["Date"],dayfirst=True)
print("\nMissing values Before:\n",df.isnull().sum())
df=df.dropna()
print("Missing values After:\n",df.isnull().sum())
print("Data Cleaned Successfully")

#trend analysis
df=df.sort_values("Date")
trend=df.groupby("Date")['Estimated Unemployment Rate (%)'].mean()
plt.figure(figsize=(12,6))
plt.plot(trend.index,trend.values)
plt.title("Unemployment Rate Trend in India ")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate(%)")
plt.show()

#state analysis
state_unemployment=df.groupby("Region")['Estimated Unemployment Rate (%)'].mean()
top10=state_unemployment.sort_values(ascending=False).head(10)
print(top10)
plt.figure(figsize=(12,6))
top10.plot(kind="bar")
plt.title("Top 10 states by unemployment rate")
plt.xlabel("State")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.show()
 
#covid19 analysis
pre_covid=df[df["Date"]<"2020-03-01"]
post_covid=df[df["Date"]>="2020-03-01"]
print("Pre covid average unemployment rate: ",pre_covid["Estimated Unemployment Rate (%)"].mean())
print("Post covid avergae unemployment rate: ",post_covid["Estimated Unemployment Rate (%)"].mean())
plt.figure(figsize=(12,6))
plt.plot(pre_covid.groupby("Date")["Estimated Unemployment Rate (%)"].mean(),label="Pre-COVID")
plt.plot(post_covid.groupby("Date")["Estimated Unemployment Rate (%)"].mean(),label="Post-COVID")
plt.title("COVID-19 Impact on Unemployment in India")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.legend()
plt.show()

#seasonal trends
df["Month"] = df["Date"].dt.month
monthly_trend = df.groupby("Month")["Estimated Unemployment Rate (%)"].mean()
print(monthly_trend)
plt.figure(figsize=(10,5))
monthly_trend.plot(kind="bar")
plt.title("Seasonal Trend in Unemployment (Monthly)")
plt.xlabel("Month")
plt.ylabel("Unemployment Rate (%)")
plt.show()
