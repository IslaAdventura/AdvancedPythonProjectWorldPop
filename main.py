import csv
import matplotlib.pyplot as plt



def generate_population_dictionary_from_csv(filename):
  """
  -generate dictionary of population data from a csv file
  -return a dictionary following this strucure:
    {"Africa": {populaiton: [100, 200, 300], years: [1990, 2000, 2010]}}
  """
  population_per_continent = {}

  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
      continent = line['continent']
      year = line['year']
      population = line['population']

      if continent not in population_per_continent:
        population_per_continent[continent] = {'population': [], 'years': []}

      population_per_continent[continent]['population'].append(int(population))
      population_per_continent[continent]['years'].append(int(year))
  return population_per_continent


def generate_population_plots_from_dictionary(population_dictionary):
  """
  -generate the population plots from a dictionary
  -shows one plot/continent
  """
  for continent in population_dictionary:
    years = population_dictionary[continent]['years']
    population = population_dictionary[continent]['population']
    plt.plot(years, population, label=continent, marker="o", alpha=0.75)

  plt.xlabel("Year")
  plt.ylabel("Internet Usage (in billion users)")

  plt.title("- INTERNET USERS PER CONTINENT -")
  plt.tight_layout()
  plt.legend()
  plt.grid(True)
  plt.show()


filename = 'data.csv'

#display the population data in a plot
population_per_continent = generate_population_dictionary_from_csv(filename)
generate_population_plots_from_dictionary(population_per_continent)

plt.savefig('internet_users_per_continent.png')
