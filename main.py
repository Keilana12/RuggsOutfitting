#!/usr/bin/env python

import os
from flask import Flask, render_template_string

app = Flask(__name__, static_folder='.')

# Configure cache control headers to prevent caching issues
@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

def render_page(template_name):
    """Helper function to render pages with header and footer"""
    try:
        # Read header
        with open(os.path.join('pages', 'header.html'), 'r') as f:
            header = f.read()
        
        # Read main content
        with open(os.path.join('pages', template_name), 'r') as f:
            content = f.read()
        
        # Read footer
        with open(os.path.join('pages', 'footer.html'), 'r') as f:
            footer = f.read()
        
        # Combine all parts
        full_html = header + content + footer
        return render_template_string(full_html)
    except Exception as e:
        return f"Error loading page: {e}"

@app.route('/')
def home():
    return render_page('index.html')

@app.route('/hunting')
def hunting():
    return render_page('hunting.html')

@app.route('/outfitting')
def outfitting():
    return render_page('outfitting.html')

@app.route('/ranch')
def ranch():
    return render_page('ranch.html')

@app.route('/contact')
def contact():
    return render_page('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
