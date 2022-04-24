import os
os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"

import pandas as pd
import numpy as np
import pyspark.pandas as ps
from pyspark.sql import SparkSession
from pyspark.sql import functions as fun



datos=['data/Anthem_CTC_Accidentalidad.csv','data/Anthem_CTC_AsignaciónPatinetes.csv','data/Anthem_CTC_Bicicletas_Disponibilidad.csv',
'data/Anthem_CTC_BicicletasAforo.csv','data/Anthem_CTC_Callejero.csv','data/Anthem_CTC_CallesEstacionamientoRegulado.csv',
'data/Anthem_CTC_ContaminacionAcustica.csv','data/Anthem_CTC_Contenedores_Ubicacion.csv','data/Anthem_CTC_InstalacionesFotovoltaicas.csv',
'data/Anthem_CTC_OcupacionAparcamientosRotacionales.csv','data/Anthem_CTC_PeatonesAforo.csv','data/Anthem_CTC_Taxi_ObjetosPerdidos.csv',
'data/Anthem_CTC_Taxi_ReservaParadas.csv','data/Aire/Anthem_CTC_Aire_Enero.csv','data/Aire/Anthem_CTC_Aire_Febrero.csv',
'data/Aire/Anthem_CTC_Aire_Marzo.csv','data/Aire/Anthem_CTC_Aire_Abril.csv','data/Aire/Anthem_CTC_Aire_Mayo.csv',
'data/Aire/Anthem_CTC_Aire_Junio.csv','data/Aire/Anthem_CTC_Aire_Julio.csv','data/Aire/Anthem_CTC_Aire_Agosto.csv',
'data/Aire/Anthem_CTC_Aire_Septiembre.csv','data/Aire/Anthem_CTC_Aire_Octubre.csv','data/Aire/Anthem_CTC_Aire_Noviembre.csv',
'data/Aire/Anthem_CTC_Aire_Diciembre.csv','data/Censo/Anthem_CTC_Censo_012051.csv','data/Censo/Anthem_CTC_Censo_022051.csv',
'data/Censo/Anthem_CTC_Censo_032051.csv','data/Censo/Anthem_CTC_Censo_042051.csv','data/Censo/Anthem_CTC_Censo_052051.csv',
'data/Censo/Anthem_CTC_Censo_062051.csv','data/Censo/Anthem_CTC_Censo_072051.csv','data/Censo/Anthem_CTC_Censo_082051.csv',
'data/Censo/Anthem_CTC_Censo_092051.csv','data/Censo/Anthem_CTC_Censo_102051.csv','data/Censo/Anthem_CTC_Censo_112051.csv',
'data/Censo/Anthem_CTC_Censo_122051.csv','data/Multas/Anthem_CTC_Multas_012051.csv','data/Multas/Anthem_CTC_Multas_022051.csv',
'data/Multas/Anthem_CTC_Multas_032051.csv','data/Multas/Anthem_CTC_Multas_042051.csv','data/Multas/Anthem_CTC_Multas_052051.csv',
'data/Multas/Anthem_CTC_Multas_062051.csv','data/Multas/Anthem_CTC_Multas_072051.csv','data/Multas/Anthem_CTC_Multas_082051.csv',
'data/Multas/Anthem_CTC_Multas_092051.csv','data/Multas/Anthem_CTC_Multas_102051.csv','data/Multas/Anthem_CTC_Multas_112051.csv',
'data/Multas/Anthem_CTC_Multas_122051.csv','data/Trafico/Anthem_CTC_Traffic_012051.csv','data/Trafico/Anthem_CTC_Traffic_022051.csv',
'data/Trafico/Anthem_CTC_Traffic_032051.csv','data/Trafico/Anthem_CTC_Traffic_042051.csv','data/Trafico/Anthem_CTC_Traffic_052051.csv',
'data/Trafico/Anthem_CTC_Traffic_062051.csv','data/Trafico/Anthem_CTC_Traffic_072051.csv','data/Trafico/Anthem_CTC_Traffic_082051.csv',
'data/Trafico/Anthem_CTC_Traffic_092051.csv','data/Trafico/Anthem_CTC_Traffic_102051.csv','data/Trafico/Anthem_CTC_Traffic_112051.csv',
'data/Trafico/Anthem_CTC_Traffic_122051.csv']

datos_ubicaciones=['']

def densiConten():

    spark = SparkSession.builder.master("local[*]").getOrCreate()

    datos_contenedores = (spark.read.csv(datos[7],header=True, inferSchema=True, sep =";", encoding='Latin1'))

    datos_contenedores.createOrReplaceTempView('Contenedores')

    dist_tipo = spark.sql('''SELECT DISTINCT Distrito, `Tipo Contenedor`, Count(*)OVER(PARTITION BY `Tipo Contenedor`, Distrito) AS Cantidad FROM Contenedores ORDER BY Distrito, `Tipo Contenedor` ASC''')

    dist_tipo.createOrReplaceTempView('dist_tipo')

    dist_tipo.show()

    datos_censo = (spark.read.csv(datos[35],header=True, inferSchema=True, sep =";", encoding='Latin1'))

    datos_censo.createOrReplaceTempView('Censo')


    dist_censo = spark.sql('''SELECT DISTINCT DESC_DISTRITO, (SUM(EspanolesHombres)OVER(PARTITION BY DESC_DISTRITO)  + SUM(EspanolesMujeres)OVER(PARTITION BY DESC_DISTRITO)  + SUM(ExtranjerosHombres)OVER(PARTITION BY DESC_DISTRITO)  + SUM(ExtranjerosMujeres)OVER(PARTITION BY DESC_DISTRITO) ) AS Censo FROM Censo ORDER BY DESC_DISTRITO''')

    for colname in dist_censo.columns:
        dist_censo = dist_censo.withColumn(colname, fun.trim(fun.col(colname)))

    dist_censo.createOrReplaceTempView('dense_dist')

    dist_censo.show()

    dense_conte = spark.sql('''SELECT DISTINCT Distrito, `Tipo Contenedor` AS Tipo, (Cantidad/Censo) AS Contenedores FROM dist_tipo JOIN dense_dist ON Distrito=DESC_DISTRITO ORDER BY Distrito ASC''')

    dense_conte.toPandas().to_csv('output/densidad_cubos_censo.csv', index=None, sep=';')

    dense_conte.show()

    return(dense_conte.toPandas())


def bicis_personas():

    spark = SparkSession.builder.master("local[*]").getOrCreate()

    datos_bicis = (spark.read.csv(datos[3],header=True, inferSchema=True, sep =";", encoding='UTF-8'))

    datos_peatones = (spark.read.csv(datos[10],header=True, inferSchema=True, sep =";", encoding='UTF-8'))

    datos_bicis.createOrReplaceTempView('bicis')

    datos_peatones.createOrReplaceTempView('peatones')

    dist_bicis = spark.sql('''SELECT DISTINCT UPPER(DISTRITO) AS DISTRITO, SUM(BICICLETAS)OVER(PARTITION BY DISTRITO) AS QT_BICIS FROM bicis''')

    dist_bicis.createOrReplaceTempView('qt_bicis')

    dist_peatones = spark.sql('''SELECT DISTINCT UPPER(DISTRITO) AS DISTRITO, SUM(PEATONES)OVER(PARTITION BY DISTRITO) AS QT_PEATONES FROM peatones''')


    dist_peatones.createOrReplaceTempView('qt_peatones')
    dist_peatones.toPandas().to_csv('output/dist_peatones.csv', index=None, sep=';')
    dist_bicis.toPandas().to_csv('output/dist_bicis.csv', index=None, sep=';')
    dist_peatones.show()

    return(dist_bicis.toPandas())

def estacionamiento():

    spark = SparkSession.builder.master("local[*]").getOrCreate()

    datos_bicis = (spark.read.csv(datos[5],header=True, inferSchema=True, sep =";", encoding='UTF-8'))

    return(datos_bicis.toPandas())

def accidenteletal():

    spark = SparkSession.builder.master("local[*]").getOrCreate()

    datos_accidente= (spark.read.csv(datos[0],header=True, inferSchema=True, sep =";", encoding='Latin1'))

    datos_accidente.createOrReplaceTempView('accidentes')

    # dist_tipo = spark.sql('''SELECT DISTINCT fecha COUNT(cod_lesividad) OVER (PARTITION BY fecha) as QT_mortalidad FROM accidentes WHERE cod_lesividad='3' ''')
    dist_tipo = spark.sql('''SELECT fecha, count(*) from accidentes where cod_lesividad=3 OR cod_lesividad=4 group by fecha order by fecha''')

    dist_tipo.toPandas().to_csv('output/letalidad_fecha.csv', index=None, sep=';')
