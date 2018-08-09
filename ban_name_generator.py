fuck_them = []

admin_head = 'adm'
admin_tail = 'n'
admin_var1 = ['i','l']
admin_var2 = ['i','l','']
admin_var3 = ['i','l','']
admin_var4 = ['i','l','']
admin_var5 = ['i','l','']

support_head = 'su'
supoort_tail = 't'
support_var1 = ['p','r']
support_var2 = ['p','r']
support_var3 = ['o','q']
support_var4 = ['p','r']
support_var5 = ['']


def block(head,tail,var1,var2,var3,var4,var5):
    for a in var1:
        for b in var2:
            for c in var3:
                for d in var4:
                    for e in var5:
                        result = head + a + b + c + d + e + tail
                        fuck_them.append(result)
    for r in fuck_them:
        print(r)
    

#block(admin_head,admin_tail,admin_var1,admin_var2,admin_var3,admin_var4,admin_var5)
block(support_head,supoort_tail,support_var1,support_var2,support_var3,support_var4,support_var5)
