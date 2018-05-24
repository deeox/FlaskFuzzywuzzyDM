from flask import Flask, render_template, redirect, request, url_for, flash
from fuzzywuzzy import fuzz
from doublemetaphone import doublemetaphone as dm


def homophone(str1, str2):
    print(dm(str1))
    print(dm(str2))
    if fuzz.ratio(dm(str1)[0], dm(str2)[0]) == 100:
        return 1
    elif fuzz.ratio(dm(str1)[1], dm(str2)[1]) == 100 and dm(str1)[1] != '' and dm(str2)[1] != '':
        return 1


app = Flask(__name__)


@app.route('/results')
def correct(val1, val2, flag, fuzzyDM, fuzzyNoDM):
    return render_template("results.html", value1=val1, value2=val2, ptr=flag, fuzzyDM=fuzzyDM, fuzzyNoDM=fuzzyNoDM)


@app.route('/')
def home():
    return render_template("homepage.html")


@app.route('/', methods=['POST'])
def homepage():
    value1 = str(request.form['input1'])
    value2 = str(request.form['input2'])

    fuzzyNoDM = fuzz.ratio(value1, value2)
    fuzzyDM = fuzz.ratio(dm(value1)[0], dm(value2)[1])
    ptr = homophone(value1, value2)
    print(ptr)
    redirect('/results')

    return correct(value1, value2, ptr, fuzzyDM, fuzzyNoDM)





