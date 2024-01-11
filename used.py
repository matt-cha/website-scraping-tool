import requests
import pandas as pd

url = "https://www.coastlinecdjr.com/apis/widget/INVENTORY_LISTING_DEFAULT_AUTO_USED:inventory-data-bus1/getInventory"
res = []

headers = {
    "cookie": "locale=en_US; DDC.postalCityState=RANCHOSANTAMARGARITA%2C%20CA%2C%20US; DDC.userCoordinates=33.6340%2C-117.6061; activeSession=true; __ssoid=808a15629de446d2a7fb511e88b898f5; _ga_last=undefined; userId=657b59908aa72657826b2e5f; _aeaid=56c05de0-3b90-42fd-a9bb-4ca4e20a06be; edmunds=6a2203cb-a204-4330-8da8-c838f9d1747b; AMCVS_3ECF483F53AB366E0A490D44%40AdobeOrg=1; 41086_cnpc_p=1.0; _edwpv=6e1af924-9eca-4d41-bcf2-8b81c9cdc5fa; 41086_cn_vid=6cdbebbd-c8e9-4295-a9c2-bcae98cc4ddb; 41086_cn_oref=https://www.google.com/; aelastsite=%2FA9xEY%2BES%2BEhLowyOa99YyVhZV9DTB2maI6rH%2Bue4i%2FVbZ1eoepjv8ZpmjHfxC9P; aelreadersettings=%7B%22c_big%22%3A0%2C%22rg%22%3A0%2C%22memph%22%3A0%2C%22contrast_setting%22%3A0%2C%22colorshift_setting%22%3A0%2C%22text_size_setting%22%3A0%2C%22space_setting%22%3A0%2C%22font_setting%22%3A0%2C%22k%22%3A0%2C%22k_disable_default%22%3A0%2C%22hlt%22%3A0%2C%22disable_animations%22%3A0%2C%22display_alt_desc%22%3A0%7D; forty_n_fbuid=dd69c4494f927ebec4490e56f2a15bdbc0ab0b951272358bc20c7e341d19ba41; caconsentcookie={'version':'1.0','categories':{'general':False,'performance':False,'functional':False,'targeting':False,'statistics':False},'updatedAt':'2023-12-15T23:13:51.617Z','expiresAt':'2024-12-14T23:13:51.617Z','consentMethod':'OPT_IN','hasInteractedWithBanner':True,'limitSensitivePersonalData':None}; userProfileId=65832a8cb5b8f578701fc218; MYCARS_PROFILE=65832a8cb5b8f578701fc218; DDC.postalCode=89101; mycars=recentCars%3A4%3BsavedCars%3A0%3BpriceAlerts%3A0%3B; lastItemViewed=%7B%22eventTimestamp%22%3A1704914768502%2C%22dealerCode%22%3Anull%2C%22vehicleType%22%3A%22new%22%2C%22make%22%3A%22Jeep%22%2C%22model%22%3A%22Gladiator%22%2C%22bodyStyle%22%3A%22SUV%22%2C%22vin%22%3Anull%2C%22vehicleId%22%3A%22c47461ab0a0e081d14e53636857f26c0%22%2C%22stockNumber%22%3Anull%2C%22year%22%3A2023%2C%22price%22%3A61551%2C%22pageType%22%3Anull%2C%22listingType%22%3Anull%2C%22listingDomain%22%3Anull%2C%22listingCode%22%3Anull%2C%22mpgCity%22%3A16%2C%22mpgHighway%22%3A23%2C%22odometer%22%3A19%7D; ddc_diag_akam_clientIP=2600:6c50:93f:633d:40cc:481b:68fb:78e6; ddc_diag_akam_currentTime=1705011011; ddc_diag_akam_requestID=4e71cc28; ddc_diag_akam_ghostIP=23.43.51.146; ddc_diag_akam_fullPath=/akam-sw-policy.json; callTrackingSessionId=7rcnrghl2jlr9rj8sh; edw=499983753636588453; _edwps=538195347136716271; _edwvts=499983753636588453; bm_mi=AB802DD0A3639470EFE0BBE2949754CC~YAAQ0qbcF9X0OdSMAQAAl3aT+hbmi1KbAAVkYwAcW1G9V/iMg3cSWYhtHUS+NbMuK+2sgWH6MlePhi/eH30LDb2dxyHOy3tc0wjMLCgQxUzJJVyysNE0WJvEONNJPXkGaXdfqv5s8XCK8w8tSFV1lBuc8KFZCbHyC3u2DuCfZ1nwR8jwVPEAiPAxHWkgFu+cQAddT3tRcLpR72jbVyTnOSoTv/RKo8nur98HVfCpVy1O6Ivtx1hNScuYYG5xfQQhb77w80CxB4iQ877u3QuLTvKZaPOC9WhgdZR3Xx6vyQZFrXnzNwR/j/0ErCHluKK3nsw6uLSh5C0L7Bxc8SbOEJ4glEGGjsyYwS8eGLBXCakHeoxEl7HopW4ZdHTpct79Tw==~1; forty_n_user=v2D8JChR2AvRdmsxWU5QTVp2VjZJbDd2U3pkZXZmVERNdFdXUThOTVJobjNNU1AwNXhnST0~; forty_n_t=1.fbaf61.1702582675.14.2.1705011013.1705011019.4.0; AMCV_3ECF483F53AB366E0A490D44%40AdobeOrg=179643557%7CMCIDTS%7C19734%7CMCMID%7C88547670598664807662567694004300203254%7CMCAID%7CNONE%7CMCOPTOUT-1705018219s%7CNONE%7CvVersion%7C5.5.0; aeatstartmessage=true; ak_bmsc=7A9206E1E61531F67E16ECF749689255~000000000000000000000000000000~YAAQ0qbcF2H5OdSMAQAAWJGT+hbctOzq5kIWGqpEfzC1mOwTgtE8SNye8w/liKeWcRsHJS2qlfkUasIGDjEm24ZAlirKxRNq/a2r4eCg4nzjK6DIHOrUVVlWISGDcZ7SlZ7gdiuSRZQZJehhrkjW+gOq+q2d9V+qIiSvUEC7GYyE/E0RMvUdV+Vf9TaUPq2+TIVILCSRJp7SNOwR6apvGXnCAhn+CVyl3LI74TSbhqXFAzgt0o1Zo1eBvf/fmMELAmHAaugjY5ynr/MT0R9KkIHQt01P0QXtvES4p81XnftwAJinZ3pBjFbYUDqhvekwW7HJzMcHMB858vtIHUSxl+hVO9Puog7RhwmGt9HaBM/6+wteiIaxr1Tv0mc2Le0kdoExKZFTSvwXvLz3UiP7QQvC+as3BhvHqpFLDcaUKEnR; bm_sv=D9FF18633C020C14B1781590B8E93638~YAAQ0abcF0F9NPGMAQAALqqc+haB2+QJtg+7Vl5Ba11MVuvq/yYeQkpMOEPHib6ZOECP8ASMF+ybcueOMZELqS8AMV2ORndU0dwufp/2S8qRYr7xBl7ZJq+2XYzr6EtdXv8DXUVZ/YRtHNZt8w9OhWNlrLnc/7Y3phX1WbTS7osSyNS3UbF6gbkMKoPqer0QASm1qy17YYLFLPILAnYPQVk5nIOUIgLH6dNxUWFpcCSlkyDmMXP3yV+Yy6cFbfkxnrxZy/PKQCM=~1",
    "authority": "www.coastlinecdjr.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.coastlinecdjr.com/used-inventory/index.htm?start=0",
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

df = pd.json_normalize(res)

df.to_csv('resultsused1.csv')

print(f"Scraping completed for all pages.")