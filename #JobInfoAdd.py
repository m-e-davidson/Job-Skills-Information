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
        ["Columbia", "Sales Analyst", 72000, 82000, False],
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
        (jobInfoPrimaryKeyNum, "Microsoft", "Advanced", True),
        (jobInfoPrimaryKeyNum, "MAP", "Intermediate", True),
        (jobInfoPrimaryKeyNum, "Vendor Relationships", "Intermediate", True),
        (jobInfoPrimaryKeyNum, "Documentation", "Intermediate", False),
        (jobInfoPrimaryKeyNum, "Communication", "Advanced", True),
        (jobInfoPrimaryKeyNum, "Troubleshooting", "Intermediate", True),
        (jobInfoPrimaryKeyNum, "Sales Tools", "Intermediate", False)
    ]
)
conn.commit()

conn.close()


