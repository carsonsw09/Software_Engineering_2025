import psycopg2 as pg

class Course:
    def __init__(self,newId=0,newNumber=''):
        self.id=newId
        self.number=newNumber
    def create(self,cursor,conn):
        query="insert into courses (number) values ('%s')"%(self.number) # ?? Id
        cursor.execute(query)
        conn.commit()
    def retrieve(self,row):
        ID=0
        NUMBER=1
        self.id=row[ID]
        self.number=row[NUMBER]
    def update(self,cursor,conn,newId=None,newNumber=None):
        if (newId!=None):
            self.id=newId
        if (newNumber!=None):
            self.number=newNumber
        query="update courses set number='%s' where id=%s"%(self.number,self.id)
        cursor.execute(query)
        conn.commit()
    def delete(self,cursor,conn):
        query="delete from courses where id=%s"%(self.id)
        cursor.execute(query)
        conn.commit()
    def describe(self):
        return "id=%s,number=%s"%(self.id,self.number)
        
#This is a python structure for a set of Course Objects
class Courses:
    def __init__(self):
        conn_string = "host='localhost' dbname='csci260' user='csci260' password='password'"
        self.conn = pg.connect(conn_string)
        self.cursor = self.conn.cursor() 

    def create(self,c):
        c.create(self.cursor,self.conn)

    def delete(self,c):
        c.delete(self.cursor,self.conn)

    def update(self,c):
        c.update(self.cursor,self.conn)

    def retrieve(self):
        self.cursor.execute("select id,number from courses")
        records = self.cursor.fetchall()
        ret=""
        for r in records:
            c=Course()
            c.retrieve(r)
            ret+=c.describe()+"\n"
        return ret
        #print("+--+------+")
        #print("|id|number|")
        #print("+--+------+")
            #print("|%s|%s|"%(r[ID],r[NUMBER]))
        #print("+--+------+")

