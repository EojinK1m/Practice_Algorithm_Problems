#https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    # 두번째 풀이는 for else를 사용하여 더 깔끔해졌따
    answer = 0

    for skill_tree in skill_trees:
        temp_skill = skill

        for s in skill_tree:
            if s in skill:
                if s == temp_skill[0]:
                    temp_skill = temp_skill[1:]
                else:
                    break
        else:
            answer += 1

    # 첫번째 풀이.
    #     answer = 0

    #     for skill_tree in skill_trees:
    #         temp_skill = skill
    #         try:
    #             for s in skill_tree:
    #                 if s in skill:
    #                     if s == temp_skill[0]:
    #                         temp_skill = temp_skill[1:]
    #                     else:
    #                         raise Exception('SkillError')
    #             answer += 1
    #         except Exception as e:
    #             error_name = e.args[0]
    #             if(error_name == 'SkillError'):pass
    #             else: raise e

    return answer