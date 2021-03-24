import os
import itertools

import numpy  as np
import pandas as pd



class Apriori:
    def __init__(self , itemSets , minSuport ):
        self.itemSets = itemSets
        self.minSuport = minSuport

    def conbination(self , item_set, k):# 递归产生对应长度的排列组合
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
        
    def apriori(self):
        n=self.itemSets.shape[0]
        #print(self.itemSets["商品编码"])
        all_product_num = pd.DataFrame(self.itemSets["商品编码"])
        all_shop_num = pd.DataFrame(self.itemSets["销售单明细"])
        all_product_num = all_product_num.drop_duplicates()
        all_shop_num = all_shop_num.drop_duplicates()
        #print(all_product_num.shape[0])# 共有408 种商品
        #print(all_shop_num.shape[0])#共有60个销售单
        ####所以设置最小支持率为0.2



        ###########创建两个数组分别用于储存  销售单 与对应的  商品

        item_set = []

        item_set2 = []
        dill_set = []
        for index , name in all_shop_num.iterrows():
            dill_set.append(name['销售单明细'])
        for index, name in self.itemSets.iterrows():
            item_set2.append(name['商品编码'])


        for shop_dill in dill_set:
            x= []
            for index , name in self.itemSets.iterrows():
                if shop_dill == name['销售单明细']:
                    x.append(name['商品编码'])

            item_set.append(x)

        ##############
        k=1
        #curent_set = item_set2

        dill_num = len(dill_set)

        anser = []
        debug_set = []

        while k<n:

            curent_set = self.conbination(item_set2 , k)
            k+=1
            #print(k)

            #############查看curnt_set 中每个项出现的次数
            count_list = [0 for i in range(len(curent_set))]
            for i in range(len(curent_set)):
                for j in range(len(item_set)):
                    if set(curent_set[i]) <= set(item_set[j]):
                        count_list[i] = count_list[i] + 1
            #print(count_list)
            ########## 删除低minsupport 的项
            for i in range(len(count_list)):
                if count_list[i]/dill_num<self.minSuport:
                    count_list[i] =-1
            #print(set(count_list))

            ############产生新的itemset2
            new_item_set = []
            #debug_set = []
            for i in range(len(count_list)):
                if count_list[i]!= -1:
                    new_item_set = new_item_set+ curent_set[i]
                    debug_set.append(curent_set[i])

           # print(debug_set)



            item_set2 = list(set(new_item_set))

            if len(item_set2) == 0:
                #print(k)
                break
        anser = []
        for i in debug_set:
            if len(i) == k-2:
                anser.append(i)
        return anser










        #for index , row in all_product_num.iterrows():
            #print(row['商品编码'])




if __name__ == '__main__':

    data = pd.read_excel(r"data.xlsx",index=False)
    data = data.drop_duplicates()# 去重
    Apr = Apriori(data , 0.04)
    print(Apr.apriori())



