from tools.financial_parser import calculate_financial_metrics

result = calculate_financial_metrics.run(
    "outputs/sample_financials.csv"
)

print("\nFINANCIAL ANALYSIS RESULT:\n")
print(result)
