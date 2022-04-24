from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import desc

import pandas as pd
from google.cloud import storage
import sys
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler
from pyspark.ml import Pipeline

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

sc = SparkContext('local')
spark = SparkSession(sc)

datos=['data\Anthem_CTC_Accidentalidad.csv','data\Anthem_CTC_AsignaciónPatinetes.csv','data\Anthem_CTC_Bicicletas_Disponibilidad.csv',
'data\Anthem_CTC_BicicletasAforo.csv','data\Anthem_CTC_Callejero.csv','data\Anthem_CTC_CallesEstacionamientoRegulado.csv',
'data\Anthem_CTC_ContaminacionAcustica.csv','data\Anthem_CTC_Contenedores_Ubicacion.csv','data\Anthem_CTC_InstalacionesFotovoltaicas.csv',
'data\Anthem_CTC_OcupacionAparcamientosRotacionales.csv','data\Anthem_CTC_PeatonesAforo.csv','data\Anthem_CTC_Taxi_ObjetosPerdidos.csv',
'data\Anthem_CTC_Taxi_ReservaParadas.csv']

datos_aire=['data\Aire\Anthem_CTC_Aire_Enero.csv','data\Aire\Anthem_CTC_Aire_Febrero.csv','data\Aire\Anthem_CTC_Aire_Marzo.csv',
'data\Aire\Anthem_CTC_Aire_Abril.csv','data\Aire\Anthem_CTC_Aire_Mayo.csv','data\Aire\Anthem_CTC_Aire_Junio.csv',
'data\Aire\Anthem_CTC_Aire_Julio.csv','data\Aire\Anthem_CTC_Aire_Agosto.csv','data\Aire\Anthem_CTC_Aire_Septiembre.csv',
'data\Aire\Anthem_CTC_Aire_Octubre.csv','data\Aire\Anthem_CTC_Aire_Noviembre.csv','data\Aire\Anthem_CTC_Aire_Diciembre.csv',]

datos_censo=['data\Censo\Anthem_CTC_Censo_012051.csv','data\Censo\Anthem_CTC_Censo_022051.csv','data\Censo\Anthem_CTC_Censo_032051.csv',
'data\Censo\Anthem_CTC_Censo_042051.csv','data\Censo\Anthem_CTC_Censo_052051.csv','data\Censo\Anthem_CTC_Censo_062051.csv',
'data\Censo\Anthem_CTC_Censo_072051.csv','data\Censo\Anthem_CTC_Censo_082051.csv','data\Censo\Anthem_CTC_Censo_092051.csv',
'data\Censo\Anthem_CTC_Censo_102051.csv','data\Censo\Anthem_CTC_Censo_112051.csv','data\Censo\Anthem_CTC_Censo_122051.csv',]

datos_multas=['data\Multas\Anthem_CTC_Multas_012051.csv','data\Multas\Anthem_CTC_Multas_022051.csv','data\Multas\Anthem_CTC_Multas_032051.csv',
'data\Multas\Anthem_CTC_Multas_042051.csv','data\Multas\Anthem_CTC_Multas_052051.csv','data\Multas\Anthem_CTC_Multas_062051.csv',
'data\Multas\Anthem_CTC_Multas_072051.csv','data\Multas\Anthem_CTC_Multas_082051.csv','data\Multas\Anthem_CTC_Multas_092051.csv',
'data\Multas\Anthem_CTC_Multas_102051.csv','data\Multas\Anthem_CTC_Multas_112051.csv','data\Multas\Anthem_CTC_Multas_122051.csv',]

datos_trafico=['data\Trafico\Anthem_CTC_Traffic_012051.csv','data\Trafico\Anthem_CTC_Traffic_022051.csv','data\Trafico\Anthem_CTC_Traffic_032051.csv',
'data\Trafico\Anthem_CTC_Traffic_042051.csv','data\Trafico\Anthem_CTC_Traffic_052051.csv','data\Trafico\Anthem_CTC_Traffic_062051.csv',
'data\Trafico\Anthem_CTC_Traffic_072051.csv','data\Trafico\Anthem_CTC_Traffic_082051.csv','data\Trafico\Anthem_CTC_Traffic_092051.csv',
'data\Trafico\Anthem_CTC_Traffic_102051.csv','data\Trafico\Anthem_CTC_Traffic_112051.csv','data\Trafico\Anthem_CTC_Traffic_122051.csv',]

multas = (spark.read.csv(datos_multas[11],header=True, inferSchema=True, sep =";", encoding='Latin1'))
accidentalidad = (spark.read.csv(datos[0],header=True, inferSchema=True, sep =";", encoding='UTF-8'))
trafico = (spark.read.csv(datos_trafico[11],header=True, inferSchema=True, sep =";", encoding='UTF-8'))
patinetes = (spark.read.csv(datos[1],header=True, inferSchema=True, sep =";", encoding='UTF-8'))
zonasVerdes = (spark.read.csv("data\SuperficieZonasVerdesDistritosCalles_2020.csv",header=True, inferSchema=True, sep =";", encoding='UTF-8'))

########################################################
############  Cantidad de multas por tipo  #############
########################################################

multas.createOrReplaceTempView('Multas')

multasCount = spark.sql('''SELECT DISTINCT `HECHO-BOL`, COUNT(`HECHO-BOL`)OVER(PARTITION BY `HECHO-BOL`) AS Cantidad FROM Multas ORDER BY Cantidad DESC''')
multasCount.show(truncate=False)

multasCount.toPandas().to_csv('output/multasCount.csv', index=None, sep=';', mode='w')


##########################################################
#####  Cantidad de accidentes por tipo y distrito  #######
##########################################################

accidentalidad.createOrReplaceTempView('Accidentes')

accidenteCount = spark.sql('''SELECT DISTINCT cod_distrito, tipo_accidente, COUNT(*)OVER(PARTITION BY tipo_accidente, cod_distrito) AS Cantidad FROM Accidentes ORDER BY cod_distrito''')
accidenteCount.show(truncate=False)

accidenteCount.toPandas().to_csv('output/accidentesTipo.csv', index=None, sep=';', mode='w')

##########################################################
#######  Cantidad total de patinetes por distrito  #######
##########################################################

patinetesData = patinetes.groupBy("DISTRITO").sum("TOTAL") 
patinetesData.show(truncate=False)

patinetesData.createOrReplaceTempView('patinetesData')


datos_censo = (spark.read.csv(datos_censo[11],header=True, inferSchema=True, sep =";", encoding='utf-8'))

datos_censo.createOrReplaceTempView('Censo')

dist_censo = spark.sql('''SELECT DISTINCT DESC_DISTRITO, (SUM(EspanolesHombres)OVER(PARTITION BY DESC_DISTRITO)  + SUM(EspanolesMujeres)OVER(PARTITION BY DESC_DISTRITO)  + SUM(ExtranjerosHombres)OVER(PARTITION BY DESC_DISTRITO)  + SUM(ExtranjerosMujeres)OVER(PARTITION BY DESC_DISTRITO) ) AS Censo FROM Censo ORDER BY DESC_DISTRITO''')

for colname in dist_censo.columns:
    dist_censo = dist_censo.withColumn(colname, fun.trim(fun.col(colname)))

dist_censo.createOrReplaceTempView('dense_dist')

dist_censo.show()

patinetesDistrito = spark.sql('''SELECT DISTRITO, (`sum(TOTAL)`/Censo) AS patinetes FROM patinetesData JOIN dense_dist ON DISTRITO=DESC_DISTRITO ORDER BY patinetes ASC''')

patinetesDistrito.show(truncate=False)

patinetesDistrito.toPandas().to_csv('output/patinetesDistrito.csv', index=None, sep=';', mode='w')

##########################################################
#########  Cantidad zonas verdes por distrito  ###########
##########################################################

zonasVerdeDistrito = zonasVerdes.groupBy("DISTRITO").sum("SUPERFICIE (ha)") 
zonasVerdeDistrito.show(truncate=False)

zonasVerdeDistrito.toPandas().to_csv('output/zonasVerdeDistrito.csv', index=None, sep=';', mode='w')

##########################################################
#############  Cantidad taxis por barrio  ################
##########################################################

taxis.createOrReplaceTempView('taxis')

taxisCount = spark.sql('''SELECT DISTINCT `Barrio`, COUNT(`Barrio`)OVER(PARTITION BY `Barrio`) AS Cantidad FROM taxis ORDER BY Cantidad DESC''')

taxisCount.show(truncate=False)
taxisCount.toPandas().to_csv('output/taxisCount.csv', encoding="utf-8", index=None, sep=';', mode='w')