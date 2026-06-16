"""
Nigerian Government Benefits & Social Programs Database
NaijaBenefits AI - USAII Global AI Hackathon 2026
"""

BENEFITS_DATABASE = [
    {
        "id": "npower",
        "name": "N-Power Programme",
        "category": "employment",
        "description": "Federal government empowerment program providing jobs and stipends for unemployed graduates and non-graduates.",
        "eligibility": [
            "Nigerian citizen aged 18-35",
            "Graduate track: HND/BSc degree",
            "Non-graduate track: SSCE/WAEC certificate",
            "Must be unemployed",
            "Must have valid BVN"
        ],
        "benefit_amount": "₦30,000/month stipend",
        "how_to_apply": "Apply at npower.gov.ng during open enrollment periods",
        "deadline": "Check npower.gov.ng for current batch",
        "ministry": "Ministry of Humanitarian Affairs",
        "website": "https://npower.gov.ng",
        "tags": ["youth", "employment", "graduate", "stipend", "job"]
    },
    {
        "id": "trader_moni",
        "name": "TraderMoni / MarketMoni",
        "category": "business",
        "description": "Interest-free loans for petty traders, market women, and artisans to grow their businesses.",
        "eligibility": [
            "Nigerian citizen",
            "Petty trader, market woman, or artisan",
            "Must have active trade/business",
            "Must have BVN",
            "Age 18 and above"
        ],
        "benefit_amount": "₦10,000 - ₦100,000 interest-free loan",
        "how_to_apply": "Register at your local market with GEEP agents or visit geep.gov.ng",
        "deadline": "Rolling enrollment",
        "ministry": "Government Enterprise and Empowerment Programme (GEEP)",
        "website": "https://geep.gov.ng",
        "tags": ["business", "loan", "trader", "market", "artisan", "women", "entrepreneur"]
    },
    {
        "id": "conditional_cash",
        "name": "Conditional Cash Transfer (CCT)",
        "category": "welfare",
        "description": "Monthly cash payments to extremely poor and vulnerable households under the National Social Investment Programme.",
        "eligibility": [
            "Extremely poor household",
            "Must be registered in the National Social Register",
            "Households with children must ensure school attendance",
            "Pregnant/nursing mothers qualify",
            "Elderly and disabled persons qualify"
        ],
        "benefit_amount": "₦5,000/month per household",
        "how_to_apply": "Contact your Local Government Social Welfare Office or visit nsip.gov.ng",
        "deadline": "Ongoing - contact LGA office",
        "ministry": "Ministry of Humanitarian Affairs & Disaster Management",
        "website": "https://nsip.gov.ng",
        "tags": ["poor", "vulnerable", "cash", "welfare", "family", "children", "pregnant", "elderly", "disabled"]
    },
    {
        "id": "nhis",
        "name": "National Health Insurance Scheme (NHIS)",
        "category": "health",
        "description": "Government health insurance providing affordable healthcare for Nigerians including free services for vulnerable groups.",
        "eligibility": [
            "Nigerian citizen",
            "Formal sector workers enrolled by employer",
            "Voluntary contributors welcome",
            "Children under 5 get free healthcare",
            "Pregnant women get free antenatal care"
        ],
        "benefit_amount": "Subsidized healthcare - pay 10% of costs",
        "how_to_apply": "Register through your employer or visit nhia.gov.ng",
        "deadline": "Ongoing enrollment",
        "ministry": "National Health Insurance Authority (NHIA)",
        "website": "https://nhia.gov.ng",
        "tags": ["health", "insurance", "hospital", "medical", "pregnant", "children", "healthcare"]
    },
    {
        "id": "tetfund",
        "name": "TETFund Scholarship",
        "category": "education",
        "description": "Scholarships and bursaries for Nigerian students in public tertiary institutions.",
        "eligibility": [
            "Nigerian citizen",
            "Enrolled in accredited Nigerian public university/polytechnic",
            "Minimum CGPA of 3.0/5.0 or 2nd Class Upper",
            "Not benefiting from other federal scholarships",
            "Must be sponsored by state government"
        ],
        "benefit_amount": "Full tuition + ₦200,000 - ₦500,000 annual allowance",
        "how_to_apply": "Apply through your institution's scholarship office or tetfund.gov.ng",
        "deadline": "Usually announced January-March annually",
        "ministry": "Tertiary Education Trust Fund",
        "website": "https://tetfund.gov.ng",
        "tags": ["education", "scholarship", "university", "student", "bursary", "tertiary"]
    },
    {
        "id": "federal_scholarship",
        "name": "Federal Government Scholarship (SFAMS)",
        "category": "education",
        "description": "Scholarships for undergraduate and postgraduate students at Nigerian and foreign universities.",
        "eligibility": [
            "Nigerian citizen",
            "Undergraduate: 5 O'Level credits including English & Maths",
            "Must have gained admission into accredited institution",
            "Postgraduate: Good first degree from recognized university",
            "Age limit: 35 years for postgraduate"
        ],
        "benefit_amount": "Full scholarship covering tuition, accommodation, feeding",
        "how_to_apply": "Apply at scholarship.gov.ng during annual application window",
        "deadline": "Usually June-August annually",
        "ministry": "Federal Scholarship Board",
        "website": "https://scholarship.gov.ng",
        "tags": ["scholarship", "education", "undergraduate", "postgraduate", "student", "federal"]
    },
    {
        "id": "boa_agric",
        "name": "Bank of Agriculture (BOA) Loans",
        "category": "agriculture",
        "description": "Low-interest agricultural loans for farmers, cooperatives, and agribusinesses.",
        "eligibility": [
            "Nigerian farmer or agribusiness owner",
            "Must have farmland or agricultural business",
            "Cooperative societies welcome",
            "Youth farmers (18-35) get preferential rates",
            "Must have BVN and valid ID"
        ],
        "benefit_amount": "₦50,000 - ₦50,000,000 at 9% interest rate",
        "how_to_apply": "Visit nearest BOA branch or apply at boanig.com",
        "deadline": "Rolling applications",
        "ministry": "Bank of Agriculture",
        "website": "https://boanig.com",
        "tags": ["farming", "agriculture", "loan", "food", "cooperative", "agribusiness", "farmer"]
    },
    {
        "id": "smedan",
        "name": "SMEDAN Business Support",
        "category": "business",
        "description": "Training, grants, and business development support for small and medium enterprises.",
        "eligibility": [
            "Nigerian citizen",
            "Small or medium business owner",
            "Startup founders welcome",
            "Must register business with CAC",
            "Businesses 0-5 years old prioritized"
        ],
        "benefit_amount": "Free training + grants up to ₦500,000",
        "how_to_apply": "Visit smedan.gov.ng or nearest SMEDAN office",
        "deadline": "Various programs throughout year",
        "ministry": "Small and Medium Enterprises Development Agency",
        "website": "https://smedan.gov.ng",
        "tags": ["business", "startup", "SME", "entrepreneur", "grant", "training", "small business"]
    },
    {
        "id": "homevida",
        "name": "National Housing Fund (NHF)",
        "category": "housing",
        "description": "Affordable mortgage loans for Nigerian workers to own their own homes.",
        "eligibility": [
            "Nigerian citizen aged 18-60",
            "Must contribute to NHF for minimum 6 months",
            "Employed in public or private sector",
            "Income between ₦30,000 - ₦500,000/month",
            "Must not own a house already"
        ],
        "benefit_amount": "Mortgage loan up to ₦15,000,000 at 6% interest",
        "how_to_apply": "Register through employer or visit fmbn.gov.ng",
        "deadline": "Ongoing",
        "ministry": "Federal Mortgage Bank of Nigeria",
        "website": "https://fmbn.gov.ng",
        "tags": ["housing", "house", "mortgage", "home", "accommodation", "property"]
    },
    {
        "id": "youthvita",
        "name": "Youth Investment Fund",
        "category": "youth",
        "description": "Low-interest loans and grants specifically for young Nigerian entrepreneurs.",
        "eligibility": [
            "Nigerian youth aged 18-35",
            "Must have viable business idea or existing business",
            "Business plan required",
            "Not currently benefiting from similar federal program",
            "Must complete entrepreneurship training"
        ],
        "benefit_amount": "₦250,000 - ₦2,500,000 at 5% interest",
        "how_to_apply": "Apply at youthfund.gov.ng",
        "deadline": "Check youthfund.gov.ng for open windows",
        "ministry": "Ministry of Youth and Sports Development",
        "website": "https://youthfund.gov.ng",
        "tags": ["youth", "entrepreneur", "loan", "business", "young", "startup", "grant"]
    },
    {
        "id": "disability_support",
        "name": "National Commission for Persons with Disabilities (NCPWD)",
        "category": "disability",
        "description": "Support services, assistive devices, and welfare programs for Nigerians with disabilities.",
        "eligibility": [
            "Nigerian citizen with any disability",
            "Must register with NCPWD",
            "Physical, sensory, intellectual disabilities covered",
            "All ages covered",
            "Caregivers also eligible for support"
        ],
        "benefit_amount": "Free assistive devices + monthly stipend + vocational training",
        "how_to_apply": "Register at ncpwd.gov.ng or visit nearest NCPWD office",
        "deadline": "Ongoing",
        "ministry": "National Commission for Persons with Disabilities",
        "website": "https://ncpwd.gov.ng",
        "tags": ["disability", "disabled", "handicap", "special needs", "wheelchair", "blind", "deaf"]
    },
    {
        "id": "maternal_health",
        "name": "Free Maternal & Child Health Programme",
        "category": "health",
        "description": "Free healthcare services for pregnant women and children under 5 in government hospitals.",
        "eligibility": [
            "Pregnant Nigerian women",
            "Children under 5 years",
            "Must use government health facilities",
            "No income requirement",
            "Available in all states"
        ],
        "benefit_amount": "Free antenatal care, delivery, and postnatal care",
        "how_to_apply": "Visit any government primary health center or general hospital",
        "deadline": "Ongoing",
        "ministry": "Federal Ministry of Health",
        "website": "https://health.gov.ng",
        "tags": ["pregnant", "maternal", "baby", "child", "mother", "antenatal", "delivery", "health", "free"]
    }
]

CATEGORIES = {
    "employment": "💼 Employment & Jobs",
    "business": "🏪 Business & Entrepreneurship", 
    "education": "🎓 Education & Scholarships",
    "health": "🏥 Health & Medical",
    "welfare": "🤝 Welfare & Social Support",
    "agriculture": "🌾 Agriculture & Farming",
    "housing": "🏠 Housing",
    "youth": "👨‍💼 Youth Programs",
    "disability": "♿ Disability Support"
}
