class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def length(head):

            c=0

            s1=head

            while s1:

                c=c+1

                s1=s1.next

            return c

        def rev(head,k):

            val=length(head)//k

            u=0

            c=0

            if head is None:

                return 

            prev,current,nxt=None,head,None

            while current is not None and c<k:

                nxt=current.next

                current.next=prev

                prev=current

                current=nxt
                c=c+1

            u=u+1

            if nxt is not None and u<val:
                
                head.next=rev(nxt,k)

            else:

                s2=prev

                while s2.next is not None:

                    s2=s2.next

                s2.next=current

            #head=prev
            return prev

        if k==1:

            return head
            
        return rev(head,k)