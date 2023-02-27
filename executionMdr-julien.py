# %%
%pylab inline
import pandas as pd
import numpy as np
import seaborn as sns

sns.set(rc={'figure.figsize':(11.7,8.27)})

# %%
data = pd.read_csv("./execution.csv")
data.sample(20)

# %%


# %%
data["execution"] = data["Execution Volunteer"] == "yes"
gb = data.groupby("Sex")["execution"].mean()
sns.barplot(x = data["execution"], y = data["Sex"])

# %%
sns.barplot(x = data["Region"], y= data["Number of Victims"])

# %%
gb = data.groupby("Juvenile")["Number of Victims"]
sns.scatterplot(x=data["Juvenile"], y= data["Number of Victims"])

# %%
gb = data.groupby("Sex")["Number of Victims"].mean()
sns.barplot(x = gb.index, y = gb.values)

# %%
data["Number of Female Victim"] = data["Number of American Indian or Alaska Native Female Victims"] + data["Number of Asian Female Victims"] + data["Number of Black Female Victims"] + data["Number of Latino Female Victims"] + data["Number of Other Race Female Victims"] + data["Number of White Female Victims"]
gb = data.groupby("Sex")["Number of Female Victim"].mean()
sns.barplot(x = gb.index, y = gb.values)

# %%
data["Number of Male Victim"] = data["Number of Asian Male Victims"] + data["Number of Black Male Victims"] + data["Number of Latino Male Victims"] + data["Number of Other Race Male Victims"] + data["Number of White Male Victims"]
gb = data.groupby("Sex")["Number of Male Victim"].mean()
sns.barplot(x = gb.index, y = gb.values)

# %%
data["Femme"] = data["Sex"] == "Female"
gb = data.groupby("Victim(s) Race(s)")["Femme"].mean()
sns.histplot(x = gb.index, y= gb.values)

# %%
data["Meme Race"] = (data["Race"] == data["Victim(s) Race(s)"])
gb = data.groupby("Race")["Meme Race"].mean()
sns.barplot(x = gb.index, y = gb.values)


