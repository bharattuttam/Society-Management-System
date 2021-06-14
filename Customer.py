class Query:


    RECENT_BILLS = """Select MaintenanceMonth,BillAmount,isPaid
                from Maintenance
                where MemberId=%s
                """



    PENDING_ORDERS = """select MaintenanceMonth,MemberName,BillAmount
                    from Member m 
                    join maintenance mo 
                    on m.MemberId=mo.MemberId
                    where mo.IsPaid=0; """
    EXECUTE_ORDERS = """Update world.maintenance 
                            Set IsPaid=1
                            where MaintenanceMonth (%s)"""