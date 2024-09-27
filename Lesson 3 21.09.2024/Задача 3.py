string=input()
zig_input=string.split(', ')
word,colums,split_word=zig_input[0],int(zig_input[1]),[]
if colums>1:
    long=word
    while word:
        split_word.append(word[0:colums+colums-2])
        word=word[colums+colums-2:]
    output,count='',0
    for i in range(len(split_word)):
        if len(split_word[i])<(2*colums-2):split_word[i]=split_word[i]+'*'*((2*colums-2)-len(split_word[i]))
    for z in range((len(split_word[0])//2)+1):
        for j in range(len(split_word)):
            if z==0:output+=split_word[j][z]
            elif z==(len(split_word[0])//2):output+=split_word[j][z]
            else:
                output+=split_word[j][z]
                output+=split_word[j][-z]
    output=output.replace('*','')
    print(output)
elif colums==1:print(word)
else: print('Error: Zig-zag is impossible')
