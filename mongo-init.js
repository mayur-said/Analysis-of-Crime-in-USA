db.createUser(
    {
        user: "dap_username",
        pwd: "dap_password",
        roles: [
            {
                role: "readWrite",
                db: "dap"
            }
        ]
    }
);