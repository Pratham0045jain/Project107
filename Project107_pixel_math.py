import pandas as pd
import plotly_express as px

df = pd.read_csv("./Data/pixel_math.csv")
grouped_data = df.groupby("level")["attempt"].mean()

y = ["Level 1", "Level 2", "Level 3", "Level 4"]


student_df = df.loc[df["student_id"] == "TRL_xsl"]
student_data = df.groupby(["level", "student_id"], as_index = False)["attempt"].mean()


fig = px.scatter(student_data, x="student_id", y = "level", color = "attempt", size = 'attempt')
fig.show()

