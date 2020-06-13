"""
For this challenge you need to create a simple HAVING statement, you want to count 
how many people have the same age and return the groups with 10 or more people who have that age.

people table schema

    id
    name
    age

return table schema

    age
    total_people


"""

SELECT people.age, COUNT (*) AS total_people 
FROM people 
GROUP BY people.age 
HAVING COUNT(*) >=10