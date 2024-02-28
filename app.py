import os
import io

from weasyprint import HTML
from flask import Flask, render_template, request, send_file
from datetime import datetime
from random import randrange

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    posted_data = request.get_json() or {}
    today = datetime.today().strftime("%B %d, %Y")
    invoice_number = randrange(1000, 9000, 2)
    default_data = {
        'duedate': 'January 1, 2034',
        'from_addr': {
        'addr1': '12345 Sunny Road',
        'addr2': 'Sunnyville, CA 12345',
        'company_name': 'Python Tip'
        },
        'invoice_number': 123,
        'items':[{
            'charge': 300.0,
            'title': 'website design'
            },
            {
            'charge': 75.0,
            'title': 'Hosting (3 months)'
            },
            {
            'charge': 10.0,
            'title': 'Domain name (1 year)'
            }
            ],
        'to_addr': {
            'company_name': 'Acme Corp',
            'person_email': 'john@example.com',
            'person_name': 'John Dilly'
        }
    }

    duedate = posted_data.get('duedate', default_data['duedate'])
    from_addr = posted_data.get('from_addr', default_data['from_addr'])
    to_addr = posted_data.get('to_addr', default_data['to_addr'])
    invoice_number = posted_data.get('invoice_number',
    default_data['invoice_number'])
    items = posted_data.get('items', default_data['items'])
    total = sum(item['charge'] for item in items)

    rendered =  render_template('invoice.html',
                            date = today,
                            from_addr = from_addr,
                            to_addr = to_addr,
                            items = items,
                            total = total,
                            invoice_number = invoice_number,
                            duedate = duedate)
    html = HTML(string=rendered)
    rendered_pdf = html.write_pdf()

    return send_file(
            io.BytesIO(rendered_pdf),
            attachment_filename='invoice.pdf'
            )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# html = HTML('invoice.html')
# html.write_pdf('invoice.pdf')