% Define symptoms
symptom(fever).
symptom(cough).
symptom(sore_throat).

% Define illnesses and their symptoms
illness(cold, [fever, cough, sore_throat]).
illness(unknown, []).

% Rule for diagnosis
diagnose(Illness) :-
    findall(Symptom, symptom(Symptom), AllSymptoms),
    collect_symptoms(AllSymptoms, Symptoms),
    illness(Illness, IllnessSymptoms),
    subset(IllnessSymptoms, Symptoms).

% Collect symptoms from user input
collect_symptoms([], []).
collect_symptoms([Symptom|Rest], [Symptom|Selected]) :-
    writef("Do you have %w? (yes/no) ", [Symptom]),
    read(Response),
    Response = yes,
    collect_symptoms(Rest, Selected).
collect_symptoms([Symptom|Rest], Selected) :-
    writef("Do you have %w? (yes/no) ", [Symptom]),
    read(Response),
    Response = no,
    collect_symptoms(Rest, Selected).

% Check if one list is a subset of another
subset([], _).
subset([X|Xs], Set) :-
    member(X, Set),
    subset(Xs, Set).

% Entry point for diagnosis
start_diagnosis :-
    writeln("Welcome to the Medical Diagnosis System."),
    writeln("Please answer the following questions with 'yes' or 'no'."),
    diagnose(Illness),
    format("Based on your symptoms, you might have %w.~n", [Illness]).

% Start the diagnosis when the program is run
:- initialization(start_diagnosis).
