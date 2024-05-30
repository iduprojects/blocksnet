ADVANCED_SERVICE_TYPES = {
  'education': [
    {
      'name': 'community_center',
      'name_ru': 'центр детского творчества',
      'weight': 0.2,
      'accessibility': 30,
      'demand': 65,
      'osm_tags': {
        'amenity': 'community_centre'
      }
    },
  ],
  'healthcare': [
    {
      'name': 'polyclinic',
      'name_ru': 'поликлиника / центр семейной медицины',
      'weight': 0.3,
      'accessibility': 10,
      'demand': 13,
      'osm_tags': {
        'amenity': 'clinic'
      }
    },
    {
      'name': 'hospital',
      'name_ru': 'участковая больница',
      'weight': 0.3,
      'accessibility': 60,
      'demand': 9,
      'osm_tags': {
        'amenity': 'hospital'
      }
    },
  ],
  'commerce': [
    {
      'name': 'supermarket',
      'name_ru': 'ТЦ / супермаркет',
      'weight': 0.5,
      'accessibility': 15,
      'demand': 900,
      'osm_tags': {
        'shop': 'supermarket'
      }
    },
    {
      'name': 'zoo',
      'name_ru': 'зоомагазин',
      'weight': 0.1,
      'accessibility': 60,
      'demand': 2,
      'osm_tags': {
        'shop': 'pet'
      }
    },
  ],
  'catering': [
    {
      'name': 'bar_restaurant',
      'name_ru': 'бар / ресторан',
      'weight': 0.3,
      'accessibility': 30,
      'demand': 100,
      'osm_tags': {
        'amenity': ['bar', 'restaurant']
      }
    },
  ],
  'leisure': [
    {
      'name': 'community_centre_culture_house',
      'name_ru': 'комьюнити-центр / дом культуры',
      'weight': 0.2,
      'accessibility': 30,
      'demand': 100,
      'osm_tags': {
        'amenity': 'community_centre'
      }
    },
  ],
  'recreation': [
    {
      'name': 'public_space',
      'name_ru': 'общественные пространства',
      'weight': 0.2,
      'accessibility': 30,
      'demand': 100,
      'osm_tags': {
        'place': 'square'
      }
    },
    {
      'name': 'park',
      'name_ru': 'парк',
      'weight': 0.4,
      'accessibility': 30,
      'demand': 150,
      'osm_tags': {
        'leisure': 'park'
      }
    },
  ],
  'sport': [
    {
      'name': 'gym/fitness_center',
      'name_ru': 'спортзал ОП / фитнес-центр',
      'weight': 0.2,
      'accessibility': 45,
      'demand': 25,
      'osm_tags': {
        'leisure': ['sports_hall','sports_centre','fitness_centre']
      }
    },
    {
      'name': 'skatepark/workout_for_teenagers',
      'name_ru': 'скейтпарк / воркаут для подростков',
      'weight': 0.1,
      'accessibility': 45,
      'demand': 25,
      'osm_tags': {
        'sport': 'skateboard'
      }
    },
  ],
  'service': [
    {
      'name': 'domestic_services',
      'name_ru': 'бытовые услуги',
      'weight': 0.2,
      'accessibility': 30,
      'demand': 75,
      'osm_tags': {
        'amenity': '*'
      }
    },
    {
      'name': 'bank',
      'name_ru': 'отделение банка',
      'weight': 0.3,
      'accessibility': 30,
      'demand': 20,
      'osm_tags': {
        'amenity': 'bank'
      }
    },
  ],
  'transport': [
    {
      'name': 'gas_station',
      'name_ru': 'автозаправка',
      'weight': 0.25,
      'accessibility': 60,
      'demand': 33,
      'osm_tags': {
        'amenity': 'bank'
      }
    },    
  ],
  'safeness': [
   {
      'name': 'police_supporting_point',
      'name_ru': 'опорный пункт полиции',
      'weight': 0.5,
      'accessibility': 60,
      'demand': 20,
      'osm_tags': {
        'amenity': 'bank'
      }
    },  
  ]
}