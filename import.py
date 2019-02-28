import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

f = open("books.csv")
reader = csv.reader(f)
i = 0

for bsn_id, title, author, year in reader:
    db.execute("INSERT INTO BOOKS (bsn_id, title, author, year) VALUES (:bsn_id, :title, :author, :year)",
               { "bsn_id": bsn_id, "title": title, "author": author, "year": year })

    i += 1
    print("Added entry {}".format(i))

print("Finished")
db.commit()
