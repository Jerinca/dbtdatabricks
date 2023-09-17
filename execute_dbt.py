import subprocess
import os
import json

dbt_command = os.environment.get('dbt_command', 'dbt run')

subprocess.run(['sh', -'c', dbt_command], check=True)