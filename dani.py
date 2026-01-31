import random
from statistics import mean, stdev

def roll_dice(num_sides):
    """
    Rolls a single die and returns a random value between 1 and num_sides
    
    Args:
        num_sides (int): The number of sides on the die
    
    Returns:
        int: Random number between 1 and num_sides
    """
    return random.randint(1, num_sides)


def roll_multiple_dice(num_dice, num_sides):
    """
    Rolls multiple dice and returns a list of results
    
    Args:
        num_dice (int): Number of dice to roll
        num_sides (int): Number of sides per die
    
    Returns:
        list: List of roll results
    """
    results = []
    # Loop through and roll each die
    for i in range(num_dice):
        results.append(roll_dice(num_sides))
    return results


def perform_rolls(num_dice, num_sides, num_rolls):
    """
    Performs multiple sets of rolls and stores the results
    
    Args:
        num_dice (int): Number of dice per roll
        num_sides (int): Number of sides per die
        num_rolls (int): Number of times to roll
    
    Returns:
        list: List of all rolls (each roll is a list of die values)
    """
    all_rolls = []
    
    # Perform rolls with loops
    for roll_num in range(num_rolls):
        dice_results = roll_multiple_dice(num_dice, num_sides)
        all_rolls.append(dice_results)
    
    return all_rolls


def calculate_sum(numbers):
    """
    Calculates the sum of a list of numbers
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int/float: Sum of all numbers
    """
    total = 0
    for num in numbers:
        total += num
    return total


def display_results(all_rolls):
    """
    Displays all the rolls in formatted output
    
    Args:
        all_rolls (list): List of all rolls
    """
    if not all_rolls:
        print("\nNo rolls to display.")
        return
    
    print("\n" + "="*60)
    print("ROLL RESULTS")
    print("="*60)
    
    # Loop through all rolls and display them
    for index, roll in enumerate(all_rolls, 1):
        roll_total = calculate_sum(roll)
        roll_str = ", ".join(map(str, roll))
        print(f"Roll {index:3d}: [{roll_str}] → Total: {roll_total}")
    
    print("="*60)


def calculate_statistics(all_rolls):
    """
    Calculates and displays statistics from all rolls
    
    Args:
        all_rolls (list): List of all rolls
    
    Returns:
        dict: Dictionary containing statistics
    """
    if not all_rolls:
        return None
    
    # Flatten array and calculate statistics
    all_values = []
    total_sum = 0
    roll_totals = []
    
    for roll in all_rolls:
        roll_sum = calculate_sum(roll)
        roll_totals.append(roll_sum)
        total_sum += roll_sum
        
        for value in roll:
            all_values.append(value)
    
    # Calculate statistics with conditional logic
    average = total_sum / len(all_rolls) if all_rolls else 0
    max_value = max(all_values) if all_values else 0
    min_value = min(all_values) if all_values else 0
    max_roll = max(roll_totals) if roll_totals else 0
    min_roll = min(roll_totals) if roll_totals else 0
    
    # Calculate standard deviation if we have more than one roll
    std_dev = 0
    if len(roll_totals) > 1:
        std_dev = stdev(roll_totals)
    
    stats = {
        'total_sum': total_sum,
        'average': average,
        'max_value': max_value,
        'min_value': min_value,
        'max_roll': max_roll,
        'min_roll': min_roll,
        'std_dev': std_dev,
        'all_values': all_values
    }
    
    return stats


def analyze_rolls(all_rolls, num_dice, num_sides):
    """
    Provides analysis and interpretation of the rolls with conditional statements
    
    Args:
        all_rolls (list): List of all rolls
        num_dice (int): Number of dice rolled
        num_sides (int): Sides per die
    """
    if not all_rolls:
        return
    
    stats = calculate_statistics(all_rolls)
    
    all_values = stats['all_values']
    total_sum = stats['total_sum']
    average = stats['average']
    max_value = stats['max_value']
    min_value = stats['min_value']
    
    expected_average = ((num_sides + 1) / 2) * num_dice
    
    print("\n" + "="*60)
    print("STATISTICS")
    print("="*60)
    print(f"Total Sum:        {total_sum}")
    print(f"Average Per Roll: {average:.2f}")
    print(f"Highest Die Roll: {max_value}")
    print(f"Lowest Die Roll:  {min_value}")
    print(f"Max Roll Total:   {stats['max_roll']}")
    print(f"Min Roll Total:   {stats['min_roll']}")
    if stats['std_dev'] > 0:
        print(f"Std Deviation:    {stats['std_dev']:.2f}")
    print("="*60)
    
    print("\n" + "="*60)
    print("ANALYSIS")
    print("="*60)
    
    # Conditional statements for analysis
    if len(all_rolls) == 1:
        print(f"You rolled {num_dice} dice with {num_sides} sides each.")
        
        if average == expected_average:
            print("✓ The roll matches the expected average perfectly!")
        elif average > expected_average:
            print("✓ Great luck! Your roll is above the expected average.")
        else:
            print("✗ The roll is below the expected average.")
    else:
        print(f"Over {len(all_rolls)} rolls with {num_dice}d{num_sides}:")
        
        if average >= expected_average:
            diff = average - expected_average
            print(f"✓ Your average ({average:.2f}) is {diff:.2f} above the expected average.")
        else:
            diff = expected_average - average
            print(f"✗ Your average ({average:.2f}) is {diff:.2f} below the expected average.")
        
        # Add distribution analysis
        roll_range = stats['max_roll'] - stats['min_roll']
        print(f"Distribution range: {roll_range} (from {stats['min_roll']} to {stats['max_roll']})")
        
        # Conditional feedback based on roll distribution
        if roll_range > (num_sides * 0.5):
            print("✓ You have a wide variety of results!")
        elif roll_range < (num_sides * 0.2):
            print("✓ Your results are quite consistent.")
        else:
            print("○ Your results show normal distribution.")
    
    print("="*60)


def get_positive_int(prompt, min_val=1, max_val=None):
    """
    Gets a valid positive integer from user input
    
    Args:
        prompt (str): The prompt to display
        min_val (int): Minimum allowed value
        max_val (int): Maximum allowed value (None for no limit)
    
    Returns:
        int: Valid integer input
    """
    while True:
        try:
            value = int(input(prompt))
            
            # Conditional validation
            if value < min_val:
                print(f"Please enter a number >= {min_val}")
                continue
            
            if max_val is not None and value > max_val:
                print(f"Please enter a number <= {max_val}")
                continue
            
            return value
        except ValueError:
            print("Please enter a valid number.")


def main():
    """
    Main function to run the dice rolling simulator
    """
    print("\n" + "="*60)
    print("🎲 DICE ROLLING SIMULATOR 🎲")
    print("="*60 + "\n")
    
    all_rolls = []
    
    while True:
        print("\nOptions:")
        print("1. Roll Dice")
        print("2. View Results")
        print("3. Clear All")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '1':
            print("\n--- Configuration ---")
            
            # Get number of dice
            num_dice = get_positive_int(
                "Number of dice (1-20): ",
                min_val=1,
                max_val=20
            )
            
            # Get number of sides
            print("\nDice Types:")
            print("1) 4-sided  (D4)")
            print("2) 6-sided  (D6)")
            print("3) 8-sided  (D8)")
            print("4) 10-sided (D10)")
            print("5) 12-sided (D12)")
            print("6) 20-sided (D20)")
            print("7) 100-sided (D100)")
            
            dice_choice = input("Select dice type (1-7): ").strip()
            dice_types = {'1': 4, '2': 6, '3': 8, '4': 10, '5': 12, '6': 20, '7': 100}
            
            if dice_choice not in dice_types:
                print("Invalid choice. Using D6.")
                num_sides = 6
            else:
                num_sides = dice_types[dice_choice]
            
            # Get number of rolls
            num_rolls = get_positive_int(
                "Number of rolls (1-100): ",
                min_val=1,
                max_val=100
            )
            
            # Perform rolls
            print(f"\nRolling {num_dice}d{num_sides} {num_rolls} time(s)...\n")
            all_rolls = perform_rolls(num_dice, num_sides, num_rolls)
            
            # Display and analyze
            display_results(all_rolls)
            analyze_rolls(all_rolls, num_dice, num_sides)
        
        elif choice == '2':
            if not all_rolls:
                print("\nNo rolls to display yet. Roll some dice first!")
            else:
                display_results(all_rolls)
                # Get last roll's parameters for analysis
                last_roll = all_rolls[-1]
                num_dice = len(last_roll)
                # Try to guess num_sides from max value, default to 6
                num_sides = max(last_roll) if last_roll else 6
                analyze_rolls(all_rolls, num_dice, num_sides)
        
        elif choice == '3':
            if not all_rolls:
                print("\nNothing to clear.")
            else:
                confirm = input("Are you sure you want to clear all rolls? (y/n): ").strip().lower()
                if confirm == 'y':
                    all_rolls = []
                    print("✓ All rolls cleared.")
        
        elif choice == '4':
            print("\nThanks for using the Dice Rolling Simulator! Goodbye!")
            break
        
        else:
            print("Invalid option. Please select 1-4.")


if __name__ == "__main__":
    main()