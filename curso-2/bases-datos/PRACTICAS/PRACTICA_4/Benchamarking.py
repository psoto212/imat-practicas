import os
import time
import pymysql
from typing import List
conexion = pymysql.connect(host=os.environ['MYSQL_HOST'], user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'], port=3306, database='employees')

def obtener_usuarios() -> List[str]:
    cursor = conexion.cursor()
    sql = '\n    SELECT DISTINCT first_name\n    FROM employees\n    ORDER BY first_name ASC\n    LIMIT 200\n    '
    cursor.execute(sql)
    result = cursor.fetchall()
    usuarios = [fila[0] for fila in result]
    cursor.close()
    return usuarios

def benchmark_salarios(usuarios: List[str]) -> None:
    cursor = conexion.cursor()
    sql_sin_optimizar = '\n    SELECT *\n    FROM employees e, salaries s\n    WHERE e.emp_no = s.emp_no\n      AND e.first_name = %s\n    '
    sql_optimizada = '\n    SELECT e.emp_no, s.salary, s.from_date, s.to_date\n    FROM employees e\n    INNER JOIN salaries s ON e.emp_no = s.emp_no\n    WHERE e.first_name = %s\n    '
    t0 = time.perf_counter()
    for nombre in usuarios:
        cursor.execute(sql_sin_optimizar, [nombre])
        cursor.fetchall()
    t1 = time.perf_counter()
    t2 = time.perf_counter()
    for nombre in usuarios:
        cursor.execute(sql_optimizada, [nombre])
        cursor.fetchall()
    t3 = time.perf_counter()
    print('\n[2.1] Tiempo sin optimizar:', t1 - t0)
    print('[2.1] Tiempo optimizada:', t3 - t2)
    cursor.close()

def benchmark_departamentos() -> None:
    cursor = conexion.cursor()
    sql_sin_optimizar = "\n    SELECT e.*\n    FROM employees e, dept_emp de, departments d\n    WHERE e.emp_no = de.emp_no\n      AND de.dept_no = d.dept_no\n      AND (\n        d.dept_name = 'Development'\n        OR d.dept_name = 'Marketing'\n        OR d.dept_name = 'Sales'\n        OR d.dept_name = 'Customer Service'\n      )\n    "
    sql_optimizada = "\n    SELECT e.first_name, e.last_name, e.hire_date\n    FROM employees e\n    INNER JOIN dept_emp de ON e.emp_no = de.emp_no\n    INNER JOIN departments d ON de.dept_no = d.dept_no\n    WHERE d.dept_name IN ('Development', 'Marketing', 'Sales', 'Customer Service')\n    "
    t0 = time.perf_counter()
    for _ in range(5):
        cursor.execute(sql_sin_optimizar)
        cursor.fetchall()
    t1 = time.perf_counter()
    t2 = time.perf_counter()
    for _ in range(5):
        cursor.execute(sql_optimizada)
        cursor.fetchall()
    t3 = time.perf_counter()
    print('\n[2.2] Tiempo sin optimizar:', t1 - t0)
    print('[2.2] Tiempo optimizada:', t3 - t2)
    cursor.close()

def benchmarking_fecha_contratacion() -> None:
    cursor = conexion.cursor()
    sql_sin_optimizar = "\n    SELECT e.first_name, e.last_name, e.hire_date\n    FROM employees e, dept_emp de, departments d\n    WHERE e.emp_no = de.emp_no\n      AND de.dept_no = d.dept_no\n      AND (\n        d.dept_name = 'Development'\n        OR d.dept_name = 'Marketing'\n        OR d.dept_name = 'Sales'\n        OR d.dept_name = 'Customer Service'\n        OR d.dept_name = 'Quality Management'\n      )\n    HAVING e.hire_date >= %s AND e.hire_date < %s\n    "
    sql_optimizada = "\n    SELECT e.first_name, e.last_name, e.hire_date\n    FROM employees e\n    INNER JOIN dept_emp de ON e.emp_no = de.emp_no\n    INNER JOIN departments d ON de.dept_no = d.dept_no\n    WHERE d.dept_name IN ('Development', 'Marketing', 'Sales', 'Customer Service', 'Quality Management')\n      AND e.hire_date >= %s\n      AND e.hire_date < %s\n    "
    t0 = time.perf_counter()
    for year in range(1990, 1999):
        inicio = f'{year}-01-01'
        fin = f'{year + 1}-01-01'
        cursor.execute(sql_sin_optimizar, [inicio, fin])
        cursor.fetchall()
    t1 = time.perf_counter()
    t2 = time.perf_counter()
    for year in range(1990, 1999):
        inicio = f'{year}-01-01'
        fin = f'{year + 1}-01-01'
        cursor.execute(sql_optimizada, [inicio, fin])
        cursor.fetchall()
    t3 = time.perf_counter()
    print('\n[2.3] Tiempo sin optimizar:', t1 - t0)
    print('[2.3] Tiempo optimizada:', t3 - t2)
    cursor.close()

def benchmarking_titulos_usuarios_indice(usuarios: List[str]) -> None:
    cursor = conexion.cursor()
    sql = '\n    SELECT e.first_name, e.last_name, t.title, t.from_date, t.to_date\n    FROM employees e\n    INNER JOIN titles t ON e.emp_no = t.emp_no\n    WHERE e.first_name = %s\n    '
    t0 = time.perf_counter()
    for nombre in usuarios:
        cursor.execute(sql, [nombre])
        cursor.fetchall()
    t1 = time.perf_counter()
    t2 = time.perf_counter()
    indice_creado = False
    try:
        cursor.execute('CREATE INDEX idx_employees_first_name ON employees(first_name)')
        conexion.commit()
        indice_creado = True
    except Exception:
        conexion.rollback()
    for nombre in usuarios:
        cursor.execute(sql, [nombre])
        cursor.fetchall()
    if indice_creado:
        try:
            cursor.execute('DROP INDEX idx_employees_first_name ON employees')
            conexion.commit()
        except Exception:
            conexion.rollback()
    t3 = time.perf_counter()
    print('\n[2.4] Tiempo sin índice:', t1 - t0)
    print('[2.4] Tiempo con índice:', t3 - t2)
    cursor.close()

def benchmark_salarios_superiores_media() -> None:
    cursor = conexion.cursor()
    sql_sin_optimizar = "\n    SELECT e.emp_no, e.first_name, e.last_name, s.from_date\n    FROM employees e\n    INNER JOIN salaries s ON e.emp_no = s.emp_no\n    WHERE s.to_date = '9999-01-01'\n      AND s.from_date >= %s\n      AND s.from_date < %s\n      AND s.salary > (\n        SELECT AVG(s2.salary)\n        FROM salaries s2\n        WHERE s2.to_date = '9999-01-01'\n      )\n    "
    sql_vista = "\n    CREATE VIEW vista_salarios_actuales AS\n    SELECT emp_no, salary, from_date, to_date\n    FROM salaries\n    WHERE to_date = '9999-01-01'\n    "
    sql_optimizada = '\n    SELECT e.emp_no, e.first_name, e.last_name, v.from_date\n    FROM employees e\n    INNER JOIN vista_salarios_actuales v ON e.emp_no = v.emp_no\n    JOIN (\n        SELECT AVG(salary) AS media_actual\n        FROM vista_salarios_actuales\n    ) m\n    WHERE v.from_date >= %s\n      AND v.from_date < %s\n      AND v.salary > m.media_actual\n    '
    t0 = time.perf_counter()
    for year in range(1990, 2004):
        inicio = f'{year}-01-01'
        fin = f'{year + 1}-01-01'
        cursor.execute(sql_sin_optimizar, [inicio, fin])
        cursor.fetchall()
    t1 = time.perf_counter()
    t2 = time.perf_counter()
    try:
        cursor.execute('DROP VIEW IF EXISTS vista_salarios_actuales')
        conexion.commit()
    except Exception:
        conexion.rollback()
    cursor.execute(sql_vista)
    conexion.commit()
    indice_creado = False
    try:
        cursor.execute('CREATE INDEX idx_salaries_actuales ON salaries(to_date, from_date, salary)')
        conexion.commit()
        indice_creado = True
    except Exception:
        conexion.rollback()
    for year in range(1990, 2004):
        inicio = f'{year}-01-01'
        fin = f'{year + 1}-01-01'
        cursor.execute(sql_optimizada, [inicio, fin])
        cursor.fetchall()
    if indice_creado:
        try:
            cursor.execute('DROP INDEX idx_salaries_actuales ON salaries')
            conexion.commit()
        except Exception:
            conexion.rollback()
    cursor.execute('DROP VIEW IF EXISTS vista_salarios_actuales')
    conexion.commit()
    t3 = time.perf_counter()
    print('\n[2.5] Tiempo sin optimizar:', t1 - t0)
    print('[2.5] Tiempo optimizada:', t3 - t2)
    cursor.close()

def substr_vs_like(usuarios: List[str]) -> None:
    cursor = conexion.cursor()
    sql_substr = '\n    SELECT first_name, birth_date, gender\n    FROM employees\n    WHERE SUBSTR(first_name, 1, 2) = %s\n    '
    sql_like = '\n    SELECT first_name, birth_date, gender\n    FROM employees\n    WHERE first_name LIKE %s\n    '
    t0 = time.perf_counter()
    for nombre in usuarios:
        prefijo = nombre[:2]
        cursor.execute(sql_substr, [prefijo])
        cursor.fetchall()
    t1 = time.perf_counter()
    t2 = time.perf_counter()
    indice_creado = False
    try:
        cursor.execute('CREATE INDEX idx_first_name_like ON employees(first_name)')
        conexion.commit()
        indice_creado = True
    except Exception:
        conexion.rollback()
    for nombre in usuarios:
        patron = nombre[:2] + '%'
        cursor.execute(sql_like, [patron])
        cursor.fetchall()
    if indice_creado:
        try:
            cursor.execute('DROP INDEX idx_first_name_like ON employees')
            conexion.commit()
        except Exception:
            conexion.rollback()
    t3 = time.perf_counter()
    print('\n[2.6] Tiempo SUBSTR (sin optimizar):', t1 - t0)
    print('[2.6] Tiempo LIKE + índice (optimizada):', t3 - t2)
    cursor.close()

def main():
    try:
        usuarios = obtener_usuarios()
        print('Usuarios obtenidos:', len(usuarios))
        benchmark_salarios(usuarios)
        benchmark_departamentos()
        benchmarking_fecha_contratacion()
        benchmarking_titulos_usuarios_indice(usuarios)
        benchmark_salarios_superiores_media()
        substr_vs_like(usuarios)
    except Exception as e:
        print('Error:', e)
        conexion.rollback()
    finally:
        conexion.close()
if __name__ == '__main__':
    main()
