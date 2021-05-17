from copy import deepcopy
from typing import List
import sys

class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __str__(self):
        return "<Agent: {}>".format(self._name)

    def __init__(self, name: str, skills: list, load: int):
        self.name = name
        self.skills = skills
        self.load = load


class Ticket(object):
    def __init__(self, id: str, restrictions: list):
        self.id = id
        self.restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        filtered_agent = []
        for agent in agents:
            if agent.load<=2:
                filtered_agent.append(agent)

        return filtered_agent

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        pass


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        agents = self._filter_loaded_agents(agents)

        if len(agents) == 0:
            raise NoAgentFoundException
        a = deepcopy(agents)
        a.sort(key=lambda x: x.load, reverse=False)
        return a[0]


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        agents = self._filter_loaded_agents(agents)
        best_agent = None
        best_agent_num_skills = sys.maxsize
        best_agent_load = 4

        for agent in agents:
            if self._this_agent_can_handle(ticket,agent):
                if len(agent.skills)<best_agent_num_skills:
                    best_agent = agent
                    best_agent_num_skills=len(agent.skills)
                elif len(agent.skills)==best_agent_num_skills:
                    if agent.load<best_agent_load:
                        best_agent = agent
                        best_agent_num_skills = len(agent.skills)
                        best_agent_load = agent.load
                else:
                    pass

        if best_agent is None:
            raise NoAgentFoundException
        else:
            return best_agent

    def _this_agent_can_handle(self,ticker:Ticket, agent:Agent):
        restrictions = ticker.restrictions
        agent_skills = agent.skills

        for restriction in restrictions:
            if restriction not in agent_skills:
                return False

        return True


ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)
#agent3 = Agent(name="C", skills=["English", "Japanese"], load=0)

least_loaded_policy = LeastLoadedAgent()
least_loaded_policy.find(ticket, [agent1, agent2])

least_flexible_policy = LeastFlexibleAgent()
a = least_flexible_policy.find(ticket,[agent1,agent2])

