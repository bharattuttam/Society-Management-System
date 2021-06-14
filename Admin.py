
class Query:


    ALL_BILLS="""select  MemberName,MaintenanceMonth,BillAmount from admin join
     maintenance on 
     maintenance.IsPaid=admin.IsPaid join member
      where maintenance.MemberId=member.MemberId;
    
    
    """
    ALL_COMPLAINTS="""
    select NameOfPerson,ComplaintIssueDate,
    ComplaintDescription,Contact,Email from world.complaint;
    
    """