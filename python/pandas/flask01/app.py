from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)




@app.route('/')
def show_excel():
    df = pd.read_csv(r"D:\tianxingzhe\python\pandas\data\Titanic-Dataset.csv")
    table_html = df.to_html()
    return f"""
        <html>
            <body>
                <h1>Titanic乘客信息表</h1>
                <div>{table_html}</div>
            </body>
        </html>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0")
