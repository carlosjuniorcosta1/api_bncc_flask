from flask import Flask, jsonify, request 
import pyodbc
import pandas as pd

app = Flask(__name__)

data_for_connection = (
    "Driver={SQL Server Native Client RDA 11.0};"
    "Server=DESKTOP-1698A6Q\SQLEXPRESS;"
    "Database=bncc;"  
    "Trusted_connection=YES;"
)

connection = pyodbc.connect(data_for_connection)
cursor = connection.cursor()


print("Abra o navegador e digite /apibncc após seu localhost")

show_table_names = cursor.execute(f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES \
                                  WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG='bncc'")
table_names = show_table_names.fetchall()

for x in table_names:
    print(x)
select_table = input(str(f"Digite o nome da tabela que você deseja:"))
#column_names = pd.read_sql(f"select * from {select_table}", connection)


@app.route('/apibncc', methods=["GET"])
def list_all():
    db = cursor.execute(f"SELECT * FROM {select_table}")
    data_get = db.fetchall()
    data_show = []
    if select_table == "bncc_lingua_portuguesa_ef":
        pl_list = []
        for x in data_get:
            pl_list.append({
            "column1" : x[0],
            "componente": x[1],
            'ano_faixa': x[2],
            'campo_atuacao': x[3],
            'praticas_linguagem': x[4],
            'objetos_conhecimento': x[5],
            'habilidades': x[6],
            'cod_hab': x[7],
            'descricao_cod': x[8],
            'primeiro_ef': x[9],
            'segundo_ef': x[10],
            'terceiro_ef': x[11],
            'quarto_ef': x[12],
            'quinto_ef': x[13],
            'sexto_ef': x[14],
            'setimo_ef': x[15],
            'oitavo_ef': x[16],
            'nono_ef': x[17]
        })
        return jsonify(message = "dados", data = pl_list)
    elif select_table == "bncc_lingua_inglesa_ef":
        eng_list = []
        for x in data_get:
            eng_list.append({
        'column1': x[0],
        'componente': x[1], 
        'ano_faixa': x[2], 
        'eixo': x[3], 
        'unidades_tematicas': x[4],
            
        'objetos_conhecimento': x[5], 
        'habilidades': x[6],
        'cod_hab': x[7],
        'descricao_cod': x[8],
        
        'primeiro_ef': x[9],
        'segundo_ef': x[10],
        'terceiro_ef': x[11],
        'quarto_ef': x[12], 
        'quinto_ef': x[13],
        
        'sexto_ef': x[14], 
        'setimo_ef': x[15], 
        'oitavo_ef': x[16], 
        'nono_ef': x[17]
        })
        return jsonify(message = "dados", data = eng_list)
    else: 
        for x in data_get:
            data_show.append({
            'column1': x[0],
            'componente': x[1],
            'ano_faixa' : x[2],
            'objetos_conhecimento': x[3],
            'habilidades': x[4],
            'cod_hab': x[5], 
            'descricao_cod': x[6], 
            'primeiro_ef': x[7], 
            'segundo_ef':x[8], 
            'terceiro_ef': x[9],
            'quarto_ef': x[10],
            'quinto_ef': x[11],
            'sexto_ef': x[12],
            'setimo_ef': x[13],
            'oitavo_ef': x[14],
            'nono_ef': x[15]
        })
        return jsonify(message= "dados", data = data_show)
   
app.run(debug=True)
   

    




