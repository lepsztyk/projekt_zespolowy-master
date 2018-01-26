-- DROP DATABASE systemsm;

CREATE DATABASE systemsm;

ALTER DATABASE systemsm OWNER TO systemuser;

CREATE TABLE adres (
    id INTEGER NOT NULL,
    kod_pocztowy TEXT NOT NULL,
    miasto TEXT NOT NULL,
    ulica TEXT NOT NULL,
    telefon TEXT NOT NULL,
    email TEXT NOT NULL
);

ALTER TABLE adres OWNER TO systemuser;

CREATE TABLE budynek (
    id INTEGER NOT NULL, 
    adres INTEGER NOT NULL, 
    administrator INTEGER NOT NULL
);

ALTER TABLE budynek OWNER TO systemuser;

CREATE TABLE faktura (
    id INTEGER NOT NULL,
    wartosc_netto DOUBLE PRECISION NOT NULL,
    wystawca INTEGER NOT NULL, 
    adres INTEGER NOT NULL,
    wlasciciel INTEGER NOT NULL
);

ALTER TABLE faktura OWNER TO systemuser;

CREATE TABLE licznik (
    id INTEGER NOT NULL,
    typ TEXT NOT NULL,
    cena_netto DOUBLE PRECISION NOT NULL
);

ALTER TABLE licznik OWNER TO systemuser;

CREATE TABLE mieszkanie (
    id INTEGER NOT NULL,
    budynek INTEGER NOT NULL,
    metraz DOUBLE PRECISION NOT NULL,
    liczba_pokoi INTEGER NOT NULL,
    piwnica BOOLEAN NOT NULL,
    wlasciciel INTEGER
);

ALTER TABLE mieszkanie OWNER TO systemuser;

CREATE TABLE nadgodziny (
    id INTEGER NOT NULL,
    pracownik INTEGER NOT NULL,
    ilosc DOUBLE PRECISION NOT NULL
);

ALTER TABLE nadgodziny OWNER TO systemuser;

CREATE TABLE pracownik (
    id INTEGER NOT NULL,
    stanowisko INTEGER NOT NULL,
    budynek INTEGER NOT NULL,
    imie TEXT NOT NULL,
    nazwisko TEXT NOT NULL, 
    adres INTEGER NOT NULL
);

ALTER TABLE pracownik OWNER TO systemuser;

CREATE TABLE stan_licznik (
    id INTEGER NOT NULL,
    typ INTEGER NOT NULL,
    mieszkanie INTEGER NOT NULL,
    stan DOUBLE PRECISION NOT NULL
);

ALTER TABLE stan_licznik OWNER TO systemuser;

CREATE TABLE stanowisko (
    id INTEGER NOT NULL,
    nazwa TEXT NOT NULL,
    pensja INTEGER NOT NULL
);

ALTER TABLE stanowisko OWNER TO systemuser;

CREATE TABLE ticket (
    id INTEGER NOT NULL,
    kto INTEGER NOT NULL,
    mieszkaniec INTEGER NOT NULL,
    opis TEXT NOT NULL
);

ALTER TABLE ticket OWNER TO systemuser;

CREATE TABLE wlasciciel (
    id INTEGER NOT NULL,
    imie TEXT,
    nazwisko TEXT NOT NULL, 
    adres INTEGER NOT NULL
date);


ALTER TABLE wlasciciel OWNER TO systemuser;

CREATE TABLE wydarzenie (
    id INTEGER NOT NULL,
    nazwa TEXT NOT NULL,
    opis TEXT NOT NULL,
    data DATE NOT NULL,
    budynek INTEGER
);


ALTER TABLE wydarzenie OWNER TO systemuser;

CREATE TABLE wystawca (
    id INTEGER NOT NULL,
    nazwa TEXT NOT NULL,
    adres INTEGER NOT NULL
);


ALTER TABLE wystawca OWNER TO systemuser;

ALTER TABLE ONLY adres ADD CONSTRAINT idx_17687_primary PRIMARY KEY (id);

ALTER TABLE ONLY budynek ADD CONSTRAINT idx_17690_primary PRIMARY KEY (id);

ALTER TABLE ONLY faktura ADD CONSTRAINT idx_17693_primary PRIMARY KEY (id);

ALTER TABLE ONLY licznik ADD CONSTRAINT idx_17696_primary PRIMARY KEY (id);

ALTER TABLE ONLY mieszkanie ADD CONSTRAINT idx_17699_primary PRIMARY KEY (id);

ALTER TABLE ONLY nadgodziny ADD CONSTRAINT idx_17702_primary PRIMARY KEY (id);

ALTER TABLE ONLY pracownik ADD CONSTRAINT idx_17705_primary PRIMARY KEY (id);

ALTER TABLE ONLY stanowisko ADD CONSTRAINT idx_17708_primary PRIMARY KEY (id);

ALTER TABLE ONLY stan_licznik ADD CONSTRAINT idx_17711_primary PRIMARY KEY (id);

ALTER TABLE ONLY ticket ADD CONSTRAINT idx_17714_primary PRIMARY KEY (id);

ALTER TABLE ONLY wlasciciel ADD CONSTRAINT idx_17720_primary PRIMARY KEY (id);

ALTER TABLE ONLY wydarzenie ADD CONSTRAINT idx_17723_primary PRIMARY KEY (id);

ALTER TABLE ONLY wystawca ADD CONSTRAINT idx_17726_primary PRIMARY KEY (id);

CREATE INDEX idx_17690_budynek_adres_idx ON budynek USING btree (adres);

CREATE INDEX idx_17690_budynek_pracownik_idx ON budynek USING btree (administrator);

CREATE INDEX idx_17693_wlasciciel_faktura_idx ON faktura USING btree (wlasciciel);

CREATE INDEX idx_17693_wystawca_idx ON faktura USING btree (wystawca);

CREATE INDEX idx_17699_wlasciciel_mieszkanie_idx ON mieszkanie USING btree (wlasciciel);

CREATE INDEX idx_17702_nadgodziny_pracownik_idx ON nadgodziny USING btree (pracownik);

CREATE INDEX idx_17705_pracownik_adres_idx ON pracownik USING btree (adres);

CREATE INDEX idx_17705_pracownik_stanowisko_idx ON pracownik USING btree (stanowisko);

CREATE INDEX idx_17711_licznik_stan_licznik_idx ON stan_licznik USING btree (typ);

CREATE INDEX idx_17711_mieszkanie_stan_licznik_idx ON stan_licznik USING btree (mieszkanie);

CREATE INDEX idx_17714_pracownik_ticket_idx ON ticket USING btree (kto);

CREATE INDEX idx_17720_adres_wlasciciel_idx ON wlasciciel USING btree (adres);

CREATE INDEX idx_17723_budynek_wydarzenie_idx ON wydarzenie USING btree (budynek);

CREATE INDEX idx_17726_adres_wystawca_idx ON wystawca USING btree (adres);

ALTER TABLE ONLY budynek ADD CONSTRAINT adres_budynek FOREIGN KEY (adres) REFERENCES adres(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY wlasciciel ADD CONSTRAINT adres_wlasciciel FOREIGN KEY (adres) REFERENCES adres(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY wystawca ADD CONSTRAINT adres_wystawca FOREIGN KEY (adres) REFERENCES adres(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY wydarzenie ADD CONSTRAINT budynek_wydarzenie FOREIGN KEY (budynek) REFERENCES budynek(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY ticket ADD CONSTRAINT kto_ticket FOREIGN KEY (kto) REFERENCES wlasciciel(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY stan_licznik ADD CONSTRAINT licznik_stan_licznik FOREIGN KEY (typ) REFERENCES stan_licznik(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY stan_licznik ADD CONSTRAINT mieszkanie_stan_licznik FOREIGN KEY (mieszkanie) REFERENCES mieszkanie(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY pracownik ADD CONSTRAINT pracownik_adres FOREIGN KEY (adres) REFERENCES adres(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY budynek ADD CONSTRAINT pracownik_budynek FOREIGN KEY (administrator) REFERENCES pracownik(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY nadgodziny ADD CONSTRAINT pracownik_nadgodziny FOREIGN KEY (pracownik) REFERENCES pracownik(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY pracownik ADD CONSTRAINT pracownik_stanowisko FOREIGN KEY (stanowisko) REFERENCES stanowisko(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY ticket ADD CONSTRAINT pracownik_ticket FOREIGN KEY (kto) REFERENCES pracownik(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY faktura ADD CONSTRAINT wlasciciel_faktura FOREIGN KEY (wlasciciel) REFERENCES wlasciciel(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY mieszkanie ADD CONSTRAINT wlasciciel_mieszkanie FOREIGN KEY (wlasciciel) REFERENCES wlasciciel(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY faktura ADD CONSTRAINT wystawca_faktura FOREIGN KEY (wystawca) REFERENCES wystawca(id) ON UPDATE CASCADE ON DELETE CASCADE;
