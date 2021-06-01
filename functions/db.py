import pymysql

db = pymysql.connect(
                    host='180.69.72.45',
                    port=3306,
                    user='nature',
                    passwd='bmF0dXJlDQo=',
                    db='naturebot',
                    charset='utf8'
                    )

cursor = db.cursor()

# SQL 문 만들기
sql = '''
            CREATE TABLE your_table (
                   id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                   name VARCHAR(20) NOT NULL,
                   model_num VARCHAR(10) NOT NULL,
                   model_type VARCHAR(10) NOT NULL,
                   PRIMARY KEY(id)
            );
        '''
