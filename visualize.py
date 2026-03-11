import matplotlib.pyplot as plt
from database import get_connection


def course_statistics():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT c.name, COUNT(uc.user_id)
        FROM courses c
        LEFT JOIN user_courses uc ON c.id=uc.course_id
        GROUP BY c.name
    """)

    courses=[]
    counts=[]

    for row in cursor:
        courses.append(row[0])
        counts.append(row[1])

    cursor.close()
    conn.close()

    plt.bar(courses, counts)
    plt.xlabel("Kurslar")
    plt.ylabel("İstifadəçi sayı")
    plt.title("Kurslara qoşulan istifadəçilərin sayı")
    plt.show()


course_statistics()