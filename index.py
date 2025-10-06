from flask import Flask

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import interp1d

app = Flask(__name__)

@app.route("/")
def index():
    df= pd.read_csv('Reporte Flotacion.csv')
    #df.head()
    return len(df)

if __name__=="__main__":
	app.run(debug=True)