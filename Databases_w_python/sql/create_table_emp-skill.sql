CREATE TABLE IF NOT EXISTS employees_skills (
    register decimal(5),
    skill_id decimal(5) REFERENCES skills(skill_id),
    date date,
    FOREIGN KEY (register) REFERENCES employees(register),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);