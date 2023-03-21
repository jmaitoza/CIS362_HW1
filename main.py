# Problem 1
# picking column num_loves & num_likes as our x values and num_reactions as our y values which will always be compared against
# scatter plot, bar chart, histogram

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import altair_viewer

dataset = pd.read_csv("datasets/Facebook_LiveSellers_Thailand.csv")
dataset.head()
xcol1 = pd.DataFrame(dataset, columns = ["num_loves"])
xcol2 = pd.DataFrame(dataset, columns = ["num_likes"])
ycol = pd.DataFrame(dataset, columns = ["num_reactions"])

# scatter plot for num_loves vs num_reactions
plt.scatter(xcol1, ycol)
plt.title("num_loves vs num_reactions")
plt.xlabel("num_loves")
plt.ylabel("num_reactions")
plt.xlim(-40 , 800)
plt.ylim(-300 , 4000)
plt.show()

# scatter plot for num_likes vs num_reactions
plt.scatter(xcol2, ycol)
plt.title("num_likes vs num_reactions")
plt.xlabel("num_likes")
plt.ylabel("num_reactions")
plt.xlim(-40 , 2000)
plt.ylim(-300 , 2500)
plt.show()

# histogram for num_loves
plt.hist(xcol1, bins = 7)
plt.title("Num Loves Histogram")
plt.xlabel("Num Loves")
plt.ylabel("Frequency")
plt.xlim(-10, 400)
# make x axis ticks every 25
plt.xticks(np.arange(0, 400, 50))
plt.show()

# histogram for num_likes
plt.hist(xcol2, bins = 7)
plt.title("Num Likes Histogram")
plt.xlabel("Num Likes")
plt.ylabel("Frequency")
# plt.xlim(-10, 400)
# plt.ylim(0, 3000)
plt.show()