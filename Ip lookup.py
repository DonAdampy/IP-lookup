import requests
import tkinter as tk

def get_ip_details():
    ip = entry_ip.get()

    response = requests.get(f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,mobile,proxy,hosting,query')

    data = response.json()

    ipaddress = data['query']
    continett = data['continent']
    countryy = data['country']
    zipcode = data['zip']
    latt = data['lat']
    lonn = data['lon']
    ispp = data['isp']
    orgg = data['org']
    proxyy = data['proxy']
    hostingg = data['hosting']

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f'IP: {ipaddress}\nContinent: {continett}\nCountry: {countryy}\nZip Code: {zipcode}\nLat: {latt}\nLon: {lonn}\nIsp: {ispp}\nOrg: {orgg}\nProxy: {proxyy}\nHosting: {hostingg}')

window = tk.Tk()
window.title("IP Details Lookup")

label_ip = tk.Label(window, text="IP Address:")
label_ip.pack()

entry_ip = tk.Entry(window)
entry_ip.pack()

button_get_details = tk.Button(window, text="Get Details", command=get_ip_details)
button_get_details.pack()

result_text = tk.Text(window, height=10, width=40)
result_text.pack()

window.mainloop()
