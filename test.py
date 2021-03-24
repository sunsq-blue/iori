

def combination(item_set, k):# 递归产生对应长度的排列组合
    anser = []

    single = []

    count = 0##递归次数计数器

    def dfs(count ,item_set):
        if count == k:
            anser.append(list(single))# 申请新的list
            return
        else:

            for i in range(len(item_set)):
                count = count + 1
                single.append(item_set[i])
                dfs(count ,  item_set[i+1 :])
                single.pop()
                count = count -1

    dfs(count , item_set)
    return anser


print(combination([1,2,3,4,5] , 3))