def study_schedule(permanence_period, target_time):
    students = 0
    try:
        for student_permanence in permanence_period:
            if student_permanence[0] <= target_time <= student_permanence[1]:
                students += 1
        return students
    except TypeError:
        return None
