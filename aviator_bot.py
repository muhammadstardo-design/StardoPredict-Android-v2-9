def analyser_aviator(coefficients):
    if not coefficients:
        return "⚪ Aucun historique"

    moyenne = sum(coefficients) / len(coefficients)
    petits = sum(1 for x in coefficients if x < 2)
    gros = sum(1 for x in coefficients if x >= 5)

    if moyenne < 2 and petits >= len(coefficients) * 0.7:
        signal = "🟠 PRUDENCE"
    elif moyenne >= 3 and gros >= 2:
        signal = "🔴 ATTENTION"
    else:
        signal = "🟢 SIGNAL MODÉRÉ"

    return f"""
🤖 STARDOPREDICT AVIATOR

📊 Moyenne : {moyenne:.2f}x
📉 < 2x : {petits}
📈 ≥ 5x : {gros}

🎯 Signal : {signal}

⚠️ Ce signal est statistique et ne garantit
pas le prochain coefficient.
"""


# Exemple
historique = [1.20, 1.55, 2.10, 1.30, 4.50, 1.80, 7.20]

print(analyser_aviator(historique))
