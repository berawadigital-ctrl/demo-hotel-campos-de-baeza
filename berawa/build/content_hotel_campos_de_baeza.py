# Contenido de la demo Hotel Campos de Baeza (Baeza) (es/en/fr/de). Hechos de hotelcamposdebaeza.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Doble e individual','Doble con supletoria','Junior Suite'],'en':['Double and single','Double with extra bed','Junior Suite'],'fr':['Double et individuelle','Double avec lit d’appoint','Junior Suite'],'de':['Doppel- und Einzelzimmer','Doppelzimmer mit Zustellbett','Junior Suite']}
RD={
'es':['Cama de matrimonio o dos camas separadas (Hollywood twin); la mayoría con amplios ventanales y vistas al mar de olivos.','Para 3 adultos: 1 o 2 camas más una cama extra. La mayoría con balcón.','Tres diseños únicos, con amplio salón, mirador en la terraza privada, jacuzzi y ducha de hidromasaje.'],
'en':['A double bed or two separate beds (Hollywood twin); most with large windows and views over the sea of olive trees.','For 3 adults: 1 or 2 beds plus an extra bed. Most with a balcony.','Three unique designs, with a large lounge, a viewpoint on the private terrace, jacuzzi and hydromassage shower.'],
'fr':['Lit double ou deux lits séparés (Hollywood twin) ; la plupart avec de grandes baies et vue sur la mer d’oliviers.','Pour 3 adultes : 1 ou 2 lits plus un lit d’appoint. La plupart avec balcon.','Trois designs uniques, avec grand salon, belvédère sur la terrasse privée, jacuzzi et douche hydromassante.'],
'de':['Doppelbett oder zwei getrennte Betten (Hollywood twin); meist mit großen Fenstern und Blick auf das Meer aus Olivenbäumen.','Für 3 Erwachsene: 1 oder 2 Betten plus Zustellbett. Meist mit Balkon.','Drei einzigartige Designs, mit großem Wohnbereich, Aussichtspunkt auf der privaten Terrasse, Whirlpool und Massagedusche.']}
ART={
'hero':('hills',1511,['#26301c','#8a9a4a','#e8e6c8','#5e6b3a','#3e4a26','#1c2412']),
'intro':('columns',1512,['#f4f1e6','#faf8f1','#6b5a2a','#5f5a48','#2f2a1c']),
'r1':('hills',1521,['#f1efe2','#dfe3c4','#a7b26e','#7d8556','#5a6140','#3a3f2a']),
'r2':('arches',1522,['#f4f1e6','#e6dcc0','#6b5a2a','#5f5a48','#2f2a1c']),
'r3':('waves',1523,['#1a2a33','#5f8fa3','#dbe9ef','#4d6a77','#344e5a','#111d24']),
'g1':('skyline',1531,['#26301c','#a0a85a','#eeeacb','#6d7542','#4a522c','#1c2412']),
'g2':('hills',1532,['#f1efe2','#dfe3c4','#a7b26e','#7d8556','#5a6140','#3a3f2a']),
'g3':('columns',1533,['#f4f1e6','#faf8f1','#6b5a2a','#5f5a48','#2f2a1c']),
'g4':('waves',1534,['#1a2a33','#5f8fa3','#dbe9ef','#4d6a77','#344e5a','#111d24'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Campos de Baeza · Hotel de 4 estrellas en Baeza',see_rooms='Ver habitaciones',hero_k='Baeza · Avda. Alcalde Eusebio Ortega Molina, 43',hero_t='Un hotel de 4 estrellas en la Baeza Patrimonio de la Humanidad',hero_s='Terraza con piscina y vistas panorámicas a la ciudad y al mar de olivos.',
 intro_t='Tranquilidad y un exquisito interior',intro_p1='Una elegante construcción de 4 plantas con fachada de estilo renacentista, 50 habitaciones y, desde 2008, referente para viajes de negocios y de turismo en Baeza.',
 intro_p2='A menos de 500 metros, la fuente de los Leones, la plaza de la Constitución y el casco antiguo. Aparcamiento gratuito al aire libre en las inmediaciones.',
 stats=['4 estrellas','50 habitaciones','Terraza con piscina','Desde 2008'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Con suelo de madera, TV de pantalla plana, wifi gratuito, minibar, caja fuerte, calefacción central, secador, colchones nuevos y almohadas a la carta.',
 svcs=['Terraza con piscina y vistas panorámicas','Desayuno buffet recién preparado','Restaurante en el interior del hotel','Salón «Andalucía» para eventos y reuniones','Aparcamiento gratuito en las inmediaciones y de pago en el hotel','Cunas bajo petición y disponibilidad'],
 loc_p='Avda. Alcalde Eusebio Ortega Molina, 43 · 23440 Baeza (Jaén). Teléfono: 953 747 311. Correo: reservas@hotelcamposdebaeza.com.',
 chips=['¿Qué habitaciones tenéis?','¿Tenéis parking?','¿Hay piscina?','¿Cómo reservo?']),
'en':dict(title='Hotel Campos de Baeza · 4-star hotel in Baeza',see_rooms='See rooms',hero_k='Baeza · Avda. Alcalde Eusebio Ortega Molina, 43',hero_t='A 4-star hotel in World Heritage Baeza',hero_s='A terrace with a pool and panoramic views over the city and the sea of olive trees.',
 intro_t='Tranquillity and an exquisite interior',intro_p1='An elegant four-storey building with a Renaissance-style façade, 50 rooms and, since 2008, a reference for business and leisure travellers in Baeza.',
 intro_p2='Less than 500 metres away: the Fuente de los Leones, the Plaza de la Constitución and the old town. Free open-air parking nearby.',
 stats=['4 stars','50 rooms','Terrace with pool','Since 2008'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='With wooden floors, flat-screen TV, free wifi, minibar, safe, central heating, hairdryer, new mattresses and a pillow menu.',
 svcs=['Terrace with pool and panoramic views','Freshly prepared buffet breakfast','Restaurant inside the hotel','«Andalucía» room for events and meetings','Free parking nearby and paid parking at the hotel','Cots on request and subject to availability'],
 loc_p='Avda. Alcalde Eusebio Ortega Molina, 43 · 23440 Baeza (Jaén). Phone: +34 953 747 311. Email: reservas@hotelcamposdebaeza.com.',
 chips=['Which rooms do you have?','Do you have parking?','Is there a pool?','How do I book?']),
'fr':dict(title='Hotel Campos de Baeza · Hôtel 4 étoiles à Baeza',see_rooms='Voir les chambres',hero_k='Baeza · Avda. Alcalde Eusebio Ortega Molina, 43',hero_t='Un hôtel 4 étoiles à Baeza, patrimoine mondial',hero_s='Une terrasse avec piscine et vue panoramique sur la ville et la mer d’oliviers.',
 intro_t='Tranquillité et intérieur raffiné',intro_p1='Un élégant bâtiment de 4 étages à la façade de style Renaissance, 50 chambres et, depuis 2008, une référence pour les voyages d’affaires et de loisirs à Baeza.',
 intro_p2='À moins de 500 mètres : la Fuente de los Leones, la Plaza de la Constitución et la vieille ville. Parking gratuit en plein air à proximité.',
 stats=['4 étoiles','50 chambres','Terrasse avec piscine','Depuis 2008'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Avec parquet, TV écran plat, wifi gratuit, minibar, coffre-fort, chauffage central, sèche-cheveux, matelas neufs et carte d’oreillers.',
 svcs=['Terrasse avec piscine et vue panoramique','Petit-déjeuner buffet préparé chaque matin','Restaurant à l’intérieur de l’hôtel','Salon «Andalucía» pour événements et réunions','Parking gratuit à proximité et payant à l’hôtel','Lits bébé sur demande et selon disponibilité'],
 loc_p='Avda. Alcalde Eusebio Ortega Molina, 43 · 23440 Baeza (Jaén). Téléphone : +34 953 747 311. E-mail : reservas@hotelcamposdebaeza.com.',
 chips=['Quelles chambres avez-vous ?','Avez-vous un parking ?','Y a-t-il une piscine ?','Comment réserver ?']),
'de':dict(title='Hotel Campos de Baeza · 4-Sterne-Hotel in Baeza',see_rooms='Zimmer ansehen',hero_k='Baeza · Avda. Alcalde Eusebio Ortega Molina, 43',hero_t='Ein 4-Sterne-Hotel im Welterbe Baeza',hero_s='Eine Terrasse mit Pool und Panoramablick über die Stadt und das Meer aus Olivenbäumen.',
 intro_t='Ruhe und ein exquisites Interieur',intro_p1='Ein elegantes vierstöckiges Gebäude mit Renaissance-Fassade, 50 Zimmern und seit 2008 eine feste Größe für Geschäfts- und Urlaubsreisende in Baeza.',
 intro_p2='Weniger als 500 Meter entfernt: die Fuente de los Leones, die Plaza de la Constitución und die Altstadt. Kostenlose Parkplätze im Freien in der Nähe.',
 stats=['4 Sterne','50 Zimmer','Terrasse mit Pool','Seit 2008'],nav_rooms='Zimmer',rooms_t='Zimmer',rooms_s='Mit Holzboden, Flachbild-TV, kostenlosem WLAN, Minibar, Safe, Zentralheizung, Föhn, neuen Matratzen und Kissenmenü.',
 svcs=['Terrasse mit Pool und Panoramablick','Frisch zubereitetes Frühstücksbuffet','Restaurant im Hotel','Salon «Andalucía» für Events und Meetings','Kostenlose Parkplätze in der Nähe, kostenpflichtig im Hotel','Kinderbetten auf Anfrage und je nach Verfügbarkeit'],
 loc_p='Avda. Alcalde Eusebio Ortega Molina, 43 · 23440 Baeza (Jaén). Telefon: +34 953 747 311. E-Mail: reservas@hotelcamposdebaeza.com.',
 chips=['Welche Zimmer gibt es?','Gibt es einen Parkplatz?','Gibt es einen Pool?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://hotelcamposdebaeza.com/reservas/'
BOOK=dict(mode='engine',url=dict(es=R,en=R,fr=R,de=R))
D=dict(name='Hotel Campos de Baeza',ac='#26301c',ac2='#5e6b2e',ac2_a11y='#525e27',book=BOOK,around=[],foot=FOOT,
 address='Avda. Alcalde Eusebio Ortega Molina, 43 · 23440 Baeza',phones=['+34 953 747 311'],emails=['reservas@hotelcamposdebaeza.com'],maps='Hotel Campos de Baeza, Avenida Alcalde Eusebio Ortega Molina 43, 23440 Baeza',t=T)
META=dict(repo='demo-hotel-campos-de-baeza',name='Hotel Campos de Baeza',legal_name='INVERSIONES CAMPOS DE BAEZA, S.L., CIF B23519002 (política de cancelación y aviso legal de su web)',registry_ids=['B23519002'],
 url='https://hotelcamposdebaeza.com/',domain='hotelcamposdebaeza.com',municipality='Baeza',province='Jaén',sector='hotel de 4 estrellas con terraza y piscina en Baeza',
 read_at='2026-11-02T10:50:00+01:00',created_at='2026-11-02T10:48:00+01:00',built_at='2026-11-02T11:15:00+01:00',audit_date='2026-11-02T10:50:00+01:00',
 rating=dict(value=4.1,coincide=['tel','web'],date='2026-10-30',url='https://www.google.com/maps/search/Hotel+Campos+de+Baeza+Baeza'),
 book=dict(mode='engine',url=R,note='motor propio de su web (VikBooking) en su pagina /reservas/ (boton RESERVAS del menu), HTTP 200 (02/11/2026 11:02); la web solo esta en espanol, mismo enlace en los 4 idiomas.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Cómo es la Junior Suite?','K02'),('¿Qué tienen las habitaciones?','K03'),('¿Tenéis parking?','K04'),('¿Hay piscina?','K05'),('¿Hay desayuno?','K06'),('¿Dónde estáis?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿A qué hora es el check-out?','K09'),('¿Puedo cancelar la reserva?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Tenéis cuna?','K12'),('¿Cuánto cuesta la noche?',None),('¿Admitís mascotas?',None)],
'en':[('Which rooms do you have?','K01'),('What is the Junior Suite like?','K02'),('What do the rooms include?','K03'),('Do you have parking?','K04'),('Is there a pool?','K05'),('Is there breakfast?','K06'),('Where are you?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('What time is check-out?','K09'),('Can I cancel my booking?','K10'),('What is your phone number?','K11'),('Do you have a cot?','K12'),('How much is a night?',None),('Do you allow pets?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Comment est la Junior Suite ?','K02'),('Que comprennent les chambres ?','K03'),('Avez-vous un parking ?','K04'),('Y a-t-il une piscine ?','K05'),('Y a-t-il un petit-déjeuner ?','K06'),('Où êtes-vous ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('À quelle heure est le check-out ?','K09'),('Puis-je annuler ma réservation ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Avez-vous un lit bébé ?','K12'),('Combien coûte la nuit ?',None),('Acceptez-vous les animaux ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Wie ist die Junior Suite?','K02'),('Was bieten die Zimmer?','K03'),('Gibt es einen Parkplatz?','K04'),('Gibt es einen Pool?','K05'),('Gibt es Frühstück?','K06'),('Wo liegt das Hotel?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Wann ist der Check-out?','K09'),('Kann ich meine Buchung stornieren?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Haben Sie ein Kinderbett?','K12'),('Was kostet eine Nacht?',None),('Sind Haustiere erlaubt?',None)]}
