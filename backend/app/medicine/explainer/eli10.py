# --------------------------------------------------
# File: eli10.py
# Purpose: Explain Like I'm 10 (ELI10) plain language analogies for prescribed medicines.
# Module: Medicine Explanation Engine / ELI10
# Used By: Medicine Explainer Engine
# Future Phase: Phase 3A Medicine Intelligence
# --------------------------------------------------

ELI10_ANALOGIES = {
    "metformin": "Think of Metformin as a helpful key. When you eat food, sugar enters your blood. Metformin helps your body's cells open their doors to let the sugar in so it can be used for energy instead of floating around in your blood.",
    "amoxicillin": "Think of Amoxicillin as tiny shields that stop bad bacteria from building their protective walls. Without their walls, the bad bacteria can't survive, allowing your body's immune system to clear the infection.",
    "atorvastatin": "Think of Atorvastatin as a gentle cleaning crew for your blood vessels. It slows down the liver factory that makes extra cholesterol, keeping your blood pipes clean and healthy.",
    "amlodipine": "Think of Amlodipine as relaxing tight garden hoses. When blood vessels are tight, blood pressure goes up. Amlodipine relaxes the vessel walls so blood flows smoothly and your heart doesn't have to pump as hard.",
    "pantoprazole": "Think of Pantoprazole as turning down the burner on a hot stove. It calms down the acid factories in your stomach so your food pipe doesn't feel burnt or irritated.",
    "omeprazole": "Think of Omeprazole as putting a soft shield over your stomach lining by lowering acid levels, letting any sore spots heal comfortably.",
    "azithromycin": "Think of Azithromycin as a smart pause button for bacteria. It stops bad bacteria from multiplying so your body can easily defeat them.",
    "telmisartan": "Think of Telmisartan as blocking a signal that tells your blood vessels to squeeze tight. By keeping vessels relaxed, your blood pressure stays nicely balanced.",
    "paracetamol": "Think of Paracetamol as turning down your body's internal fever thermostat and soothing pain signals so you feel comfortable and rested.",
    "cetirizine": "Think of Cetirizine as catching allergy alarm letters before your body opens them. It stops histamine signals so your nose stops running and your eyes stop itching.",
    "levothyroxine": "Think of Levothyroxine as topping up your body's energy battery when your thyroid gland isn't making enough natural energy hormone.",
    "aspirin": "Think of Aspirin as making your blood platelets less sticky, like putting non-stick oil on frying pans so smooth blood flow is maintained.",
}


def generate_eli10_explanation(generic_name: str, brand_name: str) -> str:
    key = generic_name.lower().strip()
    analogy = ELI10_ANALOGIES.get(
        key,
        f"Think of {brand_name} ({generic_name}) as a targeted medicine that helps your body restore normal organ balance and stay healthy."
    )
    return analogy
