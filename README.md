# HooGives

Hoo Gives is a marketplace website application that allows UVA organizations to post philanthropy and community service events for all students to learn more about and get involved in.  Removing the hassle of passing out flyers and sending out Facebook posts to a select number of people, this application aims to efficiently provide an aggregation of events hosted by verified university organizations for all students to join in on the good cause.  How it works: 1) Organization owners and executive members post philanthropy and community service events coming up soon onto the discussion board, and 2) UVA students are able to browse through, learn more, and potentially join events that they are interested in participating in right in the marketplace.

## API's (how to call)

### Reading:

curl --location --request GET 'http://localhost:8001/api/v1/users/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'user_id=<insert-user-id>'

### Writing:

curl --location --request POST 'http://localhost:8001/api/v1/users/create/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'first_name=<insert-first-name>' \
--data-urlencode 'last_name=<insert-last-name>' \
--data-urlencode 'phone_number=<insert-phone-number>' \
--data-urlencode 'email=<insert-email>'

### Updating:

curl --location --request POST 'http://localhost:8001/api/v1/users/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'first_name=<insert-first-name>' \
--data-urlencode 'last_name=<insert-last-name>' \
--data-urlencode 'phone_number=<insert-phone-number>' \
--data-urlencode 'email=<insert-email>' \
--data-urlencode 'user_id=<insert-user-id>'

### Deleting:

curl --location --request GET 'http://localhost:8001/api/v1/users/delete/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'user_id=<insert-user-id>'
