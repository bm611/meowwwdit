import reflex as rx
from datetime import datetime, timedelta

from .post import post

# Sample posts data
sample_posts = [
    {
        "title": "Just caught my first mouse! ",
        "content": "After weeks of training and patience, I finally caught my first mouse! The thrill of the chase was incredible. Any other cats here with hunting tips?",
        "author": "WhiskerNinja",
        "subreddit": "CatHunting",
        "upvotes": 128,
        "comments": 45,
        "time_posted": datetime.now() - timedelta(hours=2),
    },
    {
        "title": "Best cat nap spots in the house? ",
        "content": "Looking for new places to nap. The sunbeam by the window is getting too mainstream. Share your secret spots!",
        "author": "SleepyPaws",
        "subreddit": "CatLifestyle",
        "upvotes": 256,
        "comments": 89,
        "time_posted": datetime.now() - timedelta(hours=5),
    },
    {
        "title": "New catnip toy review ",
        "content": "Just got my paws on the latest organic catnip mouse toy. It's purr-fectly amazing! Full review in the comments.",
        "author": "CatnipConnoisseur",
        "subreddit": "CatReviews",
        "upvotes": 512,
        "comments": 167,
        "time_posted": datetime.now() - timedelta(days=1),
    },
    {
        "title": "Help! My human keeps working from home ",
        "content": "Short rant: My human won't stop sitting in MY office chair. That's my spot for bird watching! What do I do?",
        "author": "ChairDefender",
        "subreddit": "CatComplaints",
        "upvotes": 89,
        "comments": 23,
        "time_posted": datetime.now() - timedelta(hours=1),
    },
    {
        "title": "The Ultimate Guide to Knocking Things Off Tables ",
        "content": "After years of extensive research and practical experiments, I've perfected the art of knocking things off tables. Here's my comprehensive guide:\n\n1. Assessment Phase: Start by examining the object. Is it fragile? Valuable to humans? These are key factors.\n\n2. Positioning: Approach casually. Humans are less likely to intervene if you appear disinterested.\n\n3. The Touch Test: Gently tap the object with your paw. This builds suspense and often gets human attention.\n\n4. The Final Push: Here's where technique matters. A swift, clean motion works best. Remember, it's all in the wrist.\n\n5. The Aftermath: Maintain eye contact with your human. This establishes dominance.\n\nBonus Tip: Glass objects make the most satisfying sound!\n\nWhat are your favorite techniques?",
        "author": "ChaosMaster",
        "subreddit": "CatScience",
        "upvotes": 1024,
        "comments": 234,
        "time_posted": datetime.now() - timedelta(days=2),
    },
    {
        "title": "Lost my favorite toy ",
        "content": "It's under the fridge.",
        "author": "TinyTrouble",
        "subreddit": "CatProblems",
        "upvotes": 45,
        "comments": 12,
        "time_posted": datetime.now() - timedelta(minutes=30),
    },
    {
        "title": "PSA: The red dot is NOT real!",
        "content": "I've spent countless hours investigating this phenomenon. Multiple test cases, various lighting conditions, different surfaces - the results are conclusive. The red dot is an illusion! Don't fall for it like I did. Stay woke, fellow felines! ",
        "author": "LaserTruth",
        "subreddit": "CatConspiracy",
        "upvotes": 789,
        "comments": 156,
        "time_posted": datetime.now() - timedelta(hours=8),
    },
    {
        "title": "My human finally got me a water fountain! ",
        "content": "No more drinking from the tap! It's amazing how the water just keeps flowing. Technology is incredible. Highly recommend!",
        "author": "HydratedWhiskers",
        "subreddit": "CatTechnology",
        "upvotes": 342,
        "comments": 67,
        "time_posted": datetime.now() - timedelta(hours=12),
    },
]


def feed_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            *[
                post(
                    title=p["title"],
                    content=p["content"],
                    author=p["author"],
                    subreddit=p["subreddit"],
                    upvotes=p["upvotes"],
                    comments=p["comments"],
                    time_posted=p["time_posted"],
                )
                for p in sample_posts
            ],
            class_name="space-y-4 w-full max-w-3xl mx-auto px-4 mt-8",
        ),
        class_name="mt-10",
    )
