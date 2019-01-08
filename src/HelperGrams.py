import nltk
from nltk.corpus import stopwords


def get_keepterms():
    """ List of word with zipf score > 3.4 but has biological revelance

    Returns:
        [list] -- list of words to be keeped in the analysis
    """

    keepterms = ['especi','head', 'growth', 'oil', 'age', 'pain', 'air', 'sleep', 'dead', 'mother', 'human', 'earth', 'body', 'hand', 'network', 'island', 'sea', 'face', 'baby', 'heart', 'population', 'river', 'wall', 'pressure', 'weight', 'food', 'blood', 'cat', 'dog', 'nail', 'defensive', 'potato', 'pepper', 'bird', 'grass', 'marijuana', 'translation', 'oxygen', 'california', 'indian', 'atlanta', 'pig', 'intelligence', 'silence', 'foot', 'nonsense', 'shell', 'rabbit', 'ghost', 'elephant', 'ethnic', 'stress', 'clock', 'compound', 'egyptian', 'genius', 'manchester', 'breathe', 'oral', 'hostile', 'vacuum', 'fox', 'tension', 'humor', 'beer', 'metal', 'circuit', 'nest', 'philadelphia', 'mineral', 'thermal', 'snow', 'widow', 'bug', 'cognitive', 'blind', 'blast', 'patient', 'japanese', 'inflation', 'nutrition', 'signature', 'breed', 'buffalo', 'cope', 'trunk', 'giant', 'rat', 'belt', 'bread', 'pole', 'protection', 'tunnel', 'hmm', 'attract', 'brain', 'skull', 'solid', 'depression', 'taste', 'brussels', 'racial', 'survival', 'deer', 'queensland', 'cave', 'toronto', 'transfer', 'smell', 'skin', 'shock', 'brazilian', 'dutch', 'height', 'essence', 'gdp', 'sweet', 'salt', 'arizona', 'geneva', 'wire', 'columbia', 'cancer', 'environment', 'lip', 'asian', 'burst', 'throat', 'mountain', 'micro', 'invasion', 'diabetes', 'boundary', 'zone', 'kenya', 'rhythm', 'shield', 'bone', 'pregnancy', 'beauty', 'todd', 'ring', 'honey', 'toe', 'memory', 'arc', 'flower', 'nerve', 'vision', 'eagle', 'wind', 'italian', 'transition', 'dominant', 'bite', 'flash', 'orientation', 'horse', 'virus', 'repair', 'spider', 'tropical', 'berlin', 'crown', 'sexual', 'kidney', 'warm', 'resistance', 'canal', 'integrity', 'chile', 'progressive', 'pregnant', 'autumn', 'hook', 'hole', 'disk', 'sheep', 'breast', 'root', 'childhood', 'coat', 'viral', 'arabia', 'behavior', 'victoria', 'vienna', 'deep', 'communicate', 'arctic', 'shark', 'fitness', 'urban', 'african', 'grain', 'holland', 'glasgow', 'rice', 'wheat', 'kennedy', 'matrix', 'female', 'britain', 'flame', 'timber', 'wing', 'pine', 'motivation', 'moon', 'cure', 'disease', 'olive', 'stomach', 'bee', 'breath', 'fat', 'electric', 'bucket', 'gulf', 'consciousness', 'argentina', 'cow', 'panic', 'cycle', 'visual', 'habitat', 'gap', 'dublin', 'diet', 'delhi', 'teeth', 'bell', 'male', 'plant', 'leaf', 'facial', 'newcastle', 'lamb', 'marine', 'sydney', 'conscience', 'mirror', 'apple', 'killer', 'duck', 'cock', 'communication', 'sept', 'hiv', 'mouse', 'fever', 'sun', 'disorder', 'behaviour', 'immune', 'valve', 'shoulder', 'storm', 'mortality', 'angry', 'nightmare', 'muscle', 'vitamin', 'chicago', 'ear', 'injury', 'strength', 'wolf', 'alcohol', 'tiger', 'panel', 'shape', 'cbs', 'horn', 'channel', 'bull', 'mouth', 'amsterdam', 'snake', 'surgery', 'canadian', 'korean', 'cattle', 'dick', 'protective', 'thumb', 'coal', 'lemon', 'smoke', 'baltimore', 'coffee', 'spring', 'tooth', 'guide', 'fear', 'sheet', 'leather', 'danger', 'boston', 'illness', 'minnesota', 'bridge', 'arrest', 'virgin', 'egg', 'toxic', 'crowd', 'milk', 'asia', 'spin', 'anxiety', 'bloody', 'nervous', 'dental', 'wood', 'silent', 'circulation', 'barrier', 'migration', 'sand', 'mobility', 'divide', 'sweat', 'wave', 'harvest', 'corn', 'vessel', 'founder', 'tobacco', 'athletic', 'drain', 'surface', 'singapore', 'recovery', 'silk', 'tongue', 'tail', 'discrimination', 'react', 'pollution', 'tree', 'irish', 'map', 'polar', 'sick', 'maintenance', 'grow', 'guinea', 'stem', 'environmental', 'lung', 'organ', 'chicken', 'lesbian', 'transport', 'feedback', 'frequency', 'neck', 'spanish',
                 'therapy', 'hunter', 'mac', 'oak', 'tide', 'intellectual', 'moscow', 'portuguese', 'clinic', 'colorado', 'attraction', 'determination', 'iron', 'bend', 'drug', 'knee', 'battle', 'sugar', 'pocket', 'bear', 'russian', 'motor', 'liver', 'cigarette', 'musical', 'delivery', 'bat', 'gay', 'recognition', 'clinical', 'intelligent', 'bubble', 'testosterone', 'mutation', 'aggression', 'grape', 'arthritis', 'infectious', 'obese', 'maternity', 'hereditary', 'crab', 'landmark', 'shalt', 'plasma', 'endemic', 'sensory', 'zinc', 'inflammation', 'transitional', 'fatty', 'cone', 'juvenile', 'tolerant', 'sponge', 'veterinary', 'agony', 'insect', 'platinum', 'distress', 'colon', 'cardiac', 'homo', 'node', 'bleed', 'heel', 'climax', 'homicide', 'goat', 'rift', 'cerebral', 'claw', 'ape', 'vegan', 'lethal', 'feminine', 'schizophrenia', 'tor', 'enzyme', 'hormone', 'tomato', 'allergic', 'penetration', 'fork', 'nutrient', 'bipolar', 'progression', 'abdominal', 'heroin', 'gut', 'autopsy', 'masculine', 'bulb', 'differentiate', 'irrigation', 'headache', 'mast', 'rosemary', 'rib', 'oyster', 'suppression', 'dementia', 'paralysis', 'reproduction', 'sensor', 'cholesterol', 'flora', 'cinnamon', 'duct', 'maturity', 'muscular', 'autonomous', 'breadth', 'fisher', 'allergy', 'rag', 'fda', 'ark', 'porter', 'stimulus', 'maze', 'epidemic', 'bengal', 'lang', 'abdomen', 'hepatitis', 'displacement', 'carrot', 'ecology', 'abduction', 'heartbeat', 'parasite', 'algeria', 'deaf', 'psychiatric', 'cardiovascular', 'elbow', 'medicare', 'dwarf', 'vaccine', 'malaria', 'psa', 'titanium', 'substitution', 'fatigue', 'trout', 'maxwell', 'fiber', 'hoover', 'behavioral', 'tidal', 'metabolic', 'obesity', 'sensitivity', 'calcium', 'vein', 'aluminum', 'turtle', 'asteroid', 'poisonous', 'sperm', 'cox', 'adolescent', 'urine', 'contagious', 'gluten', 'ankle', 'butterfly', 'toxicity', 'diarrhea', 'crossover', 'fetus', 'floral', 'iris', 'hostility', 'collateral', 'confrontation', 'rehab', 'mentality', 'vaccination', 'clearance', 'salvage', 'anal', 'penetrate', 'prostate', 'repression', 'webster', 'protector', 'psychic', 'projection', 'inheritance', 'dentist', 'audition', 'disposition', 'vinegar', 'adaptive', 'ecstasy', 'appetite', 'instability', 'restless', 'swan', 'locomotive', 'erection', 'mushroom', 'antibiotic', 'owl', 'invasive', 'pneumonia', 'pyramid', 'aquatic', 'plantation', 'curtis', 'junction', 'neural', 'eruption', 'insanity', 'homosexual', 'caffeine', 'promoter', 'vomit', 'bloom', 'asylum', 'homosexuality', 'onion', 'hairy', 'flavor', 'regulator', 'membrane', 'immature', 'oxide', 'sting', 'bind', 'skeleton', 'amp', 'developmental', 'swell', 'plague', 'spinal', 'cbc', 'goose', 'flu', 'peripheral', 'motive', 'adapter', 'fog', 'alcoholic', 'spine', 'nap', 'reg', 'insulin', 'larvae', 'glucose', 'stationary', 'autism', 'tumor', 'mole', 'envy', 'tuberculosis', 'starvation', 'segregation', 'frog', 'immunity', 'nucleus', 'respiratory', 'resistant', 'inflammatory', 'fusion', 'venom', 'banana', 'mosquito', 'reproductive', 'proliferation', 'digestive', 'cohesion', 'deprivation', 'beetle', 'serpent', 'obstruction', 'insomnia', 'blindness', 'nasal', 'leukemia', 'amnesia', 'fungus', 'diabetic', 'snail', 'lac', 'moth', 'peacock', 'colonization', 'embryo', 'cortex', 'pediatric', 'vascular', 'magnesium', 'cholera', 'fetal', 'exhaustion', 'fungi', 'intolerance', 'marrow', 'innate', 'acne', 'mule', 'provocative', 'semen', 'cervical', 'nicotine', 'retina', 'cdc', 'thyroid', 'influenza', 'differentiation', 'alcoholism', 'vaginal', 'benign', 'adrenaline', 'pulmonary', 'migrate', 'atp', 'perennial']
    return keepterms


def generate_stop_grams():
    """ Remove common frequent term with no relevance in the term discovery process

    Returns:
        [list] -- List of words to be removed in the analysis
    """

    stoponegram = ['rt-pcr','fulli', 'arise', 'luciferase', 'clearly', 'mechanistic', 'elevate', 'fxr', 'atypycal', 'orfs', 'spectroscopic', 'orthology', 'strikingly', 'reciprocal', 'devoid', 'transrciptomics', 'genomics', 'in-silico', 'p005', 'p00001', 'p0001', 'ass', 'subsequent', 'manner', 'aid', 'score', 'correct', 'gain', 'receive', 'partner', 'neither', 'temperature', 'physiological', 'induction', 'hybrid', 'crucial', 'similarity', 'directly', 'phase', 'core', 'impair', 'define', 'specificity', 'double', 'mass', 'kda', 'basis', 'marker', 'interestingly', 'regulatory', 'affinity', 'nuclear', 'recently', 'screen', 'fold', 'structural', 'appear', 'characterization', 'critical', 'library', 'direct', 'independent', 'approximately', 'electron', 'consist', 'band', 'primary', 'conclude', 'separate', 'stimulate', 'block', 'alpha', 'beta', 'larger', 'smaller', 'additional', 'chain', 'carry', 'secondary', 'pre', 'label', 'internal', 'hybridization', 'transfer', 'alter', 'accumulate', 'restriction', 'modification', 'frame', 'chromosome', 'extra', 'eukaryote', 'synthesis', 'rpl22', 'fragment', 'plasmid', 'precursor', 'bacterial', 'derive', 'contain', 'yeast', 'amino', 'peptide', 'transcribe', 'initiation', 'bp', 'residue', 'clone', 'helix', 'locate', 'infection', 'terminus', 'mutant', 'terminal', 'bacteria', 'virus', 'strand', 'pair', 'microscopy', 'gel', 'reaction', 'contrast', 'rnase', 'fraction', 'host', 'repeat', 'iii', 'generate', 'probe', 'tissue', 'electrophoresis', 'domain', 'obtain', 'formation', 'eukaryotic', 'purify', 'cleavage', 'pattern', 'characteristic', 'clade', 'identical', 'product', 'transcription', 'complex', 'proteomic', 'relevance', 'additionally', 'derivative', 'functionality', 'differential', 'clue', 'insight', 'involvement', 'stability', 'pcr', 'spp', 'favor', 'gc', 'conserve', 'cod', 'amplification', 'discrete', 'complementary', 'mix', 'correspond', 'transcript', 'abundant', 'divergent', 'comparative', 'vicinity', 'interact', 'circular', 'rna', 'interference', 'stag', 'remarkably', 'withdrawal', 'notably', 'measurement', 'mature', 'rely', 'distinctive', 'expand', 'newly', 'strain', 'participate', 'aspect', 'meanwhile', 'barely', 'discovery', 'formula', 'switch', 'bind', 'closely', 'genome', 'display', 'raise', 'toward', 'apply', 'copy', 'mostly', 'prevent', 'progress', 'animal', 'reference', 'indeed', 'location', 'responsible', 'relevant', 'throughout', 'specifically', 'element', 'v79', 'structure', 'absent', 'regulation', 'kb', 'additionally', 'transcriptomics', 'transcriptomics', 'ribonomics', 'ribonomic', 'constitutive', 'encode', 'relevance', 'seq', 'pcr', 'electrophoretic', 'inhibit', 'mediate', 'activate', 'mammalian', 'inhibition', 'regulate', 'inhibitor', 'activation', 'cell', 'agent', 'express', 'molecule', 'downstream', 'activation', 'inhibitor', 'regulate', 'inhibition', 'activate', 'assay', 'inhibit', 'treat', 'promote', 'anti', 'mediate', 'suppress', 'cellular', "addres", "identification", "poorly", "confirm", "extent", "strongly", "distinct", "moreover", "experimental", "mrna", "cdna", "overexpression", "inhibited", "attenuated", "transcriptional", "knockdown", "proccesing", "intracellular", "dataset", "polymorphism", "phenotype", "subunit", "mediate", "understand", "wether", "constitutively", "homologues", "determinant", "transiently", "blot", "recombinant", "modulate", "nucleotide",
                   "polypeptide", "putative", "homologous", "exon", "elucidate", "concomitant", "homolog", "chromosomal", "loci", "biomarker", "causative", "overexpressed", "recombination", "inducible", "mechanistically", "ubiquitously", "correlate", "subtype", "determinant", "perturbation", "implicate", "cluster", "probands", "counteract", "overlap", "supplementation", "alternation", "underrepresented", "transfected", "upregulated", "homology", "differentially", "uncharacterized", "upregulation", "quantitation", "colocalization", "localization", "orthologue", "ortholog", "downregulated", "category", "composition", "primer", "linkage", "conservation", "diversity", "canonical", "administration", "intrinsic", "structurally", "soluble", "comprenhensive", "availability", "adaptation", "confer", "highest", "reactive", "pool", "prepare", "vector", "situ", "classical", "classification", "coordinate", "independently", "positively", "null", "localize", "specie", "termini", "deduce", "effector", "discus", "activity", "require", "thousand", "protein", "typically", "occur", "essential", "demonstrate", "component", "active", "initial", "reduce", "train", "context", 'μmol', 'μm', 'μg', 'µm', 'yr', 'yield', 'wo', 'widespread', 'widely', 'wide', 'whereas', 'weak', 'volume', 'vivo', 'vitro', 'via', 'versus', 'verify', 'vary', 'variety', 'variation', 'variant', 'variance', 'variable', 'variability', 'valuable', 'validate', 'utilize', 'utilization', 'utility', 'useful', 'uptake', 'upper', 'update', 'unlike', 'unknown', 'unite', 'unit', 'unique', 'underlie', 'undergo', 'unclear', 'uncertainty', 'un', 'ultimately', 'ubiquitous', 'sub', 'sup', 'gene', 'suggest', 'sample', 'analysis', 'identify', 'associate', 'indicate', 'variation', 'concentration', 'impact', 'genetic', 'relate', 'distribution', 'compare', 'affect', 'factor', 'sequence', 'sp', 'condition', 'scale', 'describe', 'reveal', 'method', 'interaction', 'significantly', 'investigate', 'influence', 'mechanism', 'acid', 'function', 'observe', 'genus', 'approach', 'significant', 'abundance', 'decrease', 'analyse', 'expression', 'determine', 'measure', 'limit', 'examine', 'relative', 'remain', 'collect', 'induce', 'experiment', 'strategy', 'molecular', 'estimate', 'sit', 'target', 'respectively', 'nutrient', 'dynamic', 'content', 'protect', 'evolution', 'wild', 'global', 'predict', 'multiple', 'presence', 'dna', 'resource', 'develop', 'organism', 'taxa', 'novel', 'positive', 'consider', 'evolutionary', 'contribute', 'improve', 'phylogenetic', 'signal', 'native', 'evaluate', 'addition', 'ratio', 'produce', 'hypothesis', 'involve', 'represent', 'characterize', 'enhance', 'highly', 'detect', 'focus', 'functional', 'importance', 'compound', 'overall', 'differ', 'le', 'greater', 'highlight', 'negative', 'copyright', 'combine', 'lineage', 'biological', 'exhibit', 'reduction', 'correlation', 'occurrence', 'consistent', 'quantify', 'aim', 'combination', 'conduct', 'analyze', 'pathway', 'lack', 'ability', 'explain', 'challenge', 'flow', 'effective', 'previously', 'perform', 'propose', 'isolate', 'explore', 'transmission', 'maintain', 'length', 'despite', 'establish', 'stable', 'facilitate', 'furthermore', 'dependent', 'enzyme', 'consequence', 'potentially', 'mg', 'feature', 'profile', 'quantitative', 'select', 'monitor', 'tool', 'relatively', 'comparison', 'link', 'framework', 'distance', 'evolve', 'genomic']
    return stoponegram + stopwords.words('english')
