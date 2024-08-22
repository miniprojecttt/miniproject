from google_play_scraper import reviews, app
from textblob import TextBlob
from summarizer_code import summarize
import sqlite3

appid = input("Enter the App Link: ")[46:].split('&pcampaignid=')[0]
N = 1000  # reviews count

con = sqlite3.connect('database/apps.db')
cur = con.cursor()

resultt = cur.execute(f'select * from app where appid = "{appid}";').fetchall()
if not resultt:
    result = reviews(
        appid,
        count=N,
        country='us',
        lang='en'
    )

    if len(result[0]) == N:
        s = 0
        content = []
        for review in result[0]:
            text = review['content']
            pol = TextBlob(text).sentiment.polarity
            s += pol

            if pol < 0:
                content.append(text)

        if s / N >= 0:
            result = app(
                app_id=appid,
                lang='en',  # defaults to 'en'
                country='us'  # defaults to 'us'
            )
            print('Not fraudulent')
            # temp = f'{result["summary"]}' .replace('\'ll', ' will').replace('n\'t', ' not').replace('can\'t', 'cannot')
            print(f'Description\n{result["summary"]}')
            cur.execute("INSERT INTO app VALUES(?, 'Not Fraudulent', ?)", (appid, result["summary"]))
        else:
            print('Fraudulent')
            print('\nReviews Summary\n')
            res = summarize(content)
            cur.execute("INSERT INTO app VALUES(?, 'Fraudulent', ?)", (appid, res))
            print(res)
    else:
        print("The Reviews are less than the threshold to check whether the application if fraudulent or not!\n")
        about_app = app(appid)
        details = ["title", "containsAds", "developer", "developerEmail", "developerWebsite", "free", "genre",
                   "inAppProductPrice", "realInstalls", "released", "score"]

        for cat in details:
            print(f'{cat.title()}: {about_app[cat]}')

    con.commit()
    con.close()
else:
    print(resultt[0][1])
    print('\nDescription')
    print(resultt[0][2])
