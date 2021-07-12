
       strs=input()
       if len(strs)==0:
            return ""
       
        mm=len(strs[0])
        for i in range(len(strs)):
            mm=min(len(strs[i]),mm)
            
        pre="" 
        
        i=0
        while(i<mm):
            char=strs[0][i]
            for j in range(len(strs)):
                if strs[j][i]!=char:
                    return pre
            pre=pre+char
            i+=1
        return pre    
