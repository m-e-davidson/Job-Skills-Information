

import sqlite3

conn = sqlite3.connect('jobInfo.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# Create the jobInfo table
cursor.execute('''
CREATE TABLE IF NOT EXISTS jobInfo (
    id INTEGER PRIMARY KEY,
    jobCompany TEXT,
    jobTitle TEXT,
    salaryMin INTEGER, 
    salaryMax INTEGER,
    remoteWork BOOLEAN
)
''')

conn.commit()

cursor.execute(
    """
    INSERT INTO jobInfo
        (jobCompany, jobTitle, salaryMin, salaryMax, remoteWork)
    VALUES (?, ?, ?, ?, ?)
    """,
        ["Delta Power", "Data Engineer", 85000, 115000, True],
)
jobInfoPrimaryKeyNum = cursor.lastrowid
conn.commit()



# Create the jobSkill table
cursor.execute('''
CREATE TABLE IF NOT EXISTS jobSkill (
    id INTEGER PRIMARY KEY,
    jobCompanyID INTEGER,
    skillName TEXT,
    skillLevel TEXT,   
    mustHave BOOLEAN,
    FOREIGN KEY (jobCompanyID) REFERENCES jobInfo(id)
)
''')

conn.commit()


cursor.executemany(
    """
    INSERT INTO jobSkill
        (jobCompanyID, skillName, skillLevel, mustHave)
    VALUES (?, ?, ?, ?)
    """,
    [
        (jobInfoPrimaryKeyNum, "Python", "Advanced", True),
        (jobInfoPrimaryKeyNum, "SQL", "Advanced", True),
        (jobInfoPrimaryKeyNum, "Power BI", "Intermediate", False),
        (jobInfoPrimaryKeyNum, "Microsoft", "Advanced", True),
        (jobInfoPrimaryKeyNum, "Documentation", "Intermediate", False)
    ]
)
conn.commit()

conn.close()
