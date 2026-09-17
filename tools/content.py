# -*- coding: utf-8 -*-
"""
All website copy for IsabelleJosephDNP.com, transcribed from the supplied
content blueprints (Homepage, About, Services Hub, Tox, Hyperhidrosis,
Chemical Peels, GLP-1, HRT, Hair Loss) and the Sitemap + Team Guide.

Anything in [SQUARE BRACKETS] is a clearly-marked placeholder that still
needs to be supplied. Nothing medical or factual has been invented.
"""

BOOK_URL = "https://book.skinclique.com/webstoreNew/services/97d1c710-b934-4863-a258-42d8dce92b9c"
SHOP_URL = "https://shop.skinclique.com/?provider=97d1c710-b934-4863-a258-42d8dce92b9c"
SITE_URL = "https://isabellejosephdnp.com"
BRAND = "Isabelle Joseph, DNP"
BRAND_FULL = "Isabelle Joseph, DNP, NP-BC"
SERVICE_AREA = "South Easton, Norwell, Randolph, Somerset, Stoughton, Westwood + surrounding Massachusetts communities"
CONCIERGE_AREA_P = ("Isabelle is based in South Easton, Massachusetts and serves South Easton and "
                    "select surrounding communities, including Norwell, Randolph, Somerset, Stoughton, and Westwood.")

# ---------------------------------------------------------------- navigation
NAV = [
    ("About", "about"),
    ("Services", "services"),   # dropdown
    ("Skincare", "skincare"),
    ("The Isabelle Edit", "blog"),
]
SERVICE_GROUPS = [
    ("Aesthetics", [("Tox", "tox"), ("Hyperhidrosis", "hyperhidrosis"), ("Chemical Peels", "chemical-peels")]),
    ("Wellness", [("GLP-1 Weight Management", "weight-loss"),
                  ("Hormone Replacement Therapy", "hormone-replacement-therapy"),
                  ("Hair Loss", "hair-loss")]),
    ("Skin Health", [("Skincare", "skincare"), ("Skincare Consultations", "skincare-consultations")]),
]

# ---------------------------------------------------------------- pages
PAGES = {}

PAGES["index"] = dict(
    slug="", title="Concierge Aesthetics & Wellness | Isabelle Joseph, DNP",
    description="Discover personalized concierge aesthetics, wellness and skincare with Isabelle Joseph, DNP, NP-BC, serving South Easton and surrounding MA communities.",
    h1="Expert Care. Personalized to You. Delivered Where You Are.",
)

PAGES["about"] = dict(
    slug="about", title="Meet Isabelle Joseph, DNP, NP-BC | South Easton, MA",
    description="Meet Isabelle Joseph, DNP, NP-BC, a concierge aesthetics and wellness provider bringing personalized care to patients in South Easton, MA and surrounding communities.",
    h1="Meet Isabelle Joseph, DNP, NP-BC",
)

PAGES["services"] = dict(
    slug="services", title="Concierge Aesthetics & Wellness Services | Isabelle Joseph",
    description="Explore concierge aesthetics, wellness and skincare services with Isabelle Joseph, DNP, NP-BC, serving South Easton and surrounding Massachusetts communities.",
    h1="Concierge Aesthetics, Wellness + Skincare",
)

PAGES["skincare"] = dict(
    slug="skincare", title="Medical-Grade & Prescription Skincare | Isabelle Joseph, DNP",
    description="Skincare shouldn't be guesswork. Explore medical-grade and prescription skincare guidance with Isabelle Joseph, DNP, NP-BC, and shop her curated Skin Clique storefront.",
    h1="Skincare Shouldn't Be Guesswork.",
)

PAGES["skincare-consultations"] = dict(
    slug="skincare-consultations", title="Personalized Skincare Consultations | Isabelle Joseph, DNP",
    description="Stop guessing which products belong in your routine. Book a personalized skincare consultation with Isabelle Joseph, DNP, NP-BC.",
    h1="Personalized Skincare Consultations With Isabelle Joseph, DNP, NP-BC",
)

PAGES["faqs"] = dict(
    slug="faqs", title="Frequently Asked Questions | Isabelle Joseph, DNP",
    description="Answers to common questions about Tox, hyperhidrosis treatment, chemical peels, GLP-1 weight management, hormone replacement therapy and hair loss care with Isabelle Joseph, DNP, NP-BC.",
    h1="Frequently Asked Questions",
)

PAGES["blog"] = dict(
    slug="blog", title="The Isabelle Edit | Aesthetics, Skin + Wellness Education",
    description="The Isabelle Edit: straightforward education from Isabelle Joseph, DNP, NP-BC to help you better understand your options, your skin, and your health.",
    h1="The Isabelle Edit",
)

PAGES["book"] = dict(
    slug="book", title="Book With Isabelle | Isabelle Joseph, DNP, NP-BC",
    description="Book concierge aesthetic, wellness and skincare care with Isabelle Joseph, DNP, NP-BC. Appointments are scheduled securely through Skin Clique.",
    h1="Book With Isabelle",
)

# ---------------------------------------------------------------- service pages
# Each service page follows the reusable Service Page Template:
# hero -> overview -> addresses -> approach -> steps -> concierge -> candidates
# -> before/after -> faq -> related -> final CTA

SERVICES = {}

SERVICES["tox"] = dict(
    slug="tox", group="Aesthetics", name="Tox",
    title="Tox Treatments in South Easton, MA | Isabelle Joseph, DNP",
    description="Explore personalized concierge Tox treatments with Isabelle Joseph, DNP, NP-BC, serving South Easton and select surrounding Massachusetts communities.",
    h1="Tox Treatments With Isabelle Joseph, DNP, NP-BC",
    tagline="Look Refreshed. Still Look Like You.",
    intro=[
        "Fine lines are a natural part of expression—but sometimes they begin to linger even when your face is at rest.",
        "Tox treatments can temporarily soften the appearance of expression lines by relaxing targeted facial muscles, creating a smoother, refreshed appearance without changing what makes you look like you.",
        "Isabelle Joseph, DNP, NP-BC takes a personalized, thoughtful approach to Tox, considering your facial anatomy, natural movement, concerns, and goals before creating your treatment plan.",
        "And with concierge care, treatment comes to you.",
    ],
    hero_cta="Book Tox With Isabelle",
    hero_image=("tox-hero", "Editorial portrait — natural expression, warm light"),
    overview_h2="What Is Tox?",
    overview=[
        "Tox is an injectable treatment using a type of medication known as a neuromodulator.",
        "These medications work by temporarily reducing targeted muscle activity. When carefully placed in muscles responsible for repeated facial expressions, they can soften the appearance of dynamic lines and wrinkles.",
        "Skin Clique offers FDA-approved neurotoxins including Xeomin, Dysport, and Botox. The appropriate product, placement, and amount of treatment will depend on your individual needs and treatment plan.",
        "Isabelle will evaluate your facial movement, discuss what you'd like to accomplish, and help determine an approach designed specifically for you.",
    ],
    addresses_h2="What Can Tox Address?",
    addresses=[
        ("Forehead Lines", "Repeatedly raising your eyebrows can eventually create horizontal lines across the forehead. Strategically placed Tox can help soften these lines while preserving natural-looking facial expression."),
        ("Frown Lines", "The vertical lines that develop between the eyebrows are sometimes called “11s.” These lines can make you appear concerned, tired, or frustrated even when you don't feel that way. Tox can temporarily relax the muscles responsible for creating these expression lines."),
        ("Crow's Feet", "Smiling and squinting can create fine lines extending from the outer corners of the eyes. Tox can soften the appearance of these lines while allowing your smile to still look like your smile."),
        ("Neck + Jawline", "For appropriate patients, strategically placed Tox may be used to address visible neck bands and improve the appearance of the neck and jawline."),
        ("Lip Flip", "Small amounts of Tox placed around the upper lip can relax targeted muscles, allowing more of the upper lip to show when smiling. A lip flip does not add volume in the way dermal filler does."),
        ("Masseter Treatment", "Tox may also be used in the masseter muscles of the jaw. Depending on the patient's needs, treatment may help reduce muscle activity and can create a softer appearance through the lower face."),
    ],
    addresses_cta="Book a Tox Consultation",
    approach_eyebrow="Isabelle's Approach to Tox",
    approach_h2="Your Face Isn't a Formula.",
    approach=[
        "There isn't one perfect number of units or one injection pattern that works for everyone.",
        "Your facial anatomy, muscle movement, previous treatments, preferences, and goals all matter.",
        "Before treatment, Isabelle evaluates how your face moves and talks with you about what you're noticing and what you'd like to achieve.",
        "Her approach is centered on thoughtful placement and personalized treatment—not simply treating lines because they're there.",
        "The goal? To help you look refreshed while maintaining the expressions that make you look like you.",
    ],
    approach_image=("tox-approach", "Isabelle in consultation — detail crop"),
    steps_h2="What to Expect",
    steps=[
        ("Consultation + Assessment", "Your appointment begins with a conversation. Isabelle will review your goals, relevant medical history, previous treatments, and any concerns you have. She'll also evaluate your facial anatomy and muscle movement before recommending a personalized treatment plan."),
        ("Your Treatment", "Once your treatment plan is established, small amounts of neurotoxin are precisely injected into the targeted areas. The injections themselves are quick, and many patients describe them as feeling like a small pinch."),
        ("Results Develop", "Tox results aren't immediate. You may begin noticing changes within several days, with the treatment effect continuing to develop afterward. Results commonly last approximately three to four months, although individual experiences vary. Isabelle can help you determine an appropriate treatment schedule based on your response and goals."),
    ],
    concierge_eyebrow="Concierge Tox",
    concierge_h2="Your Appointment. Your Space.",
    concierge=[
        "Aesthetic care doesn't have to mean spending part of your day traveling to and waiting inside a traditional clinic.",
        "Isabelle provides concierge Tox treatments, bringing care directly to patients at home, at work, or another convenient location.",
        "That means you can receive personalized aesthetic care in a comfortable environment with a provider you know and trust.",
        CONCIERGE_AREA_P,
    ],
    candidates_h2="Is Tox Right for Me?",
    candidates_intro=[
        "Tox may be worth exploring if you're bothered by expression lines or are looking for a subtle aesthetic refresh.",
        "Potential candidates may include adults interested in addressing concerns such as:",
    ],
    candidates=["Forehead lines", "Frown lines between the eyebrows", "Crow's feet", "Certain neck or jawline concerns", "A lip flip", "Masseter treatment", "Preventative treatment of dynamic expression lines"],
    candidates_outro=[
        "Tox isn't appropriate for everyone.",
        "Your medical history, medications, pregnancy or breastfeeding status, allergies, neuromuscular conditions, skin condition at the treatment site, and other individual factors may affect whether treatment is appropriate.",
        "Your consultation with Isabelle is the place to discuss these considerations and determine whether Tox makes sense for you.",
    ],
    before_h2="Before Your Tox Appointment",
    before=[
        "Your medical provider will give you individualized instructions based on your health history and treatment plan.",
        "Before your appointment, make sure Isabelle knows about your medications, supplements, medical conditions, allergies, previous neuromodulator treatments, and any prior complications with injectable treatments.",
        "If you take prescribed medications, including medications that affect bleeding or clotting, do not stop them unless instructed to do so by the clinician who prescribed them.",
        "You'll also receive any applicable Skin Clique pre-treatment instructions before your appointment.",
    ],
    faq_h2="Tox Frequently Asked Questions",
    faq=[
        ("Will Tox make me look frozen?", "The goal of Isabelle's approach is natural-looking treatment—not removing every bit of facial movement. Treatment is personalized according to your anatomy, movement, and goals. Talk with Isabelle about how much movement you'd like to maintain so she can incorporate your preferences into your treatment plan."),
        ("When will I see my results?", "Tox doesn't work immediately. Many patients begin noticing an effect within several days, with results continuing to develop during the days following treatment."),
        ("How long does Tox last?", "Results commonly last approximately three to four months, although this varies by patient, treatment area, product, dose, and individual response."),
        ("Does getting Tox hurt?", "Most patients describe the injections as brief and similar to a small pinch. Let Isabelle know if you're particularly concerned about discomfort so you can discuss what to expect before treatment begins."),
        ("Is there downtime?", "Most patients can return to many of their normal daily activities after treatment. Follow the specific post-treatment instructions provided by Isabelle and Skin Clique, as certain activities may need to be temporarily avoided."),
        ("What's the difference between Botox, Dysport, and Xeomin?", "Botox, Dysport, and Xeomin are different brands of botulinum toxin products used to temporarily reduce targeted muscle activity. They are not identical products, and dosing is not interchangeable. Isabelle can discuss the available options and determine which treatment is appropriate for your individual needs."),
        ("What's the difference between Tox and filler?", "They work differently. Tox temporarily reduces targeted muscle activity and is commonly used for dynamic expression lines. Dermal fillers are injectable products designed to add or restore volume in targeted areas. Your provider can help determine which type of treatment aligns with the concern you'd like to address."),
        ("Am I too young—or too old—for Tox?", "There isn't one universal age when someone should begin Tox. The decision should be based on your individual concerns, facial movement, health history, goals, and whether treatment is appropriate for you—not simply your age."),
        ("Can I receive Tox while pregnant or breastfeeding?", "Neurotoxin treatment is generally not recommended during pregnancy or breastfeeding. Always tell Isabelle if you are pregnant, breastfeeding, planning a pregnancy, or if there have been changes to your health before receiving treatment."),
    ],
    related=[
        ("Tox + Your Skincare Routine", [
            "Injectable treatments and skincare address different aspects of how your skin looks and feels.",
            "While Tox targets specific muscle activity, a personalized skincare routine can help address concerns involving skin tone, texture, pigmentation, hydration, and overall skin health.",
            "Isabelle can help you look at the bigger picture and determine whether your aesthetic treatment plan could benefit from changes to your at-home skincare routine.",
        ], ("Explore Skincare", "skincare")),
        ("Want to Make Tox a Group Experience?", [
            "For patients who enjoy receiving treatments with friends, Skin Clique also offers qualifying group Tox experiences.",
            "Ask Isabelle about current group options, eligibility, and Skin Clique group pricing if you're interested in hosting an aesthetic event at your home or another appropriate location.",
        ], ("Ask About Group Tox", "book")),
    ],
    notsure_h2="Not Sure If Tox Is What You Need?",
    notsure=[
        "You don't have to diagnose your concern or decide how many units you need before scheduling.",
        "Start with what you're noticing.",
        "Isabelle can evaluate your concerns, answer your questions, and help determine whether Tox—or another option—best aligns with your goals.",
    ],
    final_h2="A More Personal Approach to Aesthetics",
    final=["Natural-looking aesthetic care starts with understanding the person receiving it.",
           "Experience personalized, concierge Tox treatment with Isabelle Joseph, DNP, NP-BC."],
    final_cta="Book Tox With Isabelle",
)

SERVICES["hyperhidrosis"] = dict(
    slug="hyperhidrosis", group="Aesthetics", name="Hyperhidrosis",
    title="Hyperhidrosis Treatment in South Easton, MA | Isabelle Joseph",
    description="Explore concierge treatment for excessive sweating of the underarms, palms and feet with Isabelle Joseph, DNP, NP-BC in South Easton, MA.",
    h1="Hyperhidrosis Treatment With Isabelle Joseph, DNP, NP-BC",
    tagline="Sweat Less. Worry About It Less.",
    intro=[
        "Choosing clothes based on whether they'll show sweat. Keeping an extra shirt nearby. Avoiding handshakes because your palms are damp. Worrying about sweating through an important meeting, event, or everyday activity.",
        "For people living with excessive sweating, these small decisions can become a regular part of life.",
        "Hyperhidrosis is more than simply “sweating a lot.” It's a condition in which the body produces more sweat than is necessary for temperature regulation—and treatment options are available.",
        "Isabelle Joseph, DNP, NP-BC provides personalized hyperhidrosis treatment using targeted neurotoxin injections designed to temporarily reduce excessive sweating. And with concierge care, treatment comes to you.",
    ],
    hero_cta="Book Hyperhidrosis Treatment",
    hero_image=("hyperhidrosis-hero", "Calm lifestyle image — linen, movement, ease"),
    overview_h2="What Is Hyperhidrosis?",
    overview=[
        "Sweating is normal. It's one of the ways your body regulates temperature. Hyperhidrosis is different.",
        "People with hyperhidrosis experience excessive sweating that goes beyond what the body needs for normal temperature regulation. It may occur even when you aren't exercising, aren't overheated, or don't have an obvious reason to be sweating.",
        "For some people, excessive sweating is an inconvenience. For others, it can affect clothing choices, work, social situations, exercise, confidence, and everyday comfort.",
        "If excessive sweating has become something you constantly think about or plan around, it's worth having a conversation about your options.",
    ],
    addresses_h2="Where Can Excessive Sweating Occur?",
    addresses=[
        ("Underarms", "Excessive underarm sweating can soak through clothing regardless of temperature or activity level. Treatment can help temporarily reduce sweat production in the targeted area."),
        ("Palms", "Excessively sweaty hands can affect everything from holding objects and using electronics to writing, working, and shaking someone's hand. Targeted treatment may help reduce sweat production in the palms."),
        ("Soles of the Feet", "Excessive sweating of the feet can contribute to persistent dampness and discomfort inside socks and shoes. For appropriate patients, targeted neurotoxin treatment may help reduce excessive sweating in the soles of the feet."),
    ],
    addresses_cta="Talk to Isabelle About Excessive Sweating",
    extra_after_addresses=[
        ("How Does Hyperhidrosis Treatment Work?", "The Same Type of Medication. A Different Goal.", [
            "You may already be familiar with neurotoxins such as Botox, Dysport, or Xeomin because of their use in aesthetic treatments. For hyperhidrosis, neurotoxin is used differently.",
            "Rather than targeting muscles responsible for facial expression, small amounts of medication are strategically injected into the treatment area to temporarily block the chemical signals that activate sweat glands. When those signals are reduced, the treated sweat glands produce less sweat.",
            "The treatment is localized, meaning it targets excessive sweating in the specific area being treated rather than preventing your body from sweating everywhere.",
        ]),
        ("This Isn't About Never Sweating Again", "It's About Reducing Excessive Sweating.", [
            "Sweating serves an important purpose. The goal of hyperhidrosis treatment isn't to prevent your body from regulating its temperature or eliminate normal sweating throughout your body.",
            "Instead, treatment targets sweat glands within a specific problem area. Your body can continue regulating temperature and producing sweat in untreated areas.",
            "The goal is simply to reduce the excessive sweating that's interfering with your everyday life.",
        ]),
    ],
    approach_eyebrow="Isabelle's Approach to Hyperhidrosis",
    approach_h2="Treat the Concern, Not Just the Symptom on a Checklist.",
    approach=[
        "Excessive sweating can be uncomfortable to talk about. It can also be frustrating when you've tried stronger antiperspirants, changed your clothes, adjusted your routine, or simply learned to live around the problem.",
        "Isabelle approaches hyperhidrosis the same way she approaches all of her care: by starting with you.",
        "She'll ask about what you're experiencing, where the sweating occurs, how long it has been happening, how it affects your daily life, and relevant aspects of your medical history. That conversation helps determine whether neurotoxin treatment may be appropriate or whether your symptoms should be evaluated further.",
        "No embarrassment. No judgment. Just a straightforward conversation about what's happening and what options may be available.",
    ],
    approach_image=("hyperhidrosis-approach", "Isabelle listening — one-on-one consultation"),
    steps_h2="What to Expect From Hyperhidrosis Treatment",
    steps=[
        ("Consultation + Assessment", "Your appointment begins with a conversation about your symptoms. Isabelle will review the areas affected, your health history, medications, previous treatments, and other relevant factors before determining whether treatment is appropriate."),
        ("Identify the Treatment Area", "The area of excessive sweating will be evaluated so treatment can be appropriately planned. The number and placement of injections depend on the area being treated and your individual needs."),
        ("Treatment", "Small amounts of neurotoxin are injected at multiple points throughout the treatment area. Because areas such as the palms and soles can be more sensitive than the underarms, the treatment experience may differ depending on the location. Isabelle will discuss what you can expect before treatment begins."),
        ("Results Develop", "The reduction in sweating develops after treatment rather than occurring immediately. As the neurotoxin begins blocking the signals responsible for activating the treated sweat glands, patients may notice a significant reduction in sweating in the targeted area. Results are temporary and may last for several months. Individual results and treatment duration vary."),
    ],
    concierge_eyebrow="Concierge Hyperhidrosis Treatment",
    concierge_h2="Private Care in a Comfortable Setting",
    concierge=[
        "For something as personal as excessive sweating, receiving care in your own environment can make the experience feel much easier.",
        "Isabelle provides concierge treatment in your home, office, or another appropriate location. You receive one-on-one care without a traditional waiting room and without having to fit another clinic visit into an already busy day.",
        CONCIERGE_AREA_P,
    ],
    candidates_h2="Is Hyperhidrosis Treatment Right for Me?",
    candidates_intro=[
        "Neurotoxin treatment may be worth exploring if excessive sweating is persistent, bothersome, or interfering with your daily activities.",
        "You may want to talk with Isabelle if you experience:",
    ],
    candidates=["Excessive underarm sweating", "Excessively sweaty palms", "Excessive sweating of the feet", "Sweating that occurs even when you aren't hot or exercising", "Sweat that frequently soaks through clothing", "Sweating that affects work, social activities, or confidence", "Symptoms that haven't responded adequately to your current approach"],
    candidates_outro=[
        "Not all excessive sweating is primary hyperhidrosis. In some cases, increased sweating can be associated with medications, hormonal changes, medical conditions, or other underlying factors. That's one reason an appropriate medical assessment matters.",
        "Isabelle can review your symptoms and health history and determine whether treatment is appropriate or whether additional evaluation may be needed.",
    ],
    before_h2="Before Your Hyperhidrosis Appointment",
    before_intro="Before treatment, make sure Isabelle knows about:",
    before_list=["Your current medications and supplements", "Medical conditions", "Allergies", "Previous neurotoxin treatments", "Previous reactions or complications from injectable treatments", "Neuromuscular conditions", "Skin irritation, infection, or wounds in the treatment area", "Pregnancy or breastfeeding", "Any recent changes in your health", "When the excessive sweating began and whether it has changed over time"],
    before=[
        "Do not stop prescribed medications unless instructed to do so by the clinician who prescribed them.",
        "Isabelle will provide any additional pre-treatment instructions specific to your treatment area.",
    ],
    after_h2="After Hyperhidrosis Treatment",
    after=[
        "Recovery recommendations can vary depending on the treatment area. You may experience temporary redness, tenderness, swelling, bruising, or discomfort at injection sites.",
        "Follow the individualized post-treatment instructions provided by Isabelle and Skin Clique. If you have questions or experience unexpected symptoms following treatment, contact your medical provider for guidance.",
    ],
    faq_h2="Hyperhidrosis Frequently Asked Questions",
    faq=[
        ("How do I know if I sweat “too much”?", "There isn't a single amount of sweat that defines every patient's experience. One important question is whether sweating seems excessive for the situation and whether it regularly interferes with your comfort or daily activities. If you're constantly planning around sweat, changing clothing because of it, or avoiding situations because of it, it's reasonable to discuss your symptoms with a medical provider."),
        ("Is hyperhidrosis just caused by anxiety?", "No. Stress or anxiety can trigger sweating, but hyperhidrosis can occur even without those triggers. Some patients experience excessive sweating during ordinary daily activities or even while resting. Because increased sweating can have different causes, your individual symptoms should be evaluated rather than automatically attributed to anxiety."),
        ("How does Tox stop sweating?", "Neurotoxin temporarily blocks the chemical signals that tell the targeted sweat glands to produce sweat. By interrupting those signals in the treated area, sweat production can be significantly reduced."),
        ("Will I stop sweating everywhere?", "No. Treatment is targeted to specific areas. Your body continues to sweat from untreated areas and retains its ability to regulate temperature."),
        ("Which areas can Isabelle treat?", "Skin Clique offers hyperhidrosis treatment for excessive sweating involving the underarms, palms, and soles of the feet. Isabelle can determine whether your specific area of concern is appropriate for treatment."),
        ("Does hyperhidrosis treatment hurt?", "Treatment involves multiple small injections throughout the affected area. Discomfort varies depending on the individual and treatment location. The palms and soles can be particularly sensitive, so discuss any concerns about discomfort with Isabelle before treatment."),
        ("When will I notice less sweating?", "Results develop gradually following treatment rather than immediately. Your individual response may vary, and Isabelle can discuss what to expect based on the area being treated."),
        ("How long does hyperhidrosis treatment last?", "The effects are temporary but may last for several months. Treatment duration varies from person to person, and repeat treatment may be appropriate once the effects begin to wear off."),
        ("Is there downtime?", "Many patients can return to normal activities relatively quickly, although recommendations can vary depending on the area treated. Follow Isabelle's specific aftercare instructions."),
        ("Will I sweat more somewhere else?", "Neurotoxin treatment targets the sweat glands within the treated area rather than redirecting sweat to another part of the body. Your untreated sweat glands continue to function normally."),
        ("Is hyperhidrosis treatment the same as cosmetic Tox?", "The medication may be the same type of neurotoxin used for aesthetic Tox, but the treatment goal, injection pattern, location, and dosing are different. Cosmetic Tox targets specific muscles to reduce movement associated with expression lines. Hyperhidrosis treatment targets the nerve signals responsible for activating sweat glands."),
        ("Can I receive treatment while pregnant or breastfeeding?", "Neurotoxin treatment is generally not recommended during pregnancy or breastfeeding. Tell Isabelle if you are pregnant, breastfeeding, planning a pregnancy, or if your health status has changed before treatment."),
    ],
    related=[
        ("When Is It Worth Asking for Help?", [
            "Everyone sweats. Exercise, heat, stress, and certain situations can naturally increase perspiration.",
            "Hyperhidrosis becomes different when sweating is excessive compared with what the body needs and begins interfering with daily life. You don't need to wait until the problem feels “severe enough” to ask about it.",
            "If sweating is bothering you, that's enough reason to start the conversation.",
        ], ("Book a Hyperhidrosis Consultation", "book")),
        ("What If Something Else Is Causing My Sweating?", [
            "Excessive sweating can sometimes occur secondary to another medical issue or medication.",
            "If your sweating began suddenly, occurs primarily at night, affects your entire body, or is accompanied by other unexplained symptoms, additional medical evaluation may be appropriate.",
            "Hyperhidrosis treatment should begin with understanding what you're experiencing—not simply treating the sweat. Isabelle can help determine the appropriate next step based on your individual history and symptoms.",
        ], ("Explore Tox", "tox")),
    ],
    notsure_h2="You Don't Have to Plan Your Life Around Sweat",
    notsure=[
        "If excessive sweating has become part of how you choose clothes, approach work, interact socially, exercise, or move through everyday life, it's worth learning about your options.",
        "Start with a conversation. Isabelle can help determine whether hyperhidrosis treatment may be appropriate for you and answer your questions about what to expect.",
    ],
    final_h2="Ready to Sweat Less?",
    final=["Experience personalized, concierge hyperhidrosis care with Isabelle Joseph, DNP, NP-BC."],
    final_cta="Book Hyperhidrosis Treatment With Isabelle",
)

SERVICES["chemical-peels"] = dict(
    slug="chemical-peels", group="Aesthetics", name="Chemical Peels",
    title="Chemical Peels in South Easton, MA | Isabelle Joseph, DNP",
    description="Explore personalized concierge chemical peels with Isabelle Joseph, DNP, NP-BC for concerns including dullness, texture, pigmentation and congested skin.",
    h1="Chemical Peels With Isabelle Joseph, DNP, NP-BC",
    tagline="Reveal Brighter, Smoother, More Even-Looking Skin",
    intro=[
        "Sometimes even a great skincare routine needs a little help.",
        "If your skin feels dull, uneven, congested, or simply isn't responding the way you'd like to your current routine, a professional chemical peel may help give your skin the reset it needs.",
        "Chemical peels use carefully selected solutions to exfoliate damaged surface layers of the skin and encourage cellular renewal, helping reveal fresher, smoother-looking skin underneath.",
        "Isabelle Joseph, DNP, NP-BC personalizes each treatment based on your skin, your concerns, and your goals—because the right peel isn't the same for everyone. And with concierge care, your treatment comes to you.",
    ],
    hero_cta="Book a Chemical Peel With Isabelle",
    hero_image=("peels-hero", "Skin texture / natural skin editorial close-up"),
    overview_h2="What Is a Chemical Peel?",
    overview=[
        "A chemical peel is a professional skin-resurfacing treatment that uses a carefully selected solution to exfoliate the skin.",
        "Different peel formulations and strengths work at different depths, which means treatment can be customized according to your skin type, concerns, previous treatments, and desired level of correction and downtime.",
        "Rather than simply choosing a peel from a menu, Isabelle evaluates your skin and helps determine which approach is appropriate for you. The goal is controlled exfoliation that supports skin renewal while addressing the concerns that matter most to you.",
    ],
    addresses_h2="What Can Chemical Peels Help Address?",
    addresses=[
        ("Hyperpigmentation + Dark Spots", "Sun exposure, hormonal changes, inflammation, and previous breakouts can leave areas of unwanted pigmentation behind. Chemical peels may help improve the appearance of certain dark spots, post-inflammatory marks, melasma, and uneven pigmentation by accelerating cellular turnover. Because pigmentation can have different causes—and some skin types require additional precautions—Isabelle will evaluate your skin before recommending treatment."),
        ("Acne + Congestion", "Clogged pores, breakouts, and lingering post-acne marks can make skin feel difficult to manage. Certain peel formulations may help exfoliate the skin, clear congestion, and support cellular turnover as part of a broader acne-focused skincare plan."),
        ("Dullness + Uneven Texture", "When dead surface cells accumulate, skin can begin to look dull or feel rough. A chemical peel can remove damaged surface cells and reveal fresher-looking skin underneath, helping improve the appearance of overall tone and texture."),
        ("Fine Lines + Visible Signs of Aging", "As skin changes with age and environmental exposure, fine lines, uneven texture, and loss of radiance can become more noticeable. Chemical peels may help soften the appearance of superficial fine lines and support smoother, brighter-looking skin."),
    ],
    addresses_cta="Book a Skin Consultation",
    extra_after_addresses=[
        ("Not Every Peel Is the Same", "Your Skin Determines the Treatment.", [
            "Chemical peels aren't one-size-fits-all. Different formulations may contain ingredients such as glycolic, salicylic, mandelic, TCA, or combinations of active ingredients. The appropriate formulation and strength depend on several factors, including your skin type, concerns, treatment history, and goals.",
            "That's why your skin assessment matters. Isabelle will evaluate your skin and determine which available peel option is appropriate rather than choosing treatment based solely on what's trending or what worked for someone else.",
            "Your treatment should fit your skin—not the other way around.",
        ]),
    ],
    approach_eyebrow="Isabelle's Approach to Chemical Peels",
    approach_h2="Thoughtful Skin Treatment Starts With Understanding Your Skin",
    approach=[
        "Isabelle's approach to skin health isn't about doing the strongest treatment possible. It's about choosing the right treatment.",
        "Before recommending a chemical peel, Isabelle considers what you're experiencing, what products you're currently using, your previous treatments, your skin type, and what you'd ultimately like to improve. She'll also help you understand what kind of recovery to expect and how a peel fits into your broader skincare plan.",
        "For some patients, that may mean an individual treatment. For others, a planned series of treatments combined with an appropriate at-home routine may make more sense. The plan is personalized to you.",
    ],
    approach_image=("peels-approach", "Skincare products on linen — editorial still life"),
    steps_h2="What to Expect From Your Chemical Peel",
    steps=[
        ("Skin Assessment", "Your appointment begins with an evaluation of your skin, current concerns, skincare routine, relevant medical history, and treatment goals. This helps Isabelle determine whether a chemical peel is appropriate and which available formulation and strength best fit your needs."),
        ("Skin Preparation", "Your skin will be carefully cleansed and prepared for treatment. Depending on the peel selected and your existing skincare routine, you may also receive instructions to modify certain products before your appointment."),
        ("Peel Application", "The selected peel solution is applied carefully to the treatment area. The application process and number of layers will depend on the treatment selected. You may experience sensations such as warmth or tingling during treatment."),
        ("Recovery + Renewal", "What happens afterward depends on the depth of your peel. Some lighter treatments may produce little or no visible peeling, while other peels can result in several days of dryness, flaking, or visible peeling. Your skin may continue to improve after the visible recovery period as the renewal process continues. Isabelle will explain what you can expect from your specific treatment and provide appropriate aftercare instructions."),
    ],
    extra_after_steps=[
        ("Will My Skin Actually Peel?", None, [
            "Maybe—and that's completely dependent on the treatment.",
            "One of the biggest misconceptions about chemical peels is that your skin must dramatically peel for the treatment to be effective. That's not necessarily true. Lighter peels may cause minimal or no visible flaking. Other formulations may result in more noticeable peeling for several days.",
            "The amount of visible peeling isn't the measure of whether you received a “good” treatment. The goal is to select an appropriate treatment for your skin and the concern you're trying to address—not to create the most dramatic recovery possible.",
        ]),
        ("How Many Chemical Peels Will I Need?", None, [
            "There isn't one answer for everyone. Some patients may benefit from an individual peel, while others may achieve their goals through a planned series of treatments.",
            "Skin Clique currently offers both individual peels and peel series, with series commonly spaced approximately four to six weeks apart. Isabelle can recommend an appropriate treatment schedule based on your skin, response to treatment, and goals.",
        ]),
    ],
    concierge_eyebrow="Concierge Chemical Peels",
    concierge_h2="Professional Skin Care—Without the Traditional Waiting Room",
    concierge=[
        "Your skin treatment doesn't have to mean adding another trip across town to your schedule.",
        "Through her concierge model, Isabelle brings professional aesthetic care directly to you at your home, office, or another appropriate location. You'll receive personalized one-on-one care in a setting designed around your comfort and convenience.",
        CONCIERGE_AREA_P,
    ],
    candidates_h2="Is a Chemical Peel Right for Me?",
    candidates_intro=["Chemical peels may be worth exploring if you're concerned about:"],
    candidates=["Uneven skin tone", "Sun damage", "Hyperpigmentation or dark spots", "Post-acne marks", "Dullness", "Rough or uneven texture", "Congested pores", "Certain types of acne", "Superficial fine lines", "Overall skin radiance"],
    candidates_outro=[
        "Chemical peels aren't appropriate for everyone, and not every peel is appropriate for every skin type. Your medical history, current skin condition, medications, skincare products, pregnancy or breastfeeding status, recent procedures, history of cold sores, sun exposure, and other factors may affect whether or how you should be treated. Isabelle will review these considerations before recommending a peel.",
        "Customization matters across skin tones. Chemical peels can be used across a range of skin tones, but selecting the appropriate formulation and treatment depth is especially important. Certain skin types may have a greater risk of unwanted pigment changes following aggressive treatment. Isabelle evaluates your individual skin characteristics and chooses an appropriate approach based on your skin—not a universal treatment protocol.",
    ],
    before_h2="Before Your Chemical Peel",
    before_intro="Preparation can be an important part of a successful chemical peel. Before treatment, tell Isabelle about:",
    before_list=["Prescription and over-the-counter skincare products you use", "Retinoids such as tretinoin or retinol", "Acne medications", "Recent aesthetic treatments", "Current medications and supplements", "Allergies", "History of cold sores", "Pregnancy or breastfeeding", "Recent sun exposure or sunburn", "Any active irritation, wounds, or infection"],
    before=[
        "Certain skincare products may need to be temporarily paused before treatment. Do not stop a prescribed medication or prescription skincare product unless instructed by the appropriate medical provider.",
        "Isabelle will provide specific preparation instructions based on the peel selected and your individual skincare regimen.",
    ],
    after_h2="After Your Chemical Peel",
    after=[
        "Your aftercare will depend on the depth and formulation of your treatment. In general, your skin may temporarily feel dry, tight, sensitive, or begin to flake.",
        "During recovery, it is especially important to follow the instructions provided by Isabelle, protect your skin from sun exposure, and avoid picking or manually removing peeling skin. Your regular skincare routine may also need to be temporarily modified while your skin recovers. Isabelle will tell you when it's appropriate to restart active ingredients and other products.",
    ],
    faq_h2="Chemical Peel Frequently Asked Questions",
    faq=[
        ("Does a chemical peel hurt?", "Most patients experience some degree of warmth, tingling, or stinging while the peel is being applied. The sensation varies depending on the formulation and treatment depth. Isabelle will talk you through what to expect from the peel selected for you."),
        ("How much downtime should I expect?", "Downtime varies. Some lighter peels may cause little visible peeling, while other treatments may result in approximately three to five days of flaking or peeling. Your expected recovery will be discussed before treatment."),
        ("When will I see results?", "You may begin noticing improvements as your skin completes the initial recovery process. Skin can continue to look and feel different over the following weeks as renewal continues. Results vary based on the treatment selected, your skin, and the concern being addressed."),
        ("How often can I get a chemical peel?", "Treatment frequency depends on the type and depth of peel. Some light-to-medium peels may be performed approximately every four to six weeks as part of a treatment series, while deeper treatments require more time between sessions. Isabelle will recommend an appropriate schedule for you."),
        ("Can I use retinol or tretinoin before a chemical peel?", "Certain retinoids and other active skincare ingredients may need to be temporarily paused before and after treatment. Exactly when you should stop and restart a product depends on what you're using and the peel you're receiving. Follow Isabelle's individualized instructions rather than stopping prescription skincare on your own."),
        ("Are chemical peels safe for darker skin tones?", "Chemical peels may be appropriate for a variety of skin tones when the formulation and treatment depth are selected carefully. Because the risk of unwanted pigment changes can differ among patients, an individualized skin assessment is important."),
        ("Can I get a chemical peel while pregnant or breastfeeding?", "Certain chemical peel ingredients may not be recommended during pregnancy or breastfeeding. Tell Isabelle if you are pregnant, breastfeeding, trying to become pregnant, or if your health status has changed so she can determine which options, if any, are appropriate."),
        ("Can chemical peels help acne?", "Certain chemical peel formulations may be helpful for some patients with clogged pores, acne, or post-acne marks. Acne can have multiple causes, however, so treatment should be individualized. Isabelle can help determine whether a peel, prescription skincare, changes to your home routine, or another approach may be appropriate."),
        ("Will a stronger peel give me better results?", "Not necessarily. The best peel is the one that appropriately matches your skin, concern, goals, and tolerance for recovery. A stronger treatment isn't automatically a better treatment."),
    ],
    related=[
        ("What You Do Between Treatments Matters.", [
            "A chemical peel can be an important part of a skin-health plan, but professional treatments are only one piece of the picture. Your everyday skincare routine plays an important role in protecting your skin and supporting your goals between appointments.",
            "Isabelle can help you determine which cleansers, antioxidants, moisturizers, retinoids, pigment-focused products, and sun protection may make sense for your individual skin. If your current routine feels complicated—or simply isn't working—this can also be a good opportunity to simplify it.",
        ], ("Explore Skincare", "skincare")),
        ("Chemical Peel Packages + Group Experiences", [
            "For patients who may benefit from multiple treatments, Skin Clique offers chemical peel packages in addition to individual treatments. Rather than deciding in advance that you need a package, start with your skin. Package availability and pricing can change, so ask Isabelle about current Skin Clique options when booking.",
            "Chemical peels may also be available as part of qualifying Skin Clique group experiences. If you're interested in hosting an aesthetic event at your home, office, or another appropriate space, ask Isabelle about current group options and requirements.",
        ], ("Ask About Chemical Peel Options", "book")),
    ],
    notsure_h2="Not Sure What Your Skin Needs?",
    notsure=[
        "You don't need to arrive knowing which peel, ingredient, or treatment you need. Start with your skin.",
        "Tell Isabelle what you're noticing, what you've tried, and what you'd like to improve. She can help you understand your options and determine whether a chemical peel—or another approach—makes sense for you.",
    ],
    final_h2="Ready to Reveal Healthier-Looking Skin?",
    final=["Experience personalized, concierge skin care with Isabelle Joseph, DNP, NP-BC."],
    final_cta="Book a Chemical Peel With Isabelle",
)

SERVICES["weight-loss"] = dict(
    slug="weight-loss", group="Wellness", name="GLP-1 Weight Management",
    title="GLP-1 Weight Management | Isabelle Joseph, DNP",
    description="Explore medically supervised GLP-1 weight management with Isabelle Joseph, DNP, NP-BC, including personalized treatment and ongoing provider support.",
    h1="GLP-1 Weight Management With Isabelle Joseph, DNP, NP-BC",
    tagline="Weight Management Is More Than Willpower.",
    intro=[
        "If you've spent years trying to lose weight only to feel like you're constantly fighting hunger, cravings, or weight regain, you aren't alone. Weight is influenced by much more than simply eating less and exercising more.",
        "For appropriate patients, GLP-1 medications can be one tool in a medically guided approach to weight management.",
        "With Isabelle Joseph, DNP, NP-BC, treatment isn't simply about receiving a prescription. It's about having a dedicated medical provider who understands your goals, monitors your progress, answers your questions, and adjusts your plan as your needs change.",
    ],
    hero_cta="Get Started With Isabelle",
    hero_image=("glp1-hero", "Wellness lifestyle — movement, light, calm"),
    overview_h2="What Are GLP-1 Medications?",
    overview=[
        "GLP-1 medications work with biological pathways involved in appetite, fullness, blood sugar regulation, and digestion.",
        "By affecting these signals, GLP-1 therapy may help appropriate patients experience reduced appetite and cravings, feel satisfied with smaller amounts of food, and make sustainable changes easier to maintain. Some medications target the GLP-1 pathway alone, while others target both GLP-1 and another hormone pathway known as GIP.",
        "These are prescription medications and aren't appropriate for everyone. That's why treatment should begin with a medical evaluation—not simply choosing a medication online.",
    ],
    extra_before_addresses=[
        ("A Different Approach to Weight Management", "Less Judgment. More Understanding.", [
            "Weight management can become frustrating when every solution seems to come back to the same message: Eat less. Move more. Try harder. But appetite and weight regulation involve complex biological, behavioral, environmental, and health factors.",
            "GLP-1 medications don't replace healthy habits. For appropriate patients, they may make it easier to build those habits by addressing some of the biological signals that can make weight management difficult.",
            "Isabelle's role is to help you understand the medical options available and develop a plan that fits your health, goals, and individual response to treatment.",
        ]),
    ],
    addresses_h2="How Can GLP-1 Therapy Help?",
    addresses=[
        ("Reduced Appetite", "GLP-1 medications can affect the signals involved in hunger and fullness, which may help reduce appetite."),
        ("Fewer Cravings", "Some patients report that persistent thoughts about food and cravings become easier to manage during treatment."),
        ("Feeling Satisfied With Less", "Changes in appetite and digestion may help patients feel satisfied after eating smaller portions."),
        ("Sustainable Habit Changes", "When hunger and cravings feel more manageable, it may become easier to focus on nutrition, movement, sleep, and other habits that support long-term health."),
        ("Clinically Meaningful Weight Loss", "Clinical studies of GLP-1 and GLP-1/GIP medications have demonstrated meaningful average weight loss in appropriate patients. Individual results vary significantly based on the medication, dose, health history, adherence, nutrition, activity, and other factors. Your results are your own—not a guaranteed percentage or number on a scale."),
    ],
    addresses_cta="Explore GLP-1 Treatment With Isabelle",
    options_h2="Medication Options",
    options_sub="Your Treatment Should Be Based on You.",
    options_intro="Skin Clique currently offers several approaches to GLP-1-based weight management. Depending on medical appropriateness and availability, options may include:",
    options=[
        ("Semaglutide", "Semaglutide is a GLP-1 receptor agonist that may help regulate appetite and support weight management. Skin Clique currently offers compounded semaglutide options as part of its medically supervised program."),
        ("Tirzepatide", "Tirzepatide targets both GLP-1 and GIP pathways involved in appetite and metabolic regulation. Skin Clique currently offers compounded tirzepatide options for appropriate patients."),
        ("Name-Brand Medications", "Depending on your individual situation, prescription options may also include name-brand medications available through a local pharmacy. Availability, eligibility, insurance coverage, medication cost, and pharmacy requirements can vary."),
        ("Lower-Dose Options", "Skin Clique also currently offers lower-dose approaches for certain patients. Isabelle can help you understand the available options and determine which approach, if any, is medically appropriate for you."),
    ],
    options_note="Medication availability, formulations, and pricing may change. Current options should always be confirmed during the Skin Clique intake and consultation process.",
    approach_eyebrow="Isabelle's Approach to Weight Management",
    approach_h2="You're More Than a Number on the Scale.",
    approach=[
        "Isabelle believes effective wellness care starts by understanding the person—not simply recording a weight.",
        "Your health history matters. Your previous experiences with weight loss matter. Your relationship with food matters. Your lifestyle, medications, goals, challenges, and concerns matter.",
        "Rather than handing you a prescription and sending you on your way, Isabelle provides ongoing clinical support throughout treatment. Together, you'll evaluate how you're responding, discuss challenges and side effects, monitor progress, and adjust the treatment plan when medically appropriate.",
        "The goal isn't perfection. It's creating an approach that can realistically work in your life.",
    ],
    approach_image=("glp1-approach", "Isabelle — portrait, warm and direct"),
    steps_h2="What to Expect",
    steps=[
        ("Complete Your Intake", "You'll begin by completing Skin Clique's health questionnaire. This gives Isabelle important information about your medical history, medications, health concerns, previous weight-management experiences, and goals."),
        ("Meet With Your Provider", "You'll connect with Isabelle for a medical consultation. She'll review your information, discuss your goals and concerns, and determine whether prescription weight-management treatment may be appropriate. Not every patient will qualify for GLP-1 treatment, and medication is prescribed only when clinically appropriate."),
        ("Build Your Treatment Plan", "If you're an appropriate candidate, Isabelle will discuss available medication options and create an individualized treatment plan. Your starting medication and dose will depend on your health history and the treatment selected."),
        ("Receive Your Medication", "Depending on the medication and plan selected, medication may be shipped directly to your home or obtained through a pharmacy. You'll receive instructions for using your medication appropriately."),
        ("Ongoing Follow-Up", "Weight-management treatment isn't a one-time prescription. Skin Clique's current program includes ongoing provider support and monthly follow-up. Isabelle can monitor your progress, discuss side effects or concerns, and make medically appropriate adjustments as treatment continues."),
    ],
    steps_cta="Start Your GLP-1 Intake",
    extra_after_steps=[
        ("What About Side Effects?", None, [
            "Like any prescription medication, GLP-1 medications can cause side effects. Common gastrointestinal side effects can include nausea, vomiting, diarrhea, constipation, abdominal discomfort, and changes in appetite. Side effects can differ depending on the medication, dose, and individual patient.",
            "Some potential risks are more serious. Before beginning treatment, Isabelle will review your medical history and discuss relevant risks, contraindications, medication interactions, and warning signs that require medical attention.",
            "If you're experiencing side effects during treatment, communicate with Isabelle rather than adjusting your medication on your own.",
        ]),
    ],
    concierge_eyebrow="Care From a Provider Who Knows You",
    concierge_h2="Not Just a Prescription in Your Inbox.",
    concierge=[
        "One of the most important parts of medically supervised weight management is having a provider who understands how you're responding.",
        "Skin Clique's current GLP-1 program pairs patients with a dedicated provider and includes monthly clinical follow-up as well as access to that provider between visits.",
        "With Isabelle, you have someone to ask when you're unsure whether a symptom is normal, your appetite changes, you're struggling with side effects, your progress changes, you have questions about your dose, or you simply aren't sure what comes next. Treatment should evolve with you.",
    ],
    candidates_h2="Is GLP-1 Weight Management Right for Me?",
    candidates_intro=[
        "GLP-1 medication isn't appropriate for every person who wants to lose weight. Eligibility is based on a medical evaluation that considers factors such as your weight and health history, current medications, medical conditions, previous treatments, and other individual risk factors.",
        "Make sure Isabelle knows about your complete medical history, including any history of:",
    ],
    candidates=["Pancreatitis", "Gallbladder problems", "Kidney problems", "Significant gastrointestinal conditions", "Diabetes or blood sugar concerns", "Personal or family history of certain thyroid cancers", "Multiple Endocrine Neoplasia syndrome type 2 (MEN 2)", "Pregnancy, breastfeeding, or plans to become pregnant", "Current prescription medications and supplements"],
    candidates_outro=[
        "This isn't an exhaustive list. Your intake and consultation allow Isabelle to determine whether GLP-1 therapy may be appropriate and discuss the risks and benefits that apply specifically to you.",
    ],
    before_h2="Medication Is a Tool—Not the Entire Plan",
    before=[
        "GLP-1 medications can be powerful tools, but they aren't a replacement for taking care of your body. Nutrition, movement, sleep, hydration, stress management, and maintaining muscle mass remain important parts of overall health during weight-management treatment.",
        "The goal isn't simply to eat as little as possible. It's to use treatment, when appropriate, as part of a broader strategy that supports your health. Isabelle can help you think beyond the prescription and focus on habits that support your progress during treatment and beyond.",
    ],
    after_h2="Protecting Muscle During Weight Loss",
    after=[
        "Weight loss can include both fat and lean tissue. Maintaining muscle matters for strength, function, metabolism, and long-term health. That's why an effective weight-management plan should consider more than the number on the scale.",
        "Adequate nutrition, sufficient protein, and resistance-based activity may be important components of maintaining lean mass during weight loss when medically appropriate for you. Talk with Isabelle about how these pieces fit into your individual plan.",
        "Weight management doesn't necessarily end when you reach a particular number. For some patients, continued medication may be appropriate. For others, the treatment plan may change over time. Rather than deciding that at the beginning, Isabelle can evaluate your progress with you and discuss an appropriate long-term strategy as your needs evolve.",
    ],
    faq_h2="GLP-1 Weight Management Frequently Asked Questions",
    faq=[
        ("Is GLP-1 treatment just an injection?", "Many GLP-1-based weight-management medications are injectable, but the medication itself is only one part of medically supervised treatment. Your program also includes medical evaluation, an individualized treatment plan, ongoing monitoring, and provider support."),
        ("Do I need a prescription?", "Yes. GLP-1 medications require a prescription and should only be used when determined medically appropriate by a licensed provider."),
        ("How much weight will I lose?", "There is no way to guarantee an individual's results. Clinical trials have demonstrated meaningful average weight loss with certain GLP-1 and GLP-1/GIP medications, but your response will depend on many individual factors. Isabelle can help you establish realistic goals without promising a particular number."),
        ("How quickly will I lose weight?", "Weight loss typically occurs gradually rather than overnight. The pace varies depending on the medication, dose, individual response, nutrition, activity, and other health factors. Faster isn't necessarily better. The goal is medically appropriate progress that can be monitored over time."),
        ("Will I need to take GLP-1 medication forever?", "There isn't one answer for every patient. Obesity and weight regulation can involve chronic biological factors, and some patients may benefit from longer-term treatment. Your medication plan should be reassessed over time based on your health, response, goals, risks, and preferences."),
        ("What happens if I stop taking the medication?", "Appetite and weight-regulating signals can change after medication is discontinued, and some people regain weight. That is one reason long-term planning and sustainable health habits are important. Discuss any desire to stop or change medication with Isabelle rather than discontinuing treatment without guidance."),
        ("Can I use GLP-1 medication if I only want to lose a few pounds?", "Prescription weight-management medications are intended for patients who meet appropriate medical criteria. They aren't simply cosmetic weight-loss products. Isabelle will determine whether medication is medically appropriate based on your individual health information."),
        ("What's the difference between semaglutide and tirzepatide?", "Semaglutide primarily targets the GLP-1 receptor. Tirzepatide targets both GLP-1 and GIP receptors. Both affect pathways involved in appetite and metabolic regulation, but they are different medications with different dosing, indications, potential benefits, and risks. Isabelle can help determine which available option may be appropriate for you."),
        ("What's the difference between compounded and name-brand GLP-1 medication?", "Name-brand medications are FDA-approved drug products manufactured under their respective approvals. Compounded medications are prepared by compounding pharmacies and are not FDA-approved in the same way as name-brand products. Availability and regulatory circumstances surrounding compounded GLP-1 medications can change. Isabelle can explain the options currently available through Skin Clique, including important differences, so you can make an informed decision."),
        ("Will insurance cover my medication?", "Insurance coverage varies considerably by medication, diagnosis, and individual health plan. Skin Clique's current program states that its compounded GLP-1 prescriptions are not billed through insurance, while name-brand medications are obtained separately through a pharmacy and may have different coverage considerations. Confirm current pricing and coverage when you begin the intake process."),
        ("Can I use HSA or FSA funds?", "Skin Clique currently states that prescribed GLP-1 medications through its program are eligible for HSA/FSA payment. Eligibility can depend on your individual account and plan rules, so confirm requirements with your HSA/FSA administrator."),
        ("Can I take GLP-1 medication while pregnant?", "Weight-loss medications are not appropriate during pregnancy. Tell Isabelle if you are pregnant, breastfeeding, trying to become pregnant, or planning a pregnancy so she can provide appropriate guidance about treatment and medication timing."),
    ],
    related=[
        ("GLP-1s + Hormonal Changes", [
            "Weight, appetite, energy, body composition, and overall well-being can be influenced by many different factors. For some patients, hormonal changes may be part of the bigger picture.",
            "If you're also experiencing symptoms that make you wonder whether hormones could be affecting how you feel, talk with Isabelle. She can help you determine whether your concerns warrant additional evaluation and whether hormone-related care may be appropriate.",
        ], ("Explore Hormone Replacement Therapy", "hormone-replacement-therapy")),
        ("Hair Changes + Weight Loss", [
            "Hair shedding can sometimes occur following significant or rapid weight loss. If you've noticed increased shedding while losing weight, tell Isabelle. She can help evaluate the timing, severity, nutrition, medications, and other potential contributors before determining the appropriate next step.",
        ], ("Explore Hair Loss Treatment", "hair-loss")),
    ],
    notsure_h2="Ready to Explore a Different Approach to Weight Management?",
    notsure=[
        "You don't need another promise that this time you'll just have more willpower. You need information, appropriate medical guidance, and a plan built around your individual health.",
        "Start with Isabelle. Together, you can determine whether GLP-1 weight-management treatment is an appropriate option for you.",
    ],
    final_h2="Start Your GLP-1 Weight Management Intake",
    final=["Medically supervised weight management with a dedicated provider who knows you—Isabelle Joseph, DNP, NP-BC."],
    final_cta="Start Your GLP-1 Intake",
    local_seo=False,
)

SERVICES["hormone-replacement-therapy"] = dict(
    slug="hormone-replacement-therapy", group="Wellness", name="Hormone Replacement Therapy",
    title="Hormone Replacement Therapy (HRT) | Isabelle Joseph, DNP",
    description="Explore personalized hormone replacement therapy for perimenopause and menopause with Isabelle Joseph, DNP, NP-BC, including lab-guided care and ongoing support.",
    h1="Hormone Replacement Therapy With Isabelle Joseph, DNP, NP-BC",
    tagline="When You Don't Feel Like Yourself, It's Worth Asking Why.",
    intro=[
        "Maybe your sleep has changed. Your energy isn't what it used to be. You're experiencing hot flashes, brain fog, mood changes, or changes in your libido. Or maybe you simply know that something feels different—even if you're having trouble putting your finger on exactly what it is.",
        "Hormonal changes during perimenopause and menopause can affect many aspects of how you feel. Hormone replacement therapy (HRT) may be an option for appropriate patients experiencing bothersome symptoms associated with these changes.",
        "With Isabelle Joseph, DNP, NP-BC, care starts by listening to what you're experiencing, evaluating your health and symptoms, and building a personalized plan based on you.",
    ],
    hero_cta="Start Your HRT Journey With Isabelle",
    hero_image=("hrt-hero", "Woman at ease at home — morning light"),
    overview_h2="What Is Hormone Replacement Therapy?",
    overview=[
        "Hormone replacement therapy is a medical treatment used to supplement hormones that decline or fluctuate during perimenopause and menopause.",
        "Depending on your symptoms, health history, and individual needs, treatment may involve estrogen, progesterone, or, for some appropriately evaluated patients, testosterone. Estrogen therapy can be particularly effective for symptoms such as hot flashes and night sweats and may also play a role in supporting bone health and addressing certain genitourinary symptoms. For women with a uterus who use systemic estrogen, progesterone or another appropriate progestogen is generally used to help protect the uterine lining. Testosterone is not automatically appropriate for every patient experiencing fatigue, low libido, or changes in muscle mass, and treatment should be based on appropriate clinical evaluation.",
        "Your treatment plan may include one hormone or a combination depending on your symptoms, medical history, anatomy, laboratory findings when appropriate, and treatment goals.",
    ],
    extra_before_addresses=[
        ("Could Your Symptoms Be Related to Hormonal Changes?", None, [
            "Perimenopause and menopause don't look exactly the same for every woman. Some symptoms are obvious. Others are easier to dismiss as stress, aging, lack of sleep, or simply having too much going on.",
            "Hormonal changes may be associated with symptoms such as hot flashes, night sweats, difficulty sleeping, brain fog, changes in concentration, mood changes, changes in energy, changes in libido, vaginal dryness or discomfort, changes in body composition, and changes in muscle or bone health.",
            "Experiencing one of these symptoms doesn't automatically mean hormones are the cause. That's why appropriate evaluation matters. Instead of guessing, Isabelle can help you look at your symptoms, health history, and other relevant information together.",
        ]),
        ("Perimenopause vs. Menopause", "You Don't Have to Wait Until Your Period Stops to Ask Questions.", [
            "Menopause is reached after 12 consecutive months without a menstrual period when there isn't another medical explanation. Perimenopause is the transition leading up to menopause. During this time, hormone levels can fluctuate and menstrual cycles may become irregular.",
            "Symptoms can begin during perimenopause—sometimes years before the final menstrual period. That means you don't necessarily need to wait until you've officially reached menopause to discuss bothersome symptoms with a medical provider.",
            "If something has changed and it's affecting your quality of life, it's worth having the conversation.",
        ]),
    ],
    addresses_h2="What Can HRT Help Address?",
    addresses=[
        ("Hot Flashes + Night Sweats", "Hot flashes and night sweats—known medically as vasomotor symptoms—are among the most recognizable symptoms associated with menopause. Hormone therapy is an effective treatment option for vasomotor symptoms in appropriately selected patients. Reducing these symptoms can also make a meaningful difference in sleep and everyday comfort."),
        ("Sleep", "Hormonal changes and nighttime symptoms can make restful sleep more difficult. Understanding what is disrupting your sleep is an important part of determining whether hormone therapy or another approach may help."),
        ("Mood + Mental Clarity", "Some women describe increased irritability, mood changes, difficulty concentrating, or a sense of “brain fog” during the menopausal transition. These symptoms can have multiple causes, but hormonal changes may be one piece of the picture."),
        ("Vaginal + Urinary Symptoms", "Declining estrogen levels can contribute to vaginal dryness, discomfort with intimacy, and certain urinary symptoms. These concerns are common—and worth discussing. Depending on your symptoms, localized or systemic treatment options may be considered."),
        ("Bone Health", "Estrogen plays an important role in maintaining bone density. The decline in estrogen associated with menopause can contribute to bone loss over time. Hormone therapy may provide bone-health benefits for appropriately selected patients."),
        ("Sexual Wellness", "Changes in hormones can coincide with changes in libido, vaginal comfort, and sexual well-being. These concerns deserve the same thoughtful medical attention as any other symptom."),
    ],
    addresses_cta="Explore HRT With Isabelle",
    options_h2="Personalized HRT Options",
    options_sub="Your Plan Should Fit Your Body—and Your Life.",
    options_intro="Skin Clique's current women's HRT program offers several treatment approaches that can be individualized by the treating provider. Depending on your clinical needs, available options may include:",
    options=[
        ("Progesterone", "Progesterone-only treatment may be considered in certain situations based on symptoms and medical evaluation."),
        ("Estrogen + Progesterone", "For appropriate patients, estrogen and progesterone may be used together. Skin Clique currently offers transdermal estrogen options including topical cream and patches."),
        ("Testosterone", "Topical testosterone may be considered for selected patients when clinically appropriate."),
        ("Provider-Guided Prescriptions", "Skin Clique also currently offers provider-guided hormone management in which prescriptions can be sent to a pharmacy selected by the patient."),
    ],
    options_note="The right option isn't determined by choosing a package first. Your provider evaluates your symptoms, history, labs when appropriate, and goals before determining a treatment plan. Medication options, formulations, availability, and program pricing can change. Current options should be confirmed through Isabelle and Skin Clique.",
    approach_eyebrow="Isabelle's Approach to Hormone Health",
    approach_h2="Treat the Person—Not Just a Lab Number.",
    approach=[
        "Hormone care shouldn't begin and end with a laboratory result.",
        "Your symptoms matter. Your health history matters. Your age and stage of the menopausal transition matter. Your medications, personal risk factors, goals, and preferences matter. Laboratory testing may also provide important information depending on your individual situation.",
        "Isabelle considers these pieces together to determine whether hormone replacement therapy may be appropriate and, if so, which treatment approach makes sense for you.",
        "The goal isn't to chase a particular hormone number. It's to create an evidence-informed plan centered around your health and how you actually feel.",
    ],
    approach_image=("hrt-approach", "Isabelle — conversation, seated, warm"),
    steps_h2="What to Expect",
    steps=[
        ("Tell Isabelle What You're Experiencing", "Your care begins with your symptoms and health history. You'll discuss what's changed, how long you've noticed it, how those symptoms affect your life, your menstrual and reproductive history when relevant, medications, previous treatments, and your goals."),
        ("Clinical Evaluation + Labs", "Isabelle will evaluate whether additional testing is appropriate. Skin Clique's current HRT program includes access to a comprehensive female hormone panel, and laboratory information may be used alongside symptoms and medical history to help guide care. Labs are one part of the picture—not the entire picture."),
        ("Personalized Treatment Plan", "If HRT is appropriate, Isabelle will develop a plan based on your individual needs. That may include estrogen, progesterone, testosterone when appropriate, or another individualized approach. The formulation, route, and dose depend on your health and treatment plan."),
        ("Begin Treatment", "Depending on the prescription selected, medication may be shipped directly to you or obtained from a local pharmacy. You'll receive instructions for using your medication appropriately."),
        ("Follow-Up + Optimization", "Hormone therapy isn't “set it and forget it.” Your symptoms, response, side effects, health, and laboratory findings when appropriate should be reassessed over time. Isabelle can adjust your treatment plan when clinically indicated."),
    ],
    steps_cta="Start Your HRT Intake",
    extra_after_steps=[
        ("HRT Isn't One-Size-Fits-All", "Route of Treatment Matters.", [
            "You may hear HRT discussed as though it is one medication. It isn't. Hormone therapy can involve different hormones, doses, formulations, and routes of administration.",
            "For example, estrogen may be delivered through the skin using a patch or topical preparation rather than taken orally. Progesterone may be prescribed separately. Some patients may have different needs depending on whether they have a uterus, their symptoms, medical history, and individual risk factors.",
            "This is one reason comparing your HRT prescription with a friend's treatment plan isn't particularly useful. The right plan is the one developed for you.",
        ]),
        ("What Does “Bioidentical” HRT Mean?", None, [
            "The term “bioidentical” describes hormones that have the same molecular structure as hormones produced by the human body. It's important to know that “bioidentical” does not automatically mean compounded.",
            "FDA-approved hormone medications—including certain forms of estradiol and micronized progesterone—can also be bioidentical. Compounded hormone preparations may be appropriate in certain circumstances, but they are not FDA-approved in the same way as commercially manufactured medications.",
            "Isabelle can explain the available options and help you understand why a particular formulation may or may not make sense for you.",
        ]),
    ],
    concierge_eyebrow="Care That Evolves With You",
    concierge_h2="Hormone Care Should Be a Conversation, Not a Transaction.",
    concierge=[
        "Your symptoms can change. Your health can change. Your goals can change. And your hormone treatment may need to change with them.",
        "Skin Clique's HRT program is built around a dedicated provider, personalized protocols, laboratory evaluation when appropriate, and ongoing optimization rather than a one-time prescription.",
        "With Isabelle, you have a provider who can help you understand what's happening, evaluate how you're responding, and make thoughtful adjustments over time.",
    ],
    candidates_h2="Is HRT Right for Me?",
    candidates_intro=[
        "HRT may be worth discussing if you're experiencing bothersome symptoms associated with perimenopause or menopause. Potential candidates can include women experiencing symptoms such as:",
    ],
    candidates=["Hot flashes", "Night sweats", "Sleep disruption", "Vaginal or genitourinary symptoms", "Mood or cognitive changes during the menopausal transition", "Symptoms associated with premature ovarian insufficiency", "Symptoms following surgical menopause"],
    candidates_outro=[
        "Whether HRT is appropriate depends on your individual medical history and risk factors. For many healthy women experiencing bothersome menopausal symptoms—particularly those younger than 60 or within approximately 10 years of menopause onset—the balance of benefits and risks may be favorable. But there is no universal answer. The decision should be individualized between you and your medical provider.",
    ],
    before_h2="When HRT May Not Be Appropriate",
    before_intro="Certain medical histories require additional caution, specialist involvement, or may make systemic hormone therapy inappropriate. Make sure Isabelle knows about any history of:",
    before_list=["Breast or other hormone-sensitive cancers", "Unexplained vaginal bleeding", "Blood clots or pulmonary embolism", "Stroke", "Heart attack or significant cardiovascular disease", "Liver disease", "Pregnancy or possibility of pregnancy", "Migraine history", "Gallbladder disease", "Other significant medical conditions", "Current prescription medications and supplements"],
    before=[
        "This is not a complete screening list. Some conditions do not automatically rule out every form of hormone therapy, but they can affect which treatments are appropriate. Your medical history should be reviewed before treatment begins.",
    ],
    faq_h2="Hormone Replacement Therapy Frequently Asked Questions",
    faq=[
        ("Is HRT safe?", "HRT has potential benefits and risks. For many healthy women who begin treatment for bothersome menopausal symptoms before age 60 or within approximately 10 years of menopause onset, current evidence supports a favorable benefit-risk profile. Your personal medical history can significantly change that assessment. That's why HRT should be prescribed based on an individualized medical evaluation rather than a universal rule."),
        ("Do I need hormone labs before starting HRT?", "Not every menopausal symptom requires hormone testing to establish that menopause is occurring, particularly in women with a typical clinical presentation. However, laboratory testing may be useful in certain situations and can help guide aspects of individualized treatment. Skin Clique's program includes lab options, and Isabelle can determine which testing is appropriate for you."),
        ("Can I start HRT during perimenopause?", "Potentially, yes. You don't necessarily need to wait until you've gone 12 months without a period to discuss hormone therapy. Treatment decisions during perimenopause depend on your symptoms, health history, menstrual pattern, contraception needs, and other individual factors."),
        ("How quickly will I feel different?", "It depends on the symptom, medication, dose, and individual patient. Some symptoms may begin improving within weeks, while others can take longer. Your response should be monitored over time rather than judged after only a few days."),
        ("Will HRT help me lose weight?", "HRT is not a weight-loss medication. Hormonal changes during menopause can affect body composition and fat distribution, but hormone therapy should not be prescribed solely as a weight-loss treatment. If weight management is one of your concerns, Isabelle can help determine whether a separate evaluation or GLP-1 weight-management approach may be appropriate."),
        ("Does HRT cause breast cancer?", "The relationship between hormone therapy and breast cancer risk is complex and depends on factors including the type of hormone therapy, duration of use, individual risk factors, and medical history. It isn't accurate to describe all HRT as having one universal level of risk. Isabelle will review your personal and family history and discuss how the potential benefits and risks apply to you."),
        ("Do I have to stop HRT after five years?", "There isn't a universal five-year stopping rule. How long someone remains on HRT should be individualized based on symptoms, treatment benefits, risks, age, health, and personal preferences. The decision should be revisited periodically with your medical provider."),
        ("What's the difference between a patch and a cream?", "Both can deliver hormones through the skin. The medication, dose, absorption, application schedule, convenience, and individual clinical considerations may differ. Isabelle can help determine which available delivery method best fits your treatment plan."),
        ("Will I need progesterone?", "If you have a uterus and use systemic estrogen, progesterone or another appropriate progestogen is generally needed to protect the uterine lining. Individual situations can differ, so your prescription should be determined by your medical provider."),
        ("What about testosterone for women?", "Testosterone therapy may be considered for selected women after appropriate evaluation, particularly for certain sexual-health concerns. It isn't an automatic treatment for every symptom associated with menopause. Potential benefits, side effects, monitoring, and the limitations of available formulations should be discussed with Isabelle before treatment."),
        ("Can HRT help with vaginal dryness?", "Yes, hormone-based treatments can be effective for genitourinary symptoms associated with menopause, including vaginal dryness and discomfort. For some patients, localized vaginal estrogen or other therapies may be appropriate rather than—or in addition to—systemic HRT. Your symptoms and medical history help determine the appropriate approach."),
    ],
    related=[
        ("HRT + Weight Management", [
            "Hormonal changes and weight changes can occur during the same stage of life, but that doesn't mean every change in weight is caused by hormones. Sleep, muscle mass, activity, nutrition, medications, aging, and metabolic health can all play a role.",
            "If weight management is also a concern, Isabelle can help you look at the bigger picture rather than assuming one treatment will solve every symptom. For appropriate patients, HRT and medically supervised weight-management care may address different needs within a broader wellness plan.",
        ], ("Explore GLP-1 Weight Management", "weight-loss")),
        ("HRT + Hair Changes", [
            "Hormonal transitions can also coincide with changes in hair density, shedding, or texture. Hair loss has many possible causes, so changes shouldn't automatically be attributed to menopause.",
            "If you've noticed increased shedding or thinning, Isabelle can help determine whether a separate hair-loss evaluation and treatment plan may be appropriate.",
        ], ("Explore Hair Loss Treatment", "hair-loss")),
    ],
    notsure_h2="Ready to Feel More Like Yourself?",
    notsure=[
        "You don't need to know whether you need estrogen, progesterone, testosterone—or hormone therapy at all—before reaching out. Start with what you're experiencing.",
        "Isabelle can help you understand your symptoms, review your options, and determine whether hormone replacement therapy may be appropriate for you.",
    ],
    final_h2="Start Your HRT Journey With Isabelle",
    final=["Personalized, lab-guided hormone care with ongoing support from Isabelle Joseph, DNP, NP-BC."],
    final_cta="Start Your HRT Intake",
    local_seo=False,
)

SERVICES["hair-loss"] = dict(
    slug="hair-loss", group="Wellness", name="Hair Loss",
    title="Hair Loss Treatment | Isabelle Joseph, DNP",
    description="Explore personalized hair loss treatment with Isabelle Joseph, DNP, NP-BC, including medically guided topical and oral options for thinning hair and hair loss.",
    h1="Hair Loss Treatment With Isabelle Joseph, DNP, NP-BC",
    tagline="Your Hair Is Changing. Let's Understand Why.",
    intro=[
        "Maybe your ponytail feels thinner than it used to be. Your part looks wider. You're noticing more hair in the shower, on your brush, or on your clothes. Or perhaps the change has been gradual enough that you're only now realizing your hair doesn't have the density it once did.",
        "Hair loss can be frustrating—and figuring out what to do about it can feel even more overwhelming. The first step isn't another shampoo, supplement, or serum. It's understanding what may be causing the change.",
        "Isabelle Joseph, DNP, NP-BC provides personalized, medically guided hair-loss care designed to identify your pattern of hair loss and develop an evidence-based treatment plan when appropriate.",
    ],
    hero_cta="Start Your Hair Loss Consultation",
    hero_image=("hair-hero", "Hair detail — natural texture, soft light"),
    overview_h2="Hair Loss Isn't One Single Condition",
    overview_sub="Finding the Cause Matters.",
    overview=[
        "It's easy to talk about “hair loss” as though everyone experiencing thinning hair has the same problem. They don't. Hair changes can occur for many reasons.",
        "Some people experience gradual pattern hair loss related to genetics and hormones. Others notice increased shedding after an illness, major stressor, pregnancy, nutritional change, rapid weight loss, medication change, or another event. Thyroid conditions, iron deficiency, hormonal changes, scalp conditions, and certain medical conditions can also contribute to hair changes.",
        "That means effective treatment starts with an important question: Why are you losing hair? Isabelle evaluates your symptoms, history, hair-loss pattern, medications, health changes, and other relevant factors before determining which treatment options may be appropriate.",
    ],
    extra_before_addresses=[
        ("What Does Hair Loss Look Like?", None, [
            "Hair loss doesn't always mean bald spots or dramatic shedding. For many people, the earliest signs are subtle: a widening part, a thinner ponytail, more visible scalp, gradual thinning at the crown, a receding hairline, increased shedding in the shower, more hair on your brush or pillow, or hair that doesn't seem as full as it once was.",
            "If something about your hair has changed, you don't have to wait until the loss becomes severe to ask about it. Earlier evaluation may provide more options for protecting existing hair and addressing the underlying cause.",
        ]),
        ("Understanding Pattern Hair Loss", "One of the Most Common Causes of Thinning Hair", [
            "Androgenetic alopecia—often called male or female pattern hair loss—is a common form of progressive hair loss influenced by genetics and hormones. It can look different in women and men. Women may notice a widening part, diffuse thinning across the top of the scalp, or decreased overall hair density. Men may notice recession around the temples, thinning at the crown, or progressive changes to the hairline.",
            "Pattern hair loss tends to progress over time. Prescription treatment may help slow further loss and, for some patients, support regrowth. Skin Clique's current hair-loss program is designed primarily around medically supervised treatment for androgenetic hair loss and other appropriate forms of thinning.",
        ]),
        ("What Else Can Cause Hair Shedding?", "Not Every Hair Change Is Genetic.", [
            "Sudden or increased shedding can sometimes have a different explanation. Potential contributors can include significant physical or emotional stress, illness or surgery, pregnancy or postpartum changes, rapid weight loss, nutritional deficiencies, thyroid conditions, hormonal changes, certain medications, scalp conditions, and other medical conditions.",
            "This is one reason jumping immediately into a hair-growth medication isn't always the best first step. Your pattern, timeline, health history, and symptoms help determine what should happen next. When appropriate, Isabelle may also recommend laboratory evaluation or additional medical assessment to investigate potential contributors.",
        ]),
    ],
    addresses_h2="Prescription Hair-Loss Treatment Options",
    addresses_sub="Your Treatment Depends on Your Pattern, Health + Goals.",
    addresses_intro="Skin Clique currently offers personalized topical and oral prescription options for hair loss. Depending on your diagnosis, health history, sex, reproductive considerations, and individual risk factors, a treatment plan may include options such as:",
    addresses=[
        ("Minoxidil", "Minoxidil is a well-established medication used to support hair growth. It may be used topically or, for selected patients, prescribed orally. Your provider can determine whether minoxidil is appropriate and which route may make sense for you."),
        ("Finasteride", "Finasteride works by reducing the conversion of testosterone to dihydrotestosterone, or DHT, a hormone involved in androgenetic hair loss. It may be considered for certain patients with pattern hair loss. Finasteride is not appropriate for everyone and has important reproductive and potential side-effect considerations that should be reviewed with your provider."),
        ("Dutasteride", "Dutasteride also affects the hormonal pathway involved in DHT production and may be considered in selected patients. As with other prescription hair-loss medications, its use should be individualized based on your health history and risk factors."),
        ("Spironolactone", "Spironolactone has anti-androgen effects and may be considered for certain women experiencing hormonally influenced pattern hair loss. It isn't appropriate for every patient, and medical screening and monitoring may be necessary."),
        ("Customized Topical Formulations", "Skin Clique also currently offers compounded topical formulations that may combine multiple ingredients into a single treatment. The appropriate formulation depends on your diagnosis, goals, and medical history."),
    ],
    addresses_note="Medication availability, formulations, and pricing may change. Current treatment options should always be confirmed with Isabelle and Skin Clique.",
    addresses_cta="Talk to Isabelle About Your Hair Changes",
    approach_eyebrow="Isabelle's Approach to Hair Loss",
    approach_h2="Don't Just Treat the Hair. Look at the Bigger Picture.",
    approach=[
        "Hair loss can feel very personal. It can affect confidence, self-image, and how you feel when you look in the mirror. And when you've already spent money on products that haven't helped, another generic solution isn't particularly reassuring.",
        "Isabelle's approach starts with understanding your experience. When did you first notice the change? Is your hair thinning gradually or shedding suddenly? Where is the change occurring? Has anything changed with your health, medications, hormones, nutrition, stress, or weight? What have you already tried?",
        "Your answers help Isabelle determine whether your hair-loss pattern may respond to treatment and whether additional evaluation is appropriate. The goal isn't simply to prescribe something. It's to create a plan that makes sense for your hair and your health.",
    ],
    approach_image=("hair-approach", "Isabelle — attentive, listening"),
    steps_h2="What to Expect",
    steps=[
        ("Understand What's Happening", "Your first step is a medical evaluation. Isabelle will ask about your hair changes, timeline, family history, health history, medications, hormonal changes, recent illnesses or stressors, nutrition, weight changes, and previous treatments."),
        ("Identify the Pattern", "The location and pattern of hair loss provide important clues about what may be happening. Isabelle will evaluate whether your presentation appears consistent with pattern hair loss or whether another cause should be investigated."),
        ("Additional Evaluation When Needed", "Not everyone needs the same testing. Depending on your symptoms and history, laboratory evaluation or referral for additional medical or dermatologic assessment may be appropriate."),
        ("Build Your Treatment Plan", "If prescription treatment is appropriate, Isabelle can develop an individualized plan using topical and/or oral therapies based on your hair-loss pattern, medical history, risk factors, and goals."),
        ("Track + Adjust", "Hair growth takes time. Your treatment needs to be given enough time to evaluate whether it's working. Isabelle can monitor your progress, address side effects or concerns, and adjust your plan when medically appropriate."),
    ],
    steps_cta="Get Started With Isabelle",
    extra_after_steps=[
        ("Hair Growth Takes Time", "This Isn't an Overnight Treatment.", [
            "Hair grows in cycles. That means even an effective treatment can't create a dramatic change within a few days or weeks. Skin Clique currently advises patients that meaningful improvement generally requires months of consistent treatment, with early stabilization potentially becoming apparent before visible regrowth.",
            "Progress also looks different from person to person. For one patient, success may mean seeing new growth. For another, the first important win may simply be slowing or stabilizing continued loss. Consistency matters. And so does setting realistic expectations from the beginning.",
        ]),
        ("What About Increased Shedding?", None, [
            "Some hair-loss treatments—particularly minoxidil—can temporarily increase shedding when treatment begins. That can be alarming if you aren't expecting it. This doesn't necessarily mean treatment is making your hair loss worse. Changes in the hair-growth cycle can cause older hairs to shed as follicles transition into a new growth phase.",
            "If you notice significant or concerning shedding after beginning treatment, talk with Isabelle rather than stopping medication without guidance.",
        ]),
        ("Nutrition Matters, Too", None, [
            "Healthy hair growth depends on adequate nutrition. Protein, iron, and other nutrients all play roles in normal hair growth and follicle function. But taking more supplements isn't automatically better.",
            "Hair supplements can't correct every cause of hair loss, and unnecessary supplementation isn't a substitute for identifying an underlying medical issue. If a nutritional deficiency is suspected, appropriate evaluation can help determine what actually needs to be addressed.",
        ]),
    ],
    concierge_eyebrow="A Real Provider Following Your Progress",
    concierge_h2="Because Hair Loss Treatment Takes Time.",
    concierge=[
        "One of the hardest parts about treating hair loss is waiting. You shouldn't have to spend those months wondering whether you're doing everything correctly or whether your treatment needs to change.",
        "Skin Clique's current program pairs patients with a dedicated clinician who can monitor progress, review treatment response, and adjust the plan over time.",
        "With Isabelle, your care isn't reduced to an automatic prescription renewal. You have a provider who knows what you're treating, why you're treating it, and how your plan is progressing.",
    ],
    candidates_h2="Is Hair-Loss Treatment Right for Me?",
    candidates_intro=["Prescription treatment may be worth exploring if you:"],
    candidates=["Have noticed gradual thinning or reduced hair density", "Have a widening part", "Have a receding hairline or thinning crown", "Have experienced increased shedding", "Have a family history of pattern hair loss", "Haven't seen meaningful improvement with over-the-counter products", "Want to intervene before hair loss progresses further", "Want a medically supervised treatment plan rather than continuing to experiment with products on your own"],
    candidates_outro=[
        "Not every type of hair loss should be treated with the same medications. Certain inflammatory, autoimmune, infectious, or scarring forms of hair loss require different evaluation and management. Isabelle can help determine whether your presentation fits the types of hair loss she treats or whether referral to another medical professional is the better next step.",
        "Additional medical or dermatologic evaluation may be appropriate if you experience sudden or dramatic hair loss, smooth round bald patches, scalp pain or burning, significant redness or inflammation, scarring, scaling or signs of infection, loss of eyebrows or eyelashes, or hair loss accompanied by other unexplained symptoms. The right treatment starts with the right diagnosis.",
    ],
    before_h2="Before Starting Hair-Loss Medication",
    before_intro="Make sure Isabelle knows about:",
    before_list=["All prescription medications", "Over-the-counter medications and supplements", "Allergies", "Current medical conditions", "Blood pressure concerns", "Kidney or heart conditions", "Hormonal conditions", "Pregnancy or breastfeeding", "Plans to become pregnant", "Changes in menstrual cycles", "Recent illness, surgery, or significant stress", "Recent weight loss", "Family history of hair loss", "Previous hair-loss treatments", "Any scalp pain, itching, scaling, redness, or lesions"],
    before=["Your individual medical history helps determine which treatment options are safe and appropriate."],
    after_h2="Pregnancy + Hair-Loss Medication",
    after=[
        "Pregnancy and pregnancy planning are particularly important when discussing prescription hair-loss treatments. Certain medications used for pattern hair loss—including finasteride and dutasteride—are contraindicated during pregnancy. Other medications may also need to be discontinued before or during pregnancy or breastfeeding.",
        "If you are pregnant, breastfeeding, trying to conceive, or think pregnancy may be possible, tell Isabelle before beginning or continuing treatment. Never assume that a topical medication is automatically safe simply because it is applied to the scalp.",
    ],
    faq_h2="Hair Loss Frequently Asked Questions",
    faq=[
        ("How do I know if I'm actually losing too much hair?", "Everyone naturally sheds hair each day. What's more important than counting individual hairs is noticing a change from what's normal for you. A widening part, thinner ponytail, visible scalp, receding hairline, increased shedding, or noticeable reduction in density can all be reasons to seek an evaluation."),
        ("Can lost hair grow back?", "It depends on why the hair was lost and whether the follicles remain capable of producing hair. Some types of hair loss can improve substantially when the underlying cause is addressed. Pattern hair loss can often be managed with treatments designed to slow progression and support regrowth, but individual response varies."),
        ("How soon will I see results?", "Hair grows slowly. Meaningful improvement usually takes months rather than weeks. Skin Clique currently advises that stabilization may become apparent around the first few months, while visible regrowth can take longer. Your individual response will vary."),
        ("Will my hair get worse before it gets better?", "Some patients using minoxidil experience temporary increased shedding early in treatment. This can occur as hairs transition through the growth cycle. Talk with Isabelle if you're concerned about changes after beginning treatment."),
        ("Do I need oral medication?", "Not necessarily. Some patients may be appropriate candidates for topical treatment alone. Others may benefit from an oral medication or combination approach. Your treatment should be based on your diagnosis, health history, risk factors, and goals."),
        ("Is minoxidil only for men?", "No. Minoxidil may be used in both men and women when medically appropriate. The formulation and treatment plan may differ depending on the patient."),
        ("Can women take finasteride or dutasteride?", "These medications may be considered in selected women under appropriate medical supervision, but they have significant pregnancy-related restrictions and aren't appropriate for women who are pregnant or may become pregnant. Your reproductive status and goals must be discussed before treatment."),
        ("Will I have to use hair-loss medication forever?", "For progressive pattern hair loss, ongoing treatment is typically needed to maintain the benefits. Stopping an effective treatment may allow the underlying hair-loss process to resume. Other forms of temporary shedding may have a different treatment course. Your diagnosis matters."),
        ("Does biotin fix hair loss?", "Biotin deficiency can affect hair, but true deficiency is uncommon. Taking high-dose biotin doesn't treat every cause of hair loss and can interfere with certain laboratory tests. Rather than assuming you need a supplement, identify the reason for your hair changes first."),
        ("Are expensive shampoos enough to treat hair loss?", "Shampoos can support scalp and hair care, but they generally cannot address the underlying biological process responsible for androgenetic hair loss on their own. A medically guided treatment plan may include prescription therapy when appropriate."),
        ("Is stress really enough to make my hair fall out?", "Significant physical or emotional stress can trigger a type of increased shedding known as telogen effluvium. The shedding may occur months after the triggering event, which can make the connection difficult to recognize. Other potential causes should still be considered."),
        ("Can menopause cause hair loss?", "Hormonal changes around menopause may contribute to changes in hair density and pattern. However, hair loss can have multiple causes. Evaluation helps determine whether hormones, genetics, nutrition, thyroid health, medications, or another factor may be involved."),
        ("Can losing weight cause hair shedding?", "Significant or rapid weight loss can contribute to temporary shedding in some people. Nutrition, illness, stress, medication changes, and other factors may also contribute. If you're experiencing shedding during weight loss, discuss it with Isabelle rather than assuming there is a single cause."),
        ("Can hair loss be a sign of another medical problem?", "Sometimes. Hair changes can be associated with thyroid disorders, iron deficiency, autoimmune conditions, hormonal changes, nutritional issues, medications, and other health conditions. Sudden, severe, patchy, painful, inflamed, or otherwise unusual hair loss deserves appropriate medical evaluation."),
    ],
    related=[
        ("Hair Loss + Hormonal Changes", [
            "Hair changes can occur during periods of hormonal transition, including perimenopause and menopause. Declining estrogen levels and changes in the balance of other hormones may influence hair density and growth patterns in some women. But hair loss during midlife shouldn't automatically be blamed on menopause.",
            "If you're experiencing hair changes along with symptoms such as hot flashes, night sweats, sleep changes, brain fog, or other concerns associated with perimenopause or menopause, Isabelle can help determine whether a broader hormone-health evaluation may also be appropriate.",
        ], ("Explore Hormone Replacement Therapy", "hormone-replacement-therapy")),
        ("Hair Changes + Weight Loss", [
            "Hair shedding can sometimes occur following significant or rapid weight loss. Changes in nutrition, calorie intake, illness, physical stress, or rapid changes in body weight can temporarily shift more hairs into the shedding phase of the hair cycle. That doesn't mean everyone who loses weight will experience hair loss, and it doesn't mean GLP-1 medications directly cause every case of shedding that occurs during weight-management treatment.",
            "If you've noticed increased shedding while losing weight, tell Isabelle. She can help evaluate the timing, severity, nutrition, medications, and other potential contributors before determining the appropriate next step.",
        ], ("Explore GLP-1 Weight Management", "weight-loss")),
    ],
    notsure_h2="Ready to Stop Guessing About Your Hair?",
    notsure=[
        "You don't need to diagnose your own hair loss before reaching out. You don't need to know which medication you need. And you don't need another shelf full of products promising thicker hair.",
        "Start by understanding what's changing. Isabelle can help evaluate your concerns and determine whether a medically guided hair-loss treatment plan may be appropriate for you.",
    ],
    final_h2="Start Your Hair Loss Consultation",
    final=["Medically guided hair-loss care with a provider who follows your progress—Isabelle Joseph, DNP, NP-BC."],
    final_cta="Start Your Hair Loss Consultation",
    local_seo=False,
)

# Order services appear in navigation / hub
SERVICE_ORDER = ["tox", "hyperhidrosis", "chemical-peels", "weight-loss", "hormone-replacement-therapy", "hair-loss"]

# ---------------------------------------------------------------- blog placeholders (from Homepage Section 10)
BLOG_LAUNCH = [
    ("Tox 101: What to Know Before Your First Treatment", "Aesthetics"),
    ("Medical-Grade Skincare: Is It Really Different?", "Skin"),
    ("GLP-1 Weight Loss: What You Should Know Before Getting Started", "Wellness"),
]
BLOG_CATEGORIES = ["Skin", "Wellness", "Aesthetics", "Education", "Lifestyle"]
