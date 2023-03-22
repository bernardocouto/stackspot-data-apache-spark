from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException

try:
    spark = (
        SparkSession
        .builder
        .appName("{{inputs.project_name_normalized}}")
        .getOrCreate()
    )
    reader = (
        spark
        .readStream
        .format("{{inputs.read_format}}")
        .load("{{inputs.read_load}}")
        .writeStream
        .format("{{inputs.write_format}}")
        .option("checkpointLocation", "{{inputs.write_checkpoint_location}}")
        .toTable(tableName="{{inputs.write_table_normalized}}")
        .awaitTermination()
    )
except AnalysisException as e:
    raise AnalysisException
except Exception as e:
    raise Exception
