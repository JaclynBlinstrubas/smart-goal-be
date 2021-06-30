-- settings.sql
CREATE DATABASE smart_goals;
CREATE USER smart_goalsuser WITH PASSWORD 'smart_goals';
GRANT ALL PRIVILEGES ON DATABASE smart_goals TO smart_goalsuser;