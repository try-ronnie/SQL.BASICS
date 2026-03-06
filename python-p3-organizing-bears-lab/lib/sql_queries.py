select_all_female_bears_return_name_and_age = """
    SELECT
        bears.name , 
        bears.age
    From bears 
    WHERE sex = 'F'; 
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT
        bears.name
    FROM bears
    Order by name;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT 
        bears.name,
        bears.age
    FROM bears
    WHERE alive = 1 
    ORDER BY age;
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE age = (SELECT MAX(age) FROM bears)
    LIMIT 1;
"""
select_youngest_bear_and_returns_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears 
    WHERE age = (SELECT MIN(age) FROM bears);

"""