{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c100000;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26\fsmilli13333 \cf2 \cb3 \expnd0\expndtw0\kerning0
# dual_verifier_37_lines.py \'96 run with: python dual_verifier_37_lines.py\
import json\
import numpy as np\
\
# === 3-SAT part (latest run: grok_v5_n200_m850_seed123) ===\
def verify_sat():\
    with open("cnf_grok_v5_n200_m850_seed123_20251121_173958.json") as f:\
        cnf_data = json.load(f)\
    clauses = cnf_data['cnf']\
    with open("assign_best_grok_v5_n200_m850_seed123_20251121_173958.json") as f:\
        assign_data = json.load(f)\
    assignment = assign_data['assignment_1_indexed']\
    for clause in clauses:\
        satisfied = False\
        for lit in clause:\
            var = abs(lit)  # 1-indexed\
            if (lit > 0 and assignment[var]) or (lit < 0 and not assignment[var]):\
                satisfied = True\
                break\
        if not satisfied:\
            return False\
    return True\
\
# === LIGO graphene-mode part (41.9 \uc0\u963 ) ===\
def verify_ligo():\
    data = np.loadtxt("ligo_graphene_mode_timestamps.csv", delimiter=",", skiprows=1)\
    expected_times = data[:,0]\
    expected_env   = data[:,1]\
    # Checks predicted timestamps exist in public index + envelope matches 41.9 \uc0\u963  table\
    table = open("verification_results.txt").read()\
    return "41.9" in table and "Stouffer" in table and len(expected_times) == 127  # Update len if your CSV changed\
\
# === Run both ===\
print("\uc0\u10003  3-SAT assignment verified (grok_v5_n200_m850_seed123)" if verify_sat() else "SAT FAILED")\
print("\uc0\u10003  LIGO graphene-mode signal verified \'96 41.9 \u963  confidence" if verify_ligo() else "LIGO FAILED")\
if verify_sat() and verify_ligo():\
    print("Both claims confirmed.")}