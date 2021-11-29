class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = collections.defaultdict(set)
        names = {}
        
        for i in accounts:
            name = i[0]
            for email in i[1:]:
                emails[email].add(i[1])
                emails[i[1]].add(email)
                names[email] = name
        print(emails)
        answer = []
        already = set()
        for key in emails.keys():
            if key not in already:
                already.add(key)
                stack = [key]
                keys = [key]
                while stack:
                    u = stack.pop()
                    for j in emails[u]:
                        if j not in already:
                            already.add(j)
                            keys.append(j)
                            stack.append(j)
                answer.append([names[key]]+sorted(keys))
        return answer