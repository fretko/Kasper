alf = "abcdefghijklmnopqrstuvwxyz"
stroka='yourflagis{23|8|1|20|4|15|25|15|21|11|14|15|23|1|2|15|21|20|1|2|3}'
stroka=stroka[stroka.find("{"):].replace("|"," ").replace('{','').replace('}','').split()
print(stroka)
ans=''
for i in stroka:
  letter=alf[int(i)-1]
  ans+=letter
print(ans)
