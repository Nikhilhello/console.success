# from icrawler.builtin import BingImageCrawler

# categories = {
#     "phase1_healthy": "cotton vegetative boll",
#     "phase1_damaged": "cotton bud disease",
#     "phase2_healthy": "cotton flowering boll",
#     "phase2_damaged": "cotton flowering disease",
#     "phase3_healthy": "cotton bursting boll",
#     "phase3_damaged": "cotton bollworm damage",
#     "phase4_healthy": "cotton harvest ready boll",
#     "phase4_damaged": "cotton damaged harvest boll"
# }

# for category, keyword in categories.items():
#     print(f"Downloading {category} images...")
#     crawler = BingImageCrawler(
#         storage={"root_dir": f"dataset/train/{category}"}
#     )
#     crawler.crawl(keyword=keyword, max_num=50)
#     print(f"Finished downloading {category} images.")

from icrawler.builtin import BingImageCrawler

download_plan = {
    "phase1_healthy": [
        "cotton vegetative boll",
        "cotton bud stage plant",
        "young cotton boll close up"
    ],
    "phase1_damaged": [
        "cotton bud disease",
        "early cotton pest damage",
        "cotton bud bollworm"
    ],
    "phase2_healthy": [
        "cotton flowering boll",
        "cotton flower and boll",
        "healthy cotton flowering stage"
    ],
    "phase2_damaged": [
        "cotton flowering disease",
        "cotton flower pest damage",
        "cotton flowering discoloration"
    ],
    "phase3_healthy": [
        "cotton bursting boll",
        "cotton ripped boll open",
        "cotton boll opening stage"
    ],
    "phase3_damaged": [
        "pink bollworm cotton damage",
        "cotton boll pest hole",
        "cotton boll rot disease"
    ],
    "phase4_healthy": [
        "cotton harvest ready boll",
        "mature cotton boll white",
        "fully opened cotton boll"
    ],
    "phase4_damaged": [
        "damaged cotton harvest boll",
        "cotton harvest disease",
        "cotton dirty damaged boll"
    ]
}

IMAGES_PER_KEYWORD = 40   # 3 keywords × 40 = ~120 images per class

for category, keywords in download_plan.items():
    for keyword in keywords:
        print(f"Downloading {category} → {keyword}")
        crawler = BingImageCrawler(
            storage={"root_dir": f"dataset/train/{category}"}
        )
        crawler.crawl(
            keyword=keyword,
            max_num=IMAGES_PER_KEYWORD,
            filters={"size": "medium"}
        )
        print(f"Finished downloading {category} → {keyword}")