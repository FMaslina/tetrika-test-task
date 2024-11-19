def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']

    pupil_intervals = [(start, end) for start, end in zip(intervals['pupil'][::2], intervals['pupil'][1::2])]
    tutor_intervals = [(start, end) for start, end in zip(intervals['tutor'][::2], intervals['tutor'][1::2])]

    intersection_intervals = []

    for pupil_start, pupil_end in pupil_intervals:
        for tutor_start, tutor_end in tutor_intervals:
            start = max(pupil_start, tutor_start, lesson_start)
            end = min(pupil_end, tutor_end, lesson_end)

            if start < end:
                intersection_intervals.append((start, end))

    intersection_intervals.sort(key=lambda x: x[0])

    merged = []
    for start, end in intersection_intervals:
        if not merged or merged[-1][1] < start:
            merged.append((start, end))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))

    return sum(end - start for start, end in merged)


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
