import streamlit as st

st.set_page_config(
    page_title="Sudo Team",
    page_icon="💻",
)

st.title("Fase final: Sudo Team")

st.write("Hello, *World!* :sunglasses:")

secciones = [
    [
        "1.Volumen total agrupado por sector",
        "topIngresosSector.csv",
        "En este punto visualizamos los sectores que más euros brutos manejan. Destaca el sector de la salud debido a que las operaciones y el material sanitario tiene un elevado coste. Sorprendentemente el sector de la moda maneja un elevado volumen, con razón Amancio Ortega es el más rico de España.",
    ],
    [
        "2.Movimientos totales agrupados por sector",
        "topMovimientosSector.csv",
        "Aquí podrá visualizar cuales son los sectores que más movimientos (independientemente de su cuantía) tienen. No es de extrañar que destaque la alimentación ya que todo el mundo hace la compra cada pocos días. De nuevo llama la atención el sector de la moda que incluso se sitúa por encima de la alimentación.",
    ],
    [
        "3.Movimientos totales agrupados por franja horaria",
        "totalMovsPorHoras.csv",
        "En este KPI se puede ver como las franjas horarias con más movimiento son las 12-14 y 18-20 que coincide con los datos del punto anterior ya que la compra se suele hacer a última hora de la mañana y de 18 a 20 son las horas típicas de irse a comprar ropa a un centro comercial. También puede ser útil para saber en qué franja temporal realizar las labores de mantenimiento.",
    ],
    [
        "4.Movimientos totales agrupados por día de la semana",
        "totalMovsDiaSemana.csv",
        "Aquí podemos ver que días de la semana tienen más movimientos, no es de extrañar que el domingo tenga un volumen muy inferior debido a que es el día típico de descanso. También puede ser útil para saber en qué franja temporal realizar las labores de mantenimiento.",
    ],
    [
        "5.Volumen total en días lluviosos agrupado por sector",
        "topSectorLluvia.csv",
        "Este KPI es el mismo que el punto 1 pero teniendo en cuenta solo los días lluviosos, es muy útil compararlo con el KPI 1 para poder sacar algunas conclusiones. La principal diferencia es que baja el volumen en Ocio y tiempo libre y sube en Otros.",
    ],
    [
        "6.Barrios (código postal) ordenados por importe total",
        "barriosPorImporte.csv",
        "Mediante este mapa tendrá la capacidad de hacer zoom y con un esquema de colores visualizar los barrios con mayor volumen en euros.",
    ],
    [
        "7.Gráfica con las transacciones de media en cada franja horaria de los 10 sectores",
        "totalMovsPorHorasSector.csv",
        "Este KPI es muy útil compararlo con el 3 ya que se trata de la misma información pero segmentada por sectores. Destaca por ejemplo que casi todas las transacciones que se hacen de 22 a 24 son en restauración.",
    ],
    [
        "8.Barrios donde se compran muchos alimentos pero no hay comercio de alimentación",
        "barriosAlimentacioSinTiendas.csv",
        "Este KPI está pensado para encontrar barrios donde la gente decide hacer la compra en un barrio diferente al suyo, de ese modo es una información útil para invertir en un nuevo supermercado en la zona.",
    ],
    [
        "9.Barrios donde más se gasta en salud",
        "barriosMayorSalud.csv",
        "Este punto es útil para localizar la zona donde se gasta más en salud para futuras campañas de captación en seguros.",
    ],
    [
        "10.Ranking barrios que más gastan",
        "barriosMayorSector.csv",
        "Teniendo en cuenta todos los sectores, visualizamos los barrios que más gastan.",
    ],
    [
        "11.Por cada sector ver el volumen de compras durante el año, se puede filtrar por código postal.",
        "volumenComprasSector.csv",
        "En este KPI el usuario puede filtrar por código postal para ver cuantas transacciones se hacen en cada sector y en cada barrio.",
    ],
    [
        "12.Media de importes por sector pudiendo elegir el clima",
        "mediaImportesClima.csv",
        "En este KPI le permitimos al usuario poder elegir el clima entre soleado, lluvioso y nublado para poder ver el importe medio en los distintos sectores.",
    ],
]

checkboxes = []

checkboxes.append(st.sidebar.checkbox("Introducción", True))

for section in secciones:
    checkboxes.append(st.sidebar.checkbox(section[0]))

if checkboxes[0]:

    st.write(
        """
    # Bienvenido a nuestro trabajo de Big Data!
    👋 En esta web encontrará información de utilidad para distintos futuros servicios que puede ofrecer un banco.

    🌅 Esta información esta basada en datos de movimientos bancarios y el tiempo atmosférico de la región de Almeria en el año 2015.

    👈 En la barra lateral podrá ir navegando por los distintos KPIs.

    🚀 Pulsando en el siguiente botón podrá actualizar las consultas Spark por si hay nuevos datos"""
    )
