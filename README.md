This project uses a travel API to search for cheap flights within specified parameters. 
1. Copy google sheet from here: https://docs.google.com/spreadsheets/d/1rOuc-l1ffyaXTC_R9YuCKMp-SBbAOd1QsnPaoT_O-l4/edit?usp=sharing
2. Fill in desired destinations and price you would want to pay. 
3. In main.py, change the "ORIGIN_IATA" to whichever airport you want to fly from. 
4. In flight_search.py, you can adjust the range of nights you want to spend in your destination by altering "nights_in_dst_from" and
            "nights_in_dst_to".
5. See tequila api documentation for further refinements: https://tequila.kiwi.com/portal/docs/tequila_api/locations_api
6. In notification manager, you can adjust your inputs for smptlib and twilio to send you alerts when the price is below your threshold.
7. Run main.py.

Thank you!
