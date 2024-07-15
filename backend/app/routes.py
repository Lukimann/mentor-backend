from flask import Blueprint, request, jsonify
from .models import db, Volunteer, NewsletterSubscriber, Contacts

bp = Blueprint('api', __name__, url_prefix='/api')

# Contacts endpoints
@bp.route('/contacts', methods=['GET'])
def get_contacts():
    try:
        contacts = Contacts.query.all()
        contacts_list = [{'name': contact.name, 'email': contact.email, 'message': contact.message} for contact in contacts]
        return jsonify(contacts_list), 200
    except Exception as e:
        print(f"Error in get_contacts: {str(e)}")
        return jsonify(message="An internal error occurred"), 500

@bp.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    new_contact = Contacts(
        name=data['name'],
        email=data['email'],
        message=data['message']
    )
    db.session.add(new_contact)
    db.session.commit()
    return jsonify(message='Your message has been sent successfully'), 201

# Volunteer endpoints
@bp.route('/volunteer', methods=['GET']) #added s
def get_volunteers():
    try:
        volunteers = Volunteer.query.all()
        volunteers_list = [{'name': volunteer.name, 'email': volunteer.email, 'phone': volunteer.phone,
                            'address': volunteer.address, 'occupation': volunteer.occupation, 'country': volunteer.country,
                            'days': volunteer.days, 'times': volunteer.times, 'motivation': volunteer.motivation} 
                           for volunteer in volunteers]
        return jsonify(volunteers_list), 200
    except Exception as e:
        print(f"Error in get_volunteers: {str(e)}")
        return jsonify(message="An internal error occurred"), 500

@bp.route('/volunteer', methods=['POST'])
def add_volunteer():
    data = request.get_json()

    # Ensure all mandatory fields are present
    required_fields = ['name', 'email', 'phone', 'address', 'occupation', 'country', 'days', 'times', 'motivation']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify(message=f'Missing or empty field: {field}'), 400

    # Create a new Volunteer object
    new_volunteer = Volunteer(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        address=data['address'],
        occupation=data['occupation'],
        country=data['country'],
        days=data['days'],
        times=data['times'],
        motivation=data['motivation']
    )

    # Add the new volunteer to the database
    db.session.add(new_volunteer)
    db.session.commit()

    return jsonify(message='Volunteer added successfully'), 201


# Newsletter endpoints
@bp.route('/newsletter', methods=['GET'])
def get_newsletters():
    try:
        subscribers = NewsletterSubscriber.query.all()
        subscribers_list = [{'email': subscriber.email} for subscriber in subscribers]
        return jsonify(subscribers_list), 200
    except Exception as e:
        print(f"Error in get_newsletters: {str(e)}")
        return jsonify(message="An internal error occurred"), 500

@bp.route('/newsletter', methods=['POST'])
def add_newsletter():
    data = request.get_json()
    if not data or 'email' not in data:
        return jsonify(message='Invalid input'), 400
    
    new_subscriber = NewsletterSubscriber(
        email=data['email']
    )
    try:
        db.session.add(new_subscriber)
        db.session.commit()
        return jsonify(message='Newsletter subscription added successfully'), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(message='Failed to add subscription', error=str(e)), 500
