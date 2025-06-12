## Why EidosUI since I created MonsterUI already?  

I love MonsterUI and still support it.  But I built it around a completely different philosophy, and as a results works best in different situations.

I believe I will still use Monster UI in some situations personally.  I will use Eidos UI in other situations.

### MonsterUI

MonsterUI is extremely opinionated and glues together a curated collection of many frameworks (FrankenUI, DaisyUI, Tailwind, HighlightJS, Katext), and then adds some custom styled components on top (Semantic HTML typography, Navigation Bars, server side markdown rendering, etc.).  It is a fantastic way to build extremely quickly, but as a result customization of it is challenging.  It was built for maximum developer velocity.  

However it's often unclear what styles are coming from which dependency, how to change those incrementally, and the central mental model for what it does is hard to convey.  Customization is harder.  It's the classic flexibility vs verbosity tradeoff (of course we want both flexibility and conciseness and MonsterUI hits a really special balance there and does both quite well IMO :D)

As a result, even the most experienced users often communicate it as mostly a wrapper for FrankenUI.  In early dev it under my personal github account named `fh-frankenui` because it was going to be a wrapper, but that turned out to be incredibly confusing to users who would start and not realize that loads of it's features have nothing to do with FrankenUI.  As it was transferred to Answer AI and I worked on it in a more dedicated way as an full-time employee, it grew and changed shape.  When it came time to release Version 1, I finally decided (thanks to consultation with Audrey and Danny) that the name was not representative of what the library does and so I came up with MonsterUI.  I kept the monster theme in the name as a nod to the original core inspiration (FrankenUI).

TLDR: FrankenUI is a big part, but there are lots of other big parts.  And yet, communicating the model for what is in there is hard because the true answer is "whatever Isaac found helpful when he was building at the time".  Incredibly useful, but hard for people to wrap their head around.  So it is usually described as a thin wrapper for FrankenUI anyway because that's simpler to communicate.

### Eidos UI

Edidos UI is build with a different philosophy in mind.  It is built to have many of the conveniences of MonsterUI for UI development, with fewer dependencies, stronger typing, easier customization, and an easier path to scale to larger web applications and improving small UX/design pieces.  This means there will be some extra verbosity in places, less "magic" (whatever that means), and clearer separation of concerns.  The goal of EidosUI to be close to as simple to use but easier to understand and customize inside of common FastAPI and python usage patterns.  The goal of MonsterUI was to create something new that is tailored to the exact things I wanted to build.

I also found when I wanted to bring my vision for my personal website and blog alive, rewriting it without MonsterUI was the easier path.  It was perfectly functional and readable, and looked just fine (if you want a really nice simple blog it was fantastic!).  But I had my own vision to improve it and MonsterUI got in the way of that detailed design and customization work.

EidosUI is meant to be a great choice for when you want extra customization and a clearer separation of concerns as the project gets larger and scales in complexity.
