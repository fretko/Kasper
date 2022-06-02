alf='qwertyuiopasdfghjklzxcvbnm_{}1234567890'
data='yourflagis{fhke37_kdrjknbmpr_04374j}'
gamma='thekey'
ans=''
a=len(data)-len(gamma*(len(gamma)//len(data)))
if len(data)%len(gamma)==0:
  gamma=gamma*(len(data)//len(gamma))
else:
  gamma=gamma*(len(data)//len(gamma))+gamma[0:len(data)-len(gamma*(len(data)//len(gamma)))]
for i in data:
  letterindex1=data.find(i)
  letterindex2=letterindex1
  j=gamma[letterindex2]
  indexfordata=alf.find(i)
  indexforgamma=alf.find(j)
  ans+=alf[(indexfordata+indexforgamma)%len(alf)]
print(ans)
