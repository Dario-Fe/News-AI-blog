---
tags: ["Security", "Ethics & Society", "Applications"]
date: 2025-12-26
author: "Dario Ferrero"
---

# When the City Stops: The Hidden Fragilities of the Autonomous Age
![waymo-blackout-analysis.jpg](waymo-blackout-analysis.jpg)

*The San Francisco blackout paralyzed hundreds of Waymo robotaxis, revealing the critical dependence of autonomous systems on urban infrastructure. As AI data centers double their electricity consumption and solar storms threaten our grids, an uncomfortable question arises: are we designing a resilient future or building technological houses of cards?*

On Saturday, December 21, 2025, in the early afternoon, a fire at the Pacific Gas & Electric substation in the Bayview-Hunters Point neighborhood plunged [over 130,000 customers](https://techcrunch.com/2025/12/21/waymo-suspends-service-in-san-francisco-as-robotaxis-stall-during-blackout/) in San Francisco into darkness. Traffic lights went out, house lights vanished, and something unexpectedly symbolic happened on the city streets: dozens of Waymo robotaxis stopped, motionless at intersections like soulless automatons.

Videos shared on social media show a scene that would have made Philip K. Dick smile: the characteristic white and blue Jaguar I-Paces with their hazard lights flashing, stuck in traffic while humans in their traditional cars carefully maneuvered around them. Some drivers filmed robotaxis stopped in the middle of the road, unable to decide how to proceed. [Waymo had to suspend its service](https://www.businessinsider.com/waymo-suspends-robotaxi-service-san-francisco-power-outage-tesla-2025-12) in the entire affected area, leaving passengers already on board wondering what was happening.

The contrast with Tesla vehicles equipped with Full Self-Driving was stark and immediate. While the Waymos remained paralyzed, the Teslas continued to drive, leveraging their local processing architecture. The episode raised a question that resonates far beyond the hills of San Francisco: if a local power outage can paralyze technology hailed as "the future," how robust is the infrastructure on which we are building autonomous mobility?

## The Digital Achilles' Heel

To understand why some autonomous cars stop while others keep moving, we need to look under the technological hood. [Waymo bases its architecture](https://missionlocal.org/2025/12/sf-waymo-halts-service-blackout/) on a complex ecosystem: LIDAR sensors generating three-dimensional maps of the surroundings, centimeter-accurate HD maps that need constant updates, and continuous remote communication with central servers to process data and make decisions. When the power went out, it wasn't just the traffic lights that failed; 5G cell towers, GPS repeaters, and communication infrastructure also suffered a chain of disruptions.

Tesla, on the other hand, adopts a radically different philosophy. Its Full Self-Driving system processes everything locally, relying primarily on cameras and neural networks running directly on the car's onboard computer. There is no need for a constant connection, no dependency on real-time updated external maps. It's like the contrast between a 1970s mainframe and a personal computer: centralization versus distributed processing, cloud versus edge computing.

The paradox is as fascinating as it is unsettling: [Waymo completes about 450,000 trips weekly](https://www.quattroruote.it/news/tecnologia/2025/12/22/san_francisco_waymo_robotaxi.html) in San Francisco, an industrial-scale operation that works beautifully as long as the ecosystem holds up. But that very scale amplifies the vulnerability: the more sophisticated the system, the more numerous the points of failure. GPS, 5G, cloud maps, a constant power supply for supporting infrastructure—when one of these links breaks, the entire chain collapses.

In the field of autonomous agriculture, this lesson was learned the hard way. During Israeli military operations in 2023, [deliberate GPS jamming by the IDF](https://www.calcalistech.com/ctechnews/article/q9msjj6cb) forced farmers to return to traditional methods. Rami Laner, 73, had to go back to working in the fields of Kibbutz Mevo Hama after a thirty-year absence because younger operators didn't know how to drive tractors without GPS systems. Plantations suffered from overlapping applications of fertilizers and pesticides, leading to crop damage and increased costs. The centimeter-level precision that had made Israeli agriculture so efficient turned out to be a structural weakness when satellite coordinates became unreliable.

Civilian drones have shown similar fragilities. DJI platforms, widely used in agriculture, aerial photography, and industrial inspections, [critically depend on the GPS signal](https://forum.dji.com/thread-254715-1-1.html) to maintain stability and orientation. When the signal degrades or disappears, the drones enter ATTI (attitude) mode, losing their ability to hold a fixed position and becoming vulnerable to wind and currents. Several users have reported critical situations during mapping or delivery missions, with drones suddenly losing satellite connection mid-flight and risking collisions.

## The Energy That Isn't There

But the energy problem isn't just about local outages. The consumption of data centers powering artificial intelligence systems is growing at a dizzying pace. According to the [International Energy Agency](https://www.punto-informatico.it/blackout-paralizza-self-driving-car-waymo/), the electricity consumption of data centers has increased from 415 terawatt-hours in 2024 to a projected 945 TWh by 2030—more than double in six years. To put that in perspective, it's like adding the entire electricity consumption of India to the global demand.

OpenAI's Stargate project in Texas will require 1.2 gigawatts of power, the equivalent of a medium-sized nuclear reactor. In Virginia, the so-called Data Center Alley already consumes 26% of the entire state's electricity. Texas, which in February 2021 experienced [the blackout from Winter Storm Uri](https://nt24.it/2025/09/energia-ia-vertiv/) with over 4.5 million customers in the dark and 246 deaths, is seeing its power grid stressed by new AI data centers.

The paradox is glaring: the technology that is supposed to make us more efficient and sustainable is consuming energy like entire nations. And this consumption is not evenly distributed but concentrated in a few geographical areas where the density of data centers creates energy hotspots. When these areas experience grid stress, it's not just local systems that suffer: the entire cloud computing infrastructure that underpins autonomous services, predictive analytics, and remote AI processing can falter.

Italy itself is not immune. Forecasts indicate a [growing risk of blackouts](https://prometeo.adnkronos.com/territorio/prossimo-blackout-previsioni-ai-dopo-spagna-2025/) for 2026, amplified by the race to install AI infrastructure. Cogeneration and microgrids are becoming increasingly discussed solutions for businesses wanting to protect themselves from the vulnerability of the national grid.
![waymo.jpg](waymo.jpg)
[Image from techcrunch.com](https://techcrunch.com/2025/12/21/waymo-suspends-service-in-san-francisco-as-robotaxis-stall-during-blackout/)

## Storms from Above

As if terrestrial fragilities weren't enough, the sky itself is becoming a threat. Solar Cycle 25 reached its peak between 2025 and 2026, bringing with it [G4 and G5-class geomagnetic storms](https://congressiinternazionali.it/blog/tempesta-solare-2025-rischi-comunicazione-e-soluzioni/). In November 2024, a G4 storm produced auroras visible as far south as Alabama—a magnificent spectacle that concealed significant problems for GPS systems and high-frequency radio communications.

The most dramatic historical precedent is the Carrington Event of 1859, when an exceptional solar storm produced auroras visible down to the Caribbean and knocked out telegraph lines across North America and Europe. Operators reported sparks setting paper on fire in their offices, and some telegraph systems continued to work even after being disconnected from their batteries, powered solely by geomagnetically induced currents.

Today, an event of that magnitude would be catastrophic. The United States Geological Survey warns that the Midwest and the East Coast of the United States are [particularly vulnerable](https://www.smartphonology.it/i-grandi-blackout-digitali-del-2025-quando-le-piattaforme-globali-si-fermano/) to geomagnetically induced currents (GICs) that can irreparably damage high-voltage transformers. This isn't a matter of flipping a switch off and on: a burned-out transformer can take months to replace, as they are huge, expensive, custom-made components.

For autonomous systems that depend on GPS, solar storms pose an existential threat. The charged particles distort the ionosphere, making satellite signals unreliable. Drones lose their orientation, autonomous tractors go off-course, and robotaxis no longer know where they are. And unlike terrestrial blackouts that can be geographically contained, a solar storm affects entire planetary regions simultaneously.

## The World Adapting to Machines

However, a deeper, more philosophical question emerges from these episodes of technological fragility. Instead of designing systems that adapt to the human world with all its imperfections and unpredictability, we are progressively modifying cities and infrastructure to accommodate rigid technologies that only work under ideal conditions.

San Francisco is investing millions in V2X (vehicle-to-everything) infrastructure, smart traffic lights that communicate with autonomous vehicles, dedicated lanes, and roadside sensors. It's an urban retrofitting on a billion-dollar scale to allow robotaxis to move safely. But this strategy inverts the traditional engineering paradigm: it's not the machines adapting to the environment, but the environment being reshaped for the machines.

The story of Cruise in San Francisco is a prime example. In October 2023, the California DMV [suspended the company's operations](https://www.punto-informatico.it/blackout-paralizza-self-driving-car-waymo/) after a robotaxi dragged a pedestrian for twenty feet following an accident, unable to recognize that the person was trapped under the vehicle. The incident raised uncomfortable questions about the ability of these systems to handle unexpected situations that a human driver would recognize immediately.

Sociologist M.C. Elish coined the term "moral crumple zone" to describe how humans in semi-autonomous systems become the scapegoats when something goes wrong. In aviation, when a pilot fails to intervene in time to correct an autopilot error, they are blamed for not properly supervising the system. But if the system is designed to operate autonomously 99% of the time, how can a human maintain the attention needed to intervene in that critical 1%?

Technology philosopher Luciano Floridi has argued that we need a "green and blue" approach: technology that respects both the natural environment (green) and the social and human environment (blue). The temptation to redesign the world to fit the limitations of our algorithms is strong, but it risks creating increasingly fragile urban ecosystems that depend on perfect conditions.

Autonomous agriculture, with its reliance on centimeter-level GPS and constant connectivity, works magnificently in the open fields of Kansas or Iowa, but it fails as soon as conditions deviate from the norm. Autonomous tractors [require GPS signals with three-centimeter accuracy](https://guidenav.com/handling-gnss-outages-in-agricultural-robots-ins-dead-reckoning-strategies/), which is impossible to maintain under dense canopies or near metal structures. The result is that some specialized crops, like vineyards and orchards with narrow rows, remain difficult to fully automate.

## Future Scenarios and Solutions

Yet not all is lost, and looking only at the failures would be reductive. Tesla has shown that different architectures can offer greater resilience. Hybrid edge computing, which balances local processing with cloud support when available, represents a promising middle ground. The most advanced agricultural systems are already implementing [inertial navigation systems](https://guidenav.com/handling-gnss-outages-in-agricultural-robots-ins-dead-reckoning-strategies/) (INS) that allow them to continue operating during temporary GPS outages, using accelerometers and gyroscopes to estimate position and orientation.

Regulation is slowly adapting to reality. The California Department of Motor Vehicles has shown it is willing to suspend operations when safety issues become apparent, as in the case of Cruise in 2023 and now with the Waymo disruptions. The European Union is developing standards that include resilience testing under degraded conditions, not just performance in ideal scenarios.

But a more radical shift in perspective is needed. Mandatory tests should include simulated blackouts, GPS jamming, and 5G connectivity interruptions. We cannot afford to discover vulnerabilities when hundreds of thousands of autonomous vehicles are already on the roads and millions of acres of farmland depend on driverless tractors.

Urban redesign must be holistic, not technology-centric. The cities of the future will have lanes for autonomous vehicles, but also redundancy in critical infrastructure: distributed microgrids, local backup generation, and multi-path communication systems that don't rely on a single technology. Robotaxis will need to be designed to degrade gracefully, like commercial aircraft that have triple and quadruple redundant systems for every critical function.

The experience of the [July 2024 CrowdStrike outage](https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages) offers a crucial lesson: 8.5 million Windows computers were knocked out by a single faulty software update, with estimated damages exceeding $10 billion. Airports halted, hospitals were forced to revert to paper, and banks were frozen. The system had a single point of failure, and when it broke, the consequences were global. Technological diversification is not just a matter of efficiency, but of systemic survival.

## Unfinished Epilogue

The Waymo cars stopped at San Francisco intersections were not just a temporary inconvenience for the passengers of those robotaxis. They were a mirror reflecting the hidden fragilities of a future we thought was already solid. As in the video game "The Last of Us," where technological civilization collapses in a matter of days when complex systems break, we are building a world where interconnected complexity can quickly turn into systemic vulnerability.

The question is not whether there will be more blackouts, more solar storms, more disruptions. The question is: when they arrive, will we have built systems robust enough to degrade gracefully instead of collapsing completely? Autonomous technology promises efficiency, safety, sustainability. But those promises are only valid if the systems also work when conditions are imperfect, when the power is out, when GPS is distorted, when the real world refuses to conform to the optimal parameters of our algorithms.

Perhaps true artificial intelligence will not be the one that works perfectly under perfect conditions, but the one that knows how to adapt, improvise, and survive when everything else fails. Just as humans have always done.
