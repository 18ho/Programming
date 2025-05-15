import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='news_db',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def load_news_from_db():
    with db.cursor() as cursor:
        sql = "SELECT * FROM news ORDER BY created_at DESC"
        cursor.execute(sql)
        return cursor.fetchall()

def save_news_to_db(title, content, summary, url):
    with db.cursor() as cursor:
        sql = "INSERT INTO news (title, content, summary, url) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(sql, (title, content, summary, url))
            db.commit()
            print(f"뉴스 저장 성공: {title}")
        except Exception as e:
            print(f"뉴스 저장 실패: {e}")
