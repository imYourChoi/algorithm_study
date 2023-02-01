# https://www.acmicpc.net/problem/1991

n = int(input())
graph = {}

for _ in range(n):
    p,l,r = input().split()
    graph[p] = (l,r)

def preorder(node):
    print(node, end="")
    children = graph[node]
    if children[0] != ".":
        preorder(children[0])
    if children[1] != ".":
        preorder(children[1])

def inorder(node):
    children = graph[node]
    if children[0] != ".":
        inorder(children[0])
    print(node, end="")
    if children[1] != ".":
        inorder(children[1])

def postorder(node):
    children = graph[node]
    if children[0] != ".":
        postorder(children[0])
    if children[1] != ".":
        postorder(children[1])
    print(node, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")
print()