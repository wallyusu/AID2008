# 小学春游 - 两组同学，每组1-3人，每组有一个队长;春游期间，由于景点人数较多，秩序混乱，班主任要求在指定地点，按组集合

# 源数据
s = [{'name': 'leader-1', 'belong_to': None}, {'name': 'jack', 'belong_to': 'leader-2'},
     {'name': 'lili', 'belong_to': 'leader-1'}, {'name': 'leader-2', 'belong_to': None},
     {'name': 'Tom', 'belong_to': 'leader-1'}]
# 目标数据
d = [
    {'name': 'leader-1', 'team': [{'name': 'lili'}, {'name': 'Tom'}]},
    {'name': 'leader-2', 'team': [{'name': 'jack'}]}
]

# 函数作用：将源数据转换为目标数据【源数据作为参数，目标数据作为返回值】
def find_team(data):
    # 定义一个返回值变量
    leader_data = []
    m_dict = {}
    for d in data:
        if d['belong_to']:
            # 队员
            m_dict.setdefault(d['belong_to'],[])  # setdefault当字典的键存在时则忽略，不存在则创建
            m_dict[d['belong_to']].append({'name':d['name']})
        else:
            # 队长
            leader_data.append({'name':d['name'],'team':[]})
    print(m_dict)
    for l in leader_data:
        if l['name'] in m_dict:
            l['team'] = m_dict[l['name']]
    return leader_data

if __name__ == '__main__':
    print(find_team(s))