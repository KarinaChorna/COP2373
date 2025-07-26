# Karina Chorna
# Programming Exercise 13
# The purpose of this code is to create a population table with the data of 10 cities in Florida, then prompt the user
# to choose a city and show a visual display of the city's population growth.

import sqlite3
import random
import matplotlib.pyplot as plt

# create the database and initial table
def create_database():
    conn = sqlite3.connect('population_KC.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS population (
                    city TEXT,
                    year INTEGER,
                    population INTEGER
                 )''')

    cities = [
        "Miami", "Orlando", "Tampa", "Jacksonville", "Tallahassee",
        "Fort Lauderdale", "St. Petersburg", "Sarasota", "Naples", "Gainesville"
    ]

    # initial populations for 2023
    initial_populations = {
        "Miami": 470000,
        "Orlando": 310000,
        "Tampa": 400000,
        "Jacksonville": 950000,
        "Tallahassee": 200000,
        "Fort Lauderdale": 180000,
        "St. Petersburg": 260000,
        "Sarasota": 57000,
        "Naples": 22000,
        "Gainesville": 140000
    }

    # insert data for 2023
    for city, pop in initial_populations.items():
        c.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)", (city, 2023, pop))

    conn.commit()
    conn.close()


# simulate population growth and decline for 20 years
def simulate_population_growth():
    conn = sqlite3.connect('population_KC.db')
    c = conn.cursor()

    c.execute("SELECT DISTINCT city FROM population WHERE year=2023")
    cities = [row[0] for row in c.fetchall()]

    for city in cities:
        c.execute("SELECT population FROM population WHERE city=? AND year=2023", (city,))
        pop = c.fetchone()[0]

        for year in range(2024, 2044):
            rate = random.uniform(-0.02, 0.05)
            pop = int(pop * (1 + rate))
            c.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)", (city, year, pop))

    conn.commit()
    conn.close()


# 3. plot population growth for a selected city
def plot_population_growth():
    conn = sqlite3.connect('population_KC.db')
    c = conn.cursor()

    c.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in c.fetchall()]
    conn.close()

    print("Available cities:")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")

    try:
        choice = int(input("Enter the number of the city you want to view: "))
        selected_city = cities[choice - 1]
    except (IndexError, ValueError):
        print("Invalid choice. Exiting.")
        return

    conn = sqlite3.connect('population_KC.db')
    c = conn.cursor()
    c.execute("SELECT year, population FROM population WHERE city=? ORDER BY year", (selected_city,))
    data = c.fetchall()
    conn.close()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    plt.figure(figsize=(10, 5))
    plt.plot(years, populations, marker='o', linestyle='-', color='blue')
    plt.title(f'Population Growth for {selected_city}')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# run functions
if __name__ == "__main__":
    create_database()
    simulate_population_growth()
    plot_population_growth()
