import requests
import pandas as pd
from pandas import json_normalize

url = "https://www.coastlinecdjr.com/apis/widget/INVENTORY_LISTING_DEFAULT_AUTO_NEW:inventory-data-bus1/getInventory"
res = []

headers = {
    "cookie": "locale=en_US; DDC.postalCityState=RANCHOSANTAMARGARITA%2C%20CA%2C%20US; DDC.userCoordinates=33.6340%2C-117.6061; activeSession=true; __ssoid=808a15629de446d2a7fb511e88b898f5; _ga_last=undefined; userId=657b59908aa72657826b2e5f; _aeaid=56c05de0-3b90-42fd-a9bb-4ca4e20a06be; edmunds=6a2203cb-a204-4330-8da8-c838f9d1747b; AMCVS_3ECF483F53AB366E0A490D44%40AdobeOrg=1; 41086_cnpc_p=1.0; _edwpv=6e1af924-9eca-4d41-bcf2-8b81c9cdc5fa; 41086_cn_vid=6cdbebbd-c8e9-4295-a9c2-bcae98cc4ddb; 41086_cn_oref=https://www.google.com/; aelastsite=%2FA9xEY%2BES%2BEhLowyOa99YyVhZV9DTB2maI6rH%2Bue4i%2FVbZ1eoepjv8ZpmjHfxC9P; aelreadersettings=%7B%22c_big%22%3A0%2C%22rg%22%3A0%2C%22memph%22%3A0%2C%22contrast_setting%22%3A0%2C%22colorshift_setting%22%3A0%2C%22text_size_setting%22%3A0%2C%22space_setting%22%3A0%2C%22font_setting%22%3A0%2C%22k%22%3A0%2C%22k_disable_default%22%3A0%2C%22hlt%22%3A0%2C%22disable_animations%22%3A0%2C%22display_alt_desc%22%3A0%7D; forty_n_fbuid=dd69c4494f927ebec4490e56f2a15bdbc0ab0b951272358bc20c7e341d19ba41; caconsentcookie={'version':'1.0','categories':{'general':False,'performance':False,'functional':False,'targeting':False,'statistics':False},'updatedAt':'2023-12-15T23:13:51.617Z','expiresAt':'2024-12-14T23:13:51.617Z','consentMethod':'OPT_IN','hasInteractedWithBanner':True,'limitSensitivePersonalData':None}; userProfileId=65832a8cb5b8f578701fc218; MYCARS_PROFILE=65832a8cb5b8f578701fc218; DDC.postalCode=89101; ddc_diag_akam_clientIP=2600:6c50:93f:633d:40cc:481b:68fb:78e6; ddc_diag_akam_fullPath=/akam-sw-policy.json; callTrackingSessionId=kjjut9rhs1lr85xaqn; mycars=recentCars%3A4%3BsavedCars%3A0%3BpriceAlerts%3A0%3B; edw=908500544276125382; _edwps=470979788832922597; _edwvts=908500544276125382; bm_mi=BD0E10245B2F0C3574F631E25712DC9C~YAAQB608F4AygPSMAQAAKqrQ9BY066LfjqKIhgZWtRB1hCrQGGa4sRRI0YdSIlhFRYrh+JNDE3PmGGKgdi0m9B8cUMtoH3430q5E2wL2wXEtBoUVoRmXbdnwK4P67ve2WQZspfIDdyUNf2wRjoztMBmLVevHHutF8AdflIhKOX3pzwHEaWwqE5PUktpFtuNwQ09E0D4gX+HGq6rOaPsh5HmpD7LphaZqhP9FOYjLf9zyuR5YJtADKqpcsERRtoBpVZdXdf0aamF/Io4EKwsMq0dNg+TuXB0GJMhSqYiddTpTrHavbXpLKItq03vq2Ox4deLtnNy1eVberF9BQvgoLVlCrWG9ke/ElTXmbjMklRZ3u1fnH/vtdgUND/8=~1; ak_bmsc=861262BEB91B0E6E92EF03C7B64798B6~000000000000000000000000000000~YAAQB608F5E7gPSMAQAAT+DR9BaU8gfelIpgp92Y0Lwi3lOig4NW34yUutNsUNc0ySZzFJFTc+VxYUY18WS3KsRVNRXghFFzYFthtuGS2Tyi7rKYcYHv/swWf1oM/PHP0KWnccVfMvpwnBrfg3fbLdHr/q6novmVnJGYh39HAHeI65SL1RmFM9c9kGQCMzjTGonlNVaAoJNQm8yNMNwgKtqcwad3XRpf2oWK9jntGr/p7DJNOl+sy0lcxTj9CHeJne2+2tUjUR7CRH9XGG1QTbWvDuH/E14gxB4Kb8s6/krIpfQkRFEYczUNWuOsoWZRaC89y35MjoIOTvVd03Ej9tzIv5I8oCURvVtgXsaJl2I3mKkMKMf2e6xihi67wcPixPBGKEH8I+GhFNCAq7XHuYZ/sh23KWPuv3BIcOZNIwCPmdGQlMGGLDO9clfAABNe4Mnzet+cFnxNSACZ+cAg2fVTTNdVmzEG1diLOFjQYQwTcOeKm/6ZObn3jrVcQgWHLn40IOOXJRi6++o=; ddc_diag_akam_currentTime=1704914580; ddc_diag_akam_requestID=1183a6; ddc_diag_akam_ghostIP=2600:1406:6c00::173c:ad0b; forty_n_user=v2D8JChR2AvRK2h4STNaVEtubVBlTGpLYXJiMGtIQTcyZEprREUvMlIrdk9XWFVGSmNIVT0~; forty_n_t=1.fbaf61.1702582675.11.9.1704914252.1704914589.4.0; aeatstartmessage=true; lastItemViewed=%7B%22eventTimestamp%22%3A1704914768502%2C%22dealerCode%22%3Anull%2C%22vehicleType%22%3A%22new%22%2C%22make%22%3A%22Jeep%22%2C%22model%22%3A%22Gladiator%22%2C%22bodyStyle%22%3A%22SUV%22%2C%22vin%22%3Anull%2C%22vehicleId%22%3A%22c47461ab0a0e081d14e53636857f26c0%22%2C%22stockNumber%22%3Anull%2C%22year%22%3A2023%2C%22price%22%3A61551%2C%22pageType%22%3Anull%2C%22listingType%22%3Anull%2C%22listingDomain%22%3Anull%2C%22listingCode%22%3Anull%2C%22mpgCity%22%3A16%2C%22mpgHighway%22%3A23%2C%22odometer%22%3A19%7D; AMCV_3ECF483F53AB366E0A490D44%40AdobeOrg=179643557%7CMCIDTS%7C19732%7CMCMID%7C88547670598664807662567694004300203254%7CMCAID%7CNONE%7CMCOPTOUT-1704921971s%7CNONE%7CvVersion%7C5.5.0; bm_sv=597F76A23F088143B41F6781E8B4ED4A~YAAQNK08FwBj+maMAQAAk9/W9BaRdPIIABj4A0wDNHZIlP5dBL/1U0xl6JTh0YiQt/xXGqddciYEmtJAKYtlP1pbGg7PdQk/PeclcP1uh7SZY54t4KKCKwrml7rnqRmvcX3mLnZzLzanrfEruXGWeMf51FN/xsycaN2FRe0yCtQe/IyF71kzg0n2636ScALvj0D3yEu/4SmSpxN0f4/EgKSP0opBroOSJj0ADMKWaQVzADI2RF4Yi/RjS8falwBAsG4Vz3M0NaY=~1",
    "authority": "www.coastlinecdjr.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.coastlinecdjr.com/new-inventory/index.htm",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

start_value = 0

while True:
    params = {
        "start": start_value,
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        if not data['pageInfo']['trackingData']:
            break

        for p in data['pageInfo']['trackingData']:
            res.append(p)

        start_value += 18
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        break

print(data)


df = pd.json_normalize(res)

df = df.assign(id=df['vin'])

df = df.assign(vehicle_id=df['vin'])

df = df.assign(condition=df['newOrUsed'])

df = df.assign(exterior_color=df['exteriorColor'])

df.rename(columns={"old_transmission": "transmission"}, inplace=True)

df['transmission'] = 'automatic'

df = df.assign(state_of_vehicle=df['condition'])

df['body_style'] = 'other'

df['title'] = df['condition'].str.capitalize() + ' ' + df['modelYear'].astype(str) + ' ' + df['make'] + ' ' + df['model'] + (' ' + df['trim'] if not df['trim'].isnull().values.any() else '') + ' ' + df['bodyStyle']

df['description'] = df['condition'].str.capitalize() + ' ' + df['modelYear'].astype(str) + ' ' + df['make'] + ' ' + df['model'] + (' ' + df['trim'] if not df['trim'].isnull().values.any() else '') + ' ' + df['bodyStyle']

df = df.assign(year=df['modelYear'])

df.rename(columns={"old_condition": "condition"}, inplace=True)

df['condition'] = 'EXCELLENT'

df['visibility'] = 'active'

df['mileage.value'] = 0

df['mileage.unit'] = 'MI'

df = df.assign(region=df['address.state'])

# address = {
#     'addr1': '32881 Camino Capistrano',
#     'city': 'San Juan Capistrano',
#     'region': 'CA',
#     'postal_code': '92675-4509',
#     'country': 'US'
# }

# df['address'] = [address] * len(df)

def get_address(row):
    if 'accounts' in data and 'coastlinechryslerdodgejeepramcllc' in data['accounts']:
        account_info = data['accounts']['coastlinechryslerdodgejeepramcllc']
        address_info = account_info.get('address')
        if address_info:
            return (
                address_info['firstLineAddress'] + ', ' + 
                address_info['city'] + ', ' + 
                address_info['state'] + ' ' + 
                address_info['postalCode'] + ', ' + 
                address_info['country']
            )
    return None

# Apply the function to create the address column
df['address'] = df.apply(get_address, axis=1)

# address
# if 'accounts' in data:
#     accounts_data = data['accounts']
#     print("Accounts keys:", accounts_data.keys())
#     if 'coastlinechryslerdodgejeepramcllc' in accounts_data:

#         address_info = accounts_data['coastlinechryslerdodgejeepramcllc'].get('address')
#         if address_info:
#             df['address'] = (
#                 address_info['firstLineAddress'] + ', ' + 
#                 address_info['city'] + ', ' + 
#                 address_info['state'] + ' ' + 
#                 address_info['postalCode'] + ', ' + 
#                 address_info['country']
#             )
#         else:
#             print("No address info for coastlinechryslerdodgejeepramcllc")
#     else:
#         print("coastlinechryslerdodgejeepramcllc not found in accounts")
# else:
#     print("No accounts data in the response")
  # address end  

# if 'accounts' in data:
#     accounts_data = data['accounts']
#     print("response.text:", response.text)
#     if 'coastlinechryslerdodgejeepramcllc' in accounts_data:
#         address_info = accounts_data['coastlinechryslerdodgejeepramcllc'].get('address')
#         if address_info:
#             df['address'] = (
#                 address_info['firstLineAddress'] + ', ' + 
#                 address_info['city'] + ', ' + 
#                 address_info['state'] + ' ' + 
#                 address_info['postalCode'] + ', ' + 
#                 address_info['country']
#             )
#         else:
#             print("No address info for coastlinechryslerdodgejeepramcllc")
#     else:
#         print("coastlinechryslerdodgejeepramcllc not found in accounts")
# else:
#     print("No accounts data in the response")

    
df['availability'] = 'available'

df['price'] = df['pricing.finalPrice'].replace('[^\d.]', '', regex=True).astype(float)

df['price'] = df['price'].map('{:,.0f} USD'.format)

df.rename(columns={"link": "old_link"}, inplace=True)

df['url'] = 'https://www.coastlinecdjr.com' + df['old_link']

image_data = df['images'].apply(lambda x: {str(img['id']): (img['uri'], img['thumbnail']['uri']) for img in x})

image_columns = {}
for img_dict in image_data:
    for img_id, img_urls in img_dict.items():
        if img_id not in image_columns:
            image_columns[img_id] = {'uri': [], 'thumbnail_uri': []}
        image_columns[img_id]['uri'].append(img_urls[0])
        image_columns[img_id]['thumbnail_uri'].append(img_urls[1])

for img_id, img_urls in image_columns.items():
    df[f'image[{img_id}].url'] = img_urls['uri'] + [float('nan')] * (len(df) - len(img_urls['uri']))
    df[f'image[{img_id}].thumbnail_url'] = img_urls['thumbnail_uri'] + [float('nan')] * (len(df) - len(img_urls['thumbnail_uri']))

df.to_csv('results_address.csv', index=False)

print(f"Scraping completed for all pages.")

