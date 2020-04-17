#!/usr/bin/env python
from typing import Type


def main():
    doctor1 = Doctor('Michael', 'Smith', Neurology)
    doctor2 = Doctor('Tonya', 'Harding', Cardiology)
    doctor3 = Doctor('Jonathan', 'Michel', Oncology)

    patient1 = Patient('Adam', 'Brown', 1, Neurology)
    patient2 = Patient('Clint', 'Strong', 2, Cardiology)
    patient3 = Patient('Bill', 'Newman', 1, Oncology)
    patient4 = Patient('Danna', 'Osbourne', 2, Oncology)
    patient5 = Patient('Emily', 'Welsh', 3, Oncology)

    clinic = Clinic()

    clinic.add_doctor(doctor1)
    clinic.add_doctor(doctor2)
    clinic.add_doctor(doctor3)

    clinic.add_patient(patient1)
    clinic.add_patient(patient2)
    clinic.add_patient(patient3)
    clinic.add_patient(patient4)
    clinic.add_patient(patient5)

    clinic.approve_patient()
    clinic.approve_patient()
    clinic.approve_patient()
    clinic.approve_patient()
    clinic.approve_patient()
    clinic.approve_patient()
    pass


class Specialization:
    pass


class Neurology(Specialization):
    pass


class Cardiology(Specialization):
    pass


class Oncology(Specialization):
    pass


class Patient:
    def __init__(self, name, sure_name, priority: int, sickness_type: Type[Specialization]):
        self.name = name
        self.sure_name = sure_name
        # The lower number the higher priority
        self.priority = priority
        self.sickness_type = sickness_type


class Doctor:
    def __init__(self, name, sure_name, specialization: Type[Specialization]):
        self.name = name
        self.sure_name = sure_name
        self.specialization = specialization


class Clinic:
    def __init__(self):
        self.patient_list = {}
        self.doctor_list = {}

    def add_patient(self, patient: Patient):
        self.patient_list[patient] = patient.priority
        self.patient_list = {k: v for k, v in sorted(self.patient_list.items(), key=lambda item: item[1])}
        pass

    def add_doctor(self, doctor: Doctor):
        self.doctor_list[doctor.specialization] = doctor
        pass

    def approve_patient(self):
        try:
            patient = next(iter(self.patient_list))
            del self.patient_list[patient]

            print('Patient: {} {}, Doctor: {} {}, Sickness type: {}'.
                  format(patient.name, patient.sure_name, self.doctor_list[patient.sickness_type].
                         name, self.doctor_list[patient.sickness_type].sure_name, patient.sickness_type.__name__))
        except StopIteration:
            print("No more patients")
            pass
        pass


if __name__ == '__main__':
    main()