from django.shortcuts import render_to_response
from itertools import permutations
import itertools
import json
def cal(request):
    s=request.GET["t1"]
    final_str=[]
    if ' ' in s:
        l = s.split()
        lst= set(itertools.permutations(l))
        for i in lst:
            st2=""
            for j in i:
                st2+=j+' '
            final_str.append(st2)
        res_data=json.dumps(final_str)
        print res_data
        return render_to_response('display.html',{'res': res_data})
    else:
        per_str=s[0:10]
        perms = [''.join(p) for p in permutations(per_str)]
        res_data=json.dumps(perms)
        print res_data
        return render_to_response('display.html',{'res': res_data})