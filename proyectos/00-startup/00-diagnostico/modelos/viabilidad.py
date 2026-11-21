#!/usr/bin/env python3
"""Modelo de viabilidad preliminar (analista-financiero). Uso: python3 viabilidad.py [supuestos.csv]"""
import csv, os, sys

ruta = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "supuestos.csv")
s = {r["variable"]: r for r in csv.DictReader(open(ruta, encoding="utf-8"))}
faltan = [k for k, r in s.items() if not r["valor"].strip() or not r["fuente"].strip()]
if faltan:
    sys.exit(f"No se calcula: faltan valor o fuente en {faltan}. No se inventan supuestos.")
v = {k: float(r["valor"]) for k, r in s.items()}
margen = v["ticket_medio_usd"] - v["costo_variable_usd"]
cap = min(v["proyectos_mes"], v["horas_fundador_mes_max"] / v["horas_fundador_proyecto"])
print(f"Margen de contribución por proyecto: {margen:,.0f} USD")
print(f"Capacidad efectiva (limitada por el fundador): {cap:.1f} proyectos/mes")
print(f"Punto de equilibrio: {v['costos_fijos_usd'] / margen:.1f} proyectos/mes" if margen > 0 else "Margen ≤ 0: inviable")
print(f"Resultado mensual a capacidad: {cap * margen - v['costos_fijos_usd']:,.0f} USD")
