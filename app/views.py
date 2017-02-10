from flask import render_template, redirect, url_for, flash
from app import app
import flask_login
from flask_login import login_required

@app.route('/vm')
@login_required
def index():
	import sys
	import libvirt
	conn = libvirt.open('qemu:///system')
	doms = conn.listAllDomains(0)
	domains = []
	alert = {}
	#alert.setdefault("message", "This is a message")

	def dom_state(libvirt_state):
		if libvirt_state == libvirt.VIR_DOMAIN_NOSTATE:
			state = "No state"
			return state
		elif libvirt_state == libvirt.VIR_DOMAIN_RUNNING:
			state = "Running"
			return state
		elif libvirt_state == libvirt.VIR_DOMAIN_BLOCKED:
			state = "Blocked"
			return state
		elif libvirt_state == libvirt.VIR_DOMAIN_PAUSED:
			state = "Paused"
			return state
		elif libvirt_state == libvirt.VIR_DOMAIN_SHUTDOWN:
			state = "Shutdown"
			return state
		elif libvirt_state == libvirt.VIR_DOMAIN_SHUTOFF:
			state = "Shutoff"
			return state
		elif libvirt_state == libvirt.VIR_DOMAIN_CRASHED:
			state = "Crashed"
			return state
		elif libvirt_state == libvirt.VIR_DOMAIN_PMSUSPENDED:
			state = "Suspend"
			return state
		else:
			state = "Unknown"
			return state

	print("Hello World")

	if len(doms) != 0:
		for dom in doms:
			domain = {}
			domain.setdefault("name", dom.name())
			print('' + dom.name() + '')

			if "name" in domain:
				print("Get her 1")

			print('' + domain["name"] + '')
			domain.setdefault("uuid", dom.UUIDString())
			state, reason = dom.state()
			domain.setdefault("state", dom_state(state))


			print('' + domain["uuid"] + '')
			print('' + domain["state"] + '')

			domains.append(domain)
	conn.close()

	for domain in domains:
		print('' + domain["name"] + '')
		print('' + domain["uuid"] + '')
		print('' + domain["state"] + '')


	return render_template("vm.html",
				domains=domains,
				alert=alert)
