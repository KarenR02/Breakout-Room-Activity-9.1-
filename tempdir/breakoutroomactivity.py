from flask import Flask, render_template
import urllib 
import requests

sample = Flask(__name__)

@sample.route('/')

def main():
    #Getting the public/external IP address using an API
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

    #URL for the API that gets information from their external IP
    url = "https://ipapi.co/" + external_ip + "/json"

    #Getting the JSON data from the URL
    json_data = requests.get(url).json()

    ip = json_data['ip']
    version = json_data['version']
    city = json_data['city']
    region = json_data['region']
    country_name = json_data['country']
    isp = json_data['org']
    return render_template('index.html', html_ip = ip, html_version = version, html_city = city, html_region = region, html_country = country_name, html_isp = isp)

#return render_template('index.html', html_ip = ip, html_version = version, html_city = city, html_region = region, html_country = country_name, html_isp = isp)
if __name__ == "__main__":
    sample.run(host="0.0.0.0")