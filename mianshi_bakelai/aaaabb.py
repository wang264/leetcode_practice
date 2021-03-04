# check if there is pattern of aaaabb


def solution(s: str):
    idx = 0
    for idx, char in enumerate(s):
        if char == "a":
            continue
        else:
            break

    # idx point to the location of first b.
    for i in range(idx, len(s)):
        if s[i] == "a":
            return False

    return True

solution(s="aaaabbb")

solution(s="abab")

solution(s="b")
