"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 50%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""
import json

infile = open('school_data.json', 'r')

schools = json.load(infile)

conference_codes = [372,108,107,130]
conference_schools = []
high_women_graduation = []
high_cost_school = []

for school in schools:
    if school["NCAA"]["NAIA conference number football (IC2020)"] in conference_codes:
        conference_schools.append(school)
    if school["Graduation rate  women (DRVGR2020)"] and school["Graduation rate  women (DRVGR2020)"] > 75:
        high_women_graduation.append(school)
    if school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] and school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 50000:
        high_cost_school.append(school)


print("Schools in ACC, Big 12, Big Ten, Pac-12, and SEC:\n")
for school in conference_schools:
    print(f"University: {school["instnm"]}")
    print(f"Conference: {school['NCAA']['NAIA conference number football (IC2020)']}")
    print()


print("Universities with graduation rate for Women over 75%:\n")
for school in high_women_graduation:
    print(school["instnm"])
    print(f"Graduation Rate for Women: {school['Graduation rate  women (DRVGR2020)']}%")
    print()


print("Universities with total price for in-state students living off campus over $50,000:\n")
for school in high_cost_school:
    print(school["instnm"])
    print(f"Total Price: {school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)']:,}")
    print()
