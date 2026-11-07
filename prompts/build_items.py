# -*- coding: utf-8 -*-
import json
import os

here = os.path.dirname(os.path.abspath(__file__))
prompts_dir = here if os.path.basename(here) == "prompts" else os.path.join(here, "site", "prompts")
os.makedirs(prompts_dir, exist_ok=True)

# Shared labels. Each item references these by key to keep copy consistent.
INPUT = {
    "photo": ("1 张照片", "1 photo"),
    "travel": ("1 张旅行照", "1 travel photo"),
    "photos": ("1 张或多张照片", "1+ photos"),
    "photo-ref": ("照片 + 参考图", "Photo + ref"),
    "photo-text": ("人物照 + 文字", "Photo + text"),
    "text": ("一句文字", "Text"),
    "theme": ("主题 + 可选参考图", "Theme + optional ref"),
    "photo-or-theme": ("照片或主题", "Photo or theme"),
    "copy": ("文案", "Copy"),
    "raw": ("RAW / JPEG", "RAW / JPEG"),
    "link": ("外链", "Link"),
}
RUNTIME = {
    "gpt": ("GPT 直出", "GPT direct"),
    "script": ("本地脚本", "Local script"),
    "codex": ("本地 Codex", "Local Codex"),
    "render": ("本地渲染", "Local render"),
    "site": ("网站", "Site"),
    "post": ("原帖", "Post"),
    "repo": ("仓库", "Repo"),
}
LICENSE = {
    "own": ("自有 · 可公开", "Own · public"),
    "mit": ("MIT", "MIT"),
    "none": ("无授权声明", "No license grant"),
    "nc": ("仅个人非商用", "Personal, non-commercial"),
    "agpl": ("AGPL-3.0", "AGPL-3.0"),
    "source": ("Source-Available 1.0", "Source-Available 1.0"),
    "works": ("作品禁未授权复用", "No unauthorized reuse"),
    "link": ("外链", "External link"),
}
DISCOVERY = {
    "": ("", ""),
    "x": ("X 原帖", "X post"),
    "douyin": ("抖音图文", "Douyin note"),
    "xhs": ("小红书", "Xiaohongshu"),
    "fork": ("GitHub Fork", "GitHub fork"),
}
COPY_LABEL = {
    "prompt": ("复制提示词", "Copy prompt"),
    "invoke": ("复制调用口令", "Copy invocation"),
    "link": ("复制链接", "Copy link"),
}

# (kind-specific) items. gallery rows are (file, label_zh, label_en).
RAW = [
    {
        "id": "gpt-editorial-gouache-poster",
        "kind": "prompt",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "photo",
        "runtime": "gpt",
        "license": "own",
        "license_tier": "own",
        "discovery": "",
        "copy_label": "prompt",
        "title_zh": "照片 × 手绘水粉版画对照海报",
        "title_en": "Photo × editorial gouache print poster",
        "summary_zh": "风景上下 50:50、人像左右 40:60 分割，原片与哑光水粉版画对照。",
        "summary_en": "Auto-splits 50:50 horizontally for landscapes or 40:60 vertically for portraits, pairing the photo with a matte gouache print.",
        "aspect": "3:4",
        "author": "Juns",
        "source_url": "",
        "discovery_url": "",
        "gallery": [
            [
                "gouache-editorial-wanaka.jpg",
                "瓦纳卡孤树实测",
                "Wanaka Tree"
            ]
        ],
        "palette": [
            "#5d7c99",
            "#7b8449",
            "#f2ece1"
        ],
        "copy_text": "将上传的参考照片制作成一张高端极简主义编辑风格海报，画面比例为3:4竖版。\n【版式自动选择】\n根据照片主体自动判断，只使用一种布局。若为风景、建筑、静物或物品照片，采用水平50:50分割构图：上半部分原始照片，下半部分同一主题手绘水粉版画。若为人物或人像照片，采用不对称垂直分割构图：左侧约40%原始照片，右侧约60%同一人物手绘水粉版画。不得同时使用两种布局。\n【原始照片区域】\n最大程度保持照片本身不变。完整保留主体、构图、比例、空间关系、姿态、轮廓、材质、光影、色彩与整体氛围。禁止改变主体比例、人物姿态、建筑结构、物体形态、构图关系和视觉比例。禁止放大、裁剪、拉伸、压缩、变形、重新构图、改变透视、改变姿势，或为填满版面强行放大主体。若照片比例与海报区域不匹配，只允许自然扩展主体周围背景，绝对不能裁剪或改变主体。照片区域保持真实摄影质感，与另一侧或下方的水粉版画形成“真实摄影×手工绘画”的明显对照。\n【水粉版画区域】\n将原始照片中的同一主体重新诠释为平面手绘水粉版画、Editorial Gouache Illustration、Contemporary Art Print。保持主体原有整体轮廓、基本比例、主要结构、姿态动作与关键识别特征。将真实摄影转化为高度概括的平面手绘水粉语言，用简洁的大面积平面色块表现主体，通过形状、轮廓和色块叠加关系建立结构。避免写实、卡通化和标准矢量插画效果。水粉主体应独立、克制、适中，约占所在区域可用宽度或高度的50–55%。主体必须精确居中，四周保持均衡负空间，不接触边缘、不靠近边缘、不被裁切、不过度放大。整体呈现高端艺术杂志、设计画册、独立艺术出版物中的手工版画作品感。\n【水粉材质】\n必须具有真实手工绘画痕迹：可见自然笔触、略不均匀颜料密度、干刷痕迹、局部纸张裸露、细微羽状边缘、断裂轮廓、轻微颜料堆积和自然手绘不规则。呈现不透明、哑光、手工绘制、纸张印刷般的水粉质感。避免过度精细和过度光滑，保留少量自然人工痕迹。",
        "slots_zh": [],
        "notes_zh": [
            "无需填槽，上传风景或人像照片即可自动选择上下 50:50 或左右 40:60 构图。",
            "强调哑光干刷、纸张裸露与色块概括，避免数码滤镜感。"
        ],
        "notes_en": [
            "Zero-slot prompt: upload any landscape or portrait photo and it selects 50:50 horizontal or 40:60 vertical split automatically.",
            "Emphasizes dry-brush matte gouache and exposed paper margins."
        ]
    },
    {
        "id": "gpt-shadow-puppet-poster",
        "kind": "prompt",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "photo",
        "runtime": "gpt",
        "license": "link",
        "license_tier": "external-link",
        "discovery": "x",
        "copy_label": "prompt",
        "title_zh": "照片 → 东方皮影戏偶双联海报",
        "title_en": "Photo → shadow puppet diptych poster",
        "summary_zh": "上半保留原图，下半将主体转译为暖光宣纸幕布上的半透明皮影戏偶。",
        "summary_en": "Top half keeps the original photo; bottom half reinterprets the subject as a translucent Chinese shadow puppet on a warm lit screen.",
        "aspect": "3:4",
        "author": "@daaihq",
        "source_url": "https://x.com/daaihq/status/2112897710147977271",
        "discovery_url": "https://x.com/daaihq/status/2112897710147977271",
        "gallery": [
            [
                "shadow-puppet-1.jpg",
                "作者示例 1",
                "Example 1"
            ],
            [
                "shadow-puppet-2.jpg",
                "作者示例 2",
                "Example 2"
            ]
        ],
        "palette": [
            "#c87d45",
            "#2b2118",
            "#f3e5c8"
        ],
        "copy_text": "请将我上传的每一张照片分别制作成一张独立的高级设计海报，不多图拼接，每张照片单独输出。整体采用 3:4 竖版构图，上下两个区域高度严格 1:1，各占画面 50%。\n\n上半部分保留原始照片，保持主体身份、结构、姿态、真实质感、自然光影与原有色彩氛围，仅进行轻微高级调色，使其具有艺术摄影与东方展览图像质感。为适配画幅，可自然扩展环境背景，但不得拉伸、扭曲或改变主体。\n\n下半部分提取照片中最具识别性的主体、轮廓、姿态与叙事关系，重构为一具中国传统皮影戏偶 / shadow puppet，在一面被暖光照亮的半透明宣纸幕布上演出。无论原图是人物、动物、建筑、植物、器物还是风景，都被理解为一个“可以被操纵的角色”：主体被拆分为少量关节部件，以铆钉相连，姿态取自原照片中最有表情的那个瞬间，并配有一两根细长的操纵竹签自画面下方伸入。\n\n不要写实描绘，不要卡通化，而是用皮影的造型语法重新概括：侧面化、平面化、装饰性镂空、云纹与几何雕刻纹样、局部的半透明彩染。保留原物最具识别度的特征，使观者一眼认出，同时感到它被一位老手艺人重新理解和雕刻过。\n\n光影是这件作品的灵魂：幕布后方一盏暖色灯光，使皮影的镂空处透出温暖光点，彩染部分呈现半透明的朱红、靛青、橄榄绿与琥珀黄，皮影边缘带有柔和的投影虚边和轻微光晕，仿佛正在缓慢移动。可以有极轻微的双影或动态虚影，表现戏偶正在演出的一瞬间。\n\n构图以一幕一偶 + 大量留白为核心。幕布是一片温暖的米黄或浅琥珀色光场，四周自然暗下，主体只占画面约25%–35%，可偏心或位于黄金分割位置，其余空间保持安静，像戏开场前的停顿。不出现观众、舞台全景或复杂道具。\n\n配色从上方照片中提取 2–3 种最具情绪价值的颜色，转译为皮影彩染的半透明色，与暖灯光场统一；阴影使用深褐与暖墨色，而不是冷黑。\n\n文字少量介入，可以竖排小字的方式写一个“戏名”或一句短句，像戏班手写的节目单，安静落在幕布一角，不限制语种。\n\n整体呈现皮影镂刻、半透明彩染、暖灯幕布、柔和投影与东方留白共同构成的光影视觉。核心原则是：把照片里的主角请上幕布，让它用一个姿态演完一整出戏。避免完整写实、满场景堆砌、廉价国潮、塑料质感、3D渲染、卡通感和模板化海报。\n\n（来源原帖：https://x.com/daaihq/status/2112897710147977271）",
        "slots_zh": [],
        "notes_zh": [
            "来自 X 书签收藏（@daaihq），人像、宠物、建筑或器物照片均可直接投喂。"
        ],
        "notes_en": [
            "From X bookmarks (@daaihq); works with portraits, pets, architecture, or objects."
        ]
    },
    {
        "id": "gpt-monet-oil-comparison",
        "kind": "prompt",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "photos",
        "runtime": "gpt",
        "license": "link",
        "license_tier": "external-link",
        "discovery": "x",
        "copy_label": "prompt",
        "title_zh": "旅行照 → 莫奈印象派油画装裱对照",
        "title_en": "Travel photo → Monet impressionist oil comparison",
        "summary_zh": "保留原图结构与光影，生成莫奈厚涂油画并装裱在暖白画纸上对照输出。",
        "summary_en": "Preserves the original photo and pairs it with a Monet-style impressionist oil painting mounted on warm gallery paper.",
        "aspect": "自适应横竖",
        "author": "@alin_zone",
        "source_url": "https://x.com/alin_zone/status/2092526611560280365",
        "discovery_url": "https://x.com/alin_zone/status/2092526611560280365",
        "gallery": [
            [
                "monet-oil-1.jpg",
                "作者示例 1",
                "Example 1"
            ],
            [
                "monet-oil-2.jpg",
                "作者示例 2",
                "Example 2"
            ]
        ],
        "palette": [
            "#5e7d69",
            "#d4a86a",
            "#f7f4ee"
        ],
        "copy_text": "请批量处理我本次上传的所有图片。\n\n无论我上传一张还是多张图片，都要按照上传顺序逐张独立处理。每张原图分别生成一张莫奈风格效果图，再分别制作成一张“原图＋效果图”对照成品。\n\n第一步：保留原图\n将当前处理的原图完整保留，作为最终对照成品中的“原图区域”。原图区域必须保持原始内容，不得重绘、风格化、美化、调色、裁切、拉伸、模糊或改变任何物体。\n\n第二步：生成莫奈风格效果图\n以当前原图为唯一内容依据，生成一张莫奈式印象派油画效果图。\n要求：严格保留原图的画幅比例、构图、视角、主体位置、地平线和主要几何结构。只改变画面媒介、色彩、光线质感和笔触，不改变原图所表现的内容。使用手绘油画质感：可见的断续笔触、柔和边缘、空气透视、明亮分色和自然的画布肌理。阴影使用蓝绿、淡紫或冷灰色，避免纯黑。不得添加文字、签名、水印、Logo、相框或原图中不存在的物体。\n\n第三步：制作独立对照成品\n将当前未经修改的原图和对应的莫奈风格效果图，排版到一张独立的暖白色画布（#F7F4EE）上：\n- 横版图片：上下排列，上方放原图，下方放莫奈油画效果图。\n- 竖版或正方形图片：左右排列，左侧放原图，右侧放莫奈油画效果图。\n四周保留约短边 4% 的均匀留白，两图之间保留 4% 间隔，每张图外沿加极细浅暖灰描边（#E5E0D7）。\n\n（来源原帖：https://x.com/alin_zone/status/2092526611560280365）",
        "slots_zh": [],
        "notes_zh": [
            "来自 X 书签收藏（@alin_zone），会根据原片横竖自动切换上下或左右装裱。"
        ],
        "notes_en": [
            "From X bookmarks (@alin_zone); auto-switches between vertical stack for landscape photos and side-by-side for portraits."
        ]
    },
    {
        "id": "gpt-photo-shape-translation",
        "kind": "prompt",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "photo",
        "runtime": "gpt",
        "license": "link",
        "license_tier": "external-link",
        "discovery": "xhs",
        "copy_label": "prompt",
        "title_zh": "照片借形转译（风景纹理入自然轮廓）",
        "title_en": "Photo shape translation into organic silhouette",
        "summary_zh": "提炼照片核心纹理与明暗节奏，重组填入匹配的鱼、鸟、树叶等自然轮廓中。",
        "summary_en": "Distills 2–4 core textures and lighting rhythms from a photo and reorganizes them inside a matching organic silhouette.",
        "aspect": "3:4 / 自适应",
        "author": "@李德月与电子羊",
        "source_url": "https://www.xiaohongshu.com/explore/6a76fb3f000000002c001fc5",
        "discovery_url": "https://www.xiaohongshu.com/explore/6a76fb3f000000002c001fc5",
        "gallery": [
            [
                "xhs-shape-translation-1.jpg",
                "小红书原帖示例",
                "XHS Example"
            ]
        ],
        "palette": [
            "#2b4a5e",
            "#d8cfc2",
            "#f7f6f2"
        ],
        "copy_text": "请将上传的照片作为唯一视觉内容来源，创作一张具有艺术感和平面设计感的“照片借形转译”作品。\n不要简单给照片加滤镜，也不要把照片完整重画。\n请先从原照片中提取最有代表性的 2—4 个核心视觉特征，例如：纹理、明暗起伏、色彩渐变、光点、波纹、边界走势、颗粒感、自然节奏、空间方向、重复结构。\n不要平均保留全部内容，应主动删减次要信息，避免画面过碎。\n然后将这些视觉信息重新组织，填充进一个清晰的【生物 / 自然物体，如：鲸鱼 / 飞鸟 / 银杏叶，或留给模型自动匹配】轮廓之中，使原本的风景转化为新的视觉形象。\n【目标轮廓】应尽量与原照片气质匹配，例如：海面适合鱼 / 鲸鱼 / 水母，天空适合鸟 / 云 / 蝴蝶，树影适合鹿 / 树 / 叶子。\n生成结果应体现“原照片内容仍然可感知，但整体已经转化为一个新的轮廓形象”的效果。\n风格要求如下：\n- 整体偏艺术化、克制、安静，带有现代平面设计感\n- 主体置于大面积留白背景中，背景建议为白色、暖白色或极浅灰色\n- 不要做成普通剪影，也不要做成写实插画；不要只是把照片硬塞进轮廓里，要保留自然纹理的流动感与图像内部的层次\n- 可以加入适度的切片、重复、错位、阶梯边缘、分帧叠片效果，让画面更有设计语言\n- 构图简洁，主体居中或偏中部，最终效果像一张兼具摄影、图形设计与视觉转译意味的艺术海报\n\n（来源小红书收藏：https://www.xiaohongshu.com/explore/6a76fb3f000000002c001fc5）",
        "slots_zh": [
            "【生物 / 自然物体轮廓】如：海面填鲸鱼/水母、天空填飞鸟/蝴蝶，也可不改让模型自选"
        ],
        "notes_zh": [
            "来自小红书收藏（@李德月与电子羊），纯提示词直出，适合海面、云层、森林等有肌理感的风景照。"
        ],
        "notes_en": [
            "From Xiaohongshu favorites; works especially well on textured landscapes like ocean waves, clouds, or foliage."
        ]
    },
    {
        "id": "gpt-pyramids-editorial-diptych",
        "kind": "prompt",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "travel",
        "runtime": "gpt",
        "license": "own",
        "license_tier": "own",
        "discovery": "",
        "copy_label": "prompt",
        "title_zh": "旅行照片 → 上下双联展览海报",
        "title_en": "Travel photo → editorial diptych",
        "summary_zh": "一张旅行照进，上半保留原图，下半提炼同色系几何抽象。",
        "summary_en": "One travel photo in; the photo on top, a geometric abstract in its palette below.",
        "aspect": "4:5",
        "author": "Juns",
        "source_url": "https://github.com/ZzzLc0405/photo-abstract-editorial",
        "discovery_url": "",
        "gallery": [
            [
                "own-pyramids-editorial.jpg",
                "实测",
                "My test"
            ],
            [
                "photo-abstract-editorial-author.jpg",
                "作者示例",
                "Author"
            ]
        ],
        "palette": [
            "#d6a96a",
            "#3a4e63",
            "#f3efe6"
        ],
        "copy_text": "Create a vertical 4:5 editorial exhibition diptych poster based on the attached photograph:\n\n1. Upper Panel (top 55%): Keep the original photograph's scene, lighting, horizon, and subject composition intact with clean gallery framing.\n2. Lower Panel (bottom 45%): On a warm archival paper background, construct a minimalist geometric abstract study distilled strictly from the upper photograph's dominant color palette, horizon line, and structural proportions (inspired by Rothko / Albers / Bauhaus print design).\n3. Typography: Add restrained, small-scale Swiss editorial microtype in the margin — a short title「【填入地点或主题，如：GIZA · SILENT STONE】」, coordinates or year「【如：2026 ARCHIVE】」, and a 3-color palette swatch bar.\n4. Keep the layout calm, museum-grade, with generous paper breathing room and zero watermarks or messy text.\n\n（参考原仓库：https://github.com/ZzzLc0405/photo-abstract-editorial）",
        "slots_zh": [
            "【地点或主题】如：GIZA · SILENT STONE / GREAT OCEAN ROAD",
            "【年份或注记】如：2026 ARCHIVE / 38°40'S 143°06'E"
        ],
        "notes_zh": [
            "上半张也会被模型重绘，原片像素不保证不变。",
            "要像素零改动，改用「上片下画」本地精拼版。参考仓库无授权声明。"
        ],
        "notes_en": [
            "GPT re-renders the whole canvas, so the top photo is not pixel-identical.",
            "For an untouched top photo, use the local Travel Photo Abstraction skill. The reference repo grants no license."
        ]
    },
    {
        "id": "gpt-cinema-dna-triptych",
        "kind": "prompt",
        "input_mode": "text",
        "runtime_mode": "gpt-direct",
        "input": "text",
        "runtime": "gpt",
        "license": "own",
        "license_tier": "own",
        "discovery": "",
        "copy_label": "prompt",
        "title_zh": "21:9 电影三联静帧",
        "title_en": "21:9 cinematic triptych",
        "summary_zh": "一句故事设定进，先拆三个镜头，再依次出三张 21:9 胶片静帧。",
        "summary_en": "A one-line story in; three connected 21:9 film frames out, planned shot by shot.",
        "aspect": "21:9 ×3",
        "author": "dacnay816y62-hub",
        "source_url": "https://github.com/dacnay816y62-hub/cinema-dna-21x9x3",
        "discovery_url": "",
        "gallery": [
            [
                "cinema-dna-21x9x3.jpg",
                "示例 1",
                "Example 1"
            ],
            [
                "cinema-dna-21x9x3-2.jpg",
                "示例 2",
                "Example 2"
            ]
        ],
        "palette": [
            "#1d2b36",
            "#c48d52",
            "#476056"
        ],
        "copy_text": "我将给你一句故事或场景设定：【在这里填入一句故事、时代地点与人物关系，例如：梅雨季傍晚的旧书店走廊，两个避雨的人隔着玻璃窗看外面的电车驶过】\n\n请按 21:9 真人电影静帧（CinemaScope 35mm film still）规范，分两步帮我生成：\n第一步：先列出三张镜头的叙事递进（Shot 1 空间与气压建立 → Shot 2 人物关系与动作中景 → Shot 3 关键物件或眼神情绪特写），固定同一套色温、胶片颗粒、光源方向与年代质感，不指名抄袭具体商业电影或演员。\n第二步：依次生成三张独立的宽幅电影静帧（不要在一张图里加乱码字幕或粗劣边框）。如果需要合成三联竖图，等三张单帧确认后再拼。\n\n（参考原仓库：https://github.com/dacnay816y62-hub/cinema-dna-21x9x3）",
        "slots_zh": [
            "【一句故事/时代地点/人物】如：梅雨季傍晚的旧书店走廊，两个避雨的人隔着玻璃窗看外面的电车驶过"
        ],
        "notes_zh": [
            "分三张单帧出图，比挤进一张竖图更能保持人物与光影连续。",
            "需要宣发主图时，再追加一张 3:4 电影海报。"
        ],
        "notes_en": [
            "Three separate frames hold character and light better than one stacked image.",
            "Add a 3:4 key-art poster only when you need one."
        ]
    },
    {
        "id": "gc-minimal-zine-poster",
        "kind": "skill",
        "input_mode": "text",
        "runtime_mode": "gpt-direct",
        "input": "theme",
        "runtime": "gpt",
        "license": "mit",
        "license_tier": "mit",
        "discovery": "",
        "copy_label": "invoke",
        "title_zh": "极简独立杂志海报",
        "title_en": "Minimal zine poster",
        "summary_zh": "输入主题或参考图，得到大留白、单焦点的杂志感海报提示词。",
        "summary_en": "A theme or reference image in; a whitespace-heavy, single-focus zine poster prompt out.",
        "aspect": "3:4 / 4:5",
        "author": "LiamGvchi",
        "source_url": "https://github.com/LiamGvchi/gc-minimal-zine-poster",
        "discovery_url": "",
        "gallery": [
            [
                "gc-minimal-zine-poster.jpg",
                "作者示例",
                "Author"
            ]
        ],
        "palette": [
            "#e9e6df",
            "#24303c",
            "#8f9489"
        ],
        "copy_text": "用 gc-minimal-zine-poster 风格做一张 3:4 独立杂志感竖版海报，主题是「【填入主题，如：台风过境后的海边清晨】」，保持大面积纸张留白、单一视觉重心和克制的编辑部小字，不要堆砌装饰元素。\n\n（Skill 仓库：https://github.com/LiamGvchi/gc-minimal-zine-poster）",
        "slots_zh": [
            "【海报主题与情绪】如：台风过境后的海边清晨 / 深夜便利店的暖光"
        ],
        "notes_zh": [
            "拆成样式系统、提示词编译、变体发散和质检几个模块。",
            "MIT 许可，可交给本地 Codex 运行，或把 SKILL.md 贴进网页版 ChatGPT。"
        ],
        "notes_en": [
            "Split into a style system, prompt compiler, variation engine and quality gate.",
            "MIT. Run it in local Codex, or paste SKILL.md into ChatGPT web."
        ]
    },
    {
        "id": "photo-revival",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "photo",
        "runtime": "gpt",
        "license": "mit",
        "license_tier": "mit",
        "discovery": "x",
        "copy_label": "invoke",
        "title_zh": "旧照诗意白纸重绘",
        "title_en": "Photo Revival",
        "summary_zh": "一张生活照进，得到大面积留白、小主体插画的手绘纸页。",
        "summary_en": "An everyday photo in; a small illustrated subject on a mostly blank paper page.",
        "aspect": "原图 / 3:4",
        "author": "dacnay816y62-hub",
        "source_url": "https://github.com/dacnay816y62-hub/photo-revival",
        "discovery_url": "https://x.com/oran_ge/status/2087818420150731057?s=46",
        "gallery": [
            [
                "photo-revival.jpg",
                "示例 1",
                "Example 1"
            ],
            [
                "photo-revival-2.jpg",
                "示例 2",
                "Example 2"
            ]
        ],
        "palette": [
            "#f7f5f0",
            "#c93b2b",
            "#2d2d2a"
        ],
        "copy_text": "按 photo-revival 工作流处理这张照片：保留原片核心主体与动态特征，转化为大面积白纸留白（70%以上留白）、小主体比例的温暖插画纸页，不加多余背景杂物；手写字仅保留【填入短句，或写：不加任何文字】。\n\n（Skill 仓库：https://github.com/dacnay816y62-hub/photo-revival）",
        "slots_zh": [
            "【手写短句或无字】如：保留一句简短英文注记 / 完全不加文字"
        ],
        "notes_zh": [
            "要点是小主体加 70% 以上留白，别让模型画满画布。",
            "出图后检查主体比例、白底是否干净、手写字有无拼写错误。"
        ],
        "notes_en": [
            "Key look: a small subject in over 70% blank paper. Keep the model from filling the canvas.",
            "Check subject scale, a clean white ground and handwriting spelling."
        ]
    },
    {
        "id": "photo-to-zine-postcard",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "photo",
        "runtime": "gpt",
        "license": "mit",
        "license_tier": "mit",
        "discovery": "",
        "copy_label": "invoke",
        "title_zh": "照片转正反双面明信片",
        "title_en": "Photo → zine postcard",
        "summary_zh": "一张照片进，不裁切，得到正反两面的独立出版风明信片。",
        "summary_en": "A photo in, uncropped; a front-and-back zine-style postcard out.",
        "aspect": "Front + back",
        "author": "Whiplashzeb",
        "source_url": "https://github.com/Whiplashzeb/photo-to-zine-postcard",
        "discovery_url": "",
        "gallery": [
            [
                "photo-to-zine-postcard.jpg",
                "示例 1",
                "Example 1"
            ],
            [
                "photo-to-zine-postcard-2.jpg",
                "示例 2",
                "Example 2"
            ]
        ],
        "palette": [
            "#eef1ee",
            "#2c5e63",
            "#886f58"
        ],
        "copy_text": "用 photo-to-zine-postcard 风格把这张照片做成正反双面独立明信片：保持原照片完整比例不裁切，提取照片里的主色调做背面线条与邮戳点缀，地点/日期写「【填入地点与日期】」。\n\n（Skill 仓库：https://github.com/Whiplashzeb/photo-to-zine-postcard）",
        "slots_zh": [
            "【地点与日期】如：Lake Tekapo · 2026.11"
        ],
        "notes_zh": [
            "适合旅行风光归档：原片不裁切、不改透视，靠纸边距和字重出质感。"
        ],
        "notes_en": [
            "Suits travel landscapes: the photo is never cropped or re-perspectived."
        ]
    },
    {
        "id": "make-photo-stamp-archive",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "photo",
        "runtime": "gpt",
        "license": "mit",
        "license_tier": "mit",
        "discovery": "douyin",
        "copy_label": "invoke",
        "title_zh": "档案邮票卡",
        "title_en": "Photo stamp archive",
        "summary_zh": "一张照片进，得到带齿孔、骑缝章和编号的米色档案邮票卡。",
        "summary_en": "A photo in; an archive stamp card with perforated edges, cancel mark and catalog number.",
        "aspect": "Portrait / square",
        "author": "Dlcccc71913",
        "source_url": "https://github.com/Dlcccc71913/skill-make-photo-stamp-archive",
        "discovery_url": "https://www.douyin.com/note/7674260868216938313",
        "gallery": [
            [
                "make-photo-stamp-author.jpg",
                "作者示例",
                "Author"
            ],
            [
                "make-photo-stamp-author-2.jpg",
                "示例 2",
                "Example 2"
            ],
            [
                "own-stamps-archive.jpg",
                "实测",
                "My test"
            ]
        ],
        "palette": [
            "#f3efe4",
            "#b5382a",
            "#2b2b28"
        ],
        "copy_text": "用 make-photo-stamp-archive 风格把这张照片做成收藏级档案邮票卡：保留原片主体与光影，外圈做干净的邮票齿孔边框与浅米色档案底纸，角落加一枚克制的骑缝邮戳与编号「【填入编号或地点，如：NO. 042 · AUTUMN】」。\n\n（Skill 仓库：https://github.com/Dlcccc71913/skill-make-photo-stamp-archive）",
        "slots_zh": [
            "【档案编号与注记】如：NO. 042 · HANGZHOU"
        ],
        "notes_zh": [
            "上游仓库附完整英文提示词模板，可直接复制到 ChatGPT。"
        ],
        "notes_en": [
            "The upstream repo ships a full English prompt template you can paste into ChatGPT."
        ]
    },
    {
        "id": "photo-to-organic-knit",
        "kind": "skill",
        "input_mode": "photo-ref",
        "runtime_mode": "local-codex",
        "input": "photo-ref",
        "runtime": "codex",
        "license": "mit",
        "license_tier": "mit",
        "discovery": "douyin",
        "copy_label": "invoke",
        "title_zh": "照片转毛线针织海报",
        "title_en": "Photo → organic knit poster",
        "summary_zh": "照片加内置材质图进，提取视觉锚点，重构成毛线针织艺术海报。",
        "summary_en": "A photo plus a bundled texture reference in; a knitted-wool art poster out.",
        "aspect": "Source ratio",
        "author": "NalaZhang27",
        "source_url": "https://github.com/NalaZhang27/photo-to-organic-knit",
        "discovery_url": "https://www.douyin.com/note/7674260868216938313",
        "gallery": [
            [
                "photo-to-organic-knit.jpg",
                "示例 1",
                "Example 1"
            ],
            [
                "photo-to-organic-knit-2.jpg",
                "示例 2",
                "Example 2"
            ],
            [
                "own-organic-knit.jpg",
                "实测",
                "My test"
            ]
        ],
        "palette": [
            "#ebe4d8",
            "#3c5a47",
            "#c96a4b"
        ],
        "copy_text": "用 photo-to-organic-knit 工作流处理这张照片：同时附带仓库内置的 style-reference.png 仅作毛线纤维质感参考（不复制参考图里的火车和山丘），保留原片构图锚点，标题用 2–4 个英文词「【填入短英文或写无字】」。\n\n（Skill 仓库：https://github.com/NalaZhang27/photo-to-organic-knit）",
        "slots_zh": [
            "【2–4词英文短标题】如：SOFT HORIZON（或注明完全无文字）"
        ],
        "notes_zh": [
            "必须同时提供照片和仓库里的材质参考图，只给文字会变成塑料感黏土。",
            "参考图只借毛线质感，不复制其中的火车和山丘。"
        ],
        "notes_en": [
            "Supply both the photo and the repo's style-reference.png, or the result turns into plastic clay.",
            "The reference sets yarn texture only; its train and hills are not copied."
        ]
    },
    {
        "id": "paint-beyond-the-frame-shunan",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "local-script",
        "input": "photo",
        "runtime": "script",
        "license": "none",
        "license_tier": "private-eval",
        "discovery": "",
        "copy_label": "invoke",
        "title_zh": "镜外生境：向右延展插画",
        "title_en": "Paint beyond the frame",
        "summary_zh": "左侧原照片像素锁定，右侧延展成混合媒介插画，并逐像素校验。",
        "summary_en": "A photo in; the left stays pixel-locked, the right extends into a mixed-media painting, verified.",
        "aspect": "Wide",
        "author": "SkyNone",
        "source_url": "https://github.com/SkyNone/paint-beyond-the-frame-shunan",
        "discovery_url": "",
        "gallery": [
            [
                "paint-beyond-panda-author.jpg",
                "作者示例",
                "Author"
            ],
            [
                "own-paint-beyond-ocean.jpg",
                "实测 1",
                "My test 1"
            ],
            [
                "own-paint-beyond-longbridge.jpg",
                "实测 2",
                "My test 2"
            ]
        ],
        "palette": [
            "#2b4c65",
            "#d99b66",
            "#f2ece1"
        ],
        "copy_text": "用 paint-beyond-the-frame-shunan（镜外生境）工作流处理这张照片：先运行 protect_photo_extension.py prepare 生成扩展画布，向右延展混合媒介插画，最后运行 restore 和 verify 确保左侧原照片受保护列像素 100% 不变。\n\n（Skill 仓库：https://github.com/SkyNone/paint-beyond-the-frame-shunan）",
        "slots_zh": [
            "【本地原片路径】如：传入照片路径，指定延展风格偏水彩或彩铅手绘"
        ],
        "notes_zh": [
            "先 prepare，生图后 restore、verify，SHA-256 校验左侧原片不变。",
            "适合不容 AI 改动人脸与细节的原片；本地需 Python 和 Pillow。"
        ],
        "notes_en": [
            "Flow: prepare, generate, restore, verify. SHA-256 confirms the left photo is unchanged.",
            "For originals whose faces and details must not change. Needs local Python and Pillow."
        ]
    },
    {
        "id": "travel-photo-abstraction",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "local-script",
        "input": "photo",
        "runtime": "script",
        "license": "source",
        "license_tier": "source-available",
        "discovery": "",
        "copy_label": "invoke",
        "title_zh": "旅行照上片下画 · 本地精拼",
        "title_en": "Travel photo abstraction",
        "summary_zh": "上半幅是未改动的原照片，下半幅生成抽象画板，本地脚本拼合并校验。",
        "summary_en": "The original photo stays untouched on top; an abstract panel is generated below, then merged and verified locally.",
        "aspect": "Diptych",
        "author": "Evianis",
        "source_url": "https://github.com/Evianis/travel-photo-abstraction",
        "discovery_url": "",
        "gallery": [
            [
                "travel-photo-abstraction.jpg",
                "示例 1",
                "Example 1"
            ],
            [
                "travel-photo-abstraction-2.jpg",
                "示例 2",
                "Example 2"
            ]
        ],
        "palette": [
            "#263849",
            "#d48c5c",
            "#eae5dc"
        ],
        "copy_text": "用 travel-photo-abstraction 工作流处理这张本地旅行照片：原照片只作上半幅且禁止进生成式重绘，单独生成下半幅抽象色块面板后，必须通过 finalize_artwork.py 合成并拿到 DELIVERY PASS 校验。\n\n（Skill 仓库：https://github.com/Evianis/travel-photo-abstraction）",
        "slots_zh": [
            "【本地原片路径】需提供本地原文件路径以通过像素校验"
        ],
        "notes_zh": [
            "finalize_artwork.py 校验上半幅原片未被改动、下半幅底色亮度均匀。",
            "需要本地原文件，才能做像素校验。"
        ],
        "notes_en": [
            "finalize_artwork.py checks the top photo is unmodified and the lower ground is even.",
            "Needs the local original file for pixel validation."
        ]
    },
    {
        "id": "photo-abstract-editorial",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "photo",
        "runtime": "gpt",
        "license": "none",
        "license_tier": "private-eval",
        "discovery": "",
        "copy_label": "invoke",
        "title_zh": "照片 + 抽象编辑双联画",
        "title_en": "Photo abstract editorial",
        "summary_zh": "一张照片进，纯提示词生成上片下画的展览感双联海报。",
        "summary_en": "A photo in; a prompt-only editorial diptych, photo above and abstraction below.",
        "aspect": "4:5",
        "author": "ZzzLc0405",
        "source_url": "https://github.com/ZzzLc0405/photo-abstract-editorial",
        "discovery_url": "",
        "gallery": [
            [
                "photo-abstract-editorial-author.jpg",
                "作者示例",
                "Author"
            ],
            [
                "own-pyramids-editorial.jpg",
                "实测",
                "My test"
            ]
        ],
        "palette": [
            "#c79b63",
            "#314456",
            "#f4f0e8"
        ],
        "copy_text": "用 photo-abstract-editorial 工作流处理这张照片，生成一张上片下画的展览感双联竖版海报，保留克制的画廊排印注记。\n\n（Skill 仓库：https://github.com/ZzzLc0405/photo-abstract-editorial）",
        "slots_zh": [
            "【照片与标题注记】可指定展览标题或留给模型自动提炼"
        ],
        "notes_zh": [
            "原仓库未给出授权，本页只链接，不转载其内容。",
            "仓库 references/ 内有中英文完整提示词模板。"
        ],
        "notes_en": [
            "The repo grants no license; this page only links to it.",
            "Its references/ folder holds full English and Chinese prompt templates."
        ]
    },
    {
        "id": "one-frame-one-metaphor",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "photo",
        "runtime": "gpt",
        "license": "none",
        "license_tier": "private-eval",
        "discovery": "",
        "copy_label": "invoke",
        "title_zh": "一帧一隐喻",
        "title_en": "One frame, one metaphor",
        "summary_zh": "一张照片进，围绕唯一一个视觉隐喻，重绘成艺术家书页版画。",
        "summary_en": "A photo in; one anchor, one metaphor, redrawn as a quiet artist-book print.",
        "aspect": "Portrait",
        "author": "estherliu-lab",
        "source_url": "https://github.com/estherliu-lab/one-frame-one-metaphor",
        "discovery_url": "",
        "gallery": [
            [
                "one-frame-one-metaphor.jpg",
                "作者示例",
                "Author"
            ],
            [
                "one-frame-city-orbit.jpg",
                "示例 2",
                "Example 2"
            ],
            [
                "own-one-frame.jpg",
                "实测",
                "My test"
            ]
        ],
        "palette": [
            "#dcd6ca",
            "#3f4d45",
            "#8c6d53"
        ],
        "copy_text": "用 one-frame-one-metaphor 工作流把这张照片转译为艺术家书页版画：只保留一个核心视觉隐喻（不要叠加多个脑洞），保留原片的一个结构锚点，底部加极小的诗意标题与档案编号。\n\n（Skill 仓库：https://github.com/estherliu-lab/one-frame-one-metaphor）",
        "slots_zh": [
            "【可选隐喻方向】如：把山脊纹理转译为树木年轮 / 把晚霞云层转译为针脚"
        ],
        "notes_zh": [
            "整张图只允许一个隐喻，色相与块面数量要克制。",
            "例：山脊纹理转成树木年轮。"
        ],
        "notes_en": [
            "One metaphor per image; keep hue and shape count restrained.",
            "e.g. a mountain ridge becomes tree rings."
        ]
    },
    {
        "id": "starryear-abstract-quartet",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "local-script",
        "input": "photo",
        "runtime": "script",
        "license": "works",
        "license_tier": "private-eval",
        "discovery": "douyin",
        "copy_label": "invoke",
        "title_zh": "现实 → 抽象 四联竖幅",
        "title_en": "Reality to abstraction quartet",
        "summary_zh": "一张照片进，输出四格纵向长图：现实、记忆、抽象、重构。",
        "summary_en": "A photo in; a 1:2 strip of four panels: reality, memory, abstraction, reinterpretation.",
        "aspect": "1:2",
        "author": "Starryear",
        "source_url": "https://github.com/Starryear/Starryear-Abstract-Quartet",
        "discovery_url": "https://www.douyin.com/note/7675053121186815077",
        "gallery": [
            [
                "starryear-abstract-quartet.jpg",
                "示例 1",
                "Example 1"
            ],
            [
                "starryear-abstract-quartet-2.jpg",
                "示例 2",
                "Example 2"
            ]
        ],
        "palette": [
            "#2b3a42",
            "#7a8b82",
            "#d9cfc1"
        ],
        "copy_text": "按 starryear-abstract-quartet 工作流处理这张照片：第 1 格直接裁切真实原片（2:1），提取 3–5 个视觉锚点与光线不变量，分别生成第 2 格（记忆）、第 3 格（极简结构抽象）、第 4 格（综合重构），最后纵向无缝拼成 1:2 四联图，全程无边框无文字。\n\n（Skill 仓库：https://github.com/Starryear/Starryear-Abstract-Quartet）",
        "slots_zh": [
            "【2:1 裁切重心】指定原片最想保留的横向构图区域"
        ],
        "notes_zh": [
            "第 1 格是原片 2:1 裁切，第 2 至 4 格分别生成，再用 Pillow 拼合。",
            "某一格不满意，可单独重跑该格。"
        ],
        "notes_en": [
            "Panel 1 is the real 2:1 crop; panels 2-4 are generated separately and stacked with Pillow.",
            "Re-run any single panel that falls short."
        ]
    },
    {
        "id": "night-diary-image-skill",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "photo",
        "runtime": "gpt",
        "license": "none",
        "license_tier": "private-eval",
        "discovery": "",
        "copy_label": "invoke",
        "title_zh": "深夜胶片手写日记",
        "title_en": "Night diary film edit",
        "summary_zh": "一张照片进，锁定构图，压成深靛蓝夜色胶片并加白色手写日记。",
        "summary_en": "A photo in; composition locked, graded to deep-indigo night film with a handwritten diary line.",
        "aspect": "Source ratio",
        "author": "xianxie6",
        "source_url": "https://github.com/xianxie6/night-diary-image-skill",
        "discovery_url": "",
        "gallery": [
            [
                "night-diary-image-skill.jpg",
                "示例 1",
                "Example 1"
            ],
            [
                "night-diary-image-skill-2.jpg",
                "示例 2",
                "Example 2"
            ],
            [
                "own-night-diary.jpg",
                "实测",
                "My test"
            ]
        ],
        "palette": [
            "#101826",
            "#f2b66d",
            "#e8eef5"
        ],
        "copy_text": "用 night-diary-image-skill 处理这张照片：严格锁定原图比例、透视与人物位置，转为深邃夜色胶片与局部暖光，在暗部留白区写上简短白色手写日记「【填入一句英文短句】」，不要凭空增加人物或动物。\n\n（Skill 仓库：https://github.com/xianxie6/night-diary-image-skill）",
        "slots_zh": [
            "【手写英文日记短句】如：11:42 PM, the city finally slowed down."
        ],
        "notes_zh": [
            "原图比例、透视和人物位置不变，不凭空增加人物或动物。",
            "荧光人物线条模式需显式开启，出图后核对人数与肢体遮挡。"
        ],
        "notes_en": [
            "Ratio, perspective and figure positions stay fixed; no invented people or animals.",
            "Fluorescent-outline mode is opt-in; check figure count and limb occlusion."
        ]
    },
    {
        "id": "heytea-style",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "local-script",
        "input": "photo",
        "runtime": "script",
        "license": "none",
        "license_tier": "private-eval",
        "discovery": "x",
        "copy_label": "invoke",
        "title_zh": "物件锚点简笔涂鸦海报",
        "title_en": "Object + doodle poster",
        "summary_zh": "一张带物件的照片进，保留该物件，配黑色简笔小人和童趣手写标题。",
        "summary_en": "A photo with an object in; the object stays real, joined by stick figures and a chunky hand-lettered title.",
        "aspect": "2:3 / 3:4",
        "author": "Hchen1218",
        "source_url": "https://github.com/Hchen1218/heytea-style",
        "discovery_url": "https://x.com/oran_ge/status/2087818420150731057?s=46",
        "gallery": [
            [
                "heytea-typography-poster.jpg",
                "标题版",
                "Title poster"
            ],
            [
                "heytea-monster-poster.jpg",
                "互动版",
                "Monster poster"
            ]
        ],
        "palette": [
            "#f8f6f0",
            "#191918",
            "#5b8c5a"
        ],
        "copy_text": "用 heytea-style 工作流处理这张照片：保留照片中的「【指定保留的真实物件，如：咖啡杯/相机/水果】」作为真实摄影锚点，周围做大留白与简笔小人互动叙事，标题采用粗黑童趣手写字「【填入 2–5 字标题，或选无字版】」，不出现任何品牌 Logo。\n\n（Skill 仓库：https://github.com/Hchen1218/heytea-style）",
        "slots_zh": [
            "【保留的真实物件】如：桌上的冰美式 / 草地上的露营椅",
            "【海报大字标题】如：今日放空 / 先喝一口（或选纯线条无字版）"
        ],
        "notes_zh": [
            "带字版先出无字底图，再由脚本合成标题层；也有纯简笔无字版。",
            "不生成任何品牌 Logo 或商用标识。"
        ],
        "notes_en": [
            "Titled mode: wordless base image first, then a script composites the title layer. A wordless mode also exists.",
            "No brand logos or commercial marks are generated."
        ]
    },
    {
        "id": "tait-crt-interface-skill",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "local-script",
        "input": "photo-or-theme",
        "runtime": "script",
        "license": "none",
        "license_tier": "private-eval",
        "discovery": "x",
        "copy_label": "invoke",
        "title_zh": "复古 CRT 像素桌面界面",
        "title_en": "Retro CRT pixel desktop",
        "summary_zh": "照片或主题进，重构成带浮动窗口、扫描线和统一色卡的 8-bit 桌面。",
        "summary_en": "A photo or theme in; an 8-bit CRT desktop with floating windows, scanlines and a strict palette out.",
        "aspect": "3:4 / 4:3 / 1:1",
        "author": "TaiT-tt",
        "source_url": "https://github.com/TaiT-tt/tait-crt-interface-skill",
        "discovery_url": "https://x.com/oran_ge/status/2087818420150731057?s=46",
        "gallery": [
            [
                "tait-crt-interface-skill.jpg",
                "示例 1",
                "Example 1"
            ],
            [
                "tait-crt-interface-skill-2.jpg",
                "示例 2",
                "Example 2"
            ]
        ],
        "palette": [
            "#182018",
            "#65c466",
            "#d8f2d0"
        ],
        "copy_text": "用 tait-crt-interface-skill 把这张照片重构为复古 CRT 像素桌面界面：色卡选「【经典琥珀 / 极客绿磷 / 粉黛 / 冷面几何】」，比例选「【3:4 竖版 或 4:3 横版】」，包含 1 个主像素窗口与 3–5 个浮动状态子窗口。\n\n（Skill 仓库：https://github.com/TaiT-tt/tait-crt-interface-skill）",
        "slots_zh": [
            "【色卡预设】如：极客磷光绿 / 经典黑白 / 粉黛 / 赛博蓝",
            "【画幅比例】如：3:4 竖版 / 4:3 复古显示器比例"
        ],
        "notes_zh": [
            "直出模式只生图；完整模式再用 finalize_crt.py 锁色并加扫描线与桶形畸变。",
            "内置 10 套色卡。"
        ],
        "notes_en": [
            "Direct mode only generates; full mode runs finalize_crt.py to lock the palette and add scanlines and barrel distortion.",
            "Ships with 10 palettes."
        ]
    },
    {
        "id": "travel-memory-sticker-card",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "travel",
        "runtime": "gpt",
        "license": "nc",
        "license_tier": "personal-nc",
        "discovery": "xhs",
        "copy_label": "invoke",
        "title_zh": "旅行手帐贴纸卡",
        "title_en": "Travel sticker card",
        "summary_zh": "一张旅行照进，得到 3:2 水粉手帐卡：左主场景，右 6 枚贴纸。",
        "summary_en": "A travel photo in; a 3:2 gouache journal card, scene on the left, six stickers on the right.",
        "aspect": "3:2",
        "author": "carolinaaafy",
        "source_url": "https://github.com/carolinaaafy/travel-memory-sticker-card",
        "discovery_url": "http://xhslink.cn/o/3IT2loUHyfb",
        "gallery": [
            [
                "travel-memory-sticker-author.jpg",
                "示例 1",
                "Example 1"
            ],
            [
                "travel-memory-sticker-author-2.jpg",
                "示例 2",
                "Example 2"
            ]
        ],
        "palette": [
            "#f5efe2",
            "#d96b43",
            "#496a81"
        ],
        "copy_text": "用 travel-memory-sticker-card 工作流把这张旅行照片做成一张 3:2 横版哑光水粉手帐卡：左侧重绘主场景并配 3 条英文关键词，右侧从照片里提取 6 枚带白边的独立旅行小物件贴纸。\n\n（Skill 仓库：https://github.com/carolinaaafy/travel-memory-sticker-card）",
        "slots_zh": [
            "【可选英文地点关键词】不填则由模型根据照片自动提炼 3 个词"
        ],
        "notes_zh": [
            "单张出图，不需要透明通道抠图脚本。",
            "许可仅限个人非商用。"
        ],
        "notes_en": [
            "One image out; no alpha-matting script needed.",
            "Licensed for personal, non-commercial use only."
        ]
    },
    {
        "id": "travel-memory-card-duo",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "local-script",
        "input": "travel",
        "runtime": "script",
        "license": "none",
        "license_tier": "private-eval",
        "discovery": "xhs",
        "copy_label": "invoke",
        "title_zh": "旅行记忆卡 + 透明贴纸 PNG",
        "title_en": "Memory card + transparent stickers",
        "summary_zh": "一张旅行照进，输出手帐卡，再抠出四角全透明的 RGBA 贴纸 PNG。",
        "summary_en": "A travel photo in; a 3:2 card plus a transparent RGBA sticker PNG cut out by script.",
        "aspect": "3:2 ×2",
        "author": "carolinaaafy",
        "source_url": "https://github.com/carolinaaafy/travel-memory-card-duo",
        "discovery_url": "http://xhslink.cn/o/3IT2loUHyfb",
        "gallery": [
            [
                "travel-memory-duo-author.jpg",
                "贴纸",
                "Stickers"
            ],
            [
                "travel-memory-duo-author-2.jpg",
                "主卡",
                "Card"
            ]
        ],
        "palette": [
            "#eef2ea",
            "#4a7c59",
            "#d4843e"
        ],
        "copy_text": "用 travel-memory-card-duo 工作流处理这张照片：先生成 3:2 旅行记忆卡，再以卡上的 6 枚贴纸为母版生成纯色背景贴纸图，调用 remove_chroma_key.py 导出四角 Alpha=0 的真透明底 PNG 并校验。\n\n（Skill 仓库：https://github.com/carolinaaafy/travel-memory-card-duo）",
        "slots_zh": [
            "【照片路径】适合需要把生成的贴纸导入 GoodNotes / Procreate / 微信表情的场景"
        ],
        "notes_zh": [
            "比单卡版多一张真透明底 PNG，可直接导入手帐 App 或做表情。",
            "remove_chroma_key.py 去底，并校验四角 Alpha 为 0。"
        ],
        "notes_en": [
            "Adds a true transparent PNG over the single-card version, ready for planner apps or sticker packs.",
            "remove_chroma_key.py removes the key colour and checks corner alpha is 0."
        ]
    },
    {
        "id": "ip-illustration-for-yourself",
        "kind": "skill",
        "input_mode": "photo-ref",
        "runtime_mode": "local-codex",
        "input": "photo-text",
        "runtime": "codex",
        "license": "none",
        "license_tier": "private-eval",
        "discovery": "x",
        "copy_label": "invoke",
        "title_zh": "个人 IP 钢笔涂鸦配图",
        "title_en": "Personal IP pen doodles",
        "summary_zh": "人物照加文章要点进，输出白底钢笔线条的 IP 插图或 3:4 信息图。",
        "summary_en": "A character photo plus article points in; pen-doodle IP illustrations or a 3:4 infographic out.",
        "aspect": "3:4",
        "author": "EverettFish",
        "source_url": "https://github.com/EverettFish/ip_illustration_for_yourself",
        "discovery_url": "https://x.com/oran_ge/status/2087818420150731057?s=46",
        "gallery": [
            [
                "ip-illustration-author.jpg",
                "作者示例",
                "Author"
            ]
        ],
        "palette": [
            "#fbfaf7",
            "#1e1e1c",
            "#3b73b9"
        ],
        "copy_text": "用 ip_illustration_for_yourself 工作流，参考人物特征建立大白底、微抖黑钢笔线的小比例 IP 角色，把下面这段文字拆解成一张 3:4 竖版视觉信息图：「【粘贴你的文章段落或核心观点】」。\n\n（Skill 仓库：https://github.com/EverettFish/ip_illustration_for_yourself）",
        "slots_zh": [
            "【文章观点或数据要点】适合公众号/小红书干货配图或个人博客插图"
        ],
        "notes_zh": [
            "信息图须逐字核对标题、日期和数值，避免模型编造数字。",
            "需要 Codex 和 GPT Image。"
        ],
        "notes_en": [
            "Check every title, date and figure on the infographic; the model may invent numbers.",
            "Needs Codex and GPT Image."
        ]
    },
    {
        "id": "gathered-scenes-zine-skill",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "photos",
        "runtime": "gpt",
        "license": "nc",
        "license_tier": "personal-nc",
        "discovery": "fork",
        "copy_label": "invoke",
        "title_zh": "拾景小志：拼贴与单景提炼",
        "title_en": "Gathered Scenes zine",
        "summary_zh": "照片进，两种工作流：多处细节聚合成杂志内页，或单景极简提炼。",
        "summary_en": "Photos in; two workflows: a multi-detail collage page or a single-scene minimalist print.",
        "aspect": "Portrait",
        "author": "Zeejay0",
        "source_url": "https://github.com/Zeejay0/gathered-scenes-zine-skill",
        "discovery_url": "https://github.com/Juns-g/gathered-scenes-zine-skill",
        "gallery": [
            [
                "gathered-scenes-author.jpg",
                "作者示例",
                "Author"
            ]
        ],
        "palette": [
            "#ece8df",
            "#594a3c",
            "#8f9e8b"
        ],
        "copy_text": "用 gathered-scenes-zine-skill 里的【scenes-gathered-zine-v1-3（多幕聚合） / scene-distillation-zine-v1-3（单景提炼）】工作流处理这张照片，生成克制纸张排版感的独立摄影小志页面。\n\n（Skill 仓库：https://github.com/Zeejay0/gathered-scenes-zine-skill ｜ 备份：https://github.com/Juns-g/gathered-scenes-zine-skill）",
        "slots_zh": [
            "【二选一子模式】scenes-gathered-zine-v1-3 或 scene-distillation-zine-v1-3"
        ],
        "notes_zh": [
            "仅限个人非商用；商用须取得作者书面授权。",
            "含多幕聚合与单景提炼两套 v1.3 技能。"
        ],
        "notes_en": [
            "Personal, non-commercial use only; commercial use needs the author's written permission.",
            "Two v1.3 skills: scenes-gathered-zine and scene-distillation-zine."
        ]
    },
    {
        "id": "guizang-social-card-skill",
        "kind": "skill",
        "input_mode": "text",
        "runtime_mode": "local-render",
        "input": "copy",
        "runtime": "render",
        "license": "agpl",
        "license_tier": "agpl",
        "discovery": "",
        "copy_label": "invoke",
        "title_zh": "歸藏社交卡片渲染",
        "title_en": "Guizang social cards",
        "summary_zh": "文案进，经 Playwright 渲染成社媒卡片或 Live Photo。",
        "summary_en": "Copy in; HTML templates and Playwright render social card decks and Live Photos.",
        "aspect": "3:4 / 2.35:1",
        "author": "歸藏 (op7418)",
        "source_url": "https://github.com/op7418/guizang-social-card-skill",
        "discovery_url": "",
        "gallery": [
            [
                "guizang-social-card-author.jpg",
                "官方示例",
                "Official"
            ]
        ],
        "palette": [
            "#1b365d",
            "#e85d04",
            "#f5f3ef"
        ],
        "copy_text": "调用 guizang-social-card-skill 把下面这段内容排版并渲染成一套 3:4 社交分享卡片（风格选 Monocle 经典杂志风 / 森林墨绿 / 克莱因蓝波点），跑完 validate-social-deck.mjs 确认无截断后导出 PNG：「【粘贴正文】」。\n\n（Skill 仓库：https://github.com/op7418/guizang-social-card-skill）",
        "slots_zh": [
            "【卡片风格与正文】内置 Style A（纸感杂志）与 Style B（波普网格/高饱和）共 9 套背景"
        ],
        "notes_zh": [
            "本地 HTML 渲染管线，依赖浏览器与媒体工具，没有 ChatGPT 提示词包。",
            "AGPL-3.0：闭源或商业集成前，须先核对其义务。"
        ],
        "notes_en": [
            "A local HTML pipeline needing a browser and media tools; there is no ChatGPT pack.",
            "AGPL-3.0: review its obligations before any closed-source or commercial integration."
        ]
    },
    {
        "id": "spektralab-film-export",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "local-render",
        "input": "raw",
        "runtime": "render",
        "license": "own",
        "license_tier": "own",
        "discovery": "",
        "copy_label": "invoke",
        "title_zh": "SpektraLab 胶片模拟导出",
        "title_en": "SpektraLab film export",
        "summary_zh": "RAW 或 JPEG 原片进，本机 CLI 套用胶片配方导出，不经生成式 AI。",
        "summary_en": "RAW or JPEG in; a local CLI applies film, print and grain recipes with no generative AI.",
        "aspect": "Source res.",
        "author": "photo-automation (local)",
        "source_url": "",
        "discovery_url": "",
        "gallery": [
            [
                "spektralab-1.jpg",
                "界面",
                "UI"
            ],
            [
                "spektralab-2.jpg",
                "高光溢出",
                "Halation"
            ]
        ],
        "palette": [
            "#22201e",
            "#d49a45",
            "#6a8d73"
        ],
        "copy_text": "用 spektralab-film-export 技能处理这张原片：不走生成式改图，用本机 spektralab CLI 导出胶片风格成片，保留原始分辨率与真实光学细节。",
        "slots_zh": [
            "【原片路径与偏好的胶片冷暖】适合 A7C2 拍完的日常或旅行照片快速出胶片感"
        ],
        "notes_zh": [
            "像素不经生成式改动，适合人像合照和高画质风光。",
            "需本机已安装 spektralab CLI。"
        ],
        "notes_en": [
            "Pixels are never altered by generative AI; suits group portraits and high-quality landscapes.",
            "Needs the spektralab CLI installed locally."
        ]
    },
    {
        "id": "guizang-yingzao-skill",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "local-render",
        "input": "photo",
        "runtime": "render",
        "license": "mit",
        "license_tier": "mit",
        "discovery": "x",
        "copy_label": "invoke",
        "title_zh": "营造 Yingzao：古建与人文旅行废片转杂志海报",
        "title_en": "Yingzao: architectural & travel photo editorial poster",
        "summary_zh": "歸藏开源的古建与旅行摄影海报 Skill，搭配网格排版、字体设计与文化信息注记。",
        "summary_en": "Guizang's open-source skill turning architectural and travel shots into magazine posters with cultural typography.",
        "aspect": "3:4 / 自适应",
        "author": "歸藏 (op7418)",
        "source_url": "https://github.com/op7418/guizang-yingzao-skill",
        "discovery_url": "https://x.com/op7418/status/2095489678183170535",
        "gallery": [
            [
                "guizang-yingzao-1.jpg",
                "作者示例 1",
                "Example 1"
            ],
            [
                "guizang-yingzao-2.jpg",
                "作者示例 2",
                "Example 2"
            ]
        ],
        "palette": [
            "#7c3f2c",
            "#2c3531",
            "#f2ece1"
        ],
        "copy_text": "用 guizang-yingzao-skill（营造）把这张古建/人文旅行照片排版成一张杂志级摄影海报，地点与建筑信息为「【填入地点与建筑名称，如：山西大同 · 善化寺】」。\n\n（Skill 仓库：https://github.com/op7418/guizang-yingzao-skill ｜ X 原帖：https://x.com/op7418/status/2095489678183170535）",
        "slots_zh": [
            "【地点与建筑名称】如：山西大同 · 善化寺 / 卢克索 · 卡纳克神庙"
        ],
        "notes_zh": [
            "来自 X 书签收藏（歸藏《开源一个拯救你旅行废片的 Skill》）。"
        ],
        "notes_en": [
            "From X bookmarks (Guizang's open-source architectural photography poster skill)."
        ]
    },
    {
        "id": "wyyyyuu-lightroom-style",
        "kind": "skill",
        "input_mode": "photo-ref",
        "runtime_mode": "local-codex",
        "input": "photo-ref",
        "runtime": "codex",
        "license": "none",
        "license_tier": "private-eval",
        "discovery": "xhs",
        "copy_label": "invoke",
        "title_zh": "Lightroom 样片参考仿色（lightroom-style）",
        "title_en": "Lightroom reference color-matching skill",
        "summary_zh": "分析参考图的直方图与冷暖影调，驱动 Lightroom 调整原片而不重绘像素。",
        "summary_en": "Analyzes a reference photo's histogram and tonal warmth to adjust your original photo in Lightroom without generative redraw.",
        "aspect": "保持原片",
        "author": "Wyyyyuu (@悟空)",
        "source_url": "https://github.com/Wyyyyuu/lightroom-style",
        "discovery_url": "https://www.xiaohongshu.com/explore/6aac07d300000000250356f4",
        "gallery": [
            [
                "xhs-lr-style-1.jpg",
                "小红书原帖示例",
                "XHS Showcase"
            ]
        ],
        "palette": [
            "#2b3d4f",
            "#d49a56",
            "#eceae4"
        ],
        "copy_text": "用 lightroom-style 技能分析参考图的直方图、明暗与冷暖影调关系，对我的原片「【填入原片路径】」按参考图「【填入参考图路径】」进行非生成式色调匹配。\n\n（Skill 仓库：https://github.com/Wyyyyuu/lightroom-style ｜ 小红书原帖：https://www.xiaohongshu.com/explore/6aac07d300000000250356f4）",
        "slots_zh": [
            "【原片与参考图路径】传入喜欢的摄影师样张 + 自己拍的原图"
        ],
        "notes_zh": [
            "来自小红书收藏（@悟空），不让 AI 重画假图，只计算影调参数改原图。"
        ],
        "notes_en": [
            "From Xiaohongshu favorites; modifies color grading parameters rather than redrawing pixels with generative AI."
        ]
    },
    {
        "id": "daily-photo-playground",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "photo",
        "runtime": "gpt",
        "license": "none",
        "license_tier": "private-eval",
        "discovery": "xhs",
        "copy_label": "invoke",
        "title_zh": "日常照片 → 高饱和 3:4 情绪编辑海报（daily-photo-playground）",
        "title_en": "Daily photo → 3:4 high-saturation editorial poster",
        "summary_zh": "日常照片重构成适合小红书/抖音的高饱和 3:4 情绪编辑海报，保留小原片窗口与粗黑标题。",
        "summary_en": "Reconstructs everyday photos into high-saturation 3:4 editorial posters with a small source window and bold headline.",
        "aspect": "3:4",
        "author": "luji12 (螂狗日记)",
        "source_url": "https://github.com/luji12/daily-photo-playground",
        "discovery_url": "https://github.com/tluy/skill-zine-summary",
        "gallery": [
            [
                "cand-xhs-poster-1.jpg",
                "样图 1",
                "Sample 1"
            ],
            [
                "cand-xhs-poster-2.jpg",
                "样图 2",
                "Sample 2"
            ]
        ],
        "palette": [
            "#c1121f",
            "#fdf0d5",
            "#003049"
        ],
        "copy_text": "用 daily-photo-playground 工作流把这张照片重构成一张 3:4 竖版高饱和情绪编辑海报：保留小原片窗口与高光质感，留白区排入粗黑现代中文主标题「【填入 4–6 字大标题，如：风吹过山野】」与极小英文注记。\n\n（Skill 仓库：https://github.com/luji12/daily-photo-playground）",
        "slots_zh": [
            "【4–6 字主标题】如：风吹过山野 / 夏日终章"
        ],
        "notes_zh": [
            "只收录网址与思路，未克隆仓库；附一条可直接使用的替代提示词。"
        ],
        "notes_en": [
            "Bookmarked only, not cloned; includes a ready-to-use substitute prompt."
        ]
    },
    {
        "id": "pixel-style-poster-skill",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "photo-or-theme",
        "runtime": "gpt",
        "license": "mit",
        "license_tier": "mit",
        "discovery": "",
        "copy_label": "invoke",
        "title_zh": "细密点阵半色调印刷海报（pixel-style-poster）",
        "title_en": "Halftone dot-matrix print poster",
        "summary_zh": "将照片或静物转化为细密点阵印刷、半色调网点与低分辨率纸面肌理海报。",
        "summary_en": "Transforms photos or still-life subjects into fine dot-matrix halftone print posters with tactile paper grain.",
        "aspect": "3:4",
        "author": "v92388375-gif",
        "source_url": "https://github.com/v92388375-gif/pixel-style-poster-skill",
        "discovery_url": "",
        "gallery": [
            [
                "cand-pixel-poster-1.jpg",
                "作者示例 1",
                "Example 1"
            ],
            [
                "cand-pixel-poster-2.jpg",
                "作者示例 2",
                "Example 2"
            ]
        ],
        "palette": [
            "#1c3b38",
            "#6ec4b8",
            "#f3efe6"
        ],
        "copy_text": "用 pixel-style-poster-skill 把这张照片（或主题「【填入主体，如：夜色下的白百合 / 丝绒葡萄】」）转化为 3:4 细密点阵印刷与半色调网点质感海报，保留清晰明暗层次与纸面印刷肌理，不要做成粗糙游戏像素画。\n\n（Skill 仓库：https://github.com/v92388375-gif/pixel-style-poster-skill）",
        "slots_zh": [
            "【主体或照片】可直接传一张静物/植物/人像照片，或填入文字主题"
        ],
        "notes_zh": [
            "MIT 开源许可，主打平面印刷半色调网点，而非 8-bit 游戏像素风。"
        ],
        "notes_en": [
            "MIT licensed; focuses on graphic halftone print texture rather than 8-bit retro game pixels."
        ]
    },
    {
        "id": "photo-relic-editorial",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "photo",
        "runtime": "gpt",
        "license": "mit",
        "license_tier": "mit",
        "discovery": "",
        "copy_label": "invoke",
        "title_zh": "照片记忆遗物纸面双联（photo-relic-editorial）",
        "title_en": "Photo relic editorial print",
        "summary_zh": "保留上方真实照片，下方制作为「记忆遗物」式的克制纸面拼贴与画廊编号注记。",
        "summary_en": "Preserves the upper photograph and pairs it with a restrained 'memory relic' paper collage and gallery catalog notes below.",
        "aspect": "2:3",
        "author": "wnby",
        "source_url": "https://github.com/wnby/photo-relic-editorial",
        "discovery_url": "",
        "gallery": [
            [
                "cand-relic-editorial-1.jpg",
                "作者示例 1",
                "Example 1"
            ],
            [
                "cand-relic-editorial-2.jpg",
                "作者示例 2",
                "Example 2"
            ]
        ],
        "palette": [
            "#dcd5c7",
            "#3d4849",
            "#8c7a6b"
        ],
        "copy_text": "用 photo-relic-editorial 工作流处理这张照片：上方完整保留真实摄影画面，下方在暖白档案纸上生成提炼自原片肌理的「记忆遗物」纸面拼贴与克制画廊注记「【填入地点或编号，如：BEIJING · RELIC 04】」。\n\n（Skill 仓库：https://github.com/wnby/photo-relic-editorial）",
        "slots_zh": [
            "【地点或档案编号】如：BEIJING · RELIC 04 / AUTUMN LAKE"
        ],
        "notes_zh": [
            "MIT 开源许可，偏画廊馆藏图录与系列化纸面质感。"
        ],
        "notes_en": [
            "MIT licensed; designed for serializable gallery catalog and archival paper aesthetics."
        ]
    },
    {
        "id": "dyy-photo-deconstruct",
        "kind": "skill",
        "input_mode": "photo",
        "runtime_mode": "gpt-direct",
        "input": "photo",
        "runtime": "gpt",
        "license": "none",
        "license_tier": "private-eval",
        "discovery": "",
        "copy_label": "invoke",
        "title_zh": "水墨水彩剪影解构长卷（dyy_photo_deconstruct）",
        "title_en": "Ink & watercolor silhouette deconstruction",
        "summary_zh": "将照片解构为无文字、低饱和、巨大留白的水墨与水彩晕染剪影。",
        "summary_en": "Deconstructs a photograph into a wordless, low-saturation ink and watercolor silhouette with expansive whitespace.",
        "aspect": "9:20 / 竖长幅",
        "author": "121dyy",
        "source_url": "https://github.com/121dyy/dyy_photo_deconstruct",
        "discovery_url": "",
        "gallery": [
            [
                "cand-dyy-deconstruct-1.jpg",
                "作者示例 1",
                "Example 1"
            ],
            [
                "cand-dyy-deconstruct-2.jpg",
                "作者示例 2",
                "Example 2"
            ]
        ],
        "palette": [
            "#f4f2ed",
            "#2e3532",
            "#7a867e"
        ],
        "copy_text": "用 dyy_photo_deconstruct 工作流处理这张照片：提取画面最具神韵的动态与结构，解构为低饱和度、大面积宣纸留白的水墨与水彩剪影作品，全程不加任何文字或印章。\n\n（Skill 仓库：https://github.com/121dyy/dyy_photo_deconstruct）",
        "slots_zh": [],
        "notes_zh": [
            "纯提示词规范，强调无文字、极简水墨晕染与大留白。"
        ],
        "notes_en": [
            "Prompt-only workflow emphasizing wordless ink-wash silhouettes and generous negative space."
        ]
    }
]

def jpeg_size(path):
    """Return (width, height) of a JPEG by scanning markers for a SOF segment."""
    with open(path, "rb") as f:
        data = f.read()
    if data[:2] != b"\xff\xd8":
        raise ValueError(f"not a JPEG: {path}")
    i, n = 2, len(data)
    while i + 4 <= n:
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker == 0xFF:  # fill byte
            i += 1
            continue
        if marker in (0x01, 0xD8) or 0xD0 <= marker <= 0xD7:  # standalone markers
            i += 2
            continue
        seglen = int.from_bytes(data[i + 2:i + 4], "big")
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            # precision (1 byte), height (2), width (2)
            height = int.from_bytes(data[i + 5:i + 7], "big")
            width = int.from_bytes(data[i + 7:i + 9], "big")
            return width, height
        i += 2 + seglen
    raise ValueError(f"no SOF marker found: {path}")


def build_item(raw):
    in_zh, in_en = INPUT[raw["input"]]
    rt_zh, rt_en = RUNTIME[raw["runtime"]]
    lic_zh, lic_en = LICENSE[raw["license"]]
    cl_zh, cl_en = COPY_LABEL[raw["copy_label"]]
    if raw["discovery_url"]:
        ds_zh, ds_en = DISCOVERY[raw["discovery"]]
    else:
        ds_zh = ds_en = ""

    gallery = []
    for fname, label_zh, label_en in raw["gallery"]:
        path = os.path.join(prompts_dir, "thumbs", fname)
        if not os.path.isfile(path):
            raise FileNotFoundError(f"gallery image missing: {path}")
        w, h = jpeg_size(path)
        gallery.append({
            "src": f"thumbs/{fname}",
            "w": w,
            "h": h,
            "label_zh": label_zh,
            "label_en": label_en,
        })

    copy_text = raw["copy_text"]
    if copy_text is None:
        # Link-only site items: title plus URL(s).
        lines = [raw["title_zh"], raw["source_url"]]
        if raw["discovery_url"] and raw["discovery_url"] != raw["source_url"]:
            lines.append(raw["discovery_url"])
        copy_text = "\n".join(lines)

    if len(raw["notes_zh"]) != len(raw["notes_en"]):
        raise ValueError(f"notes count mismatch: {raw['id']}")

    return {
        "id": raw["id"],
        "kind": raw["kind"],
        "input_mode": raw["input_mode"],
        "runtime_mode": raw["runtime_mode"],
        "title_zh": raw["title_zh"],
        "title_en": raw["title_en"],
        "summary_zh": raw["summary_zh"],
        "summary_en": raw["summary_en"],
        "input_zh": in_zh,
        "input_en": in_en,
        "runtime_zh": rt_zh,
        "runtime_en": rt_en,
        "aspect": raw["aspect"],
        "author": raw["author"],
        "license_tier": raw["license_tier"],
        "license_zh": lic_zh,
        "license_en": lic_en,
        "source_url": raw["source_url"],
        "discovery_url": raw["discovery_url"],
        "discovery_label_zh": ds_zh,
        "discovery_label_en": ds_en,
        "palette": raw["palette"],
        "gallery": gallery,
        "copy_label_zh": cl_zh,
        "copy_label_en": cl_en,
        "copy_text": copy_text,
        "slots_zh": raw["slots_zh"],
        "notes_zh": raw["notes_zh"],
        "notes_en": raw["notes_en"],
    }


items = [build_item(r) for r in RAW]

out_json = os.path.join(prompts_dir, "items.json")
with open(out_json, "w", encoding="utf-8") as f:
    json.dump({"updated_at": "2026-11-07", "items": items}, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(items)} items to {out_json}")
