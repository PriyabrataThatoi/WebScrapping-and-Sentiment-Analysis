import twitter
import csv
import pandas as pd
import os

## General
tweet14 = project_tweet.GetSearch(raw_query='q=apple%20%20September%20event%202019')
tweet14

tweet15 = project_tweet.GetSearch(raw_query='q=apple%20product%20release%20phone%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
tweet15

tweet15 = project_tweet.GetSearch(raw_query='q=dual%20camera%20apple%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
tweet15

tweet16 = project_tweet.GetSearch(raw_query='q=Smart%20HDR%20Iphone%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
tweet16

### Iphone 11
tweet1 = project_tweet.GetSearch(raw_query='q=%23iphone11%20lang%3Aen')
tweet1

tweet2 = project_tweet.GetSearch(raw_query='q=%23iphone11%20lang%3Aen%20until%3A2019-10-24%20since%3A2019-09-20')
tweet2

##tweet9 = project_tweet.GetSearch(raw_query='q=(%23Iphone11)%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
##tweet9

tweet25 = project_tweet.GetSearch(raw_query='q=Apple%20A13%20Bionic%20chip%20lang%3Aen%20until%3A2019-10-26%20since%3A2019-09-20')
tweet25

tweet26 = project_tweet.GetSearch(raw_query='q=Apple%20Dual%2012MP%20Ultra%20Wide%20%20until%3A2019-10-26%20since%3A2019-09-20')
tweet26

### Iphone 11 pro
tweet3 = project_tweet.GetSearch(raw_query='q="%23iphone%2011%20pro"%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
tweet3

##tweet8 = project_tweet.GetSearch(raw_query='q=(%23Iphone11pro)%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
## tweet8

### Iphone 11 pro max
tweet6 = project_tweet.GetSearch(raw_query='q="%23Iphone%2011%20pro%20max"%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
tweet6

tweet7 = project_tweet.GetSearch(raw_query='q=iphone%20pro%20max%20%3A(%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
tweet7

tweet23 = project_tweet.GetSearch(raw_query='q=Apple%20Super%20Retina%20XDR%20display%20lang%3Aen%20until%3A2019-10-26%20since%3A2019-09-20')
tweet23

tweet24 = project_tweet.GetSearch(raw_query='q=Apple%20OLED%20Multi‑Touch%20display%20lang%3Aen%20until%3A2019-10-26%20since%3A2019-09-20')
tweet24




### Apple watch series 5
tweet4 = project_tweet.GetSearch(raw_query='q="%23apple%20watch%20series%205"%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
tweet4

tweet11 = project_tweet.GetSearch(raw_query='q=Apple%20watch%205')
tweet11

##tweet13 = project_tweet.GetSearch(raw_query='q=Apple%20watch%205%20%3A(%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
##tweet13

tweet17 = project_tweet.GetSearch(raw_query='q=Apple%20watch%20OS%206%20lang%3Aen%20until%3A2019-10-26%20since%3A2019-09-20')
tweet17

tweet18 = project_tweet.GetSearch(raw_query='q=Apple%20cycle%20tracking%20lang%3Aen%20until%3A2019-10-26%20since%3A2019-09-20')
tweet18

tweet19 = project_tweet.GetSearch(raw_query='q=Apple%20watch%20series%205%20noise%20app%20lang%3Aen%20until%3A2019-10-26%20since%3A2019-09-20')
tweet19

tweet20 = project_tweet.GetSearch(raw_query='q=Apple%20Watch%20activity%20trends%20lang%3Aen%20until%3A2019-10-26')
tweet20


### 7th generation Ipad
tweet5 = project_tweet.GetSearch(raw_query='q="%237th%20generation%20iPad"%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
tweet5

for item in tweet5:
    print(item.id, item.text)

tweet10 = project_tweet.GetSearch(raw_query='q=Ipad%207th%20generation%20lang%3Aen%20until%3A2019-10-25%20since%3A2019-09-20')
tweet10

tweet21 = project_tweet.GetSearch(raw_query='q=Apple%20Retina%20LED-backlit%20display%20with%20IPS%20technology%20lang%3Aen%20until%3A2019-10-26%20since%3A2019-09-20')
tweet21

tweet22 = project_tweet.GetSearch(raw_query='q=Apple%20Embedded%20M10%20coprocessor%20lang%3Aen%20until%3A2019-10-26%20since%3A2019-09-20')
tweet22



df = pd.DataFrame(tweet22) 
df
df.size

df.to_csv("t22.csv", index = None, header=True)


df.to_csv("t22.csv", index = False, sep=',')

df = pd.DataFrame(tweet25) 
df
df.size
df.to_csv("t22.csv", index = None, header=True)
df.to_csv("t22.csv", index = False, sep=',')
