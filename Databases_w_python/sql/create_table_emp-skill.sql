CREATE TABLE IF NOT EXISTS employees_skills (
    employee_id decimal(5),
    skill_id decimal(5) REFERENCES skills(id),
    date date,
    FOREIGN KEY (employee_id) REFERENCES employees(id),
    FOREIGN KEY (skill_id) REFERENCES skills(id)
);