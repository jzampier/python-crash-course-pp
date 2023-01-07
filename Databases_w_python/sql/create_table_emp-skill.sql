CREATE TABLE IF NOT EXISTS employees_skills (
    employee_id decimal(5) REFERENCES employees(id),
    skill_id decimal(5) REFERENCES skills(id),
    date date
);