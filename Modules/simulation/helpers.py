import sys
import csv
import configparser
import ast
import numpy as np
import json

def update_progress(progress, transaction):

    bar_length = 50
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
    if progress < 0:
        progress = 0
    if progress >= 1:
        progress = 1
        status = "| Simulation completed...\r\n"
    block = int(round(bar_length*progress))
    text = "\rPercent:  [{0}] {1}% | Number:  {2} {3}".\
        format( "#"*block + "-"*(bar_length-block), np.round((progress*100),1), transaction, status)
    sys.stdout.write(text)
    sys.stdout.flush()


def create_distance_matrix(no_of_agents, distance):

    m = [[distance] * no_of_agents for i in range(no_of_agents)]
    for i in range(no_of_agents):
        m[i][i] = 0
    return m


def common_elements(a, b):

    a_set = set(a)
    b_set = set(b)

    if len(a_set.intersection(b_set)) > 0:
        return list((a_set.intersection(b_set)))
    else:
        return []


def load_file(filename):

    try:
        config = configparser.ConfigParser()
        config.read(filename)
        data = []
        simulation_config_parameters = config['PARAMETERS']

        #Check if all simulation parameters provided
        if not all(key in simulation_config_parameters.keys() for key in ['no_of_transactions','lambda','no_of_agents',\
                                                                      'alpha','latency','distance','tip_selection_algo',\
                                                                      'agent_choice','printing']):

            print("Parameter error! Please provide 'no_of_transactions','lambda','no_of_agents','alpha','latency',"
            "'distance','tip_selection_algo','agent_choice','printing'!")
            sys.exit(1)

        #Load simulation parameters
        _no_of_transactions = int(simulation_config_parameters['no_of_transactions'])
        _lambda = float(simulation_config_parameters['lambda'])
        _no_of_agents = int(simulation_config_parameters['no_of_agents'])
        _alpha = float(simulation_config_parameters['alpha'])
        _latency = int(simulation_config_parameters['latency'])

        if (type(ast.literal_eval(simulation_config_parameters['distance'])) is list):
            _distance = ast.literal_eval(simulation_config_parameters['distance'])
        else:
            _distance = create_distance_matrix(_no_of_agents,float(simulation_config_parameters['distance']))

        _tip_selection_algo = simulation_config_parameters['tip_selection_algo']

        if (simulation_config_parameters['agent_choice'] == 'None'):
            _agent_choice = list(np.ones(_no_of_agents) / _no_of_agents)
        else:
            _agent_choice = ast.literal_eval(_agent_choice)

        _printing = config.getboolean('PARAMETERS','printing')

        data.append((_no_of_transactions, _lambda, _no_of_agents, \
        _alpha, _latency, _distance, _tip_selection_algo, _agent_choice, _printing))

        #Load change parameters
        for key in config:
            if(key != 'PARAMETERS' and key != 'DEFAULT'):

                event_change_parameters = config[key]

                if 'step' not in event_change_parameters:
                    print("Please provide a 'step' for the parameter change!")
                    sys.exit(1)
                step = int(event_change_parameters['step'])

                if 'distance' not in event_change_parameters:
                    _distance = False
                elif (type(ast.literal_eval(event_change_parameters['distance'])) is list):
                    _distance = ast.literal_eval(event_change_parameters['distance'])
                else:
                    _distance = create_distance_matrix(_no_of_agents,float(event_change_parameters['distance']))

                if 'agent_choice' not in event_change_parameters:
                    _agent_choice = False
                elif (event_change_parameters['agent_choice'] == 'None'):
                    _agent_choice = list(np.ones(_no_of_agents) / _no_of_agents)
                else:
                    _agent_choice = ast.literal_eval(event_change_parameters['agent_choice'])
                    if (round(sum(_agent_choice), 3) != 1.0):
                        print("Agent choice not summing to 1.0: {}".format(sum(_agent_choice)))
                        sys.exit(1)
                    if (len(_agent_choice) != _no_of_agents):
                        print("Agent choice not matching no_of_agents: {}".format(len(_agent_choice)))
                        sys.exit(1)

                data.append((step, _distance, _agent_choice))

    except Exception as e:
        print(e)

    return data


def csv_export(self):

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file, dialect='excel')
        #Write genesis
        writer.writerow([0,[]])
        for transaction in self.DG.nodes:
            #Write all other transaction
            if(transaction.arrival_time != 0):
                line = []
                line.append(transaction)
                line.append(list(self.DG.successors(transaction)))
                # line.append(transaction.arrival_time)
                # line.append(transaction.agent)
                
                writer.writerow(line)
        return writer

def string_export(self):
    output = [[0, []]]
    for transaction in self.DG.nodes:
        #Write all other transaction
        if(transaction.arrival_time != 0):
            line = []
            line.append(int(str(transaction)))
            for successor in self.DG.successors(transaction):
                line.append(int(str(successor)))
            #line.append(list(self.DG.successors(transaction)))
            # line.append(transaction.arrival_time)
            # line.append(transaction.agent)
            output.append(line)
    return json.dumps(output)


    