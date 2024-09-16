def validclock12(time):
    colon_count=time.count(":")

    if colon_count!=1 and colon_count!=2:#시각에 콜론이 없다는 것은 잘못된 시각 표현
        return False
    
    elif colon_count==1:# 시 분 am or pm만 들어 왔을 때  ex)12:00am
        hh,mmmi=time.split(":")#hh에는 시 mmmi에는 분+a,pm이 붙여서 담김 
        mm=mmmi[:2]#mmmi의 0번부터 1번까지는 분
        mi=mmmi[2:]#mmmi의 2번부터 끝까지는 am,pm

        if hh.isdigit()==False:#시를 정수화 못시키면 숫자가 아니므로 거짓 
            return False
        
        if mm.isdigit()==False:#분을 정수화 못시키면 숫자가 아니므로 거짓 
            return False
        
        if mi==("am" or "pm")==False:#2번부터 끝까지 내용이 am, pm 둘 중 같은게 아니면 거짓 
            return False
        
        if len((str(int(hh))))!=len(hh):#"0"+"10이하의 수" 시를 붙이면 숫자로 변환시 길이가 달라짐
            return False
        
        if len(mm)!=2:#분 길이는 2가 아니면 잘못된 분
            return False
        
        if (1<=int(hh)<=12 and 0<=int(mm)<=59)==False:#12시제에서는 시는 1이상 12이하 분은 24시제와 동일
            return False
        
        else:#위의 모든 조건을 통과하면 올바른 표현들만 남게 됨
            return True
        
    elif colon_count==2:# 시 분 초 am or pm만 들어 왔을 때  ex)12:00:00am
        hh,mm,ssmi=time.split(":")
        ss=ssmi[:2]#ssmi의 0번부터 1번은 초가 담김
        mi=ssmi[2:]#ssmi의 2번부터 끝까지는 am,pm이 담김

        if hh.isdigit()==False:#시를 정수화 못시키면 숫자가 아니므로 거짓 
            return False
        
        if mm.isdigit()==False:#분을 정수화 못시키면 숫자가 아니므로 거짓
            return False
        
        if ss.isdigit()==False:#초를 정수화 못시키면 숫자가 아니므로 거짓
            return False
        
        if mi==("am" or "pm")==False:#2번부터 끝까지 내용이 am, pm 둘 중 같은게 아니면 거짓 
            return False
        
        if len((str(int(hh))))!=len(hh):#"0"+"10이하의 수" 시를 붙이면 숫자로 변환시 길이가 달라짐
            return False
        
        if len(mm)!=2:#분 길이는 2가 아니면 잘못된 분
            return False
        
        if len(ss)!=2:#초 길이는 2가 아니면 잘못된 초
            return False
        
        if (1<=int(hh)<=12 and 0<=int(mm)<=59 and 0<=int(ss)<=59)==False:#12시제에서는 시는 1이상 12이하 분,초는 24시제와 동일
            return False
        
        else:#위의 모든 조건을 통과하면 올바른 표현들만 남게 됨
            return True
        


    
