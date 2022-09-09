def solution(survey, choices):
    answer = ''
    scores = dict()
    # for i in range(len(survey)):
    #     if survey[i] not in scores:
    #         scores[survey[i]] = 0
    #     scores[survey[i]] += choices[i] - 4

    for survey_type, choice in zip(survey, choices):
        if survey_type not in scores:
            scores[survey_type] = 0
        scores[survey_type] += choice - 4
    def verify_type(type):
        score = scores.get(type, 0) - scores.get(type[::-1], 0)
        if score == 0:
            return min(type[0], type[1])
        return type[0] if score < 0 else type[1]
    types = ["RT", "FC", "MJ", "AN"]
    for type in types:
        answer += verify_type(type)
    return answer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))