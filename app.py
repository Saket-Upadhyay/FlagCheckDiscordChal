from flask import Flask
from flask import request
import hashlib as hl

app = Flask(__name__)

@app.route('/')
def ma():
    return """
<html>
<head>
<title>
FrigidSec DPC Flag Check</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="keywords" content="FrigidSec">
<meta name="description" content="FrigidSec Discord Challenge Check">
<style>
body {background-color:#ffffff;background-repeat:no-repeat;background-position:top left;background-attachment:fixed;}
h1{text-align:center;font-family:Impact, sans-serif;color:#000000;background-color:#ffffff;}
p {text-align:center;font-family:Georgia, serif;font-size:14px;font-style:normal;font-weight:bold;color:#000000;background-color:#ffffff;}
</style>

</head>
<h1>FrigidSec DPC Flag Checker API</h1>

            <center><h2>Enter SHA256 hash of your flag below and click submit.</h2> <br>     <form action="/whatisthisbehaviourmona" method="POST">
    <input name="check">
    <input type="submit">
</form></center>
    """

@app.route('/whatisthisbehaviourmona',methods=['POST','GET'])
def hello_world():
    FlagList=[]
    with open("flaglist.dat",'r') as ff:
        FlagList=ff.readlines()
    if request.method == "POST":
        REQ_DAT=request.values.get("check")
        print(REQ_DAT)
        print(FlagList)
        if str(REQ_DAT) == "" or str(REQ_DAT) == None or len(REQ_DAT) < 10:
            return """
           <!DOCTYPE html>
<html>
<head>
<title>
FrigidSec DPC Flag Check</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="keywords" content="FrigidSec">
<meta name="description" content="FrigidSec Discord Challenge Check">
<style>
body {background-color:#ffffff;background-repeat:no-repeat;background-position:top left;background-attachment:fixed;}
h1{text-align:center;font-family:Times, serif;color:#000000;background-color:#ffffff;}
p {text-align:center;font-family:Georgia, serif;font-size:14px;font-style:normal;font-weight:bold;color:#000000;background-color:#ffffff;}
</style>
</head>
<body>
<h1>FrigidSec DPC Flag Checker API</h1>
<p>This API checks flag when you give SHA256 dump of your flag in ?check= parameter</p>
<p></p>
<p>For example: </p>
<p>https://frigidsec-dpc-flagcheck.herokuapp.com?check=e525dd0a29c3b8e9b223d7cc79d1393dd2b8c92ca9761968233d944242939605</p>
</body>
</html>


            """
        elif str(REQ_DAT) in FlagList or str(str(REQ_DAT)+"\n") in FlagList:
            return """
            <!DOCTYPE html>
<html>
<head>
<title>
FrigidSec DPC Flag Check</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="keywords" content="FrigidSec">
<meta name="description" content="FrigidSec Discord Challenge Check">
<style>
body {background-color:#ffffff;background-repeat:no-repeat;background-position:top left;background-attachment:fixed;}
h1{text-align:center;font-family:Impact, sans-serif;color:#000000;background-color:#ffffff;}
p {text-align:center;font-family:Georgia, serif;font-size:14px;font-style:normal;font-weight:bold;color:#000000;background-color:#ffffff;}
</style>

</head>
<h1>FrigidSec DPC Flag Checker API</h1>
            <center><h2>You got a <br> <a style=\"color:green;\">VALID</a> <br> flag! <br>Nice Job. Just don't get rusty over time!</h2></center>
            
        """
        else:
            return """
            <html>
<head>
<title>
FrigidSec DPC Flag Check</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="keywords" content="FrigidSec">
<meta name="description" content="FrigidSec Discord Challenge Check">
<style>
body {background-color:#ffffff;background-repeat:no-repeat;background-position:top left;background-attachment:fixed;}
h1{text-align:center;font-family:Impact, sans-serif;color:#000000;background-color:#ffffff;}
p {text-align:center;font-family:Georgia, serif;font-size:14px;font-style:normal;font-weight:bold;color:#000000;background-color:#ffffff;}
</style>

</head>
<h1>FrigidSec DPC Flag Checker API</h1>

            <center><h2>You got a <br><a style=\"color:red;\">INVALID :(</a> <br>flag, but don't give up mate!</h2></center>
            """

    else:
        return """
<html>
<head>
<title>
FrigidSec DPC Flag Check</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="keywords" content="FrigidSec">
<meta name="description" content="FrigidSec Discord Challenge Check">
<style>
body {background-color:#ffffff;background-repeat:no-repeat;background-position:top left;background-attachment:fixed;}
h1{text-align:center;font-family:Impact, sans-serif;color:#000000;background-color:#ffffff;}
p {text-align:center;font-family:Georgia, serif;font-size:14px;font-style:normal;font-weight:bold;color:#000000;background-color:#ffffff;}
</style>

</head>
<h1>FrigidSec DPC Flag Checker API</h1>

<center>
<p>This API checks flag when you give SHA256 dump of your flag in ?check= parameter via POST</p>
<p></p>
<p>For example: </p>
<p>https://frigidsec-dpc-flagcheck.herokuapp.com/whatisthisbehaviourmona?check=e525dd0a29c3b8e9b223d7cc79d1393dd2b8c92ca9761968233d944242939605</p>
<br>
<p>But why are you even here, when we have provided a simple input field <a href="/">HERE</a>? Not everything is a CTF, sometimes it's just simple software. Is that too much to ask?</p>
</center>

        """

if __name__ == '__main__':
    app.run("0.0.0.0",8080)
