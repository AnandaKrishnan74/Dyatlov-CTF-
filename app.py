from flask import Flask, render_template, request, redirect, url_for, session, flash, abort, send_from_directory
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

def get_progress():
    """Get current investigation progress from session."""
    if 'progress' not in session:
        session['progress'] = 0  # 0 means nothing completed
    return session['progress']

def set_progress(stage):
    """Update progress to the highest completed stage."""
    current = get_progress()
    if stage > current:
        session['progress'] = stage
        session.modified = True

def is_stage_unlocked(stage):
    """Check if a stage is unlocked (previous stage completed)."""
    progress = get_progress()
    return stage <= progress + 1

def is_stage_completed(stage):
    """Check if a stage is completed."""
    return stage <= get_progress()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/case-overview')
def case_overview():
    return render_template('case_overview.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/documents')
def documents():
    progress = get_progress()
    return render_template('documents.html', progress=progress)

@app.route('/evidence')
def evidence():
    progress = get_progress()
    if progress < 3:
        flash('Photographic evidence is not yet available. Complete previous investigation stages.', 'error')
        return redirect(url_for('investigation'))
    return render_template('evidence.html', progress=progress)

@app.route('/radio')
def radio():
    progress = get_progress()
    if progress < 5:
        flash('Radio intercept archive is restricted. Complete previous stages first.', 'error')
        return redirect(url_for('investigation'))
    return render_template('radio.html', progress=progress)

@app.route('/investigation')
def investigation():
    progress = get_progress()
    stages = []
    for i in range(1, 8):
        status = 'locked'
        if is_stage_completed(i):
            status = 'completed'
        elif is_stage_unlocked(i):
            status = 'available'
        stages.append({
            'number': i,
            'title': Config.STAGE_TITLES[i],
            'description': Config.STAGE_DESCRIPTIONS[i],
            'status': status
        })
    return render_template('investigation.html', stages=stages, progress=progress)

@app.route('/stage/<int:stage_num>', methods=['GET', 'POST'])
def flag_stage(stage_num):
    if stage_num < 1 or stage_num > 7:
        abort(404)
    
    if not is_stage_unlocked(stage_num):
        flash(f'Stage {stage_num} is locked. Complete previous stages first.', 'error')
        return redirect(url_for('investigation'))
    
    if request.method == 'POST':
        submitted_flag = request.form.get('flag', '').strip()
        expected = Config.FLAGS.get(stage_num)
        
        if submitted_flag == expected:
            set_progress(stage_num)
            flash(f'Stage {stage_num} complete: {Config.STAGE_TITLES[stage_num]}. Evidence recovered.', 'success')
            if stage_num == 7:
                return redirect(url_for('ending'))
            return redirect(url_for('investigation'))
        else:
            flash('Incorrect flag. The evidence does not match. Continue your investigation.', 'error')
    
    # Special content hints based on stage
    return render_template('flag_stage.html', 
                           stage_num=stage_num,
                           title=Config.STAGE_TITLES[stage_num],
                           description=Config.STAGE_DESCRIPTIONS[stage_num],
                           completed=is_stage_completed(stage_num),
                           progress=get_progress())

@app.route('/ending')
def ending():
    if get_progress() < 7:
        flash('The final truth remains hidden. Complete all investigation stages.', 'error')
        return redirect(url_for('investigation'))
    return render_template('ending.html')

@app.route('/reset', methods=['POST'])
def reset_progress():
    session.clear()
    flash('Investigation progress has been reset. Begin a new case file.', 'success')
    return redirect(url_for('index'))

@app.route('/download/<path:filename>')
def download_artifact(filename):
    """Serve downloadable artifacts for CTF challenges."""
    # Only allow specific files
    allowed = ['photo_04_evidence.txt', 'radio_log_fragment.txt', 'radio_intercept_4610.wav']
    if filename not in allowed:
        abort(404)
    return send_from_directory(
        os.path.join(app.root_path, 'static', 'artifacts'),
        filename,
        as_attachment=True
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
