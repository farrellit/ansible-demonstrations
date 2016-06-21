

<code>ansible-playbook -i hosts main.yml
</code>

<code>
ansible-playbook -i hosts main.yml  -e environ=env2
</code>

<pre>
vagrant@ansible:~/git/ansible-demonstrations/double-includes-resolution$ ansible-playbook -i hosts main.yml  -e environ=env2

PLAY [localhost] **************************************************************

TASK: [role2 | debug msg="Role 2"] ********************************************
ok: [127.0.0.1] => {
    "msg": "Role 2"
}

TASK: [role2 | debug var=var2] ************************************************
ok: [127.0.0.1] => {
    "var": {
        "var2": "fuzbar"
    }
}

PLAY RECAP ********************************************************************
127.0.0.1                  : ok=2    changed=0    unreachable=0    failed=0

vagrant@ansible:~/git/ansible-demonstrations/double-includes-resolution$ ansible-playbook -i hosts main.yml

PLAY [localhost] **************************************************************

TASK: [role2 | debug msg="Role 2"] ********************************************
ok: [127.0.0.1] => {
    "msg": "Role 2"
}

TASK: [role2 | debug var=var2] ************************************************
ok: [127.0.0.1] => {
    "var": {
        "var2": "foobar"
    }
}

PLAY RECAP ********************************************************************
127.0.0.1                  : ok=2    changed=0    unreachable=0    failed=0
</pre>
