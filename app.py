from flask import Flask, render_template
import folium
import pandas as pd

# Import data set
corona_df = pd.read_csv('data/newdata.csv')


def find_top_confirmed(n=15):
    '''
    Finds the top 'n' confirmed cases in all countries in the data set.
    '''
    by_country = corona_df.groupby('Country_Region').sum()[
        ['Confirmed', 'Deaths']]
    cdf = by_country.nlargest(n, 'Confirmed')[['Confirmed']]
    return cdf


cdf = find_top_confirmed()
pairs = [(country, confirmed)
         for country, confirmed in zip(cdf.index, cdf['Confirmed'])]

# Set corona_df object to have 3 necessary rows
corona_df = corona_df[['Lat', 'Long_', 'Confirmed']]
# Remove all rows with NULL values from DF
corona_df = corona_df.dropna()

# Create a folium map with center location
m = folium.Map(location=[34.223334, -82.461707],
               tiles='Stamen toner',
               zoom_start=8)


def circle_maker(x):
    '''
    Uses folium to create circles on the folium map,
    taking the lat/long locations through x, and showing the confirmed cases
    in the last 24 hours when hovered over.
    '''
    folium.Circle(location=[x[0], x[1]],
                  radius=float(x[2]) * 10,
                  color="red",
                  popup='confirmed cases:{}'.format(x[2])).add_to(m)


# Call the circle maker with the long and latitude coordinates
corona_df.apply(lambda x: circle_maker(x), axis=1)

# Linking python code to flask web page
html_map = m._repr_html_()
app = Flask(__name__)


@ app.route('/')
def home():
    return render_template("home.html", table=cdf, cmap=html_map, pairs=pairs)


if __name__ == '__main__':
    app.run(debug=True)
