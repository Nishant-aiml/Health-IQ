# --------------------------------------------------
# File: foods.py
# Purpose: Structured Food Database categorized by food groups, benefits, and evidence sources.
# Module: Nutrition Knowledge Engine / Foods
# Used By: Knowledge Base & Recommendation Engine
# Future Phase: Phase 3C Nutrition & Lifestyle Intelligence
# --------------------------------------------------

from typing import List, Dict
from backend.app.nutrition.models import FoodItem, FoodCategory, NutrientProfile, EvidenceLevel

FOOD_DATABASE: Dict[str, FoodItem] = {
    "spinach": FoodItem(
        food_id="spinach",
        name="Spinach & Dark Leafy Greens",
        category=FoodCategory.VEGETABLES,
        glycemic_index=15,
        nutrients=[
            NutrientProfile(name="Iron", amount=2.7, unit="mg", daily_value_pct=15),
            NutrientProfile(name="Folate (B9)", amount=194, unit="ug", daily_value_pct=49),
            NutrientProfile(name="Vitamin K", amount=483, unit="ug", daily_value_pct=400),
            NutrientProfile(name="Potassium", amount=558, unit="mg", daily_value_pct=12),
        ],
        health_benefits=[
            "Supports red blood cell hemoglobin synthesis.",
            "Rich in dietary nitrates to promote endothelial blood pressure regulation.",
            "High folate content aids cell repair and homocysteine metabolism.",
        ],
        limitations=[
            "High oxalate content; consume with moderation if prone to kidney stones.",
            "High Vitamin K content interferes with anticoagulant blood thinners (e.g. Warfarin).",
        ],
        food_drug_interactions=["Warfarin", "Coumadin"],
        evidence_level=EvidenceLevel.HIGH,
        evidence_source="ICMR & WHO Global Nutrition Guidelines",
    ),
    "oats": FoodItem(
        food_id="oats",
        name="Rolled Oats & Steel-Cut Oats",
        category=FoodCategory.WHOLE_GRAINS,
        glycemic_index=55,
        nutrients=[
            NutrientProfile(name="Beta-Glucan Soluble Fiber", amount=4.0, unit="g", daily_value_pct=100),
            NutrientProfile(name="Magnesium", amount=138, unit="mg", daily_value_pct=33),
            NutrientProfile(name="Manganese", amount=3.6, unit="mg", daily_value_pct=150),
        ],
        health_benefits=[
            "Beta-glucan soluble fiber binds to bile acids, reducing LDL cholesterol absorption.",
            "Slow-digesting complex carbs improve insulin sensitivity and glycemic stability.",
            "Supports gut microbiome short-chain fatty acid (SCFA) production.",
        ],
        limitations=[
            "Consume unflavored varieties; avoid instant oats with high added sodium/sugar.",
        ],
        food_drug_interactions=[],
        evidence_level=EvidenceLevel.HIGH,
        evidence_source="USDA & AHA Cardiovascular Guidelines",
    ),
    "salmon": FoodItem(
        food_id="salmon",
        name="Wild Salmon & Cold-Water Fish",
        category=FoodCategory.LEAN_PROTEINS,
        glycemic_index=0,
        nutrients=[
            NutrientProfile(name="Omega-3 EPA/DHA", amount=2.2, unit="g", daily_value_pct=100),
            NutrientProfile(name="Protein", amount=22, unit="g", daily_value_pct=44),
            NutrientProfile(name="Vitamin D", amount=570, unit="IU", daily_value_pct=71),
        ],
        health_benefits=[
            "Omega-3 fatty acids lower serum triglyceride concentration.",
            "Reduces systemic vascular inflammation and arterial stiffness.",
            "Supports bone density and calcium metabolism via natural Vitamin D.",
        ],
        limitations=[
            "Choose low-mercury, wild-caught sources.",
        ],
        food_drug_interactions=[],
        evidence_level=EvidenceLevel.HIGH,
        evidence_source="AHA & WHO Omega-3 Lipid Guidelines",
    ),
    "walnuts": FoodItem(
        food_id="walnuts",
        name="Walnuts & Flaxseeds",
        category=FoodCategory.SEEDS_NUTS,
        glycemic_index=15,
        nutrients=[
            NutrientProfile(name="Alpha-Linolenic Acid (ALA)", amount=2.5, unit="g", daily_value_pct=100),
            NutrientProfile(name="Magnesium", amount=45, unit="mg", daily_value_pct=11),
        ],
        health_benefits=[
            "Plant-based omega-3 fatty acids improve HDL-to-LDL lipid ratios.",
            "Polyphenols protect vascular endothelium against oxidative stress.",
        ],
        limitations=[
            "Calorically dense; limit portion size to 28g (approx 7 whole walnuts) daily.",
        ],
        food_drug_interactions=[],
        evidence_level=EvidenceLevel.HIGH,
        evidence_source="ICMR National Nutrition Guidelines",
    ),
    "blueberries": FoodItem(
        food_id="blueberries",
        name="Blueberries & Dark Berries",
        category=FoodCategory.FRUITS,
        glycemic_index=53,
        nutrients=[
            NutrientProfile(name="Anthocyanins", amount=163, unit="mg", daily_value_pct=100),
            NutrientProfile(name="Vitamin C", amount=14, unit="mg", daily_value_pct=16),
            NutrientProfile(name="Dietary Fiber", amount=3.6, unit="g", daily_value_pct=14),
        ],
        health_benefits=[
            "Anthocyanin antioxidants neutralize reactive oxygen species (ROS).",
            "Improves postprandial glucose regulation and capillary resistance.",
        ],
        limitations=[
            "Consume whole fruits rather than juices to preserve dietary fiber.",
        ],
        food_drug_interactions=[],
        evidence_level=EvidenceLevel.HIGH,
        evidence_source="WHO Phytonutrient Clinical Database",
    ),
    "turmeric": FoodItem(
        food_id="turmeric",
        name="Turmeric (Curcumin) with Black Pepper",
        category=FoodCategory.HERBS_SPICES,
        glycemic_index=0,
        nutrients=[
            NutrientProfile(name="Curcuminoids", amount=200, unit="mg", daily_value_pct=100),
        ],
        health_benefits=[
            "Curcumin inhibits NF-kB inflammatory cascade.",
            "Piperine from black pepper increases curcumin bio-absorption by up to 2000%.",
        ],
        limitations=[
            "High supplemental doses may exacerbate gallstones or mild GERD.",
        ],
        food_drug_interactions=[],
        evidence_level=EvidenceLevel.HIGH,
        evidence_source="ICMR Phytotherapy Guidelines",
    ),
    "citrus": FoodItem(
        food_id="citrus",
        name="Oranges, Lemons & Amla (Indian Gooseberry)",
        category=FoodCategory.FRUITS,
        glycemic_index=40,
        nutrients=[
            NutrientProfile(name="Vitamin C (Ascorbic Acid)", amount=70, unit="mg", daily_value_pct=78),
        ],
        health_benefits=[
            "Ascorbic acid converts non-heme ferric iron (Fe3+) into ferrous iron (Fe2+), dramatically improving intestinal iron absorption.",
            "Supports collagen synthesis and arterial wall integrity.",
        ],
        limitations=[
            "Avoid consuming acidic fruits immediately before bedtime if prone to acid reflux.",
        ],
        food_drug_interactions=[],
        evidence_level=EvidenceLevel.HIGH,
        evidence_source="WHO Micronutrient Deficiency Guidelines",
    ),
}
