#JobInfoAdd


import sqlite3

conn = sqlite3.connect('jobInfo.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute(
    """
    INSERT INTO jobInfo
        (jobCompany, jobTitle, salaryMin, salaryMax, remoteWork)
    VALUES (?, ?, ?, ?, ?)
    """,
        ["Canada Life", "Reporting Data Analyst 12Mon Contract", 59800, 99700, True],
)
jobInfoPrimaryKeyNum = cursor.lastrowid
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
        (jobInfoPrimaryKeyNum, "Power BI", "Intermediate", True),
        (jobInfoPrimaryKeyNum, "Data Modelling", "Advanced", True),
        (jobInfoPrimaryKeyNum, "Power BI PL-300", "Intermediate", False),
        (jobInfoPrimaryKeyNum, "Communication", "Advanced", True),
        (jobInfoPrimaryKeyNum, "Statistical Modelling", "Intermediate", True),
        (jobInfoPrimaryKeyNum, "Financial Services", "Basic", False)
    ]
)
conn.commit()

conn.close()

conn.commit()

conn.close()