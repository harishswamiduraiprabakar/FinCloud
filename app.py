from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

# Sample data
def generate_sample_data():
    base_date = datetime.today()
    return [
        {
            'date': (base_date - timedelta(days=i)).strftime('%Y-%m-%d'),
            'amount': 10000 + i * 2000,
            'profit': 3000 + i * 500,
            'tax': 500 + i * 100,
            'outstanding': 2000 + i * 300,
            'payments_received': 9000 + i * 1800,
            'payments_made': 4000 + i * 700,
            'invoice_id': f'INV-{1000 + i}'
        }
        for i in range(7)
    ]

@app.route('/')
def index():
    data = generate_sample_data()

    totals = {
        'amount': sum(item['amount'] for item in data),
        'profit': sum(item['profit'] for item in data),
        'tax': sum(item['tax'] for item in data),
        'outstanding': sum(item['outstanding'] for item in data),
        'payments_received': sum(item['payments_received'] for item in data),
        'payments_made': sum(item['payments_made'] for item in data),
        'invoices': len(data)
    }

    return render_template('index.html', data=data, totals=totals)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

