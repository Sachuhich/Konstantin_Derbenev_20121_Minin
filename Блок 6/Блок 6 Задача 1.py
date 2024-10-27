def funcName(list1, list2):
    ans1=[set(list1).intersection(set(list2)),len(set(list1).intersection(set(list2)))]
    ans2=[set(list1).symmetric_difference(set(list2)),len(set(list1).symmetric_difference(set(list2)))]
    ans3=[set(list1).difference(set(list2)),len(set(list1).difference(set(list2)))]
    ans4=[set(list2).difference(set(list1)),len(set(list2).difference(set(list1)))]
    return(ans1,ans2,ans3,ans4)

if __name__ == "__main__":
    c,list1,list2=1,input(),input() #[0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25], [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
    for i in funcName(list1, list2):
        print(str(c)+')',i[1],'элемента:',i[0])
        c+=1