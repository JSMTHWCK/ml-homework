"""             max_g = max(G)
            max_g_index = G.index(max_g)
            for i in range(0,len(splitpoints)):
                if len(splitpoints[i]) - max_g_index < 0:
                    return splitpoints[i][max_g_index]
                else:
                    max_g_index -= len(splitpoints[i]) """