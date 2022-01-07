if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for name in student_marks:
        if name == query_name:
            marks = student_marks[name]
            print("{:.2f}".format(sum(marks)/len(marks)))