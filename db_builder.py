import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE


    
def tblmkr(textfile, args):#all we need is the filename
    command = ""
    csvfile = open(textfile+".csv","r")
    data = csv.DictReader(csvfile)
    fields = data.fieldnames#list of field names
    command += "CREATE TABLE "+textfile+"("+args+")" #creates table
    c.execute(command)
    for record in data:#look at each record
        values = '('# start the values
        for field in fields:# look at each field in the record
            if field != 'name' and name != 'code': #if the field is a TEXT type, you dont need to add the ""
                values +=record[name]+', '
            else:
                values +='"'+record[name]+'", '
        values = values[:-2]#take away the last ,
        values+=')'#add the )
        insert= "INSERT INTO "+ textfile + " VALUES " #basic command
        c.execute(insert + values)#concatonates the command with the values
        csvfile.close()
        return

    tblmkr("peeps", "name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")
    tblmkr("course", "code TEXT, mark INTEGER, id INTEGER")
    

    
            
        


#==========================================================
#db.commit() #save changes
#db.close()  #close database


