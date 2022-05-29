# Face_Recognition_Project_Attendance_management
          -> Suchitra Kushwaha (20ee01053@iitbbs.ac.in)
         
**Description**The project models an attendance register where admin can register or deregister a user. 
The admin credentials are provided in credentials.txt file both id and password being space seperated which can be modified as well.
the Id is admin_ms and password is @user.engage
Each user has a unique Id which can be his/her roll number or employee Id by which he/she will be registered.
Any user can give his/her attendance via the webcam and view their annual attendance report. 
The excel sheet records the monthly records in the 12 sheets. Excel file must not be modified by anyone. User is not deleted from here.
Thus an annual report can be maintained and user can very easily give and view his/her attendance.

**Requirements.txt**
click==8.1.3
cmake==3.22.4
colorama==0.4.4
DateTime==4.4
dlib @ file:///C:/Users/Jagriti/project_face_recog/dlib-19.22.99-cp39-cp39-win_amd64.whl
et-xmlfile==1.1.0
face-recognition==1.3.0
face-recognition-models==0.3.0
Flask==2.1.2
Flask-SQLAlchemy==2.5.1
greenlet==1.1.2
importlib-metadata==4.11.3
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.1
numpy==1.22.4
opencv-python==4.5.5.64
openpyxl==3.0.10
Pillow==9.1.1
pytz==2022.1
SQLAlchemy==1.4.36
Werkzeug==2.1.2
zipp==3.8.0
zope.interface==5.4.0


the project is build on python version 3.9.5
All libraries except dlib can be installed by using the pip install command on the terminal, except the dlib library.
I have provided the file named as dlib-19.22.99-cp39-cp39-win_amd64.whl
--Instructions for dlib--
>Go to Folder [Where you have saved "dlib-19.22.99-cp39-cp39-win_amd64.whl"]
> Open "CMD" or "POWERSHELL" [Where you have saved Python Wheel] 
> Type Command : pip install dlib-19.22.99-cp39-cp39-win_amd64.whl
This should do the work, in case it doesn't, refer https://github.com/shashankx86/dlib_compiled 

**Instructions**
# The application is designed as a desktop web app.
# Single user operation at a time. In case of multiple faces the screen might freeze, just refresh and operate singly.
# Area with sufficient light is preferrable for operation.
# The excel file can be created by the commands given in workbook.py but both the excel file and the database should be renewed at the same time.
  Basically the excel file must not be modified.

**Execution**
To run the program, make sure that python 3.9.5 is installed and all requirements are satisfied.
In the root folder of the project open command propmt or  terminal.
Type the command "python .\app.py" and  execute.



## If you wish to run the file in virtual environment ##
1. Install virtualenv
    $ pip install virtualenv
2. Open a terminal in the project root directory and run
    $ virtualenv env
3. Then activate the virtual env 
    $.\env\Scripts\activate.ps1 (for powershell) or
    $.\env\Scripts\activate.bat (for terminal)
4. Then install the dependencies
    $ pip install -r requirements.txt
    *for dlib follow the Instructions for dlib
5. Finally start the web server:
    $python .\app.py
    
This server will start on port 5000 by default. You can change this in app.py by changing the following line to this
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)

