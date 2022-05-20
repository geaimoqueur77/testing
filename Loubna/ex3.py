def multiple(nb, intervalle):
    multiples = []
    for i in intervalle:
        if i % nb == 0:
            multiples.append(i)
    return multiples

print(multiple(3,range(1, 10)))