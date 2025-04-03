from django.shortcuts import render
from destinations.datas import destinations_data
activities_data = [ 
    # Goa Beach (id=1) 
    { 
        "id": 1, 
        "destination_id": 1, 
        "name": "Scuba Diving", 
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTx8kMictQ0hIPxT2-9MfwH0XFyaHqk9KEhHQ&s", 
        "description": "Explore the underwater world with expert guides." 
    }, 
    { 
        "id": 2, 
        "destination_id": 1, 
        "name": "Jet Skiing", 
        "image": "https://media.istockphoto.com/id/494094157/photo/young-guy-cruising-on-a-jet-ski.jpg?s=612x612&w=0&k=20&c=XQWhVoiI7G_GlYbK_4IjujQcZ0VjvI5tNewgMvvDO7c=", 
        "description": "Ride the waves and feel the adrenaline rush!" 
    }, 
    { 
        "id": 3, 
        "destination_id": 1, 
        "name": "Beach Volleyball", 
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0Fd3iCJWhaAJP_ETwFhTFzbJIQLuckE5-kQ&s", 
        "description": "Enjoy an exciting game of volleyball on the beach." 
    }, 
 
    # Manali Hills (id=2) 
    { 
        "id": 4, 
        "destination_id": 2, 
        "name": "Paragliding", 
        "image": "https://media.istockphoto.com/id/522078473/photo/paraglider-flying-over-mountains.jpg?s=612x612&w=0&k=20&c=fsoxFDnN_rfISUIBb65xLprBiqv60rdYRa3q_4DQAsI=", 
        "description": "Soar high above the mountains and enjoy breathtaking views." 
    }, 
    { 
        "id": 5, 
        "destination_id": 2, 
        "name": "Skiing", 
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuH2M80gUvyXwwNJSfpXJwQr938xm8aDDncA&s", 
        "description": "Hit the slopes and experience thrilling snow adventures." 
    }, 
 
    # Pyramids of Giza (id=3) 
    { 
        "id": 6, 
        "destination_id": 3, 
        "name": "Camel Ride", 
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuw0eK06XpvMIme6lh-0W1n-3nxBD7FzmyIg&s", 
        "description": "Travel across the golden sands like the ancient Egyptians." 
    }, 
    { 
        "id": 7, 
        "destination_id": 3, 
        "name": "Archaeological Tour", 
        "image": "https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F979032193%2F954457689503%2F1%2Foriginal.20250309-133921?w=600&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C1069%2C2268%2C1134&s=67c87525a764ff3a41e7a8887010ce07", 
        "description": "Discover the secrets of ancient Egypt with an expert guide." 
    }, 
 
    # Bali Paradise (id=4) 
    { 
        "id": 8, 
        "destination_id": 4, 
        "name": "Surfing", 
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEQrorqbtB7XY65RcGOk7Vsrqz7pLj2sLRWQ&s", 
        "description": "Catch the best waves in the heart of Bali!" 
    }, 
    { 
        "id": 9, 
        "destination_id": 4, 
        "name": "Island Hopping", 
        "image": "https://media.istockphoto.com/id/1396220896/photo/young-woman-traveler-relaxing-and-enjoying-at-beautiful-tropical-white-sand-beach-at-maya-bay.jpg?s=612x612&w=0&k=20&c=OsSASkFZV2UufexRVcP1Zbv9L9aqZNGlVivAiWY0ncA=", 
        "description": "Explore beautiful islands and hidden beaches." 
    }, 
 
    # Swiss Alps (id=5) 
    { 
        "id": 10, 
        "destination_id": 5, 
        "name": "Snowboarding", 
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyNisHM4MQ6RSPZTk8lyv9GdysyJEJ1rGssw&s", 
        "description": "Glide through snowy peaks with breathtaking views." 
    }, 
    { 
        "id": 11, 
        "destination_id": 5, 
        "name": "Mountain Trekking", 
        "image": "https://plus.unsplash.com/premium_photo-1677002240252-af3f88114efc?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dHJla2tpbmd8ZW58MHx8MHx8fDA%3D", 
        "description": "Experience scenic trails and enjoy panoramic views." 
    }, 
 
    # Machu Picchu (id=6) 
    { 
        "id": 12, 
        "destination_id": 6, 
        "name": "Hiking", 
        "image": "https://images.unsplash.com/photo-1551632811-561732d1e306?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aGlraW5nfGVufDB8fDB8fHww", 
        "description": "Walk the legendary Inca trail to reach the ancient ruins." 
    }, 
    { 
        "id": 13, 
        "destination_id": 6, 
        "name": "Photography Tour", 
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROrLlgmE0iR9LlqcjxqTvtTzRidwbKbL3LEA&s", 
        "description": "Capture the beauty of Machu Picchu with professional guides." 
    }, 
 
    # Amazon Rainforest (id=7) 
    { 
        "id": 14, 
        "destination_id": 7, 
        "name": "Wildlife Safari", 
        "image": "https://media.istockphoto.com/id/1086330828/photo/an-evening-well-spent-with-a-dominant-male-tiger-of-tourism-area-and-his-cubs-at-ranthambore.jpg?s=612x612&w=0&k=20&c=VN8huZhigGt0-dv-abYaZ0sgNPI-AmRBoxV9_PsXhWM=", 
        "description": "Spot rare animals in their natural habitat." 
    }, 
    { 
        "id": 15, 
        "destination_id": 7, 
        "name": "River Kayaking", 
        "image": "https://media.istockphoto.com/id/1256457327/photo/happy-best-friends-having-fun-on-a-kayaks-kayaking-on-the-river.jpg?s=612x612&w=0&k=20&c=2xqM9vn0J1j4MQt1_43UrUBAWA_F5MraARlwiWmHlJc=", 
        "description": "Paddle through Amazon’s winding rivers and experience nature." 
    }, 
 
    # Great Barrier Reef (id=8) 
    { 
        "id": 16, 
        "destination_id": 8, 
        "name": "Snorkeling", 
        "image": "https://media.istockphoto.com/id/1282649181/photo/young-couple-in-snorkeling-mask-dive-underwater-in-tropical-sea.jpg?s=612x612&w=0&k=20&c=fPpKGAnzNQLWFTc4ux696XQkcf0aCKBxCs2jr-aOP4U=", 
        "description": "Discover colorful marine life up close." 
    }, 
    { 
        "id": 17, 
        "destination_id": 8, 
        "name": "Glass Bottom Boat Tour", 
        "image": "https://media-cdn.tripadvisor.com/media/attractions-splice-spp-674x446/06/6f/55/1a.jpg", 
        "description": "See the reef without getting wet on a guided boat tour." 
    }, 
    { 
        "id": 18, 
        "destination_id": 8, 
        "name": "Underwater Photography", 
        "image": "https://images.unsplash.com/photo-1682687982502-1529b3b33f85?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8ZGl2aW5nfGVufDB8fDB8fHww", 
        "description": "Capture stunning marine life photos with expert tips." 
    }, 
    { 
        "id": 19, 
        "destination_id": 8, 
        "name": "Dolphin Watching", 
        "image": "https://plus.unsplash.com/premium_photo-1695715758373-76aa4d75515e?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZG9scGhpbiUyMHdhdGNoaW5nfGVufDB8fDB8fHww", 
        "description": "Spot playful dolphins in the crystal-clear waters." 
    }, 
    { 
        "id": 20, 
        "destination_id": 8, 
        "name": "Coral Reef Diving", 
        "image": "https://media.istockphoto.com/id/498283106/photo/underwater-scuba-diver-explore-and-enjoy-coral-reef-sea-life.jpg?s=612x612&w=0&k=20&c=xOj00xaZTpy5-AtKvMvIHHfexz9miSSct_CXb6F9KVA=", 
        "description": "Dive deep to explore breathtaking coral formations." 
    } 
] 

# Create your views here.
def activities_list(request):
    context={
        'alist':activities_data
    }
    return render(request,'activities_list.html',context)
def activities_details(request,id):
    data=None
    for x in activities_data:
        if x['id']==id:
            data=x
    ddata=[]
    for destinations in destinations_data:
        if destinations['id']==data['destination_id']:
            ddata.append((destinations["id"],destinations['name']))
    context={
        'data':data,
        'ddata':ddata,
    }
    return render(request,'activities_details.html',context)