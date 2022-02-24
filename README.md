
                                                       FLORA
#Python must be installed in the system and Jinga2 Snippet Kit extension must be installed.
#take the above files to your any drive and keep in any folder.

#In terminal:-
#   pip install virtualenv
#   virtualenv env
#Then open the powershell terminal:-
#                              Set-ExecutionPolicy unrestricted 
#                              then you will get option of yes or no enter yes.
#back into to terminal:-
#   .\env\Scripts\activate.ps1
#    pip install flask
#   pip install flask-sqlalchemy
#  pip install marshmallow-sqlalchemy
#  pip install flask-marshmallow
#  pip install Flask-Caching
#   python
#      from app import db
#      db.create_all()
#      exit()

#After this close the folder and then open it.
#In terminal.
#    .\env\Scripts\activate.ps1
#    python .\app.py
#Your server will be started
#Home page:- http://127.0.0.1:5000/
#Update any data:- http://127.0.0.1:5000/update/<int:sno>
eg:-
to update data with serial number-5   http://127.0.0.1:5000/update/5

#Delete any data:- http://127.0.0.1:5000/delete/<int:sno>
eg:-
to delete data with serial number-5   http://127.0.0.1:5000/update/5

#To retrieve data :- http://127.0.0.1:5000/retrieve

#Enter the color in form and submit it will take you to link :- http://127.0.0.1:5000/retrieve/color/<string:color>
eg:-
to retrieve Red   http://127.0.0.1:5000/retrieve/color/Red

#Enter the type in form and submit it will take you to link :- http://127.0.0.1:5000/retrieve/type/<string:type>
eg:-
to retrieve Rose   http://127.0.0.1:5000/retrieve/type/Rose

#Enter the type in form and submit it will take you to link :- http://127.0.0.1:5000/retrieve/price/<int:min>/<int:max>
eg:-
to retrieve in range 1000 to 2000   http://127.0.0.1:5000/retrieve/price/1000/2000


![s1](https://user-images.githubusercontent.com/88224901/155583847-d35ad538-a9d1-4cae-978f-465672462cf5.png)
Then to add new data to database
![s2](https://user-images.githubusercontent.com/88224901/155584152-bb853533-e563-4b8d-961d-e461d9ecead9.png)
It's get added
![s3](https://user-images.githubusercontent.com/88224901/155584171-31701286-275e-4f3c-9533-3cf0e055dcb4.png)
When you click on update button it opens this window
![s4](https://user-images.githubusercontent.com/88224901/155584624-cb97f828-78f0-4eea-873c-e5e4585b2699.png)
If you want to reterive click on Retrieve(right side of Home on left top)
![s5](https://user-images.githubusercontent.com/88224901/155584645-4a13409e-94be-4cab-938a-5d3086d16061.png)
If match are found
![s6](https://user-images.githubusercontent.com/88224901/155585790-36968831-6e8d-4dab-970b-6237053f24f2.png)
If the match is not found
![s7](https://user-images.githubusercontent.com/88224901/155584723-d108ab40-480f-4784-867d-d5abedeb4a1d.png)

If any error occurs Detail error will be shown
![s8](https://user-images.githubusercontent.com/88224901/155584745-bb82c4fa-be49-4a44-b3e1-a397547541d2.png)
