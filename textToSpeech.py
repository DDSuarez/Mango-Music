import requests

def moodPer(text):
    url = "https://api.uclassify.com/v1/prfekt/mood/classify"
    data = {"texts":[text]}
    header = {'Authorization': 'Token wbYzfuGjplGB', 'Content-Type': 'application/json'}

    resp = requests.post(url, headers=header, json=data)
    if resp.status_code != 200:
        print(resp.status_code)

    respJson = resp.json()
    respReturn = respJson[0]
    respMoods = respReturn['classification']
    respHappyValue = respMoods[0]['p']
    respUpSetValue = respMoods[1]['p']

    print(respHappyValue)
    print(respUpSetValue)

    # Big thanks to Matt

moodPer("""You tell me I'm running on lost time
            You tell me I'm dragging my heels
            Do you make the most out of our time
            Do you think you know how I feel """)

moodPer("""I need the fear of a love that's lost
            I need to stop trying to count the cost
            I need to fight on the losing side
            And always hold you
            I will always stay with you""")
