import csv

def log_analyser():
    with open("sample.log","r") as log:
        
        with open("log_analysis_results.csv","w", newline= '') as log_analysis:
            write=csv.writer(log_analysis, delimiter=',')
            data=csv.reader(log)
            ip_address=[]
            End_point=[]
            Failed_login=[]
            for row in data:
                row=row[0].split(" ")
                ip_address.append(row[0])
                End_point.append(row[6])
                if row[8]=='401':
                    Failed_login.append(row[0])
                    
            ip_address_set=set(ip_address)
            End_point_set=set(End_point)
            Failed_login_set=set(Failed_login)
            
            
            write.writerow(['IP Address','Request Count'])
            ip_address_dict={}
            for ip in ip_address_set:
                Request_Count=ip_address.count(ip)
                ip_address_dict.setdefault(ip,Request_Count)
            ip_sorted_dict = dict(sorted(ip_address_dict.items(), key=lambda x: (x[1], x[0]), reverse=True))
            for items in ip_sorted_dict.items():
                items=list(items)
                write.writerow([items[0],items[1]])
                

            write.writerow(['End Point','Access Count'])
            End_point_dict={}  
            for ep in End_point_set:
                End_point_Count=End_point.count(ep)
                End_point_dict.setdefault(ep,End_point_Count)
            End_sorted_dict = dict(sorted(End_point_dict.items(), key=lambda item: item[1], reverse=True))
            for n in End_sorted_dict.items():
                n=list(n)
                write.writerow([n[0],n[1]])
                break
            
            
            write.writerow(['IP Address', 'Failed Login Count'])        
            Failed_login_dict={}
            threshold=10
            for Fip in Failed_login_set:
                Failed_Count=Failed_login.count(Fip)
                Failed_login_dict.setdefault(Fip,Failed_Count)
            ip_sorted_dict = dict(sorted(Failed_login_dict.items(), key=lambda x: (x[1], x[0]), reverse=True))
            for items in Failed_login_dict.items():
                items=list(items)
                if items[1]>threshold:
                    write.writerow([items[0],items[1]])

log_analyser()
        
            
        
        
    
        
        
        
        
        
        
        
        