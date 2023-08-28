from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [120, 80, 30, 20, 45]
labels = ['blah', 'blah', 'blah', 'blah', 'blah']
colors = ['#eba5ac', '#edc0c4', '#cfe5df', '#8fcdb5', '#56a088']

plt.pie(slices, labels=labels, colors=colors,
         wedgeprops={'edgecolor': 'black'})

plt.title("**perfect piechart by Viktoriia**")
plt.tight_layout()
plt.show()