def set_hostname (name):
    return __salt__['cmd.run'](['/usr/bin/hostnamectl', 'set-hostname', name])
