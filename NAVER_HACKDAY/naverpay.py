id_list = ["A B C D", "A D", "A B D", "B D"]
k = 2
id_list2 = ["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"]
k2 = 3

def solution(id_list, k):
    id_only = []
    for i in range(len(id_list)): 
        id_list[i] = id_list[i].split() # 그날 고객 split
        for j in range(len(id_list[i])):
            if id_list[i][j] not in id_only:
                id_only.append(id_list[i][j]) # 고객 명단 추출

    id_counter = [0 for _ in range(len(id_only))]
    id_dict = dict(zip(id_only, id_counter)) # 고객에게 지급한 쿠폰 수 딕셔너리
    id_dayDict = dict(zip(id_only, id_counter)) # 고객에게 하루 지급한 쿠폰 수 딕셔너리

    for i in range(len(id_list)):
        for j in range(len(id_list[i])):
            if id_dayDict[id_list[i][j]] == 0:
                id_dayDict[id_list[i][j]] += 1 # 고객에게 하루동안 최대 1회 쿠폰 지급
        for j in range(len(id_only)):
            if id_dict[id_only[j]] < k: # 고객이 이때까지 받은 쿠폰 수가 k이하라면,
                id_dict[id_only[j]] += id_dayDict[id_only[j]] # 고객에게 그날 지급해야할 쿠폰을 지급한다.
            id_dayDict[id_only[j]] = 0 # 하루 지급해야하는 쿠폰 수 초기화

    answer= sum(id_dict.values())
    return answer