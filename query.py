import os
os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"

import pandas as pd
import numpy as np
import pyspark.pandas as ps
from pyspark.sql import SparkSession


datos=['data/Anthem_CTC_Accidentalidad.csv','data/Anthem_CTC_AsignaciónPatinetes.csv','data/Anthem_CTC_Bicicletas_Disponibilidad.csv',
'data/Anthem_CTC_BicicletasAforo.csv','data/Anthem_CTC_Callejero.csv','data/Anthem_CTC_CallesEstacionamientoRegulado.csv',
'data/Anthem_CTC_ContaminacionAcustica.csv','data/Anthem_CTC_Contenedores_Ubicacion.csv','data/Anthem_CTC_InstalacionesFotovoltaicas.csv',
'data/Anthem_CTC_OcupacionAparcamientosRotacionales.csv','data/Anthem_CTC_PeatonesAforo.csv','data/Anthem_CTC_Taxi_ObjetosPerdidos.csv',
'data/Anthem_CTC_Taxi_ReservaParadas.csv']

datos_aire=['data/Aire/Anthem_CTC_Aire_Enero.csv','data/Aire/Anthem_CTC_Aire_Febrero.csv','data/Aire/Anthem_CTC_Aire_Marzo.csv',
'data/Aire/Anthem_CTC_Aire_Abril.csv','data/Aire/Anthem_CTC_Aire_Mayo.csv','data/Aire/Anthem_CTC_Aire_Junio.csv',
'data/Aire/Anthem_CTC_Aire_Julio.csv','data/Aire/Anthem_CTC_Aire_Agosto.csv','data/Aire/Anthem_CTC_Aire_Septiembre.csv',
'data/Aire/Anthem_CTC_Aire_Octubre.csv','data/Aire/Anthem_CTC_Aire_Noviembre.csv','data/Aire/Anthem_CTC_Aire_Diciembre.csv',]

datos_censo=['data/Censo/Anthem_CTC_Censo_012051.csv','data/Censo/Anthem_CTC_Censo_022051.csv','data/Censo/Anthem_CTC_Censo_032051.csv',
'data/Censo/Anthem_CTC_Censo_042051.csv','data/Censo/Anthem_CTC_Censo_052051.csv','data/Censo/Anthem_CTC_Censo_062051.csv',
'data/Censo/Anthem_CTC_Censo_072051.csv','data/Censo/Anthem_CTC_Censo_082051.csv','data/Censo/Anthem_CTC_Censo_092051.csv',
'data/Censo/Anthem_CTC_Censo_102051.csv','data/Censo/Anthem_CTC_Censo_112051.csv','data/Censo/Anthem_CTC_Censo_122051.csv',]

datos_multas=['data/Multas/Anthem_CTC_Multas_012051.csv','data/Multas/Anthem_CTC_Multas_022051.csv','data/Multas/Anthem_CTC_Multas_032051.csv',
'data/Multas/Anthem_CTC_Multas_042051.csv','data/Multas/Anthem_CTC_Multas_052051.csv','data/Multas/Anthem_CTC_Multas_062051.csv',
'data/Multas/Anthem_CTC_Multas_072051.csv','data/Multas/Anthem_CTC_Multas_082051.csv','data/Multas/Anthem_CTC_Multas_092051.csv',
'data/Multas/Anthem_CTC_Multas_102051.csv','data/Multas/Anthem_CTC_Multas_112051.csv','data/Multas/Anthem_CTC_Multas_122051.csv',]

datos_trafico=['data/Trafico/Anthem_CTC_Traffic_012051.csv','data/Trafico/Anthem_CTC_Traffic_022051.csv','data/Trafico/Anthem_CTC_Traffic_032051.csv',
'data/Trafico/Anthem_CTC_Traffic_042051.csv','data/Trafico/Anthem_CTC_Traffic_052051.csv','data/Trafico/Anthem_CTC_Traffic_062051.csv',
'data/Trafico/Anthem_CTC_Traffic_072051.csv','data/Trafico/Anthem_CTC_Traffic_082051.csv','data/Trafico/Anthem_CTC_Traffic_092051.csv',
'data/Trafico/Anthem_CTC_Traffic_102051.csv','data/Trafico/Anthem_CTC_Traffic_112051.csv','data/Trafico/Anthem_CTC_Traffic_122051.csv',]

datos_ubicaciones=['']

def contenedores():

    spark = SparkSession.builder.master("local[*]").getOrCreate()

    datos_contenedores = (spark.read.csv(datos[7],header=True, inferSchema=True, sep =";", encoding='Latin1'))

    datos_contenedores.createOrReplaceTempView('Contenedores')

    datos_contenedores.show()

    dist_tipo = spark.sql('''SELECT DISTINCT Distrito, `Tipo Contenedor`, SUM(Cantidad)OVER(PARTITION BY `Tipo Contenedor`, Distrito) AS Cantidad FROM Contenedores ORDER BY Distrito, `Tipo Contenedor` ASC''')

    dist_tipo.show()

    pandas_df = dist_tipo.toPandas()
    print(type(pandas_df))
    return(pandas_df)

