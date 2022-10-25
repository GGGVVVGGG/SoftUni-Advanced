students_nr = int(input())
students_class = {}

for _ in range(students_nr):
    name, score = input().split()
    score = float(score)
    if name not in students_class:
        students_class[name] = []
    students_class[name].append(score)

for student, scores in students_class.items():
    print(f"{student} -> {' '.join([f'{score:.2f}' for score in scores])} (avg: {(sum(scores)/len(scores)):.2f})")