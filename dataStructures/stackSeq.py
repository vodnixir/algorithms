pushed = list(map(int, input().split()))
popped = list(map(int, input().split()))
st = []
j = 0
for x in pushed:
    st.append(x)
    while st and st[-1] == popped[j]:
        st.pop()
        j += 1
print('True' if not st else 'False')
