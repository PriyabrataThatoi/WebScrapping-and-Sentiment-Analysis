import twitter

apikey = 'd1TcED6Is1GklAr7gtjReQ1vG'
apisecretkey = 'Ih7HEDDv7QP1OhA8BkYSHYSG4bzvO3ifSIStfEjif0xqAldRi1'
accesstok = '1165029564952846338-A2uEIHzQsBAyG7T2eoNTjT8VYgyO4i'
accesstoksec = 'AltvYOjoEBjUNCsdLTWKRMP55cabR8LjP8rhUoDMhItes'

twitconn = twitter.Api(consumer_key=apikey, consumer_secret=apisecretkey, access_token_key=accesstok, access_token_secret=accesstoksec)

### Iphone 11
tweet1 = twitconn.GetSearch(raw_query='q=%23iphone11%20lang%3Aen')
tweet1

tweet2 = twitconn.GetSearch(raw_query='q=%23iphone11%20lang%3Aen%20until%3A2019-10-24%20since%3A2019-09-20')
tweet2

## tweet9 = twitconn.GetSearch(raw_query='q=(%23Iphone11)%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
## tweet9


### Iphone 11 pro
tweet3 = twitconn.GetSearch(raw_query='q="%23iphone%2011%20pro"%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
tweet3

##tweet8 = twitconn.GetSearch(raw_query='q=(%23Iphone11pro)%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
## tweet8

### Iphone 11 pro max
tweet6 = twitconn.GetSearch(raw_query='q="%23Iphone%2011%20pro%20max"%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
tweet6

tweet7 = twitconn.GetSearch(raw_query='q=iphone%20pro%20max%20%3A(%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
tweet7

### Apple watch series 5
tweet4 = twitconn.GetSearch(raw_query='q="%23apple%20watch%20series%205"%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
tweet4

### 7th generation Ipad
tweet5 = twitconn.GetSearch(raw_query='q="%237th%20generation%20iPad"%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
tweet5

for item in tweet5:
    print(item.id, item.text)

tweet10 = twitconn.GetSearch(raw_query='q=Ipad%207th%20generation%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
tweet10

tweet11 = twitconn.GetSearch(raw_query='q=Apple%20watch%205')
tweet11


q=Apple%20watch%205%20%3A(%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20&


    
