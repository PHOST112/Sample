def contactGenerate(minPrice,maxPrice):
    from openpyxl import Workbook
    from openpyxl.utils.dataframe import dataframe_to_rows
    import pandas as pd
    from prettytable import PrettyTable
    
    df=pd.read_excel("OUTSTANDING.xlsx",header=None)
    df1=pd.read_excel("contact list.xlsx",header=None)
    t = PrettyTable(['Name', 'Outstanding', 'Mobile No'])
    df1.drop(df1.columns[[0,2,3,5,6,7,8]], axis=1, inplace=True)
    
    workbook = Workbook()
    worksheet = workbook.active
    df = df.drop([0])
    for r in dataframe_to_rows(df, index=False, header=True):
        worksheet.append(r)
    workbook.save('output.xlsx')
    df3=pd.read_excel("output.xlsx")

    dic=df1.to_dict('list')
    i=1
    count=df3.shape[0]
    index=0
    Final_Output=list()
    # user_price=int(input())
    data_count=0

    cnt=1
    for col in df3.iterrows():
    #     print(type(int(col[1][4])))
        price=int(col[1][4])
        # if(minPrice==0):
        #     if price<=maxPrice:
        #         data_count+=1
        # #         print("Pass")
        #         if col[1][1] in dic[1]:
        #             index=dic[1].index(col[1][1])
        #             col[1][1]=col[1][1].replace("*","")
        #             if(dic[4][index]=="          "):
        # #                 Final_Output={**Final_Output,col[1][1]:"NULL"}
        #                 Final_Output.append((cnt,col[1][1],col[1][4],'NULL'))
        #                 # t.add_row((cnt,col[1][1],col[1][4],'NULL'))
        #             else:
        # #                 Final_Output={**Final_Output,col[1][1]:dic[4][index]}
        #                 Final_Output.append((cnt,col[1][1],col[1][4],dic[4][index]))
        #                 # t.add_row((cnt,col[1][1],col[1][4],dic[4][index]))
        # else:
        if minPrice<=price<=maxPrice:
            data_count+=1
        #         print("Pass")
            if col[1][1] in dic[1]:
                index=dic[1].index(col[1][1])
                col[1][1]=col[1][1].replace("*","")
                if(dic[4][index]=="          "):
                        # Final_Output={**Final_Output,col[1][1]:"NULL"}
                    Final_Output.append((cnt,col[1][1],'NULL',str(col[1][4])))
                    cnt+=1
                        # t.add_row((col[1][1],col[1][4],'NULL'))
                else:
        #                 Final_Output={**Final_Output,col[1][1]:dic[4][index]}
                    Final_Output.append((cnt,col[1][1],dic[4][index],str(col[1][4])))
                    cnt+=1
        if i==count:
            break
        i+=1
    return Final_Output

