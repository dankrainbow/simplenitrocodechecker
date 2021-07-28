import requests
import time
nitro = input("enter code you want to check:")
url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
validcodemsg= 'Code was Valid.'
response = requests.get(url)

if response.status_code == 200:
  print(validcodemsg)
  time.sleep(999)
else:
  print('Code invalid')
  print(response.status_code)
  time.sleep(999)
