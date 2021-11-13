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
    json_info = requests.get(url).json()

    ISP = json_info['org']
    IP_Address = json_info['ip']
    IP_Version = json_info['version']
    Country = json_info['country']
    Region = json_info['region']
    City = json_info['city']
    Postal_Code = json_info['postal']
    
    
    return render_template('index.html', html_isp = ISP, html_ip = IP_Address, html_version = IP_Version, html_country = Country, html_region = Region, html_city = City, html_postal = Postal_Code )

if __name__ == "__main__":
    sample.run(host="0.0.0.0")