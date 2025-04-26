# main.py

def calculate_water_saving(cars_per_day, working_days):
    traditional_per_car = 200 + 2   # 200L direct + 2L chemical water
    waterless_per_car = 2           # Only 2L (chemical manufacturing)

    total_traditional = traditional_per_car * cars_per_day * working_days
    total_waterless = waterless_per_car * cars_per_day * working_days
    water_saved = total_traditional - total_waterless
    saving_percent = (water_saved / total_traditional) * 100

    print("==== Waterless Car Wash Savings Report ====")
    print(f"Cars washed per day: {cars_per_day}")
    print(f"Working days per year: {working_days}")
    print(f"Total water used (Traditional Wash): {total_traditional:,} liters/year")
    print(f"Total water used (Waterless Wash): {total_waterless:,} liters/year")
    print(f"Water saved per year: {water_saved:,} liters")
    print(f"Saving Percentage: {saving_percent:.2f}%")
    print("===========================================")

if __name__ == "__main__":
    # Example use: 20 cars/day, 250 working days
    calculate_water_saving(cars_per_day=20, working_days=250)
