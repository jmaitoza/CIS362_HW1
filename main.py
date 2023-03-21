# Problem 1
# gonna use columns: "num_shares" and "num_likes"
# scatter plot, bar chart, histogram

# create a python program that creates a scatter plot for one column from csv file in /datasets/
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("datasets/Facebook_LiveSellers_Thailand.csv")
dataset.head()
# scatter plot of column num_shares and num_likes
plt.scatter(dataset["num_loves"], dataset["num_likes"])
# make plot look nicer and less squished together
plt.xlim(-10, 600)
# plt.ylim(262, 1000)
# label the plot
plt.xlabel("Number of Loves")
plt.ylabel("Number of Likes")
# show plot
plt.show()

# # create a python program that creates a bar chart for one column from csv file in /datasets/
# # import numpy as np
# # import pandas as pd
# # import matplotlib.pyplot as plt
#
dataset = pd.read_csv("datasets/Facebook_LiveSellers_Thailand.csv")
dataset.head()
# bar chart of column num_shares and num_likes
plt.bar(dataset["num_loves"], dataset["num_likes"])
# make plot look nicer and less squished together
plt.xlim(-10, 550)
plt.ylim(0, 2700)
# label the plot
plt.xlabel("Number of Loves")
plt.ylabel("Number of Likes")

# change the x axis to increase by 50
plt.xticks(np.arange(0, 600, 50))

# show plot
plt.show()

# histogram of num_loves and num_likes
