# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:29:47 2019

@author: Administrator
"""

# 17. Letter Combinations of a Phone Number(Medium)
#思路：经典的回溯组合问题，可以先把数字对应的字母序列做一个字典，
#循环或递归加入每个字符，需要一个list保存当前正在加入的字符串。

def letter_combinations(str):
    """循环方式
    str:输入字符串
    return: 合并后的list"""
    
    dic = {'2':'abc','3':'def','4':'ghi','5':'jkl',
           '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    result = ['']
    
    for i in str:
        tem = []
        for j in dic[i]:
            for k in result:
                tem.append(k+j)
        result = tem
    return result


def letter_combinations2(str):
    """递归方式"""
    dic = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
           '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
           '8':['t','u','v'],'9':['w','x','y','z']}
    result = []
    
    if len(str) == 0:
        return []
    # 只剩下1位数字的时候，终止循环
    if len(str) == 1:
        return dic[str]
    
    # 递归
    tem = letter_combinations2(str[1:])
    
    for i in dic[str[0]]:
        for j in tem:
            result.append(i+j)
    return(result)

#letter_combinations2('234')
#result = []
#tem = letter_combinations2('34') -->['dg', 'dh', 'di',......]
#    result = []
#    tem = letter_combinations2('4') ---> ['g','h','i']
#        return ['g','h','i']
#    for i in dic['3'] (['d','e','f']):
#        for j in ['g','h','i']:
#            result.append(i+j)
#    return reslut=['dg', 'dh', 'di', 'eg', 'eh', 'ei', 'fg', 'fh', 'fi']
#for i in dic['2'](['a','b','c'])
#        for j in tem(['dg', 'dh', 'di',......])
#            result.append(i+j)
#return(result)

#if __name__ == '__main__':
#    print(letter_combinations2('34'))


# 22. Generate Parentheses(Medium) 给的那个n对括号，写出所有配对括号的组合
def generateParentheses(n):
    res = []
    
    def dfs(res,string,n,l,r):
        if l == n: #只能加右括号)
            for i in range(r,n):
                string += ')'
            res.append(string)
            return
        elif l==0 or l==r:
            string += '('
            dfs(res,string,n,l+1,r)
        else:
            dfs(res,string+'(',n,l+1,r)
            dfs(res,string+')',n,l,r+1)
    
    dfs(res,'',n,0,0)
    return res
#if __name__ == '__main__':
#    print(generateParentheses(2))

#res = []
#dfs([],'',2,0,0)A
#    l == 0
#    dfs([],'(',2,1,0)
#            dfs([],'((',2,2,0)
#                l == n
#                string = '(())'
#                res='(())'          --'(())'
#            dfs([],'()',2,1,1)
#                l == r
#                dfs(['(())'],'()(',2,2,1)
#                    l==n
#                    string = '()()'
#                    res = ['(())','()()'] --'(())','()()'
            
        
    
    
# 39. Combination Sum(Medium)，可以重复
# 思路：该题数组首先得排序。剩下的同样，dfs递归的套路都差不多，用一个辅助函数。
# 每遍历一个数就加入待定的数组tmp，再把目标书target 减去当前遍历过的数。
            
class Combination(object):
    def combinationSum(self,list,target):
        """组合为目标数，可以重复
        list:输入列表，无序
        target:需要组合的数
        return：list，所有可能的组合方式
        """
        res = []
        list.sort()
        self.dfs(list,0,target,res,[])
        return res
    def dfs(self,list,index,target,res,tmp):
        """"""
        if target < 0:
            return
        if target == 0:
            res.append(tmp)
            return
        for i in range(index,len(list)):
            self.dfs(list,i,target-list[i],res,tmp+[list[i]])

#if __name__ == '__main__':
#    comb = Combination()
#    res = comb.combinationSum([2,3,6,7],7)
#    print(res)


# list=[2,3,6,7], target = 7
#dfs([2,3,6,7],0,7,[],[])
#    i = 0
#    dfs([2,3,6,7],0,5,[],[2])
#        i = 0
#        dfs([2,3,6,7],0,3,[],[2,2])
#            i = 0
#            dfs([2,3,6,7],0,1,[],[2,2,2])
#                i = 0
#                dfs([2,3,6,7],0,-1,[],[2,2,2,2])
#                return
#                i = 1 ...return
#                i = 2 ...return
#                i = 3 ...return
#            i = 1
#            dfs([2,3,6,7],1,0,[],[2,2,3]) -->res=[[2,2,3]]
#            i = 2...return
#            i = 3...return
#        i=1
#        dfs([2,3,6,7],1,4,[[2,2,3]],[2,3])
#           i = 1
#           i = 2
#           i = 3
#        ...
           
            
# 40. Combination Sum II(Medium) 列表中数只能用一次
class Combination2(object):
    def combination_sum(self,list,target):
        """组合目标数，不能重复"""
        res = []
        list.sort()
        self.dfs(list,0,target,res,[])
        return res
    
    def dfs(self,list,index,target,res,tmp):
        """深度遍历"""
        if target < 0:
            return
        if target == 0:
            res.append(tmp)
            return
        for i in range(index,len(list)):
            if i != 0 and list[i] == list[i-1]: #关键
                continue #关键
            self.dfs(list[i+1:],index,target-list[i],res,tmp+[list[i]])
        
#if __name__ == '__main__':
#    comb = Combination2()
#    res = comb.combination_sum([2,3,6,7],7)
#    print(res)

#dfs(list,0,8,[],[])   # list [1,1,2,5,6,7,10]
#    i = 0
#    dfs(list,0,)
#    i = 1
#    
#    i = 2
#    
#    i = 3
    
# 46. Permutations(Medium)
#Given a collection of distinct integers, return all possible permutations.
#给定不同的整数的集合,返回所有可能的排列。
#Input: [1,2,3]
#Output:
#[
#[1,2,3],
#[1,3,2],
#[2,1,3],
#[2,3,1],
#[3,1,2],
#[3,2,1]
#]
# 思路：O(n2)的方法

class Permutations(object):
    def permute(self,list):
        res = []
        self.dfs(list,res,[])
        return res
        
    def dfs(self,list,res,tmp):
        if not list:
            res.append(tmp)
        else:
            for i in range(len(list)):
                self.dfs(list[:i]+list[i+1:],res,tmp+[list[i]])
                
#if __name__ == '__main__':
#    list = [1,2,3]
#    per = Permutations()
#    res = per.permute(list)
#    print(res)
    

#dfs([1,2,3],[],[])
#    i=0
#    dfs([2,3],[],[1]):
#        i=0
#        dfs([3],[],[1,2]):
#            i=0
#            dfs[0,[],[1,2,3]]
#            res = [[1,2,3]]
#        i=1       
#    i=1    
#    i=2

#79. Word Search（Medium）
#给定一个2维数组和一个单词，找到单词是否存在于2维数组中。
#board =
#[
#['A','B','C','E'],
#['S','F','C','S'],
#['A','D','E','E']
#]
#Given word = "ABCCED", return true.
#Given word = "SEE", return true.
#Given word = "ABCB", return false
    
#思路：每次遍历到错误的节点需要返回，最完美的解决办法就是回溯了。
#从每个节点出发判断上下左右四个节点是不是匹配word的下一个字母。
#如果匹配则继续dfs递归，不匹配或者超过边界则返回。
class Word_Exist(object):
    """word search"""
    def exist(self,board,word):
        """
        board: 2D list
        word: 要查找的单词
        """
        if not word: return True
        if not board: return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,i,j,word):
                    return True
        return False
    
    def dfs(self,board,i,j,word):
        """深度递归"""
        if not word:
            return True
        if i>=len(board) or i<0 or j>=len(board[0]) or j<0 or board[i][j] != word[0]:
            return False
        tmp = board[i][j]
        board[i][j] = '.'
        if self.dfs(board,i+1,j,word[1:]) or self.dfs(board,i-1,j,word[1:])\
        or self.dfs(board,i,j+1,word[1:]) or self.dfs(board,i,j-1,word[1:]):
            return True
        board[i][j] = tmp
        return False
#if __name__  == '__main__':
#    board = [['A','B','C','E'],
#             ['S','F','C','S'],
#             ['A','D','E','E']]
#    word = 'SEE'
#    a = Word_Exist()
#    print(a.exist(board,word))

#exist(board,'SEE')
#    for i...:
#    for j...:
#        i=1,j=0
#            dfs(board,1,0,'SEE') -->False
#                tmp = 'S' 
#                board[1,0] = '.'
#                dfs(board,2,0,'EE') or dfs(board,0,0,'EE') or ....
#                board[1,0] = 'S'
#                return False      
#        i=1,j=3
#            dfs(board,1,3,'SEE') -- True
#                tmp = 'S'
#                board[1,3] = '.'
#                dfs(board,2,3,'EE'): -- True
#                    tmp = 'E'
#                    board[2,3] = '.'
#                    dfs(board,2,2,'E'): --True
#                        tmp = 'E'
#                        board[2,2] = '.' 
#                        dfs(board,,,): -- True
#                            not word --return True
#            return True

        
               
    
    































            
        
            
    
