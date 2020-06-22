if __name__ == '__main__':
    courses_n = int(input())

    seen_courses = list()
    for course_n in range(courses_n):
        course = input()
        if course not in seen_courses:
            seen_courses.append(course)

    for course in seen_courses:
        print(course)