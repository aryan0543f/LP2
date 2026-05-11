
def triage_system():
    print("=== Hospital Expert System: Patient Triage Assistant ===")

    # --- USER INTERFACE: Collect patient data ---
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    print("\nSelect Symptoms (Y/N):")

    # Collect symptoms as boolean values (True = Yes, False = No)
    chest_pain   = input("Chest Pain? ").lower() == 'y'
    short_breath = input("Shortness of Breath? ").lower() == 'y'
    bleeding     = input("Heavy Bleeding? ").lower() == 'y'
    high_fever   = input("High Fever? ").lower() == 'y'
    injury       = input("Recent Injury? ").lower() == 'y'
    dizziness    = input("Dizziness or Fainting? ").lower() == 'y'
    stomach_pain = input("Severe Stomach Pain? ").lower() == 'y'

    print("\nAnalyzing symptoms...")

    # --- INFERENCE ENGINE: Apply IF-THEN rules in priority order ---

    # Rule 1 (HIGHEST PRIORITY): Life-threatening — immediate ER
    if bleeding or injury:
        department = "Emergency Room (ER)"
        advice = "Immediate attention required. Proceed to the ER."

    # Rule 2: Cardiac symptoms — urgent cardiology care
    elif chest_pain or short_breath:
        department = "Cardiology"
        advice = "Cardiac symptoms detected. Visit Cardiology immediately."

    # Rule 3: High fever in child — pediatric care needed
    elif high_fever and age < 12:
        department = "Pediatrics"
        advice = "High fever in child. Visit Pediatrics urgently."

    # Rule 4: High fever in adult — general physician
    elif high_fever:
        department = "General Medicine"
        advice = "Consult a general physician for evaluation."

    # Rule 5: Neurological symptoms
    elif dizziness:
        department = "Neurology"
        advice = "Neurological symptoms present. Visit Neurology."

    # Rule 6: Digestive symptoms
    elif stomach_pain:
        department = "Gastroenterology"
        advice = "Visit a gastroenterologist for further diagnosis."

    # Rule 7 (LOWEST PRIORITY): No critical symptoms
    else:
        department = "Outpatient (OPD)"
        advice = "No critical symptoms. You may proceed to OPD."

    # --- OUTPUT: Patient Report ---
    print(f"\n=== Patient Report ===")
    print(f"Name: {name}")
    print(f"Recommended Department: {department}")
    print(f"Advice: {advice}")


if __name__ == "__main__":
    triage_system()


# SAMPLE INPUT/OUTPUT:
# --------------------
# Enter Patient Name: Aryan
# Enter Age: 20
# Chest Pain? y
# Shortness of Breath? n
# Heavy Bleeding? n
# High Fever? n
# Recent Injury? n
# Dizziness or Fainting? n
# Severe Stomach Pain? n
#
# Analyzing symptoms...
#
# === Patient Report ===
# Name: Aryan
# Recommended Department: Cardiology
# Advice: Cardiac symptoms detected. Visit Cardiology immediately.
#
# --------------------
# Enter Patient Name: Riya
# Enter Age: 8
# Chest Pain? n
# Shortness of Breath? n
# Heavy Bleeding? n
# High Fever? y
# Recent Injury? n
# Dizziness or Fainting? n
# Severe Stomach Pain? n
#
# Analyzing symptoms...
#
# === Patient Report ===
# Name: Riya
# Recommended Department: Pediatrics
# Advice: High fever in child. Visit Pediatrics urgently.
# =============================================================================
# PROGRAM: Hospital Expert System — Patient Triage Assistant
# =============================================================================
#
# THEORY:
# -------
# Expert System (ES):
#   - A computer program that mimics the decision-making ability of a
#     human expert in a specific domain.
#   - Uses a set of IF-THEN rules (Knowledge Base) to draw conclusions.
#   - One of the earliest and most successful applications of AI.
#
# Components of an Expert System:
#   1. Knowledge Base  : Stores domain-specific facts and rules (IF-THEN rules).
#   2. Inference Engine: Applies rules to facts to derive conclusions.
#                        (The if-elif chain in this program IS the inference engine)
#   3. User Interface  : Interacts with the user (input/output here).
#   4. Explanation     : Justifies the conclusion (advice printed at end).
#   5. Knowledge Acquisition: Process of adding new rules (done by developer).
#
# Triage System:
#   - Medical process of sorting patients based on urgency of their condition.
#   - Ensures critical patients are treated first.
#   - This ES automates triage by mapping symptoms → department.
#
# HOW THIS EXPERT SYSTEM WORKS:
#   1. Collect patient info (name, age, symptoms).
#   2. Apply IF-THEN rules (inference engine) to symptoms.
#   3. Rules have PRIORITY ORDER — most critical conditions checked first.
#   4. Output: recommended department + advice.
#
# RULE PRIORITY (most critical → least critical):
#   Rule 1: Bleeding OR Injury          → Emergency Room (ER)      [HIGHEST]
#   Rule 2: Chest Pain OR Short Breath  → Cardiology
#   Rule 3: High Fever AND Age < 12     → Pediatrics
#   Rule 4: High Fever                  → General Medicine
#   Rule 5: Dizziness                   → Neurology
#   Rule 6: Stomach Pain                → Gastroenterology
#   Rule 7: No symptoms                 → OPD                      [LOWEST]
#
# =============================================================================
# COMPLEXITY:
#   Time Complexity  : O(1) — fixed number of rules, constant time evaluation
#   Space Complexity : O(1) — fixed variables, no dynamic data structures
# =============================================================================
#
# ORAL EXAM QUESTIONS & ANSWERS:
# =============================================================================
#
# Q1. What is an Expert System?
# A1. An Expert System is an AI program that simulates the decision-making
#     of a human expert in a specific domain using a Knowledge Base of
#     IF-THEN rules and an Inference Engine to apply those rules.
#
# Q2. What are the main components of an Expert System?
# A2. 1. Knowledge Base   : Stores domain facts and IF-THEN rules.
#     2. Inference Engine : Applies rules to input facts to reach conclusions.
#     3. User Interface   : Collects input and displays output.
#     4. Explanation Facility: Explains why a conclusion was reached.
#     5. Knowledge Acquisition: Mechanism to add/update rules.
#
# Q3. What is the Knowledge Base in this program?
# A3. The IF-THEN rules that map symptoms to departments:
#     IF bleeding OR injury → Emergency Room
#     IF chest_pain OR short_breath → Cardiology
#     IF high_fever AND age < 12 → Pediatrics ... etc.
#     These rules encode the medical expert's knowledge.
#
# Q4. What is the Inference Engine in this program?
# A4. The if-elif-else chain in the triage_system() function.
#     It evaluates the patient's symptoms against the rules in the
#     Knowledge Base and determines the appropriate department.
#
# Q5. What type of reasoning does this Expert System use?
# A5. FORWARD CHAINING (Data-Driven reasoning).
#     It starts with known FACTS (symptoms entered by user) and
#     applies rules to reach a CONCLUSION (department recommendation).
#     Forward chaining: Facts → Rules → Conclusion.
#
# Q6. What is the difference between Forward and Backward Chaining?
# A6. Forward Chaining  : Starts with facts, applies rules to reach conclusion.
#                         Data-driven. Used here.
#                         Example: Symptoms → Department
#     Backward Chaining : Starts with a goal/conclusion, works backward
#                         to find supporting facts.
#                         Goal-driven.
#                         Example: "Is this Cardiology?" → check chest_pain, short_breath
#
# Q7. Why is the order of if-elif rules important?
# A7. Because rules are checked in PRIORITY ORDER — most critical first.
#     Bleeding/Injury is checked before Chest Pain, which is before Fever, etc.
#     If order were reversed, a patient with bleeding might be sent to OPD
#     instead of the Emergency Room — a potentially fatal mistake.
#
# Q8. Why is age used as a condition in one of the rules?
# A8. High fever in a child (age < 12) is more dangerous and requires
#     specialized pediatric care. The same symptom (high fever) leads to
#     different departments based on the patient's age.
#     This shows how Expert Systems can handle COMPOUND conditions.
#
# Q9. What are the symptoms collected in this system?
# A9. 1. Chest Pain
#     2. Shortness of Breath
#     3. Heavy Bleeding
#     4. High Fever
#     5. Recent Injury
#     6. Dizziness or Fainting
#     7. Severe Stomach Pain
#     Total: 7 symptoms + age as a factor.
#
# Q10. What departments can this system recommend?
# A10. 1. Emergency Room (ER)   — bleeding or injury
#      2. Cardiology             — chest pain or shortness of breath
#      3. Pediatrics             — high fever in child (age < 12)
#      4. General Medicine       — high fever in adult
#      5. Neurology              — dizziness or fainting
#      6. Gastroenterology       — severe stomach pain
#      7. Outpatient (OPD)       — no critical symptoms
#
# Q11. What are the advantages of an Expert System?
# A11. - Available 24/7, no fatigue.
#      - Consistent decisions — no human error or bias.
#      - Can handle complex rule sets quickly.
#      - Useful where human experts are scarce.
#      - Explainable — can justify its decisions.
#
# Q12. What are the limitations/disadvantages of this Expert System?
# A12. - Cannot handle cases outside predefined rules.
#      - Cannot learn from new cases (no ML).
#      - Knowledge Base must be manually updated by experts.
#      - Cannot handle uncertainty or ambiguous symptoms.
#      - Only one department recommended even if multiple apply.
#
# Q13. What is the difference between an Expert System and Machine Learning?
# A13. Expert System : Rules are manually coded by domain experts.
#                      Deterministic, explainable, no training data needed.
#      Machine Learning: Rules are LEARNED from training data automatically.
#                        Can improve with more data, handles uncertainty better.
#
# Q14. What is Triage in medical context?
# A14. Triage is the process of sorting patients based on the urgency of
#      their medical condition to prioritize treatment.
#      Critical patients (bleeding, cardiac) are treated before minor cases.
#
# Q15. What is the time complexity of this program?
# A15. O(1) — constant time. The number of rules is fixed (7 rules).
#      Regardless of input, the same number of comparisons are made.
#
# Q16. What are real-world applications of Expert Systems?
# A16. - Medical diagnosis (MYCIN — bacterial infection diagnosis)
#      - Financial/loan approval systems
#      - Fault diagnosis in engineering
#      - Legal advisory systems
#      - Tax calculation systems
#      - Customer support automation
#
# Q17. What is MYCIN? Why is it famous?
# A17. MYCIN is one of the earliest and most famous Expert Systems,
#      developed at Stanford in the 1970s.
#      It diagnosed bacterial blood infections and recommended antibiotics.
#      It performed as well as human specialists in tests.
#
# Q18. How can this Expert System be improved?
# A18. - Add more symptoms and rules for better accuracy.
#      - Handle multiple department recommendations.
#      - Add certainty factors (probability) for uncertain symptoms.
#      - Integrate with a real hospital database.
#      - Use ML to learn from past patient data.
#      - Add an explanation facility to show WHY a department was chosen.
#
# =============================================================================
# QUICK FIRE ANSWERS:
#   Type of AI system?       → Expert System (Rule-Based)
#   Knowledge Base?          → IF-THEN rules (symptom → department)
#   Inference Engine?        → if-elif chain in triage_system()
#   Reasoning type?          → Forward Chaining (Data-Driven)
#   Symptoms collected?      → 7 symptoms + age
#   Departments possible?    → 7 (ER, Cardiology, Pediatrics, General, Neurology, Gastro, OPD)
#   Highest priority rule?   → Bleeding OR Injury → Emergency Room
#   Age used for?            → Differentiating Pediatrics vs General Medicine
#   Time complexity?         → O(1)
#   Can it learn?            → No, rules are hardcoded
#   Famous ES example?       → MYCIN (Stanford, 1970s)
# =============================================================================