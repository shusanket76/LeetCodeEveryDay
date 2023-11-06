class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        haset = set()
        x=0
        while x<len(emails):
            y = 0
            newem = ""
            currem = emails[x]
            local = True
            while y<len(currem):
                if local is True:
                    if currem[y]=="+":
                        while currem[y]!="@":
                            y+=1
                        newem+="@"
                        y+=1
                        local = False
                    elif currem[y]==".":
                        y+=1
                    elif currem[y]=="@":
                        newem+="@"
                        y+=1
                        local = False

                        
                        continue
                    else:
                        newem+=currem[y]
                        y+=1
                else:
                    newem+=currem[y]
                    y+=1
                
                
            haset.add(newem)
            x+=1
        print(haset)
        return len(haset)
                
                
        
        
        
        