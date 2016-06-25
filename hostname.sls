{% set hostname = pillar.get('hostname', grains['id']) %}

{%- if grains['os_family'] == 'Suse' %}
/etc/HOSTNAME:
  file.managed:
    - contents: {{ hostname }}
{% else %}
/etc/hostname:
  file.managed:
    - contents: {{ hostname }}
{% endif %}

set-hostname:
  {% if grains["init"] == "systemd" %}
  hostname.hostnamectl:
    - name: {{ hostname }}
  {% else %}
  hostname.hostname:
    - name: {{ hostname }}
  {% endif %}
