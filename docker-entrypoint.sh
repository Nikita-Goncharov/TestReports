#!/bin/bash

while ! python /TestReports/testreports/manage.py makemigrations  2>&1; do
   echo "Migration creation is in progress status"
   sleep 3
done

while ! python /TestReports/testreports/manage.py migrate  2>&1; do
   echo "Migration is in progress status"
   sleep 3
done

echo "Django docker is fully configured successfully."

exec "$@"
