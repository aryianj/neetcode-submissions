class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for o in operations:
            if o.lstrip('-').isdigit():
                record.append(int(o))
            elif o == '+':
                a, b = record[-1], record[-2]
                record.append(a + b)
            elif o == 'D':
                record.append(record[-1] * 2)
            else:
                record.pop()
        return sum(record)

            
