#################
#### imports ####
#################
from project import db
from project.models import BlogPost
from .forms import MessageForm
from flask import render_template, Blueprint, url_for, redirect, request
from flask.ext.login import login_required, current_user

 
################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)





################
#### routes ####
################

# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])   # pragma: no cover
@login_required   # pragma: no cover
def home():
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        new_message = BlogPost(
            form.title.data,
            form.description.data,
            current_user.id
        )
        db.session.add(new_message)
        db.session.commit()
        
        return redirect(url_for('home.home'))
    else:
        posts = db.session.query(BlogPost).all()
        return render_template(
            'home.html', posts=posts, form=form, error=error)




