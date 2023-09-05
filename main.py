from __future__ import print_function

import datetime
import os.path
import pickle
import sqlite3

from tkinter import *
import tkinter.messagebox
from ui import ui_login
from ui import ui_main
from ui import ui_on
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tzlocal import get_localzone


# If modifying these scopes, delete the file token.json.

SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = None
    # Create a new event object
timezone = get_localzone()
lg = ui_login.Login()
ma = ui_main.WinGUI()
of = ui_on.WinGUI()

if os.path.exists('user.db'):
    conn2 = sqlite3.connect('user.db') 
    user = conn2.cursor()

class user:
    usernumber=0
    def __init__(self, name, ID):
      self.name = name
      self.ID = ID
      user.usernumber += 1

def login(auto):
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    global service
    service = None
    global close
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
        # If there are no (valid) credentials available, let the user log in.
        try:
            service = build('calendar', 'v3', credentials=creds)
            lg.destroy()
            close=1
            ma.deiconify()
        except HttpError as error:
            print('An error occurred: %s' % error)
    elif os.path.exists('token.json')==False:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        print("3")
        if auto=="1":
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
                lg.destroy()
                ma.deiconify()
                print("4")
        try:
            service = build('calendar', 'v3', credentials=creds)
            lg.destroy()
            close=1
            ma.deiconify()
            print("5")
            print(lg.v.get())
        except HttpError as error:
            print('An error occurred: %s' % error)               

def autolog():
    global service
    global close
    service = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
        try:
            service = build('calendar', 'v3', credentials=creds)
            try:
                lg.destroy()
            except:
                pass
            close=1
            ma.deiconify()
            showevent()
        except HttpError as error:
            print('An error occurred: %s' % error)
    elif os.path.exists('token.json')==False:
        print("2")
        ma.withdraw()
            
def logoff():
    if os.path.exists('token.json'):
        os.remove('token.json') 
        try:
            ma.destroy()
        except:
            pass
        try:
            of.destroy()
        except:
            pass
    else:
        print('you already logged off')
        try:
            ma.destroy()
        except:
            pass
        try:
            of.destroy()
        except:
            pass

def addevents(summary,location,description,start_time,end_time):
    # Create a new event object
    timezone = get_localzone()
    event = {
        'summary': summary,
        'description': description,
        'location': location,
        'start': {
            'dateTime': start_time,
            'timeZone': str(timezone),
        },
        'end': {
            'dateTime': end_time,
            'timeZone': str(timezone),
        }
    }
    try:
        event = service.events().insert(calendarId='primary', body=event).execute()
        tkinter.messagebox.showinfo(title='Successful!',message='Event created: %s' % (event.get('htmlLink')))
        print('Event created: %s' % (event.get('htmlLink')))
    except HttpError as error:
        tkinter.messagebox.showerror(title='Failed',message='An error occurred: %s' % error + "\n \n \n note: wrong time format, please fix it.")
        print('An error occurred: %s' % error)

class eventc (object):
    def __init__(self,summary,location,description,start_time,end_time,ID): 
        self.summary = summary
        self.location = location
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.ID = ID
    def show_summary(self):
        return self.summary
    def show_location(self):
        return self.location
    def show_description(self):
        return self.description
    def show_start_time(self):
        return self.start_time 
    def show_end_time(self):
        return self.end_time
    def show_ID(self):
        return self.ID

def showevent():
    events_result = service.events().list(calendarId='primary', timeMin=datetime.datetime.utcnow().isoformat() + 'Z', singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    global internalID
    internalID={}
    global n
    n=0
    global event2
    event2={}
    global we
    we={}
    print('Getting the upcoming 10 events')
    if os.path.exists('test.db'):
        os.remove('test.db') 
    if os.path.exists('test.db')==False:
        conn = sqlite3.connect('test.db')
        data = conn.cursor() 
        sql_text_1 = '''CREATE TABLE scores 
            (ID TEXT, 
            Description TEXT, 
            Summary TEXT, 
            Location TEXT, 
            start_time TEXT, 
            end_time TEXT,
            delete_ID TEXT
            );''' 
        data.execute(sql_text_1) 
        data.close()
        conn.close()
    # Display the list of events to the user and allow them to select an even
    # t to delete
    if not events:
        print('No upcoming events found.')
        tkinter.messagebox.showinfo(title='Notice',message='No upcoming events found')
        getevent()
    for event in events:
        n=n+1
        conn = sqlite3.connect('test.db')
        data = conn.cursor() 
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        print(n,event['summary'],event['description'],event['location'],start,end,event['id'])
        q =  eventc(event['summary'],event['location'],event['description'],start,end,event['id'])
        event2[n] = q
        we[n]= event['id']
        f = open('somedata', 'wb')
        pickle.dump(event2[n], f) # serialize and save object
        f.close()
        z = [(str(event['id']),event['summary'],event['description'],event['location'],start,end,n)]
        data.executemany('INSERT INTO scores VALUES (?,?,?,?,?,?,?)', z) 
        conn.commit()
        data.close()
        conn.close()
        getevent()
        #print(pickle.load(f))
        #convert external ID to internal ID to improve readability

def guiinfo():
    addevents(ma.widget_dic["tk_input_lhgy591e"].get(), ma.widget_dic["tk_input_lhgy5c6r"].get(), ma.widget_dic["tk_input_lhgy5ab3"].get(), ma.widget_dic["tk_input_lhgy5jay"].get(), ma.widget_dic["tk_input_lhgy6si8"].get())

def deleteevent():
    tkinter.messagebox.showinfo(title='Successful',message='Event deleted.')
    service.events().delete(calendarId='primary', eventId=we[int(ma.widget_dic["tk_input_lhzez65m"].get())]).execute()
    print('Event deleted.')
   
'''def gui():
    ma.widget_dic["tk_button_lhgy4y0v"].configure(command=lambda:guiinfo())'''

def select(): 
    print("<Double-Button-1>事件未处理") 

def getevent():
        #f = open('somedata', 'rb')
        #a=pickle.load(f)
        conn = sqlite3.connect('test.db')
        data = conn.cursor() 
        sql_text_3 = "SELECT * FROM scores WHERE ID!='1'" 
        data.execute(sql_text_3) 
        #print(data.fetchone())
        a=data.fetchall()
        try:
            ma.widget_dic["tk_table_lhij4qh9"].insert("", n, values=a[n-1])
        except:
            #ma.widget_dic["tk_table_lhij4qh9"].insert("", n, values=None)
            cleartable()
        data.close()
        conn.close()
        #[a.show_ID(),a.show_summary(),a.show_description(),a.show_location(),a.show_start_time(),a.show_end_time()])

def cleartable():
    for item in ma.widget_dic["tk_table_lhij4qh9"].get_children(): 
        ma.widget_dic["tk_table_lhij4qh9"].delete(item)

def refresh():
    cleartable()
    showevent()

def closelg():
    try:
        ma.destroy()
        of.destroy()
    except:
        pass
    lg.destroy()

def closema():
    try:
        lg.destroy()
    except:
        pass
    ma.destroy()
    of.destroy()

def closeof():
    try:
        lg.destroy()
    except:
        pass
    of.destroy()
    ma.destroy()

def offlinemode():
    offline = sqlite3.connect('offline') 
    offline.close()
    if os.path.exists('offline'):
        clearofftable()
        ma.withdraw()
        of.deiconify()
        try:
            lg.destroy()
        except:
            pass
        getoffevent()

def onlinemode():
    try:
        os.remove('offline') 
    except:
        pass
    if os.path.exists('offline')==False:
        cleartable()
        autolog()
        ma.deiconify()
        of.withdraw()
        
def getoffevent():
        conn = sqlite3.connect('test.db')
        data = conn.cursor() 
        sql_text_3 = "SELECT * FROM scores WHERE ID!='1'" 
        data.execute(sql_text_3) 
        #print(data.fetchone())
        a=data.fetchall()
        item=0
        print(a)
        while item < len(a): 
            of.widget_dic["tk_table_lhij4qh9"].insert("", len(a), values=a[item])
            item=item+1
        data.close()
        conn.close()       

def clearofftable():
    for item in of.widget_dic["tk_table_lhij4qh9"].get_children(): 
        of.widget_dic["tk_table_lhij4qh9"].delete(item)
        
lg.btn_google.configure(command=lambda:login(str(lg.v.get())))
lg.btn_ok.configure(command=lambda:print(str(lg.v.get())))
lg.protocol('WM_DELETE_WINDOW', closelg)
ma.protocol('WM_DELETE_WINDOW', closema)
of.protocol('WM_DELETE_WINDOW', closeof)

if os.path.exists('offline'):
    lg.destroy()
    ma.withdraw()
    getoffevent()
if os.path.exists('offline')==False:
    of.withdraw()
    autolog()
    
ma.widget_dic["tk_button_lhgy4y0v"].configure(command=lambda:guiinfo())
ma.widget_dic["tk_button_lhgy2vm0"].configure(command=lambda:logoff())
ma.widget_dic["tk_button_lhzf0v2x"].configure(command=lambda:offlinemode())
ma.widget_dic["tk_button_lhzezyzr"].configure(command=lambda:deleteevent())
ma.widget_dic["tk_button_lhzfmuo6"].configure(command=lambda:refresh())
of.widget_dic["tk_button_lhgy4y0v"].configure(command=lambda:onlinemode())

f = open('somedata', 'rb')
a=pickle.load(f)
print(a.show_ID())
print(a.show_ID())

lg.mainloop()
ma.mainloop()