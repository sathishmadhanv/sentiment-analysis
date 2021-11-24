from flask import Flask
from app import views
application=Flask(__name__)
application.add_url_rule('/base','base',views.base)
application.add_url_rule('/','index',views.index)
application.add_url_rule('/senti','senti',views.Sentiment,methods=['GET','POST'])
application.add_url_rule('/result','result',views.res)
if __name__ == '__main__':
    application.run(debug=True)
    