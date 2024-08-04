
import datetime
import psycopg2
from config import DB_NAME,DB_USER,DB_PASSWORD,DB_HOST


DB_NAME=DB_NAME
DB_USER=DB_USER
DB_PASSWORD=DB_PASSWORD
DB_HOST=DB_HOST


class DataBase:
    
    def __init__(self):
        #подключение к базе данных
        self.connection = psycopg2.connect(database = DB_NAME,
                                           user = DB_USER,
                                           password = DB_PASSWORD,
                                           host = DB_HOST,)
        self.cursor = self.connection.cursor()
        

#добаление записи      
    def add_provided(self, data):
        with self.connection:
            self.data = data
            query = "INSERT INTO base_service (name) values ('Маникюр');" 
            self.cursor.execute("INSERT INTO service (base_id, name, short, price) values (%s, %s, %s, %s);", (data))
            self.connection.commit()


#получить пользователя телеграмм     
    def check_user(self, data):
        with self.connection:
            self.data = data
            query = "SELECT id FROM manicure_telegramuser where telegram_id=%s;"%data
            self.cursor.execute(query)
            row = self.cursor.fetchall()
            return row[0][0]



#получить все записи базовой таблицы  
    def check_basic(self):
        with self.connection:
            query = "SELECT * FROM manicure_baseservice;"
            self.cursor.execute(query)
            row = self.cursor.fetchall()
            return row


#получить все все сервисы    
    def check_service(self, data):
        with self.connection:
            self.data = data
            #query = "SELECT * FROM manicure_baseservice;"
            query = """
                select manicure_service.id, manicure_service.short from manicure_baseservice 
                join manicure_service on manicure_baseservice.id=manicure_service.base_id 
                where manicure_baseservice.name='%s';
                """%data
            self.cursor.execute(query)
            row = self.cursor.fetchall()
            return row


#получить данные по дате      
    def check_provided_day(self, day, telegram_id):
        #self.user_id = user_id
        with self.connection:
            self.day = day
            self.telegram_id = telegram_id
            query = """
                select p.id, p.price, s.short, b.name from manicure_providedservice p 
                join manicure_service s on p.service_id=s.id
                join manicure_baseservice b on s.base_id=b.id
                where date=%s and telegram_user_id=%s;
                """
            self.cursor.execute(query, [day, telegram_id])
            row = self.cursor.fetchall()
            return row
        

#получить данные по дате за месяц     
    def check_provided_month(self, first_day, last_day, telegram_id):
        #self.user_id = user_id
        with self.connection:
            self.first_day = first_day
            self.last_day = last_day
            self.telegram_id = telegram_id
            query = """
                select p.price, s.short, b.name from manicure_providedservice p 
                join manicure_service s on p.service_id=s.id
                join manicure_baseservice b on s.base_id=b.id
                where telegram_user_id=%s and date>=%s and date<=%s;
                """
            self.cursor.execute(query, [telegram_id, first_day, last_day])
            row = self.cursor.fetchall()
            return row
        


#добавление записи      
    def add_provided(self, id, telegram_id):
        with self.connection:
            self.id = id
            self.telegram_id = telegram_id
            query_select = """
                select * from manicure_service 
                where id=%s
                            """%id
            
            self.cursor.execute(query_select)
            row = self.cursor.fetchall()[0]
            date = datetime.datetime.today()
            query = """
                INSERT INTO manicure_providedservice (price, date, service_id, telegram_user_id) 
                values (%s, %s, %s, %s);
                """
            self.cursor.execute(query, [row[3], date, id, telegram_id])
            self.connection.commit()
 
        


#удаление запись
    def remove_provided(self, id):
        self.id = id
        with self.connection:
            self.cursor.execute("DELETE FROM manicure_providedservice WHERE id = %s"%id)
            self.connection.commit()
            
