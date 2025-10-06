from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class PopulousTheBeginningArchipelagoOptions:
    poptb_campaigns: PopulousTBCommunityMissions
    poptb_gimmicks: PopulousTBGimmickMissions


class PopulousTheBeginningGame(Game):
    name = "Populous 3: The Beginning"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.X360,
    ]

    is_adult_only_or_unrated = False

    options_cls = PopulousTheBeginningArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Complete PLANETS",
                data={
                    "PLANETS": (self.planets, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="EASYCHALLENGE",
                data={
                    "EASYCHALLENGE": (self.easychallenge, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),

            GameObjectiveTemplate(
                label="MEDIUMCHALLENGE",
                data={
                    "MEDIUMCHALLENGE": (self.mediumchallenge, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),

            GameObjectiveTemplate(
                label="HARDCHALLENGE",
                data={
                    "HARDCHALLENGE": (self.hardchallenge, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Kill a TRIBE Shaman on any planet",
                data={
                    "TRIBE": (self.tribe, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Destroy the TRIBE Tribe on any planet",
                data={
                    "TRIBE": (self.tribe, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Charge and use the SPELLS spell on any planet",
                data={
                    "SPELLS": (self.spells, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Have 10 BUILDABLES at once on any planet",
                data={
                    "BUILDABLES": (self.buildables, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Fully worship a IDOLS on any planet",
                data={
                    "IDOLS": (self.idols, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Complete a Planet in 30 minutes or less",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=10,
            ),
        ]

    @property
    def gimmicks(self) -> List[str]:
        return sorted(self.archipelago_options.poptb_gimmicks.value)

    @property
    def hasgimmicks(self) -> bool:
        return "Gimmicks On" in self.gimmicks

    @property
    def campaigns(self) -> List[str]:
        return sorted(self.archipelago_options.poptb_campaigns.value)

    @property
    def hasundiscovered(self) -> List[str]:
        return "Undiscovered Worlds" in self.campaigns

    @property
    def hastikals(self) -> bool:
        return "Tikals Journey" in self.campaigns

    @property
    def haskatarasvoyage(self) -> bool:
        return "Kataras Voyage" in self.campaigns

    @property
    def hasascensionc1(self) -> bool:
        return "Ascension Chapter 1" in self.campaigns

    @property
    def haswitchinghour(self) -> bool:
        return "The Witching Hour" in self.campaigns

    @property
    def hasdevilsystem(self) -> bool:
        return "The Devil System Chapter 1" in self.campaigns

    @property
    def hasseasonspring(self) -> bool:
        return "Seasons: Spring" in self.campaigns

    @property
    def hasseasonsummer(self) -> bool:
        return "Seasons: Summer" in self.campaigns

    @property
    def hasseasonautumn(self) -> bool:
        return "Seasons: Autumn" in self.campaigns

    @property
    def hasseasonwinter(self) -> bool:
        return "Seasons: Winter" in self.campaigns

    @property
    def haswarofthegods(self) -> bool:
        return "War of the Gods" in self.campaigns

    @property
    def hasadaptiveai(self) -> bool:
        return "Adaptive AI" in self.campaigns

    @functools.cached_property
    def basecampaign(self) -> List[str]:
        return [
            "The Beginning - 1: The Journey Begins",
            "The Beginning - 2: Night Falls",
            "The Beginning - 3: Crisis of Faith",
            "The Beginning - 4: Combined Forces",
            "The Beginning - 6: Building Bridges",
            "The Beginning - 7: Unseen Enemy",
            "The Beginning - 8: Continental Divide",
            "The Beginning - 9: Fire in the Mist",
            "The Beginning - 11: Treacherous Souls",
            "The Beginning - 12: An Easy Target",
            "The Beginning - 13: Aerial Bombardment",
            "The Beginning - 14: Attacked From All Sides",
            "The Beginning - 16: Bloodlust",
            "The Beginning - 17: Middle Ground",
            "The Beginning - 18: Head Hunter",
            "The Beginning - 19: Unlikely Allies",
            "The Beginning - 20: Archipelago",
            "The Beginning - 21: Fractured Earth",
            "The Beginning - 23: Inferno",
	    "The Beginning - 24: Journey's End",
        ]

    def planets(self) -> List[str]:        
        planets: List[str] = self.basecampaign[:]
  
        if self.hasgimmicks:
            planets.extend(self.vanillagimmickplanets)

        if self.hasundiscovered:
            planets.extend(self.undiscoveredplanets)

        if self.hasundiscovered and self.hasgimmicks:
            planets.extend(self.undiscoveredgimmicks)

        if self.hastikals:
            planets.extend(self.tikalplanets)

        if self.hastikals and self.hasgimmicks:
            planets.extend(self.tikalgimmicks)

        if self.haskatarasvoyage:
            planets.extend(self.kataraplanets)

        if self.haskatarasvoyage and self.hasgimmicks:
            planets.extend(self.kataragimmicks)

        if self.hasascensionc1:
            planets.extend(self.ascensionplanets)

        if self.hasascensionc1 and self.hasgimmicks:
            planets.extend(self.ascensiongimmicks)

        if self.haswitchinghour:
            planets.extend(self.witchplanets)

        if self.haswitchinghour and self.hasgimmicks:
            planets.extend(self.witchgimmicks)

        if self.hasdevilsystem:
            planets.extend(self.devilsystemplanets)

        if self.hasdevilsystem and self.hasgimmicks:
            planets.extend(self.devilgimmicks)

        if self.hasseasonspring:
            planets.extend(self.springplanets)

        if self.hasseasonspring and self.hasgimmicks:
            planets.extend(self.springgimmicks)

        if self.hasseasonsummer:
            planets.extend(self.summerplanets)

        if self.hasseasonsummer and self.hasgimmicks:
            planets.extend(self.summergimmicks)

        if self.hasseasonautumn:
            planets.extend(self.autumnplanets)

        if self.hasseasonautumn and self.hasgimmicks:
            planets.extend(self.autumngimmicks)

        if self.hasseasonwinter:
            planets.extend(self.winterplanets)

        if self.hasseasonwinter and self.hasgimmicks:
            planets.extend(self.wintergimmicks)

        if self.haswarofthegods:
            planets.extend(self.warofthegodsplanets)

        if self.haswarofthegods and self.hasgimmicks:
            planets.extend(self.warofthegodsgimmicks)

        if self.hasadaptiveai:
            planets.extend(self.adaptiveaiplanets)

        return sorted(planets)
            
    @functools.cached_property
    def vanillagimmickplanets(self) -> List[str]:
        return [		
            "The Beginning - 5: Death from Above",            
            "The Beginning - 10: From the Depths",
            "The Beginning - 15: Incarcerated",
            "The Beginning - 22: Solo",
	    "The Beginning - 25: The Beginning",
        ]

    @functools.cached_property
    def undiscoveredplanets(self) -> List[str]:
        return [		
            "Undiscovered Worlds - 1: Aftermath",
            "Undiscovered Worlds - 2: Lava Flow",
	    "Undiscovered Worlds - 3: Soul Survivor",
            "Undiscovered Worlds - 4: World Wide Web",
            "Undiscovered Worlds - 5: Human Shield",
            "Undiscovered Worlds - 7: Protection Racket",
            "Undiscovered Worlds - 9: Overshadowed",
            "Undiscovered Worlds - 10: Fortress",
        ]

    @functools.cached_property
    def undiscoveredgimmicks(self) -> List[str]:
        return [		
            "Undiscovered Worlds - 4: World Wide Web",
            "Undiscovered Worlds - 6: No Man's Land",
	    "Undiscovered Worlds - 8: Prisons",
	    "Undiscovered Worlds - 11: L'Assassine",
            "Undiscovered Worlds - 12: Natural Disaster",
        ]

    @functools.cached_property
    def tikalplanets(self) -> List[str]:
        return [
		"Tikal's Journey - 1: No Turning Back",
		"Tikal's Journey - 2: Outnumbered?",
		"Tikal's Journey - 3: Painful Magic",
		"Tikal's Journey - 4: Daki-Tak Island",
		"Tikal's Journey - 5: Hidden In Darkness",
		"Tikal's Journey - 6: Two For One Deal",
		"Tikal's Journey - 7: Cyclone Fury",
		"Tikal's Journey - 8: Helping Hands",
		"Tikal's Journey - 9: Island Hopping",
		"Tikal's Journey - 10: Desert Mirage",
		"Tikal's Journey - 11: War on the Isle",
		"Tikal's Journey - 12: Tensions Arise",
		"Tikal's Journey - 13: Fire in the Hole",
		"Tikal's Journey - 14: Bog Killer",
		"Tikal's Journey - 15: Undercover From Death",
		"Tikal's Journey - 16: Boat Skirmish",
		"Tikal's Journey - 17: Quake Wars",
		"Tikal's Journey - 19: Eye of the Unbelieving",
		"Tikal's Journey - 20: Size Matters",
		"Tikal's Journey - 22: Volcanic Angels",
		"Tikal's Journey - 23: Twilight Ascends",
		"Tikal's Journey - 24: Against All Odds",
		"Tikal's Journey - 25: Raising Hell",
        ]

    @functools.cached_property
    def tikalgimmicks(self) -> List[str]:
        return [		
	        "Tikal's Journey - 18: Matak Alcatraz",
		"Tikal's Journey - 21: Tribal Struggle",
        ]    

    @functools.cached_property
    def kataraplanets(self) -> List[str]:
        return [		
		"Katara's Voyage - 1: The Voyage Begins",
		"Katara's Voyage - 2: Separated",
		"Katara's Voyage - 3: Preacher Panic",
		"Katara's Voyage - 4: Surrounded By Rivals",
		"Katara's Voyage - 5: Icy Madness",
		"Katara's Voyage - 6: Facing Worlds",
		"Katara's Voyage - 8: Air Temple of Death",
		"Katara's Voyage - 9: Azula's Stronghold",
                "Katara's Voyage - 10: End of the Line",
        ]  

    @functools.cached_property
    def kataragimmicks(self) -> List[str]:
        return [		
	        "Katara's Voyage - 7: Dakini's Prison",
        ]  
 
    @functools.cached_property
    def ascensionplanets(self) -> List[str]:
        return [		
	    "Ascension - 1: Descendants",
            "Ascension - 2: A New Journey",
            "Ascension - 3: Distress Signal",
            "Ascension - 5: Zealots",            
            "Ascension - 7: The Gift Of Flames",
            "Ascension - 8: Diverting Enemies",
            "Ascension - 9: Tyranny",
	    "Ascension - 10: Civil War",
        ] 

    @functools.cached_property
    def ascensiongimmicks(self) -> List[str]:
        return [		
	        "Ascension - 4: Prisoners of War",
	        "Ascension - 6: Trials of Blood",
        ]   

    @functools.cached_property
    def witchplanets(self) -> List[str]:
        return [		
	    "The Witching Hour - 3: Great Indian Desert",
	    "The Witching Hour - 4: Death on the Nile",
	    "The Witching Hour - 6: Crimson Graveyard",
	    "The Witching Hour - 8: The Instructor",
	    "The Witching Hour - 9: Brainlust",
            "The Witching Hour - 10: Glacial Prison",
	    "The Witching Hour - 12: Book of the Dead",
	    "The Witching Hour - 13: Avernus",
            "The Witching Hour - 14: We're Not Alone",
            "The Witching Hour - 15: Witches' Sabbath",	
        ]

    @functools.cached_property
    def witchgimmicks(self) -> List[str]:
        return [		
	    "The Witching Hour - 2: The Witching Hour",
	    "The Witching Hour - 5: Beaks of the Beast",
	    "The Witching Hour - 7: Memento Mori",
	    "The Witching Hour - 11: Looking for Answers",
	    "The Witching Hour - 16: Death's Denial",
        ] 
 
    @functools.cached_property
    def devilsystemplanets(self) -> List[str]:
        return [
		"The Devil System C1 - 1: The Exploration Begins",
		"The Devil System C1 - 2: Power of Faith",
		"The Devil System C1 - 3: Matak Attack",
		"The Devil System C1 - 4: Lightning Eel",
		"The Devil System C1 - 6: Two On Four",
		"The Devil System C1 - 7: Land of the Wilds",
		"The Devil System C1 - 8: The Legend of Kikikini",
		"The Devil System C1 - 9: Help From Nowhere",
		"The Devil System C1 - 11: Teamwork Forever",
		"The Devil System C1 - 12: Sabotage",
		"The Devil System C1 - 13: The Traitor",
		"The Devil System C1 - 14: Allies Torn Apart",
		"The Devil System C1 - 15: Taitaki's Introduction",
		"The Devil System C1 - 16: Evil Land",
		"The Devil System C1 - 18: Great Wall of Ice",
	        "The Devil System C1 - 20: Harsh Climates",
	        "The Devil System C1 - 21: Magical Protection",
	        "The Devil System C1 - 22: Frozen Seas",
	        "The Devil System C1 - 23: Hypnotic Menace",
	        "The Devil System C1 - 24: Tribal Time Bomb",
	        "The Devil System C1 - 26: Rubble Pile",
	        "The Devil System C1 - 27: Contract Binaries",
	        "The Devil System C1 - 28: Eternal Rain of Fire",
        ]

    @functools.cached_property
    def devilgimmicks(self) -> List[str]:
        return [	
	    "The Devil System C1 - 17: Cold Welcome",
	    "The Devil System C1 - 19: Wrath of the God",
	    "The Devil System C1 - 25: Rupture",
        ]

    @functools.cached_property
    def springplanets(self) -> List[str]:
        return [		
	    "Seasons: Spring - 1: Help on the Way",
	    "Seasons: Spring - 2: Tribal Ascend",
	    "Seasons: Spring - 4: Arrival",
	    "Seasons: Spring - 5: The Conjuring",
	    "Seasons: Spring - 6: Divided Attention",
	    "Seasons: Spring - 8: The Bard's Tale",
	    "Seasons: Spring - 9: Supercell Torture",
	    "Seasons: Spring - 10: Hollow Canyon",
	    "Seasons: Spring - 11: Eastern Winds",
	    "Seasons: Spring - 12: Where Shamans Fall",		
        ]

    @functools.cached_property
    def springgimmicks(self) -> List[str]:
        return [	
	    "Seasons: Spring - 3: One for the Team",
	    "Seasons: Spring - 7: Through Fear",

        ]

    @functools.cached_property
    def summerplanets(self) -> List[str]:
        return [		
	    "Seasons: Summer - 1: Ring of Fire",
	    "Seasons: Summer - 3: Clouded Warfare",
	    "Seasons: Summer - 4: Sunny Morning",
	    "Seasons: Summer - 5: Bouncin' Eight",
	    "Seasons: Summer - 6: Build'N'Conquer",
	    "Seasons: Summer - 7: Mirage",		
        ]

    @functools.cached_property
    def summergimmicks(self) -> List[str]:
        return [	
	    "Seasons: Summer - 2: A Midsummer Twilight",
	    "Seasons: Summer - 8: Southern Winds",

        ]

    @functools.cached_property
    def autumnplanets(self) -> List[str]:
        return [		
	    "Seasons: Autumn - 1: Wind Howling",
	    "Seasons: Autumn - 2: Far Steppe",
	    "Seasons: Autumn - 4: The Bitter End",
	    "Seasons: Autumn - 5: Chartreuse",
	    "Seasons: Autumn - 6: Redleaf Battle",
	    "Seasons: Autumn - 8: Western Winds",
	    "Seasons: Autumn - 9: Torn Into Shreds",
	    "Seasons: Autumn - 10: The Healer Skulks",
	    "Seasons: Autumn - 11: Message For the Chumara",
	    "Seasons: Autumn - 12: From the Shadows",		
        ]

    @functools.cached_property
    def autumngimmicks(self) -> List[str]:
        return [	
	    "Seasons: Autumn - 3: 44 Days",
	    "Seasons: Autumn - 7: The Priest's Escort",
        ]

    @functools.cached_property
    def winterplanets(self) -> List[str]:
        return [		
	    "Seasons: Winter - 1: It's Friday",
	    "Seasons: Winter - 2: Time Has Come",
	    "Seasons: Winter - 3: The Rift",
	    "Seasons: Winter - 4: Meltdown",
	    "Seasons: Winter - 5: High Issues",
	    "Seasons: Winter - 6: Thaw on the Mountains",
	    "Seasons: Winter - 8: Frozen Fruit",
	    "Seasons: Winter - 10: Shattered Ice",
	    "Seasons: Winter - 11: Pirate Isles",
	    "Seasons: Winter - 12: Snonado",		
        ]

    @functools.cached_property
    def wintergimmicks(self) -> List[str]:
        return [	
	    "Seasons: Winter - 7: Power of Two",
	    "Seasons: Winter - 9: Northern Winds",
        ]

    @functools.cached_property
    def warofthegodsplanets(self) -> List[str]:
        return [		
	    "War of the Gods - 1: Erecting Paths",
	    "War of the Gods - 2: Hornet Nest",
	    "War of the Gods - 3: Cursed Faith",
	    "War of the Gods - 4: Triforce of Storms",
	    "War of the Gods - 6: Supernatural Voodoo",
	    "War of the Gods - 7: Inconspicious Odds",
	    "War of the Gods - 8: Intercontinental Split",
	    "War of the Gods - 9: Obscured From The Flow",
	    "War of the Gods - 11: Perilous Spirits",
	    "War of the Gods - 12: A Pushover Decision",
	    "War of the Gods - 13: Ethereal Onslaught",
	    "War of the Gods - 14: Ambush Assault",
	    "War of the Gods - 16: Bloodthirsty",
	    "War of the Gods - 17: Center Field",
	    "War of the Gods - 18: Top Stalker",
	    "War of the Gods - 19: Absurd Partners",
	    "War of the Gods - 20: Demon's Flight",
	    "War of the Gods - 21: Ruptured World",
	    "War of the Gods - 23: Hellfire",
	    "War of the Gods - 24: A Mortal's End",																	
        ]

    @functools.cached_property
    def warofthegodsgimmicks(self) -> List[str]:
        return [	
	    "War of the Gods - 5: Black Death",
	    "War of the Gods - 10: A Sinking Feeling",
	    "War of the Gods - 15: Detained",
	    "War of the Gods - 22: Stranded",
	    "War of the Gods - 25: War of the Gods",
        ]


    @functools.cached_property
    def adaptiveaiplanets(self) -> List[str]:
        return [	
	    "Adaptive AI - 1: SMP Roots",
	    "Adaptive AI - 2: Mandala",
	    "Adaptive AI - 3: Persimmon",
	    "Adaptive AI - 4: Wasteland",
	    "Adaptive AI - 5: Fortresses",
	    "Adaptive AI - 6: Airstrike",
	    "Adaptive AI - 7: Bloodlust",
	    "Adaptive AI - 8: Blackout",
	    "Adaptive AI - 9: Teleport Trickery",
	    "Adaptive AI - 10: Calamity",
	    "Adaptive AI - 11: Betrayal",
	    "Adaptive AI - 12: Natural Disasters",
	    "Adaptive AI - 13: Empowerment",
	    "Adaptive AI - 14: Chosen Restrictions",
	    "Adaptive AI - 15: Ring Islands",
        ]


    @staticmethod
    def easychallenge() -> List[str]:
        return [
	    "Complete a Planet without worshipping anything",
	    "Complete a Planet where you eliminate the Dakini Tribe last",
	    "Complete a Planet where you eliminate the Chumara Tribe last",
	    "Complete a Planet where you eliminate the Matak Tribe last",
	    "Complete a Planet where all three Tribes are present",
	    "Complete a Planet with only one enemy Tribe present",
	    "Have 10 fully-built Guard Towers at once",
	    "Have 5 Warrior Training Huts at once",
	    "Have 5 Temples at once",
	    "Have 5 Firewarrior or Archer Training Huts at once",
	    "Convert an enemy Warrior with one of your Preachers",
	    "Convert an enemy Firewarrior or Archer with one of your Preachers",
	    "Kill an enemy Shaman by knocking them into water",
	    "Use Call to Arms to defeat an enemy attack (Press B when a Warrior in a Guard Tower sees an enemy)",
	    "Scare an enemy Shaman out of her Guard Tower using Swarm or Spies",
            "Kill an enemy that is in the process of worshipping",
            "Use the Lightning Bolt spell on an enemy Training Hut",
	    "Conceal all of your buildings from worldview by using Spies in Guard Towers",
	    "Destroy an enemy Warrior Training Hut",
	    "Destroy an enemy Temple",
	    "Destroy an enemy Firewarrior Training Hut",
	    "Destroy an enemy Spy Training Hut",
	    "Destroy an enemy Boat House",
	    "Destroy an enemy Balloon Hut",
            "On any planet, have one charge of every available spell",
	    "Complete a planet without your Shaman dying",
        ]

    @staticmethod
    def mediumchallenge() -> List[str]:
        return [
	    "Have 20 Large Huts at once",       
            "Complete a Planet without training any Warriors",
	    "Complete a Planet without training any Firewarriors or Archers",
	    "Complete a Planet without training any Preachers",
	    "Complete a Planet without making any vehicles",
	    "Complete a Planet without putting any Firewarriors or Archers into Guard Towers",
	    "Complete a Planet without using any patrol points or campfires",
	    "Complete a Planet without using the Blast spell",
	    "Complete a Planet without using the Convert spell",
	    "Complete a Planet without using Landbridge, Flatten or Erode",
	    "Successfully sabotage 5 buildings with Spies in a single Planet",
	    "Have at least 200 followers at once",
	    "Eliminate a tribe without ever damaging their buildings with your Shaman and her spells",
	    "Eliminate a tribe with only your Shaman and her spells",
	    "Complete a planet where you built your base far away from your reincarnation site",
	    "Have 50 Warriors at once",
	    "Have 50 Preachers at once",
	    "Have 50 Firewarriors and/or Archers at once",
            "Complete a Planet where you have an ally",
            "Have 25 followers in Boats at once",
            "Have 10 followers in Balloons at once",
            "Have a Large Hut containing a Brave, Warrior, Preacher, Firewarrior and Spy",
	    "Create a pile of at least 30 Wood",
            "Obtain one of the three Guest Spells: Bloodlust, Teleport or Armageddon",
]

    @staticmethod
    def hardchallenge() -> List[str]:
        return [
	    "Complete a Planet without any of your buildings being completely destroyed",
	    "Complete a Planet without using any building-destroying spells",
	    "Complete a Planet without ever casting a spell on an enemy Shaman",
	    "Have at least 100 followers at once without having any Braves",
	    "Kill an enemy tribe's Angel of Death",
            "Successfully defeat three tribes in Armageddon",
	    "Completely destroy an enemy Training Hut/Temple by burning it with Spies",
            "Complete a Planet where enemies are allied against you",
            "Destroy an enemy structure using the Landbridge spell",
            "Convert an enemy using a Hypnotized Preacher",
            "Train a Hypnotized enemy in one of your Training Huts",
            "Kill a non-brave Enemy in a vehicle with a Firewarrior in a vehicle",
	    "Have one of every Training Hut and Vehicle Hut at the same time",
	    "Have the maximum charges for Blast, Firestorm, Earthquake and Volcano at the same time",
	    "Have the maximum charges for Landbridge, Flatten, Swamp and Erode at the same time",
	    "Have the maximum charges for Convert, Invisibility, Magical Shield and Hypnotize at the same time",
	    "Eliminate a tribe without completely destroying any of their buildings",
            "Complete a Planet where an enemy tribe was eliminated by a tribe other than you",
            "Complete a Planet where your Shaman commanded her followers from a Guard Tower that she never left",
        ]

    @staticmethod
    def buildables() -> List[str]:
        return [
	    "Boats",
	    "Balloons",
        ]

    @staticmethod
    def tribe() -> List[str]:
        return [
            "Matak",
	    "Chumara",
            "Dakini",
        ]
        
    @staticmethod
    def spells() -> List[str]:
        return [
            "Angel of Death",
            "Blast",
            "Convert",
            "Earthquake",
            "Erode",
            "Firestorm",
            "Flatten",
            "Hypnotise",
            "Invisibility",
            "Landbridge",
            "Lightning",
            "Magical Shield",
            "Swamp",
            "Swarm",
            "Tornado",
            "Volcano",
        ]

    @staticmethod
    def idols() -> List[str]:
        return [
		"Stone Head",
                "Totem Pole",
		"Vault of Knowledge",
		"Obelisk, Gargoyle or Portal",
        ]

# Archipelago Options
class PopulousTBCommunityMissions(OptionSet):
    """
    Indicates which community-made Campaigns the player wants to draw from, if any. War of the Gods is intended for COOP play, and can be found with Adaptive AI on the Populous Reincarnated Launcher. All other campaigns can be found in the Multiverse Launcher.
    """

    display_name = "Populous The Beginning Community Campaigns"
    valid_keys = [
	"Undiscovered Worlds",
        "Tikals Journey",
        "Kataras Voyage",
        "The Devil System Chapter 1",
        "Ascension Chapter 1",
        "The Witching Hour",
        "Seasons: Spring",
        "Seasons: Summer",
        "Seasons: Fall",
        "Seasons: Winter",
        "War of the Gods",
        "Adaptive AI",
    ]

    default = valid_keys

class PopulousTBGimmickMissions(OptionSet):
    """
    Indicates if the player wishes to play non-traditional missions like Incarcerated and Solo. Also enables similar missions in any custom campaigns that you have enabled.
    """

    display_name = "Populous The Beginning Community Campaigns"
    valid_keys = [
        "Gimmicks On",
        "Gimmicks Off",
    ]

    default = valid_keys
