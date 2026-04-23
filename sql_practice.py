import pandas as pd
import sqlite3

# 1. Φόρτωση των δεδομένων (χρησιμοποιούμε το encoding επειδή το αρχείο έχει ειδικούς χαρακτήρες)
df = pd.read_csv('sales_data_sample.csv', encoding='unicode_escape')

# 2. Δημιουργία μιας προσωρινής SQL βάσης στη μνήμη
conn = sqlite3.connect(':memory:')
df.to_sql('SALES_DATA', conn, index=False, if_exists='replace')

# 3. Η συνάρτηση για να τρέχουμε SQL queries
def run_query(query):
    return pd.read_sql_query(query, conn)

query = """
SELECT COUNTRY, SUM(SALES) as TOTAL_SALES
FROM SALES_DATA
GROUP BY COUNTRY
ORDER BY TOTAL_SALES DESC
LIMIT 5
"""
query= """
SELECT PRODUCTLINE, SUM(SALES) as TOTAL_SALES
FROM SALES_DATA
WHERE COUNTRY = 'USA'
GROUP BY PRODUCTLINE
ORDER BY TOTAL_SALES DESC
LIMIT 3
"""

query= """
SELECT COUNTRY, SUM(SALES) as TOTAL_SALES
FROM SALES_DATA
GROUP BY COUNTRY
HAVING TOTAL_SALES > 1000000
ORDER BY TOTAL_SALES DESC 
"""

result = run_query(query)
print(result)
