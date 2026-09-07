export async function onRequestGet(context) {
  try {
    const url = new URL(context.request.url);
    const noteId = url.searchParams.get('id');
    const xsecToken = url.searchParams.get('xsec_token') || '';

    if (!noteId) {
      return jsonResponse({ error: '缺少 noteId' }, 400);
    }

    let xhsUrl = `https://www.xiaohongshu.com/explore/${encodeURIComponent(noteId)}`;
    if (xsecToken) {
      xhsUrl += `?xsec_token=${encodeURIComponent(xsecToken)}&xsec_source=pc_search`;
    }

    const resp = await fetch(xhsUrl, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
      }
    });

    const html = await resp.text();
    const stateMatch = html.match(/window\.__INITIAL_STATE__\s*=\s*(.*?)</);
    if (!stateMatch) {
      return jsonResponse({ error: '未能在小红书页面中提取到数据，可能已被拦截' }, 404);
    }

    let rawState = stateMatch[1].trim().replace(/;$/, '');
    rawState = rawState.replace(/\bundefined\b/g, 'null');
    const data = JSON.parse(rawState);

    const noteDetailMap = data?.note?.noteDetailMap || {};
    let noteData = null;
    for (const k in noteDetailMap) {
      if (noteDetailMap[k]?.note) {
        noteData = noteDetailMap[k].note;
        break;
      }
    }

    if (!noteData) {
      return jsonResponse({ error: '笔记数据未解析' }, 404);
    }

    const title = noteData.title || '';
    const desc = noteData.desc || '';
    const user = noteData.user || {};
    const author = user.nickname || '小红书用户';
    const avatar = user.avatar || '';
    const time = noteData.time ? new Date(noteData.time).toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' }) : '';
    
    const images = (noteData.imageList || []).map(img => {
      return img.urlDefault || img.url || '';
    }).filter(Boolean);

    return jsonResponse({
      id: noteId,
      title,
      desc,
      author,
      avatar,
      time,
      images
    });

  } catch (err) {
    return jsonResponse({ error: err.message || '抓取失败' }, 500);
  }
}

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Access-Control-Allow-Origin': '*'
    }
  });
}
