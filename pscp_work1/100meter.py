"""100meter"""
def main():
    # Step 1: Collect runner times
    times = []
    for i in range(8):
        time = float(input("Enter time for runner {}: ".format(i + 1)))
        times.append((time, i + 1))  # Store the time and runner number together

    # Step 2: Initialize variables for winners
    gold = silver = bronze = None
    gold_time = silver_time = bronze_time = float('inf')  # Set to infinity

    # Step 3: Find the three smallest times manually
    for time, runner in times:
        if time < gold_time:  # New gold
            bronze_time, silver_time, gold_time = silver_time, gold_time, time
            bronze, silver, gold = silver, gold, runner
        elif time < silver_time:  # New silver
            bronze_time, silver_time = silver_time, time
            bronze, silver = silver, runner
        elif time < bronze_time:  # New bronze
            bronze_time = time
            bronze = runner

    # Step 4: Output the results
    print(gold, silver, bronze)

# Call the main function
main()