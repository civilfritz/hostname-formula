def hostname (name):
    ret = {
        'name': name,
        'changes': {},
        'result': False,
        'comment': '',
        'pchanges': {},
        }

    current_state = __grains__['localhost']
    if current_state == name:
        ret['result'] = True
        ret['comment'] = 'hostname already set'
        return ret

    if __opts__['test'] == True:
        ret['comment'] = 'Hostname will be set to "{0}".'.format(name)
        ret['pchanges'] = {
            'old': current_state,
            'new': name,
        }
        ret['result'] = None
        return ret

    __salt__['hostname.set_hostname'](name)
    ret['comment'] = 'Hostname was set to "{0}".'.format(name)
    ret['changes'] = {
        'old': current_state,
        'new': name,
    }
    ret['result'] = True
    return ret


def hostnamectl (name):
    ret = {
        'name': name,
        'changes': {},
        'result': False,
        'comment': '',
        'pchanges': {},
        }

    current_state = __grains__['localhost']
    if current_state == name:
        ret['result'] = True
        ret['comment'] = 'hostname already set'
        return ret

    if __opts__['test'] == True:
        ret['comment'] = 'Hostname will be set to "{0}".'.format(name)
        ret['pchanges'] = {
            'old': current_state,
            'new': name,
        }
        ret['result'] = None
        return ret

    __salt__['hostnamectl.set_hostname'](name)
    ret['comment'] = 'Hostname was set to "{0}".'.format(name)
    ret['changes'] = {
        'old': current_state,
        'new': name,
    }
    ret['result'] = True
    return ret
