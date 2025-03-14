import random

def read_words_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []

def categorize_words(phrases):
    categories = {
        'Science': [],     
        'Technology': [],  
        'Space': [],       
        'Fiction': [],     
        'Biology': [],     
        'Future': [],      
        'Alien': [],       
        'Physics': [],     
        'Chemistry': [],   
        'Engineering': []   
    }

    for phrase in phrases:
        if 'bio' in phrase or phrase in ['biome', 'bioship', 'biochemistry', 'biotechnology', 'biological', 
                                          'biohazard', 'bioengineering', 'bioluminescence', 'bacteria', 'bacteriophage', 
                                          'biome', 'bipedal', 'inoculation', 'hybrid', 'hybridisation', 'lymphocyte', 
                                          'lysosome', 'leukocyte-lattice', 'lysogenic', 'myceliumdrive', 'mutation', 
                                          'mutagen', 'neurotransmitter', 'neuroplasticity', 'neurotoxin', 'neurogenic', 
                                          'neuroimplant', 'organmorphic', 'organism', 'nucleaophilic', 'neuroprosthetic', 
                                          'neoplasm', 'ribonucleic-acid', 'riboswitch', 'symbiotic', 'synaptic', 
                                          'synapticdrive', 'synapticlattice', 'synovial']:
            categories['Biology'].append(phrase)
        
        elif 'astro' in phrase or phrase in ['asteroid', 'astronaut', 'astropolis', 'atmosphere', 'astronomy', 'cosmos', 
                                             'spacecraft', 'galaxy', 'gravimetric', 'hyperdrive', 'farscape', 'gravplating', 'galactic', 
                                             'gravity-well', 'graviton', 'hypervelocity', 'interstellar', 'interdimensional', 
                                             'intergalactic', 'interspace', 'ionosail', 'interdrive', 'gravitational', 'lunar', 
                                             'nebula', 'orbit', 'oort', 'outer-space', 'orion', 'rogue-planet', 'star', 'saturn', 
                                             'sphere', 'space', 'spaceport', 'stargate', 'solar', 'system', 'solarsail', 'spacecraft', 
                                             'spacefare', 'spacefarer', 'spacer', 'spacestation', 'stellar-nursery', 'singularity', 
                                             'singularity-drive', 'singularity-lattice', 'stellarforge', 'stellar-nursery']:
            categories['Space'].append(phrase)
        
        elif 'drive' in phrase or 'engine' in phrase or phrase in ['automation', 'robotics', 'cybernetics', 'AI', 
                                                                  'machine learning', 'quantum computing', 'internet of things', 
                                                                  'flexbot', 'force-engine', 'hologram', 'hyperdrive', 'cyberdrive', 
                                                                  'hapticdrive', 'hovercraft', 'hyperfoil', 'gravitron', 'gyrodrive', 
                                                                  'joule', 'jetpack', 'laserdrive', 'cybernetics', 'impulology', 
                                                                  'jumpdrive', 'jumpgate', 'hypervelocity', 'mechsuit', 'morphdrive', 
                                                                  'metatech', 'memory-drive', 'nanotech', 'nanolattice', 'neural', 
                                                                  'nanosurgery', 'neotech', 'navigational', 'nanoengineering', 
                                                                  'neolattice', 'nucleartech', 'nanotube', 'mechdrive', 'network-engine', 
                                                                  'sonicengine', 'sonic', 'synth', 'synthlattice', 'synthcore', 'synapticdrive', 
                                                                  'synthetic', 'synthverse', 'sub-liminal', 'telekinetic-drive', 'teleportation', 
                                                                  'teleporter', 'technotroph', 'techno-organic', 'technogenesis', 'transmutation', 
                                                                  'telepresence', 'transwarp', 'technomorph', 'telekinetic']:
            categories['Technology'].append(phrase)
        
        elif phrase in ['alien', 'android', 'cyborg', 'dystopia', 'robot', 'biohazard', 'time travel', 'parallel universe', 
                         'virtual reality', 'firstspawn', 'doppelganger', 'doomstar', 'futuristic', 'cybernetic', 'cyborg', 
                         'juggernaut', 'hypernova', 'glitch', 'empath', 'insurgence', 'interdimensional', 'logicmorph', 'logitroph', 
                         'lifemind', 'liminalspace', 'liminalmind', 'overmind', 'omniscient', 'multiverse', 'metahuman', 
                         'neomorph', 'minddrive', 'multidimensional', 'multispacial', 'mechsuit', 'mechtech', 'nanite', 'nanodrone', 
                         'tesseract', 'telekinetic', 'time-dilation', 'televerse', 'time-locked', 'time-displacement', 'sporeverse', 
                         'stasis-space', 'singularity-lattice', 'subspace', 'subdrive', 'time-dilation', 'tachyondrive', 
                         'technomorph', 'time-locked']:
            categories['Fiction'].append(phrase)
        
        elif phrase in ['futuristic', 'cybernetic', 'dystopia', 'utopia', 'post-apocalyptic', 'artificial intelligence', 
                         'transhumanism', 'firstspace', 'fissioncore', 'fusioncore', 'hypernova', 'drone', 'darkweb', 'emergent', 
                         'hypervelocity', 'fusiondrive', 'jumpcraft', 'hypervelocity', 'lifesign', 'interearth', 
                         'hyperfoil', 'hyperlight', 'multicosm', 'megatech', 'hyperdrive', 'nanoscale', 'nanotech', 'null-lattice', 
                         'technogenesis', 'terraform', 'transgenesis', 'transwarp', 'subterrainian', 'time-dilation']:
            categories['Future'].append(phrase)
        
        elif 'extraterrestrial' in phrase or 'xenobiology' in phrase or phrase in ['alien planet', 'UFO', 'extraterrestrial life', 
                                                                                'extraterrestrial intelligence', 'Area 51', 'extradimensional', 
                                                                                'extraterrestrial', 'intergalactic', 'interdimensional']:
            categories['Alien'].append(phrase)
        
        elif 'thermo' in phrase or 'trajectory' in phrase or 'thermal' in phrase or phrase in ['thermodynamics', 'thermaldrive', 
                                                                                            'transduction', 'thermochemistry', 'thermoelasticity', 
                                                                                            'translation-lattice', 'thermoregulation', 'terraregulation', 
                                                                                            'teleregulation', 'titration', 'titrant', 'tropism', 'tropism', 
                                                                                            'tensor', 'toxicology', 'translation-matrix', 'thermocouple', 
                                                                                            'thermoreceptor', 'thermalsensor', 'telesensor', 'voltage', 'velocity', 
                                                                                            'vortex', 'vacuum-energy', 'vibration', 'vibration']:
            categories['Physics'].append(phrase)
        
        elif 'toxicology' in phrase or 'thermochemistry' in phrase or phrase in ['chemical', 'chemical-engineering', 'chemical-synthesis', 
                                                                             'titration', 'translation', 'radiowave', 'radioactive', 
                                                                             'transmutation', 'chemical-reaction']:
            categories['Chemistry'].append(phrase)

        elif 'sensor' in phrase or phrase in ['thermaldrive', 'trajectory', 'robot', 'mechdrive', 'system-engine', 'circuit-board', 
                                              'sensor', 'radiowave', 'vacuum-energy', 'vibration']:
            categories['Engineering'].append(phrase)

        # Default to Science category for other terms
        else:
            categories['Science'].append(phrase)
    return categories

# Debugging
def print_categories(categories):
    for category, phrases_list in categories.items():
        print(f"Category: {category}")
        print(", ".join(phrases_list) if phrases_list else "No phrases in this category")
        print("-----")

# Create random sentence
def create_random_sentence(categories, beginnings, conjoining_words):
    # Track used words
    used_phrases = set()

    def get_unique_phrase(category):
        """Retrieve a unique phrase from the given category."""
        available_phrases = [phrase for phrase in categories[category] if phrase not in used_phrases]
        if available_phrases:
            phrase = random.choice(available_phrases)
            used_phrases.add(phrase)
            return phrase
        else:
            return "unknown"

    science_phrase = get_unique_phrase('Science')
    technology_phrase = get_unique_phrase('Technology')
    space_phrase = get_unique_phrase('Space')
    fiction_phrase = get_unique_phrase('Fiction')
    biology_phrase = get_unique_phrase('Biology')
    future_phrase = get_unique_phrase('Future')
    alien_phrase = get_unique_phrase('Alien')
    physics_phrase = get_unique_phrase('Physics')
    chemistry_phrase = get_unique_phrase('Chemistry')
    engineering_phrase = get_unique_phrase('Engineering')

    beginning = random.choice(beginnings)
    conjoining = random.choice(conjoining_words) if random.random() < 0.5 else ''

    sentence_choices = [
        f"{beginning} {conjoining} scientists discovered {science_phrase}s, leading to the development of {technology_phrase}s that enabled the exploration of {space_phrase}s. These discoveries were key to the creation of {alien_phrase}s while adapting to {biology_phrase}s through {future_phrase}s.",
        f"{beginning} {conjoining} in a post-apocalyptic world, {science_phrase}s were uncovered, propelling the rise of {technology_phrase}s that allowed for the colonization of {space_phrase}s. These technological leaps paved the way for battles against {alien_phrase}s using {biology_phrase}s and enhanced by {future_phrase}s.",
        f"{beginning} {conjoining} a new era began when scientists uncovered {science_phrase}s, revolutionizing {technology_phrase}s and sending humanity on missions to explore {space_phrase}s. As they encountered strange beings, conflicts arose, forced to combat {alien_phrase}s through the use of {biology_phrase}s and {future_phrase}s.",
        f"{beginning} {conjoining} after the invention of {technology_phrase}s, humanity ventured into {space_phrase}s, where they stumbled upon {alien_phrase}s. These triggered conflicts, with humans fighting for survival while adapting through {biology_phrase}s and {future_phrase}s reshaping the fates of civilizations.",
        f"{beginning} {conjoining} during eras defined by {physics_phrase}s, scientists discovered new {chemistry_phrase}s, which were crucial to the development of {engineering_phrase}s that allowed the creation of {space_phrase}s. These led to the first encounters with {alien_phrase}s, changing the landscapes and accelerating the progress of {future_phrase}s.",
        f"{beginning} {conjoining} in ages dominated by {chemistry_phrase}s, {physics_phrase}s unlocked new possibilities for {technology_phrase}s, enabling the construction of {space_phrase}s. These breakthroughs changed the way humans interacted with {alien_phrase}s and reshaped futures with advances in {biology_phrase}s and {engineering_phrase}s.",
        f"{beginning} {conjoining} after the discovery of {science_phrase}s, humanity adapted to new environments in {space_phrase}s, while {technology_phrase}s emerged to solve the challenges of interplanetary travel. These led to the rise of encounters with {alien_phrase}s, adapting to unknown biology through {future_phrase}s.",
        f"{beginning} {conjoining} in distant futures, the search for {science_phrase}s sparked the creation of {technology_phrase}s, enabling the colonization of distant planets. The first successful expeditions to {space_phrase}s uncovered evidence of {alien_phrase}s, triggering survival conflicts enhanced by {biology_phrase}s and powered by {future_phrase}s.",
        f"{beginning} {conjoining} amidst the rise of {physics_phrase}s, breakthroughs in {chemistry_phrase}s led to the creation of {technology_phrase}s, allowing the construction of massive space stations in {space_phrase}s. These stations became the focal points of human interactions with {alien_phrase}s, adapting to new biology and technologies of {future_phrase}s.",
        f"{beginning} {conjoining} in alternate realities, cataclysmic events linked {physics_phrase}s and {chemistry_phrase}s, triggering the advent of {technology_phrase}s. The races to build {space_phrase}s became competitions between Earth and {alien_phrase}s, with adaptation to new biology and the future’s transformative possibilities.",
        f"{beginning} {conjoining} after the collapse of old governments, {science_phrase}s uncovered ancient secrets that propelled the development of {technology_phrase}s, unlocking the secrets of {space_phrase}s. These led to the discovery of {alien_phrase}s, while humanity navigated survival challenges, adapting to new biology through the integration of {future_phrase}s.",
        f"{beginning} {conjoining} in universes where {physics_phrase}s shaped the laws of nature, {chemistry_phrase}s provided the key to humanity’s survival in deep space. As {technology_phrase}s grew, they enabled the establishment of {space_phrase}s, where {alien_phrase}s were encountered. Adaptation to new biology through the use of {future_phrase}s became humanity’s hope for survival.",
        f"{beginning} {conjoining} in aftermaths of intergalactic wars, {science_phrase}s became the foundations for the creation of new technologies like {technology_phrase}s. These enabled humanity's expansion into {space_phrase}s, where they discovered {alien_phrase}s. Survival became a matter of mastering biology and futuristic technology from {future_phrase}s.",
        f"{beginning} {conjoining} while studying the mysteries of {space_phrase}s, scientists uncovered {science_phrase}s that set the foundation for the development of {technology_phrase}s. These breakthroughs allowed explorers to encounter unknown species on distant worlds, igniting conflicts with {alien_phrase}s, while adapting through the use of {biology_phrase}s and {future_phrase}s.",
        f"{beginning} {conjoining} as {chemistry_phrase}s unlocked new waves of scientific discoveries, {technology_phrase}s enabled humans to travel to the furthest reaches of {space_phrase}s. These breakthroughs allowed explorers to encounter {alien_phrase}s, sparking conflicts where humanity adapted to new biology and advanced technologies from {future_phrase}s."
        f"Captain, the engines are failing because of a {science_phrase} we discovered. It's affecting the {technology_phrase}s we need for the exploration of {space_phrase}s. We need to adapt, or we won't make it past the {alien_phrase}s.",
        f"Engineer, in a post-apocalyptic world, we've uncovered new {science_phrase}s, but the rise of {technology_phrase}s for {space_phrase}s isn’t enough. The {alien_phrase}s are causing trouble, and we need to rethink how we use {biology_phrase}s to survive.",
        f"Commander, the scientists uncovered {science_phrase}s, but the {technology_phrase}s we developed to explore {space_phrase}s are malfunctioning. 'We need a solution,' the Commander said. 'Or we won't survive the next encounter with {alien_phrase}s.'",
        f"Officer, after the invention of {technology_phrase}s, we've made it to {space_phrase}s, but we ran into {alien_phrase}s. We need to fight back, adapting our biology with {biology_phrase}s and enhancing our chances with {future_phrase}s, or it’ll be over.",
        f"Engineer, during {physics_phrase}s, scientists discovered a new {chemistry_phrase} that should have fixed our {technology_phrase}s. But the {space_phrase}s are playing havoc with our systems. We need to adapt, or we won't last.",
        f"Doctor, the {chemistry_phrase}s are reacting unpredictably with our {biology_phrase}s. I can’t get a proper read on the {alien_phrase}s either; it’s like they’re not even from this dimension. We need to come up with a new plan to survive.",
        f"Captain, we’ve discovered {science_phrase}s, but it's not enough to adapt to these new environments in {space_phrase}s. The {alien_phrase}s are already out there, and I don’t think we’ll make it unless we rethink our approach with {biology_phrase}s.",
        f"Lieutenant, the search for {science_phrase}s is taking us further into uncharted {space_phrase}s, but the technology isn’t keeping up. The {alien_phrase}s are closing in, and we need to adapt using {biology_phrase}s and {future_phrase}s, or we're done for.",
        f"Engineer, the new {chemistry_phrase}s we discovered are supposed to help us with the {technology_phrase}s for building stations in {space_phrase}s, but something’s off. The {alien_phrase}s keep causing interference. We need to figure out a way to handle this, or we’ll lose the station.",
        f"Captain, the quantum drives are malfunctioning, and it’s due to the unstable interaction between {physics_phrase}s and {chemistry_phrase}s. If we don’t find a fix, we'll never make it to {space_phrase}s in time to confront the {alien_phrase}s.",
        f"Commander, these {chemistry_phrase}s are messing with the {technology_phrase}s we need to survive. The {alien_phrase}s are evolving faster than we expected, and unless we adapt using {biology_phrase}s, we might not make it out alive.",
        f"Officer, after everything we've learned about {science_phrase}s, I’m afraid we’ve hit a dead end. Our {technology_phrase}s aren't enough to survive in {space_phrase}s. These {alien_phrase}s are more dangerous than we thought, and I’m not sure we’re ready to fight them.",
        f"Engineer, we’ve found new {space_phrase}s, but the {alien_phrase}s are unlike anything we’ve seen before. We need to find a way to adapt using {biology_phrase}s, or we’ll be overwhelmed. I’m not sure how much longer the {technology_phrase}s will hold up.",
        f"Doctor, the {alien_phrase}s are evolving, and our current biology adaptations won’t be enough. We need to accelerate our {future_phrase}s if we want to survive the next wave of attacks. It’s now or never.",
        f"Captain, the {technology_phrase}s we’ve built for exploring {space_phrase}s aren't cutting it. The {alien_phrase}s are too advanced. If we don’t adapt with the new {biology_phrase}s, we're going to be wiped out."
        f"Captain, the engines are failing because of a {science_phrase}... again. If we don’t get this fixed, we’ll be the first ship in history to be parked on an asteroid because we ran out of {technology_phrase}s.",
        f"Engineer, we’ve uncovered {science_phrase}s, but the {technology_phrase}s for {space_phrase}s aren’t working. Honestly, it’s like trying to fix a spaceship with duct tape and hope. Maybe we should try asking the {alien_phrase}s for help?",
        f"Commander, scientists discovered {science_phrase}s, but now the {technology_phrase}s we’ve developed to explore {space_phrase}s are acting like they’ve had too much coffee. They keep sputtering out. We’re gonna need more than a reset button to fix this.",
        f"Officer, after the invention of {technology_phrase}s, we managed to get to {space_phrase}s. But then the {alien_phrase}s showed up, and now it feels like we're stuck in a bad sci-fi movie. Should we try asking them for a ride home?",
        f"Engineer, during {physics_phrase}s, we found a new {chemistry_phrase}, and I thought, 'Great, this will work!' But now our {technology_phrase}s are doing the cha-cha instead of, you know, actually working. Any chance you’ve got a magic wand back there?",
        f"Doctor, I swear these {chemistry_phrase}s are doing more harm than good. The {biology_phrase}s won’t stop sneezing. I’m about to prescribe some {future_phrase}s just to get everyone to calm down.",
        f"Captain, we discovered {science_phrase}s, but I think they’ve got a personal vendetta against us. The {alien_phrase}s are already causing trouble, and our {technology_phrase}s are pretty much saying, 'Nope, not today.' Could really use a lucky break here.",
        f"Lieutenant, the search for {science_phrase}s is taking us deeper into {space_phrase}s, but the {alien_phrase}s are so weird they make your last haircut look normal. We might need to rethink our approach—or at least buy some bug spray.",
        f"Engineer, the {chemistry_phrase}s we discovered are supposed to help with the {technology_phrase}s. Instead, it’s like we tried to use a toaster to fix a spaceship. We’re currently stuck in a very expensive parking spot in {space_phrase}s.",
        f"Captain, our {technology_phrase}s are malfunctioning, and it’s definitely not because we ran out of coffee this time. The {alien_phrase}s are just mocking us now. At this point, I think we should just offer them some snacks and ask for directions.",
        f"Commander, I don’t think these {chemistry_phrase}s are as stable as they promised. Our {technology_phrase}s are having mood swings, and I’m pretty sure the {alien_phrase}s are laughing at us. This is going to be an interesting day.",
        f"Officer, after everything we’ve learned about {science_phrase}s, the {alien_phrase}s are still outsmarting us. It’s like they’ve read every sci-fi novel in the galaxy, and we’re over here trying to wing it with our old {technology_phrase}s.",
        f"Engineer, we’ve discovered new {space_phrase}s, but I think we may have accidentally insulted the {alien_phrase}s. They’ve started sending us space memes. Do you think they’re friendly, or is this their way of declaring war?",
        f"Doctor, the {alien_phrase}s are evolving faster than we can adapt. I’m starting to think they have a better HR department than we do. Can we get some {biology_phrase}s that don’t need a 6-month training course?",
        f"Captain, the {technology_phrase}s for exploring {space_phrase}s are making strange noises. It sounds like a cat that got stuck in a blender. We might want to go back to the drawing board—or at least buy the ship a treat."
    ]



    return random.choice(sentence_choices)

def main():
    phrases = read_words_from_file('sci_fi_phrases.txt')
    beginnings = read_words_from_file('beginnings.txt')
    conjoining_words = read_words_from_file('conjoining_words.txt')

    if not phrases or not beginnings or not conjoining_words:
        print("Error: One or more required files are missing or empty. Please check the files.")
        return

    categories = categorize_words(phrases)

    # print_categories(categories)

    print("\nRandom Sci-Fi Sentence:")
    print(create_random_sentence(categories, beginnings, conjoining_words))

if __name__ == "__main__":
    main()
