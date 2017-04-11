class spellCheck:

    def __init__(self,dic):
        self.dic=dic
        
    def editDist1(self,word):
        alphabets="abcdefghijklmnopqrstuvwxyz"
        split=[]
        deletes=[]
        transposes=[]
        insertions=[]
        replaces=[]
        for _ in range(len(word)+1):
            split.append((word[:_],word[_:]))

        for i,j in split:
            deletes.append(i+j[1:])
        for i,j in split:
            if len(j)>1:
              transposes.append(i+j[1]+j[0]+j[2:])
        for i,j in split:
            for _ in alphabets:
              insertions.append(i+_+j)
        for i,j in split:
            if j:
              for _ in alphabets:
                replaces.append(i+_+j[1:])

        return set(deletes+transposes+replaces+insertions)

    def editDist2(self,word):
        return (i for j in self.editDist1(word) for i in self.editDist1(j))

    def matches(self,listOfWords):
        st=set()
        for _ in listOfWords:
           if _ in self.dic:
               print(_)
               st.add(_)
        return st

    def possibleWords(self,word):
        return (self.matches([word]) or self.matches(self.editDist1(word)) or self.matches(self.editDist2(word)) or [word])

    def criteria(self,word):
        if word in self.dic:
          return len(self.dic[word])

    def correction(self,word):
        return max(self.possibleWords(word),key=self.criteria)
