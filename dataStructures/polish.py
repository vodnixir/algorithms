st = []
for t in input().split():
    if t in '+-*':
        a = st.pop()
        b = st.pop()
        if t == '+':
            st.append(a + b)
        elif t == '-':
            st.append(b - a)
        else:
            st.append(a * b)
    else:
        st.append(int(t))
print(st[-1])
