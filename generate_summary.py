def generate_summary(region, growth, category, trend):
    return f"{region} region shows {growth}% growth driven by {category}. Trend {trend}."
print(generate_summary("West",12,"Skincare","recovering"))
