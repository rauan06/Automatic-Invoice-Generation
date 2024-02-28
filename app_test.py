import requests

url = 'http://127.0.0.1:5000/'
data = {
    'duedate': 'March 27, 2034',
    'from_addr': {
        'addr1': 'Fiftyville, ABC354',
        'addr2': 'New York, CA 12345',
        'company_name': 'Python Tip'
    },
    'items': [{
        'charge': 500.0,
        'title': 'Brochure design'
        },
    {
        'charge': 85.0,
        'title': 'Hosting (6 months)'
    },
    {
        'charge': 10.0,
        'title': 'Domain name (1 year)'
    }
    ],
    'to_addr': {
        'company_name': 'hula hoop',
        'person_email': 'john@example.com',
        'person_name': 'Yasoob Khalid'
    }
    }

html = requests.post(url, json=data)
with open('invoice.pdf', 'wb') as f:
    f.write(html.content)