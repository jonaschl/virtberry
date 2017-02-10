from flask import render_template, redirect, url_for, flash, Markup
from app import app
from flask_login import login_required

@app.route('/vm/<string:uuid>/actions/<string:action>')
@login_required
def action(uuid, action):
        import sys
        import libvirt
        try :
            conn = libvirt.open('qemu:///system')
        except BaseException as error:
            # Markup is only needed because of the <br>
            flash(Markup(u"Could not connect to  \"qemu:///system\". <br> {}".format(error)), 'alert-danger')
            print('Failed to open connection to qemu:///system', file=sys.stderr)
            return redirect(url_for('index'))


        try:
            dom = conn.lookupByUUIDString(uuid)
        except:
            flash(u"Failed to get the domain object", 'alert-danger')
            print('Failed to get the domain object', file=sys.stderr)
            conn.close()
            return redirect(url_for('index'))

        domname = dom.name()
        if action == "start":
            try:
                dom.create()
            except:
                flash(u"Can not boot guest domain.", 'alert-danger')
                print('Can not boot guest domain.', file=sys.stderr)
                conn.close()
                return redirect(url_for('index'))

            flash(u"Sucessfully started Domain \"{}\"".format(domname), 'alert-info')
            conn.close()
            return redirect(url_for('index'))

        elif action == "shutdown":
            try:
                dom.shutdown()
            except:
                flash(u"Can not shutdown guest domain.", 'alert-danger')
                print('Can not shutdown guest domain.', file=sys.stderr)
                conn.close()
                return redirect(url_for('index'))

            flash(u"Sucessfully shutdowned Domain \"{}\"".format(domname), 'alert-info')
            conn.close()
            return redirect(url_for('index'))

        elif action == "destroy":
            try:
                dom.destroy()
            except:
                flash(u"Can not destroy guest domain.", 'alert-danger')
                print('Can not destroy guest domain.', file=sys.stderr)
                conn.close()
                return redirect(url_for('index'))

            flash(u"Sucessfully destroyed Domain \"{}\"".format(domname), 'alert-info')
            conn.close()
            return redirect(url_for('index'))

        elif action == "pause":
            try:
                dom.suspend()
            except:
                flash(u"Can not pause guest domain.", 'alert-danger')
                print('Can not pause guest domain.', file=sys.stderr)
                conn.close()
                return redirect(url_for('index'))

            flash(u"Sucessfully paused Domain \"{}\"".format(domname), 'alert-info')
            conn.close()
            return redirect(url_for('index'))

        elif action == "resume":
            try:
                dom.resume()
            except:
                flash(u"Can not eesume guest domain.:", 'alert-danger')
                print('Can not resume guest domain.', file=sys.stderr)
                conn.close()
                return redirect(url_for('index'))

            flash(u"Sucessfully resumed Domain \"{}\"".format(domname), 'alert-info')
            conn.close()
            return redirect(url_for('index'))

        else:
            flash(u"No such action: \"{}\"".format(action), 'alert-warning')
            conn.close()
            return redirect(url_for('index'))


'''
@app.route('/vm/<string:uuid>/actions/shutdown')
def action_shutdown(uuid):
        import sys
        import libvirt
        conn = libvirt.open('qemu:///system')
        if conn == None:
            print('Failed to open connection to qemu:///system', file=sys.stderr)
            exit(1)
        #domainUUID = '32878c67-c400-4162-9c62-d9393bc810a3'
        dom = conn.lookupByUUIDString(uuid)
        if dom == None:
            print('Failed to get the domain object', file=sys.stderr)
            exit(1)


        conn.close()
        return redirect(url_for('index'))

@app.route('/vm/<string:uuid>/actions/destroy')
def action_destroy(uuid):
        import sys
        import libvirt
        conn = libvirt.open('qemu:///system')
        if conn == None:
            print('Failed to open connection to qemu:///system', file=sys.stderr)
            exit(1)
        #domainUUID = '32878c67-c400-4162-9c62-d9393bc810a3'
        dom = conn.lookupByUUIDString(uuid)
        if dom == None:
            print('Failed to get the domain object', file=sys.stderr)
            exit(1)

        if dom.destroy() < 0:
            print('Can not destroy guest domain.', file=sys.stderr)
            exit(1)
        conn.close()
        return redirect(url_for('index'))

@app.route('/vm/<string:uuid>/actions/pause')
def action_pause(uuid):
        import sys
        import libvirt
        conn = libvirt.open('qemu:///system')
        if conn == None:
            print('Failed to open connection to qemu:///system', file=sys.stderr)
            exit(1)
        #domainUUID = '32878c67-c400-4162-9c62-d9393bc810a3'
        dom = conn.lookupByUUIDString(uuid)
        if dom == None:
            print('Failed to get the domain object', file=sys.stderr)
            exit(1)

        if dom.suspend() < 0:
            print('Can not pause guest domain.', file=sys.stderr)
            exit(1)
        conn.close()
        return redirect(url_for('index'))


@app.route('/vm/<string:uuid>/actions/resume')
def action_resume(uuid):
        import sys
        import libvirt
        conn = libvirt.open('qemu:///system')
        if conn == None:
            print('Failed to open connection to qemu:///system', file=sys.stderr)
            exit(1)
        #domainUUID = '32878c67-c400-4162-9c62-d9393bc810a3'
        dom = conn.lookupByUUIDString(uuid)
        if dom == None:
            print('Failed to get the domain object', file=sys.stderr)
            exit(1)

        if dom.resume() < 0:
            print('Can not resume guest domain.', file=sys.stderr)
            exit(1)
        conn.close()
        return redirect(url_for('index'))

'''
