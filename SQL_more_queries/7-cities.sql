-- asdadasdadadasd

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
  id int AUTO_INCREMENT PRIMARY KEY,
  state_id int NOT NULL,
  
  FOREIGN KEY (state_id)
  REFERENCES hbtn_0d_usa.states(id),

  name VARCHAR(256)
);
