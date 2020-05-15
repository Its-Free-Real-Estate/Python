import sys
from matplotlib import pyplot
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtGui import QPixmap

# Reads the csv file
data = pd.read_csv('Games.csv')

# Global sales graph

# Get x axis variable
filter1 = data.Name != 'Games'
data1 = data[filter1]

Names = list(data1.Name.unique())
# Y axis variable
Global_Sales = []

for i in Names:
    x = data1[data1.Name == i]
    Global_Sales.append(sum(x['Global_Sales'])/len(x))
df3 = pd.DataFrame({'Name': Names, 'Global_Sales': Global_Sales})

new_index = df3.Global_Sales.sort_values(ascending=False).index.values
sorted_data1 = df3.reindex(new_index)

# Size on the image length and height
plt.figure(figsize=(10.5, 9))
ax = sns.barplot(x=sorted_data1.Name, y=sorted_data1.Global_Sales, palette='deep')

# rotation of the words
plt.xticks(rotation=90)
# X axis label
plt.xlabel('Name')
# Y axis label
plt.ylabel('Global units sold (Millions)')
# Title of graph
plt.title('Top 10 Best Selling Games unit sales worldwide')
# Compresses graph into allocated space
plt.tight_layout()

# Saves graph as a png file
pyplot.savefig('Data1.png')

# European Sales graph

filter2 = data.Name != 'GamesEU'
data2 = data[filter2]

Names = list(data2.Name.unique())
EU_Sales = []

for i in Names:
    x = data2[data2.Name == i]
    EU_Sales.append(sum(x['EU_Sales'])/len(x))
df3 = pd.DataFrame({'Name': Names, 'EU_Sales': EU_Sales})

new_index = df3.EU_Sales.sort_values(ascending=False).index.values
sorted_data1 = df3.reindex(new_index)

plt.figure(figsize=(10.5, 9))
ax = sns.barplot(x=sorted_data1.Name, y=sorted_data1.EU_Sales, palette='deep')

plt.xticks(rotation=90)
plt.xlabel('Name')
plt.ylabel('European units sold (Millions)')
plt.title('Top 10 Best Selling Games unit sale in Europe')
plt.tight_layout()

pyplot.savefig('Data2.png')

# North American sales Graph


filter2 = data.Name != 'GamesNA'
data2 = data[filter2]

Names = list(data2.Name.unique())
NA_Sales = []

for i in Names:
    x = data2[data2.Name == i]
    NA_Sales.append(sum(x['NA_Sales'])/len(x))
df3 = pd.DataFrame({'Name': Names, 'NA_Sales': NA_Sales})

new_index = df3.NA_Sales.sort_values(ascending=False).index.values
sorted_data1 = df3.reindex(new_index)

plt.figure(figsize=(10.5, 9))
ax = sns.barplot(x=sorted_data1.Name, y=sorted_data1.NA_Sales, palette='deep')

plt.xticks(rotation=90)
plt.xlabel('Name')
plt.ylabel('North American units sold (Millions)')
plt.title('Top 10 Best Selling Games unit sales in North America')
plt.tight_layout()

pyplot.savefig('Data3.png')


# Japaneses sales Graph

filter2 = data.Name != 'GamesJapan'
data2 = data[filter2]

Names = list(data2.Name.unique())
JP_Sales = []

for i in Names:
    x = data2[data2.Name == i]
    JP_Sales.append(sum(x['JP_Sales'])/len(x))
df3 = pd.DataFrame({'Name': Names, 'JP_Sales': JP_Sales})

new_index = df3.JP_Sales.sort_values(ascending=False).index.values
sorted_data1 = df3.reindex(new_index)

plt.figure(figsize=(10.5, 9))
ax = sns.barplot(x=sorted_data1.Name, y=sorted_data1.JP_Sales, palette='deep')

plt.xticks(rotation=90)
plt.xlabel('Name')
plt.ylabel('Japanese units sold (Millions)')
plt.title('Top 10 Best Selling Games unit sales in Japan')
plt.tight_layout()

pyplot.savefig('Data4.png')

# Game ratings from Google Graph

filter2 = data.Name != 'Rating Google'
data2 = data[filter2]

Names = list(data2.Name.unique())
Rating_Google = []

for i in Names:
    x = data2[data2.Name == i]
    Rating_Google.append(sum(x['Rating_Google'])/len(x))
df3 = pd.DataFrame({'Name': Names, 'Rating_Google': Rating_Google})

new_index = df3.Rating_Google.sort_values(ascending=False).index.values
sorted_data1 = df3.reindex(new_index)

plt.figure(figsize=(10.5, 9))
ax = sns.barplot(x=sorted_data1.Name, y=sorted_data1.Rating_Google, palette='deep')

plt.xticks(rotation=90)
plt.xlabel('Name')
plt.ylabel('Average rating on Google')
plt.title('Top 10 Best Selling Games rating on Google')
plt.tight_layout()

pyplot.savefig('Data5.png')

# Games rating from GameStop

filter2 = data.Name != 'Rating GameStop'
data2 = data[filter2]

Names = list(data2.Name.unique())
Rating_GameStop = []

for i in Names:
    x = data2[data2.Name == i]
    Rating_GameStop.append(sum(x['Rating_GameStop'])/len(x))
df3 = pd.DataFrame({'Name': Names, 'Rating_GameStop': Rating_GameStop})

new_index = df3.Rating_GameStop.sort_values(ascending=False).index.values
sorted_data1 = df3.reindex(new_index)

plt.figure(figsize=(10.5, 9))
ax = sns.barplot(x=sorted_data1.Name, y=sorted_data1.Rating_GameStop, palette='deep')

plt.xticks(rotation=90)
plt.xlabel('Name')
plt.ylabel('Average rating on GameStop')
plt.title('Top 10 Best Selling Games rating on GameStop')
plt.tight_layout()

pyplot.savefig('Data6.png')

# Home Page


class App(QDialog):

    # loading Page1 qt file or home page

    def __init__(self):
        # Cant get rid of this python error
        super(App, self).__init__()
        loadUi('Page1.ui', self)
        self.setWindowTitle('Home')

        # Closes program

    def on_close_clicked(self):
        self.hide()
        sys.exit(app.exec_())

        # Sends user to the next page (Data)

    def on_next_clicked(self):
        # Cant get rid of this python error
        self.widget = Data()
        self.widget.show()
        self.hide()

# Unit sales data page


class Data(QDialog):

    # Loading Page2 qt file or unit sales Data page

    def __init__(self):
        # Cant get rid of this python error
        super(Data,self).__init__()
        loadUi('Page2.ui', self)
        self.setWindowTitle('Data')

        # Displays the Global sales data when opened

        label = self.label
        graph = QPixmap('Data1.png')
        label.setPixmap(graph)

        # Sends user back to the home screen

    def on_back_clicked(self):
        # Cant get rid of this python error
        self.widget = App()
        self.widget.show()
        self.hide()

        # Closes program

    def on_close_clicked(self):
        self.hide()
        sys.exit(app.exec_())

        # Goes to the rating page

    def on_next_clicked(self):
        # Cant get rid of this python error
        self.widget = Review()
        self.widget.show()
        self.hide()

        # On click will change the graph to Global sales data

    def on_global_clicked(self):
        image = QtGui.QImage(QtGui.QImageReader("Data1.png").read())
        self.label.setPixmap(QtGui.QPixmap(image))

        # On click will change the graph to European sales data

    def on_europe_clicked(self):
        image = QtGui.QImage(QtGui.QImageReader("Data2.png").read())
        self.label.setPixmap(QtGui.QPixmap(image))

        # On click will change the graph to North American sales data

    def on_america_clicked(self):
        image = QtGui.QImage(QtGui.QImageReader("Data3.png").read())
        self.label.setPixmap(QtGui.QPixmap(image))

        # On click will change the graph to Japanese sales data

    def on_japan_clicked(self):
        image = QtGui.QImage(QtGui.QImageReader("Data4.png").read())
        self.label.setPixmap(QtGui.QPixmap(image))

# Rating Page


class Review (QDialog):

    # Loads Page3 qt file or the ratings page

    def __init__(self):
        super(Review,self).__init__()
        loadUi('Page3.ui', self)
        self.setWindowTitle('Data')

        # Displays Google user rating graph when loaded.

        label = self.label
        graph = QPixmap('Data5.png')
        label.setPixmap(graph)

    # On click will change the graph to Google rating data

    def on_rating_clicked(self):
        image = QtGui.QImage(QtGui.QImageReader("Data5.png").read())
        self.label.setPixmap(QtGui.QPixmap(image))

    # On click will change the graph to GameStop rating data

    def on_game_stop_clicked(self):
        image = QtGui.QImage(QtGui.QImageReader("Data6.png").read())
        self.label.setPixmap(QtGui.QPixmap(image))

    # Next page button (Home page)

    def on_next_clicked(self):
        self.widget = App()
        self.widget.show()
        self.hide()

    # Sends user to the previous page

    def on_back_clicked(self):
        self.widget = Data()
        self.widget.show()
        self.hide()

    # Closes program

    def on_close_clicked(self):
        self.hide()
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = App()
    widget.show()
    sys.exit(app.exec_())

# exit code
