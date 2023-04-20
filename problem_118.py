def generate(numRows):
    row, result = 1, [[1]]

    while row < numRows:
        result.append([1])
        for i in range(1, row):
            result[row].append(result[row-1][i-1]+result[row-1][i])
        result[row].append(1)
        row += 1

    return result



def test_generate():
    assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
