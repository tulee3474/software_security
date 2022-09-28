# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def solution(skill, skill_trees):
    skill = list()
    skill_trees = list()
    qqq = list()
    ret = 0

    for j in skill_trees:
        for i in skill:
            qqq += skill_trees[j].index(skill[i])

        www = qqq[:]
        qqq.sort()
        if www == qqq:
            ret += 1

    answer = ret
    return answer
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #solution(1232)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/





