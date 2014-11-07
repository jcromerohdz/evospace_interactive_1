__author__ = 'JC Romero'

from FIS import *

preference = LinguisticVariable('Preference', range=(1.0, 5.0))
preference.addMF('Low',MF.Triangular(1.0, 1.0, 3.0))
preference.addMF('Mid',MF.Triangular(2.5, 3.0, 3.5))
preference.addMF('High',MF.Triangular(3.0, 5.0, 5.0))

experience = LinguisticVariable('Experience', range=(1.0, 100.0))
experience.addMF('Low',MF.Triangular(1.0, 1.0, 50.0))
experience.addMF('Mid',MF.Triangular(30.0, 50.0, 70.0))
experience.addMF('High',MF.Triangular(50.0, 100.0, 100.0))

#OUT
fitness = LinguisticVariable('Fitness', type='out', range=(1.0, 100.0))
fitness.addMF('Bad',MF.Triangular(1.0, 1.0, 50.0))
fitness.addMF('Normal',MF.Triangular(30.0, 50.0, 70.0))
fitness.addMF('Good',MF.Triangular(50.0, 100.0, 100.0))


# Rules

#if Logs == Low and Answer == low and Approached == Low then Out == Low
r1 = FuzzyRule()
r1.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['Low']),FuzzyProposition(experience,experience.mfs['Low'])))
r1.consequent.append(FuzzyProposition(fitness,fitness.mfs['Bad']))

#if Logs == Low and Answer == High and Approached == Low then fitness == Low
r2 = FuzzyRule()
r2.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['Low']),FuzzyProposition(experience,experience.mfs['Mid'])))
r2.consequent.append(FuzzyProposition(fitness,fitness.mfs['Bad']))

#if Logs == Low and Answer == High and Approached == Low then fitness == Low
r3 = FuzzyRule()
r3.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['Low']),FuzzyProposition(experience,experience.mfs['High'])))
r3.consequent.append(FuzzyProposition(fitness,fitness.mfs['Normal']))

#if Logs == Low and Answer == High and Approached == Low then fitness == Low
r4 = FuzzyRule()
r4.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['Mid']),FuzzyProposition(experience,experience.mfs['Low'])))
r4.consequent.append(FuzzyProposition(fitness,fitness.mfs['Normal']))

#if Logs == Low and Answer == High and Approached == Low then fitness == Low
r5 = FuzzyRule()
r5.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['Mid']),FuzzyProposition(experience,experience.mfs['Mid'])))
r5.consequent.append(FuzzyProposition(fitness,fitness.mfs['Normal']))

#if Logs == Low and Answer == High and Approached == Low then fitness == Low
r6 = FuzzyRule()
r6.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['Mid']),FuzzyProposition(experience,experience.mfs['High'])))
r6.consequent.append(FuzzyProposition(fitness,fitness.mfs['Good']))

#if Logs == Low and Answer == High and Approached == Low then fitness == Low
r7 = FuzzyRule()
r7.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['High']),FuzzyProposition(experience,experience.mfs['Low'])))
r7.consequent.append(FuzzyProposition(fitness,fitness.mfs['Normal']))

#if Logs == Low and Answer == High and Approached == Low then fitness == Low
r8 = FuzzyRule()
r8.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['High']),FuzzyProposition(experience,experience.mfs['Mid'])))
r8.consequent.append(FuzzyProposition(fitness,fitness.mfs['Good']))

#if Logs == Low and Answer == High and Approached == Low then fitness == Low
r9 = FuzzyRule()
r9.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['High']),FuzzyProposition(experience,experience.mfs['High'])))
r9.consequent.append(FuzzyProposition(fitness,fitness.mfs['Good']))

#if Logs == Low and Answer == High and Approached == Low then fitness == Low
Rules=[r1,r2,r3,r4,r5,r6,r7,r8,r9]
fis = FIS(Rules)


def fisuser(a,b):
    preference.current_value=a
    experience.current_value=b
    return fis.eval( out_var = 0)

if __name__ == '__main__':
    print eval(25,15)