from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from grocery_app.models import GroceryStore, GroceryItem
# from grocery_app.forms import BookForm, AuthorForm, GenreForm

# Import app and db from events_app package so that we can run app
from grocery_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    all_stores = GroceryStore.query.all()
    print(all_stores)
    return render_template('home.html', all_stores=all_stores)

@main.route('/new_store', methods=['GET', 'POST'])
def new_store():
    form = GroceryStoreForm()
    # If form was submitted and was valid:
    if form.validate_on_submit(): 
        # - creates a new GroceryStore object and save it to the database,
        new_GroceryStore = GroceryStore(
            title=form.title.data,
            address=form.address.data,
        ) 

        db.session.add(new_GroceryStore)
        db.session.commit()

        # - flashes a success message
        flash('You have created a Grocery Store successfully')
        # - redirects the user to the store detail page.
        return redirect(url_for('main.store_detail', store_id=new_GroceryStore.id))
     # Sends the form to the template and use it to render the form fields
    return render_template('new_store.html', form=form)
    
@main.route('/new_item', methods=['GET', 'POST'])
def new_item():
    # TODO: Create a GroceryItemForm
    form = GroceryItemForm()


    if forn.validate_on_submit():
        # - create a new GroceryItem object and save it to the database,
        new_GroceryItem = GroceryItem(
            name=form.name.data,
            price=form.price.data,
            category=form.category.data,
            photo_url=form.photo_url.data,
            store=form.store.data
        )
        db.session.add(new_GroceryItem)
        db.session.commit()
    # - flash a success message, and
        flash('You have successfully added a new grocery item!')
    # - redirect the user to the item detail page.
        return redirect(url_for(main.item_detail, item_id=new_GroceryItem.id))

    return render_template('new_item.html', form=form)

@main.route('/store/<store_id>', methods=['GET', 'POST'])
def store_detail(store_id):
    store = GroceryStore.query.get(store_id)
    # Created GroceryStoreForm and passed in `obj=store`
    form = GroceryStoreForm(obj=store)

    if form.validate_on_submit(): 
        store.title=form.title.data,
        store.address=form.address.data

    db.session.add(store)
    db.session.commit()

    flash('The new Grocery Store was updated succesfully')        

    store = GroceryStore.query.get(store_id)
    return render_template('store_detail.html', store=store)

@main.route('/item/<item_id>', methods=['GET', 'POST'])
def item_detail(item_id):
    item = GroceryItem.query.get(item_id)
    # Created a GroceryItemForm and passed in `obj=item`
    form = GroceryItemForm(obj=item)

    if form.validate_on_submit():
        item.name=form.name.data 
        item.price=form.price.data
        item.category=form.category.data
        item.photo_url=form.photo_url.data
        item.store=form.store.data
    
    db.session.add(item)
    db.session.commit()

    flash('You have updated the Grocery Item successfully')

    item = GroceryItem.query.get(item_id)
    return render_template('item_detail.html', item=item)

