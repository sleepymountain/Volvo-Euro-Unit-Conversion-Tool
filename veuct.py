def menu():
    print("Volvo Euro Unit Conversion Tool")
    print("\n")
    print(f"(1) Newton-Meters to Foot-Pounds Conversion")
    print(f"(2) Kilo-Pascal to PSI Conversion")
    print("\n")
    print(f"Please choose a conversion tool.")
    choice = input("Tool #: ")
    if choice == "1":
        ntf_conv()
    elif choice == "2":
        kpa_psi_conv()
    elif choice is None:
        print(f"(!) Please Choose an Option")
        menu()


def ntf_conv():
    # Newton-Meters to Foot-Pounds Conversion
    print(f"Newton-Meters to Foot-Pounds Conversion")
    print("\n")
    newton_meters_val = int(input("Newton Meters: "))
    foot_pounds_val = float(newton_meters_val * 0.73756215)
    print(str(newton_meters_val) + " Newton-Meters is " + str(foot_pounds_val) + " Foot-Pounds")


def kpa_psi_conv():
    # Kilo-Pascal to PSI Conversion
    print(f"Kilo-Pascal to PSI Conversion")
    print("\n")
    kilo_pascal_val = int(input("kPa: "))
    psi_val = float(kilo_pascal_val * 0.145)
    print(str(kilo_pascal_val) + " kPa is " + str(psi_val) + " psi")


menu()
