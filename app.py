from flask import Flask, render_template, url_for, request, redirect
import csv
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def site_root():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name+'.html')


@app.route("/submit_form", methods=["POST","GET"])
def submit_form():
    if request.method=='POST':
        try:
            data = request.form.to_dict()

            # f = open("database.txt","a")
            # write_data = data['email']+" "+data["name"]+" "+data["message"]+" "+data["subject"]
            # print(write_data,file=f,flush=True);
            write_to_file(data)
            write_to_csv(data)
            return data

            #return redirect('/thankyou')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again later.'


def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data['email']
        name = data['name']
        message = data['message']
        subject = data['subject']
        file = database.write(f'{email},{name},{subject},{message}\n')


def write_to_csv(data):
    with open('database.csv',newline='', mode='a') as database:
        email = data['email']
        name = data['name']
        message = data['message']
        subject = data['subject']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"',  quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, name, message])


@app.route('/<username>/<int:post_id>')
def hello_world(username=None,post_id=None):
    # print(url_for('static', filename='favicon.ico'))
    return render_template('index.html',name=username ,id=post_id)

#
# @app.route('/about')
# def about_page():
#     return render_template("about.html")
#
#
# @app.route('/contact')
# def contact():
#     return render_template('./templates/contact.html')
#
#
# @app.route('/image/<path:subpath>')
# def images(subpath):
#     return 'Subpath %s ' % escape(subpath)
