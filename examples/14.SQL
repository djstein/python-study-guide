#14.1
#List of tenants renting more than one apartment

SELECT TenantName FROM Tenants INNER JOIN 
    (SELECT TennatsID FROM AptTenants GROUP BY TennatsID HAVING COUNT(*) > 1) C
ON Tenants.TenantsID = C.TenantsID;

#14.2

#14.3
# Close all requests for apartment 11
UPDATE Requests SET Status='Closed' WHERE AptID IN
    (SELECT AptID FROM Apartments WHERE BuildingID = 11);