library(twitteR)

A = searchTwitter(searchString = '"iPhone11"+lang:en', n = 100)
A

B = searchTwitter(searchString = '"iPhone11"+(#iPhone11)+lang:en', n = 100)
B

C = searchTwitter(searchString = '#iphone11+lang:en', n = 100)
C

D = searchTwitter(searchString = 'iPhone11+review+lang:en', n = 100)
D

E = searchTwitter(searchString = '"iPhone11"+lang:en+until:2019-10-22+since:2019-09-20', n = 100)
E

F = searchTwitter(searchString = '(#iPhone11ProMax)+lang:en+until:2019-10-25+since:2019-09-20', n = 100)
F

G = searchTwitter(searchString = '"Apple+watch+series+5"+lang:en+until:2019-10-25+since:2019-09-20', n = 100)
G

H = searchTwitter(searchString = '"iPad+7th+gen"+lang:en', n = 70)
H

I = searchTwitter(searchString = '"iPhone11+Pro+Max"+lang:en+until:2019-10-25+since:2019-09-20', n = 100)
I

J = searchTwitter(searchString = '"Apple+watch+series+5"+lang:en+until:2019-10-25+since:2019-09-20', n = 100)
J

K = searchTwitter(searchString = '"iPad+7th+generation"+lang:en+until:2019-10-25+since:2019-09-20', n = 100)
K

L = searchTwitter(searchString = '(#iPhone11Pro)+lang:en+until:2019-10-25+since:2019-09-20', n = 100)
L

M = searchTwitter(searchString = '(#AppleWatch5)+until:2019-10-25+since:2019-09-20', n = 100)
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

S = searchTwitter(searchString = '"iPhone11+meme"+(#iPhone11)+lang:en')
S

T = searchTwitter(searchString = '(#iPhone11+OR+#iPhone11Pro+OR+#iPhone11ProMax)+lang:en', n = 100)
T

U = searchTwitter(searchString = '(#Applewatchseries5)+lang:en', n = 100)
U

V = searchTwitter(searchString = '"Applewatch+Series+5"+lang:en', n = 45)
V

W = searchTwitter(searchString = '"iPhone11Pro"+(#Triplelens)+lang:en')
W
