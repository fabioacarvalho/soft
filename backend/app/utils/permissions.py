ROLE_PERMISSIONS = {
    "superadmin": {
        "*"
    },
    "admin": {
        "client:create",
        "client:edit",
        "client:view",
        "client:delete",
        "lead:view",
        "lead:edit",
    },
    "seller": {
        "client:create",
        "client:edit",
        "client:view",
        "lead:view",
        "report:view"
    },
    "manager": {
        "client:create",
        "client:edit",
        "client:view",
        "lead:view",
        "lead:edit",
        "report:view"
    },
    "marketing": {
        "campaign:view",
        "campaign:create",
        "report:view"
    },
    "customersuccess": {
        "lead:view",
        "customer:view",
        "customer:followup",
        "report:view"
    }
}
