import MySQLdb

try:
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="spam_detection")
    print("✅ Successfully connected to MySQL!")
    db.close()
except Exception as e:
    print("❌ Error connecting to MySQL:", e)
