import copy
import random

from de_GA.core import get_best_solutions, get_worst_solutions
from de_GA.core.population import Population
from de_GA.core.test_functions import Function
from de_GA.utils import generate_rand_value


class DifferentialEvolution(object):
    def __init__(self,
                 data,
                 type,
                 num_iterations=10,
                 CR=0.4,
                 F=0.48,
                 population_size=5,
                 metric_value=False,
                 print_status=False,
                 visualize=False,
                 func=None,
                 model=None,
                 params=None):
        random.seed()
        params_ = copy.deepcopy(params)
        del params_['model']
        self.print_status = print_status
        self.visualize = visualize
        self.num_iterations = num_iterations
        self.iteration = 0
        self.CR = CR
        self.F = F
        self.population_size = population_size
        self.model = model
        self.params = params_
        self.data = data
        self.type = type
        self.metric_value = self.get_metric_value(metric_value, func) if not metric_value else metric_value
        self.func = Function(self.model, type=self.type, func=func)
        self.population = Population(data=self.data,
                                     population_size=self.population_size,
                                     init_generate=True,
                                     objective=self.func,
                                     model=model,
                                     params=self.params)

    def get_metric_value(self, metric_value, func):
        if metric_value and func == 'rmse':
            return 1 - metric_value
        elif not metric_value:
            return 0.90

    def iterate(self):
        # DE
        self.differential_evolution()

        # Mutation
        self.mutation()
        self.iteration += 1

    def differential_evolution(self):
        for ix in range(self.population.population_size):
            x = self.population.individuals[ix]
            [a, b, c] = random.sample(self.population.individuals, 3)
            while x == a or x == b or x == c:
                [a, b, c] = random.sample(self.population.individuals, 3)

            R = random.random() * x.dim
            y = copy.deepcopy(x)

            for iy in range(x.dim):
                ri = random.random()

                if ri < self.CR or iy == R:
                    # TODO verificar o tipo
                    if self.population.individuals[ix].params_type[iy] == bool:
                        y.coords[iy] = generate_rand_value(b, c, bool).coords[iy]
                    else:
                        _ = a.coords[iy] + self.F * (b.coords[iy] - c.coords[iy])
                        _ = self.population.individuals[ix].params_type[iy](_)

                        if _ < self.population.range_lower_limit[iy]:
                            _ = self.population.range_lower_limit[iy]

                        elif _ > self.population.range_upper_limit[iy]:
                            _ = self.population.range_upper_limit[iy]

                        y.coords[iy] = _

            y.evaluate_point()
            if y.z > x.z:
                self.population.individuals[ix] = y

    def mutation(self):
        worsts = get_worst_solutions(self.population.individuals, .3)
        for x, ind in enumerate(worsts):
            y = copy.deepcopy(ind)
            for iy in range(ind.dim):
                _ = generate_rand_value(self.population.range_lower_limit[iy],
                                        self.population.range_upper_limit[iy],
                                        y.params_type[iy])
                y.coords[iy] = _

            y.evaluate_point()
            if y.z > ind.z:
                _len_pop = len(self.population.individuals) - len(worsts)
                _pos = _len_pop + x
                self.population.individuals[_pos] = y

    def simulate(self):
        all_vals = []
        avg_vals = []
        pnt = get_best_solutions(self.population.individuals)
        all_vals.append(pnt.z)
        avg_vals.append(self.population.get_average_objective())
        print("Initial best value: " + str(pnt.z))

        while self.iteration < self.num_iterations and get_best_solutions(
                self.population.individuals).z < self.metric_value:

            if self.print_status and self.iteration % 50 == 0:
                pnt = get_best_solutions(self.population.individuals)
                print(pnt.z, self.population.get_average_objective())

            self.iterate()
            all_vals.append(get_best_solutions(self.population.individuals).z)
            avg_vals.append(self.population.get_average_objective())
            if self.visualize and self.iteration % 2 == 0:
                self.population.get_visualization()

        pnt = get_best_solutions(self.population.individuals)
        print("Final best value: {}".format(str(pnt.z)))
        print("Final best params: {}".format(pnt.params_model))
        return pnt.z, pnt.params_model, pnt.model_ml
