#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Visualizador de Rendimiento HormigasAIS
Archivo: visualizador_rendimiento.py
Descripción: Carga AUDITORIA_HORMIGAS_2025.csv y genera gráficos de estado por rol y tareas críticas.
Compatible con Termux
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Ruta del CSV (ajusta si es necesario)
csv_file = "AUDITORIA_HORMIGAS_2025.csv"

# Validar existencia del CSV
if not os.path.isfile(csv_file):
    raise FileNotFoundError(f"No se encontró el archivo CSV: {csv_file}")

# Cargar CSV
df = pd.read_csv(csv_file)

# Columnas requeridas
required_cols = ["timestamp", "role", "task", "status", "critical_action_blocked"]

# Validar columnas
for col in required_cols:
    if col not in df.columns:
        raise ValueError(f"Columna faltante en CSV: {col}")

# Convertir timestamp a datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Estadísticas por rol
roles = df["role"].unique()
status_map = {"completed": 1, "pending": 0, "failed": -1}

plt.figure(figsize=(10, 6))
for role in roles:
    role_df = df[df["role"] == role]
    status_counts = role_df["status"].map(status_map).value_counts().sort_index()
    plt.bar(role, status_counts.get(1, 0), color="green", label="Completed" if role==roles[0] else "")
    plt.bar(role, status_counts.get(0, 0), bottom=status_counts.get(1,0), color="orange", label="Pending" if role==roles[0] else "")
    plt.bar(role, status_counts.get(-1, 0), bottom=status_counts.get(1,0)+status_counts.get(0,0), color="red", label="Failed" if role==roles[0] else "")

plt.title("Rendimiento de Tareas por Rol - HormigasAIS")
plt.ylabel("Cantidad de Tareas")
plt.xlabel("Rol")
plt.legend()
plt.tight_layout()
plt.show()

# Estadísticas de acciones críticas bloqueadas
critical_df = df.groupby("role")["critical_action_blocked"].sum()
plt.figure(figsize=(8,5))
critical_df.plot(kind="bar", color="purple")
plt.title("Acciones Críticas Bloqueadas por Rol")
plt.ylabel("Cantidad de Bloqueos")
plt.xlabel("Rol")
plt.tight_layout()
plt.show()
