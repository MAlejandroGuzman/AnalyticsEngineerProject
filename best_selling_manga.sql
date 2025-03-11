-- Esta consulta realiza un cambio en el nombre de las columnas y remplaza la antigua tabla llama 'best_selling_manga' realizada en load_data.py ,pero se tien que llamar especificamente a los otros modelos dejando de lado esta misma

{{ config(materialized='table') }}


WITH standardized_data AS (
    SELECT
        "Manga series" AS MANGA_TITLE,
        "Author(s)" AS AUTHOR,
        "Publisher" AS PUBLISHER,
        "Demographic" AS DEMOGRAPHIC,
        CAST("No. of collected volumes" AS INTEGER) AS COLLECTED_VOLUMES,
        "Serialized" AS SERIALIZED_PERIOD,
        CAST("Approximate sales in million(s)" AS FLOAT) AS SALES_MILLIONS,
        CAST("Average sales per volume in million(s)" AS FLOAT) AS AVG_SALES_PER_VOLUME
    FROM {{ source('kaggle_data', 'best_selling_manga') }}
)

SELECT * FROM standardized_data
