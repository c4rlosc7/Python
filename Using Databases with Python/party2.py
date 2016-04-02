create table with that fields

CREATE TABLE Users (
	name VARCHAR (128),
	email VARCHAR (128)
)

CREATE TABLE Premier_League (
	Team VARCHAR (128),
	City VARCHAR (128),
	Coach VARCHAR (128),
	Stadium VARCHAR (128)
)

SQL insert: the insert statement insers a row into a table 
INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Arsenal', 'Londres','Arsène Wenger','Emirates Stadium')
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Aston Villa', 'Birmingham','Tim Sherwood','Villa Park')
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Bournemouth', 'Bournemouth','Eddie Howe','Dean Court')
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Chelsea', 'Londres','José Mourinho','Stamford Bridge')
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Crystal Palace', 'Londres','Alan Pardew','Selhurt Park')
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Everton', 'Liverpool','Roberto Martinez','Goodison Park')
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Leicester City', 'Leicester','Claudio Ranieri','King Power Stadium')
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Liverpool', 'Liverpool','Jurgen Klopp','Anfield Road')
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Manchester City', 'Manchester','Manuel Pellegrini','Etihad Stadium')
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Newcastle', 'Newcastle Upon Tyne','Steve McClaren','St James Park')
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Norwich City', 'Norwich','Alex Neil','Carrow Road')
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Southampton', 'Southampton','Ronald Koeman','St Marys Stadium' )
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Stoke City', 'Stoke-on Trent','Mark Hughes','Britannia Stadium' )
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Sunderland', 'Sunderland','Sam Allardyce','Stadium Of Light' )
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Swansea City', 'Swansea','Garry Monk','Liverty Stadium' )
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Tottenham Hotspur', 'Londres','Mauricio Pochettino','White Hart Lane' )
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('Watford', 'Watford','Quique Sanchez Flores','Vicarage Road' )
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('West Bromwich Albion', 'West Bromwich','Tony Pulis','The Hawthrns' )
INSERT INTO Premier_League (Team, City, Coach, Stadium) VALUES ('West Ham United', 'Londres','Slaven Bilic','Boleyn Ground' )


SQL Delete: Deletes a row in a table based on a selection criteria
DELETE FROM Users WHERE email='ted@umich.edu'

SQL Update: Allows the updating of a field with a where clause
UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'

Retrieving Records Select: The select statement retrieving a group of
records - you can either retrieve all the records or a subset of the 
with a WHERE clause.
SELECT * FROM Users
SELECT * FROM Users WHERE email='csev@umich.edu'

Sorting with ORDER BY 
- you can add an ORDER BY clause to SELECT statement to get the results 
sorted in ascending or descending order 
SELECT * FROM Users ORDER BY email 
SELECT * FROM Users ORDER BY name