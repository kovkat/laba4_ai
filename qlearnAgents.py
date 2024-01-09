from pacman import Directions
from game import Agent
import random
import math
import game
import util


class QLearnAgent(Agent):
    def __init__(self, alpha=0.1, epsilon=0.2, gamma=0.8, numTraining = 10):
        # alpha       - learning rate
        # epsilon     - exploration rate
        # gamma       - discount factor
        # numTraining - number of training episodes
        self.alpha = float(alpha)
        self.epsilon = float(epsilon)
        self.gamma = float(gamma)
        self.numTraining = int(numTraining)
        self.episodesSoFar = 0
        self.q_value = util.Counter()
        self.score = 0
        self.lastState = []
        self.lastAction = []

    def incrementEpisodesSoFar(self):
        self.episodesSoFar +=1

    def getEpisodesSoFar(self):
        return self.episodesSoFar

    def getNumTraining(self):
            return self.numTraining

    def setEpsilon(self, value):
        self.epsilon = value

    def getAlpha(self):
        return self.alpha

    def setAlpha(self, value):
        self.alpha = value

    def getGamma(self):
        return self.gamma

    def getMaxAttempts(self):
        return self.maxAttempts

    def getQValue(self, state, action):
        return self.q_value[(state,action)]

    def getMaxQ(self, state):
        q_list = []
        for a in state.getLegalPacmanActions():
            q = self.getQValue(state,a)
            q_list.append(q)
        if len(q_list) ==0:
            return 0
        return max(q_list)

    def updateQ(self, state, action, reward, qmax):
        q = self.getQValue(state,action)
        self.q_value[(state,action)] = q + self.alpha*(reward + self.gamma*qmax - q)

    def doTheRightThing(self, state):
        legal = state.getLegalPacmanActions()
        if self.getEpisodesSoFar()*1.0/self.getNumTraining()<0.5:
            if Directions.STOP in legal:
                legal.remove(Directions.STOP)
            if len(self.lastAction) > 0:
                last_action = self.lastAction[-1]
                distance0 = state.getPacmanPosition()[0]- state.getGhostPosition(1)[0]
                distance1 = state.getPacmanPosition()[1]- state.getGhostPosition(1)[1]
                if math.sqrt(distance0**2 + distance1**2) > 2:
                    if (Directions.REVERSE[last_action] in legal) and len(legal)>1:
                        legal.remove(Directions.REVERSE[last_action])
        tmp = util.Counter()
        for action in legal:
          tmp[action] = self.getQValue(state, action)
        return tmp.argMax()

    def getAction(self, state):
        legal = state.getLegalPacmanActions()
        if Directions.STOP in legal:
            legal.remove(Directions.STOP)

        reward = state.getScore()-self.score
        if len(self.lastState) > 0:
            last_state = self.lastState[-1]
            last_action = self.lastAction[-1]
            max_q = self.getMaxQ(state)
            self.updateQ(last_state, last_action, reward, max_q)

        if util.flipCoin(self.epsilon):
            action = random.choice(legal)
        else:
            action = self.doTheRightThing(state)

        self.score = state.getScore()
        self.lastState.append(state)
        self.lastAction.append(action)

        return action

    def final(self, state):
        reward = state.getScore()-self.score
        last_state = self.lastState[-1]
        last_action = self.lastAction[-1]
        self.updateQ(last_state, last_action, reward, 0)

        self.score = 0
        self.lastState = []
        self.lastAction = []

        ep = 1 - self.getEpisodesSoFar()*1.0/self.getNumTraining()
        self.setEpsilon(ep*0.1)

        self.incrementEpisodesSoFar()
        if self.getEpisodesSoFar() % 100 == 0:
            print("Completed %s runs of training" % self.getEpisodesSoFar())

        if self.getEpisodesSoFar() == self.getNumTraining():
            msg = 'Training Done (turning off epsilon and alpha)'
            print('%s\n%s' % (msg,'-' * len(msg)))
            self.setAlpha(0)
            self.setEpsilon(0)
