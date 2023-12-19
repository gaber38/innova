# Contacts


schema diagram:

Table Contact {
  id int [pk]
  name varchar
  created_at Date
  updated_at Date
}

Table PhoneNumber {
  id int [pk]
  number varchar
  contact int [ref: > Contact.id]
  created_at Date
  updated_at Date
}


docker-compose build
docker-compose up