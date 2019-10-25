library(twitteR)

consumer_key = "9lavKlPTdDMun4dgMnwruycX5"
consumer_secret = "HzOs39nOeSW7HpgUc0MKfCY4zO3P9cOzfD8OEo1nVClEDeFX80"
access_token = "203019280-4MJRTEfxtyBvO7E0m0vYX6Si59roZNyUwsBXASmA"
access_secret = "b2pu6GOVhqx7OTAw4YmzKsZjMaajlLVwwvGK1gwvema54"

A = searchTwitter(searchString = 'iPhone11')
A

B = searchTwitter(searchString = '"iPhone11"+(#iPhone11)')
B

C = searchTwitter(searchString = '#iphone11')
C

D = searchTwitter(searchString = 'iPhone11+review')
D

E = searchTwitter(searchString = '"iPhone11"+lang:en+until:2019-10-22+since:2019-09-20')
E



I = searchTwitter(searchString = '"iPhone11+Pro+Max"+lang:en+until:2019-10-25+since:2019-09-20')
I

J = searchTwitter(searchString = '"Apple+watch+series+5"+lang:en+until:2019-10-25+since:2019-09-20')
J

K = searchTwitter(searchString = '"iPad+7th+generation"+lang:en+until:2019-10-25+since:2019-09-20')
K

L = searchTwitter(searchString = '(#iPhone11Pro)+lang:en+until:2019-10-25+since:2019-09-20')
L

K = searchTwitter(searchString = '(#iPhone11ProMax)+lang:en+until:2019-10-25+since:2019-09-20', n = 50)
K

L = searchTwitter(searchString = '"Apple+watch+series+5"+lang:en+until:2019-10-25+since:2019-09-20')
L

M = searchTwitter(searchString = '(#AppleWatch5)+until:2019-10-25+since:2019-09-20')
M

N = searchTwitter(searchString = '"September+event+2019"+(#Apple)+lang:en')
N

O = searchTwitter(searchString = '(#Triplelens)+until:2019-10-25+since:2019-09-20')
O

P = searchTwitter(searchString = '"iPhone11+news"+lang:en+until:2019-10-25+since:2019-09-20')
P

Q = searchTwitter(searchString = '"iPhone11+design"+lang:en')
Q

R = searchTwitter(searchString = '(#iPhone11memes)')
R

