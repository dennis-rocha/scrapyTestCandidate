import pandas as pd
import saveData as dataBase

#pega as maiores ou menores notas
def list_nota(list_df, ascending=True, column='score'): 
    list_df=list_df.sort_values([column])
    if ascending == False:
        list_df=list_df.sort_values([column], ascending=False)
    new_df=list_df.iloc[[0]]
    for row in range(1,len(list_df)):
        if new_df[column].iloc[0] == list_df[column].iloc[row]:
            new_df=pd.concat([new_df,list_df.iloc[[row]]])
                
        else:
            break
    
    return new_df

#Mostra as informações num formato mais diferenciado
def show_data(new_df , name='global_name', columns=['nota','name']):
    for row in range(0,len(new_df)):
        print(name,end=" | ")
        for column in columns:
            if column == columns[-1]:
                print(new_df[column].iloc[row])
            else:
                print(new_df[column].iloc[row], end=" | ")


if __name__ == "__main__":
    db = dataBase.MongoDb()
    data = db.find_all({'status':200})
    df_data = pd.DataFrame([row['data'] for row in data])
    df_data['score'] = df_data['score'].astype(float)


    show_data(list_nota(df_data, ascending=False), name='maior_nota', columns=['name','score'])
    show_data(list_nota(df_data), name='menor_nota', columns=['name','score'])
    
    show_data(pd.DataFrame.from_dict([{'nota':df_data.score.mean(),
                                       'total':df_data.score.count()}]), 
              name='media_nota', columns=['nota','total'])
    print()
    show_data(df_data.query('score >= 99.99'), name='nota_>=_99.99', columns=['name','cpf','score'])