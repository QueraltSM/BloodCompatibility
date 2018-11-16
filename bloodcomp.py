from itertools import combinations

b_comp = {"A" : ["A", "C"],
          "Z" : ["A", "Z", "C", "X" ],
          "B" : ["B", "C"],
          "Y" : ["B", "Y", "C", "X"],
          "C" : ["C"],
          "X" : ["C", "X"],
          "O" : ["A", "B", "C", "O"],
          "W" : ["A", "Z", "B", "Y", "C", "X", "O", "W"]}
last_patient = ""


def check_compatibility(patient1_blood, patient2_blood):
    for blood in b_comp[patient1_blood]:
        if blood == patient2_blood:
            return True
    return False


def get_compatibility(combination):
    patient1 = combination[0]
    patient2 = combination[1]

    p1_blood = patient1[len(patient1)-1]
    p2_blood = patient2[len(patient2)-1]

    global last_patient
    if check_compatibility(p1_blood, p2_blood):
        if last_patient != patient1:
            last_patient = patient1
            print("\nPatient", patient1, "can donate to: ")
        print(" ", patient2)


def get_combinations(persons):
    for comb in combinations(persons, 2):
        get_compatibility(comb)
