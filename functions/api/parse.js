export async function onRequestPost(context) {
  try {
    const body = await context.request.json();
    const rawText = body.text || '';

    // 预先从原始文本中智能提取备用标题
    let extractedTitle = extractTitleFromText(rawText);

    // 1. 尝试直接从文本中捕获特征码
    // B站 BV号
    const bvMatch = rawText.match(/\b(BV[a-zA-Z0-9]{10})\b/);
    if (bvMatch) {
      return jsonResponse({
        platform: 'bili',
        name: '哔哩哔哩',
        icon: '📺',
        title: extractedTitle || '哔哩哔哩视频',
        param: 'bvid',
        value: bvMatch[1],
        url: `https://juns.page/go/bili/?bvid=${bvMatch[1]}`
      });
    }

    // 2. 提取文本中的 URL
    const urlMatch = rawText.match(/https?:\/\/[^\s\u4e00-\u9fa5]+/);
    if (!urlMatch) {
      return jsonResponse({ error: '未在文本中找到有效链接或特征码' }, 400);
    }

    const inputUrl = urlMatch[0];
    const userAgent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1';

    // 3. 针对不同平台的解析策略
    // B站短链
    if (inputUrl.includes('b23.tv')) {
      const resp = await fetch(inputUrl, {
        headers: { 'User-Agent': userAgent },
        redirect: 'manual'
      });
      const loc = resp.headers.get('location') || '';
      const m = loc.match(/(BV[a-zA-Z0-9]{10})/);
      if (m) {
        return jsonResponse({
          platform: 'bili',
          name: '哔哩哔哩',
          icon: '📺',
          title: extractedTitle || '哔哩哔哩视频',
          param: 'bvid',
          value: m[1],
          url: `https://juns.page/go/bili/?bvid=${m[1]}`
        });
      }
    }

    // 小红书短链 / 长链
    if (inputUrl.includes('xhslink.') || inputUrl.includes('xiaohongshu.com')) {
      let finalUrl = inputUrl;
      if (inputUrl.includes('xhslink.')) {
        const resp = await fetch(inputUrl, {
          headers: { 'User-Agent': userAgent },
          redirect: 'manual'
        });
        finalUrl = resp.headers.get('location') || inputUrl;
      }
      const noteMatch = finalUrl.match(/(?:item\/|explore\/)([a-f0-9]{24,32})/);
      if (noteMatch) {
        const tokenMatch = finalUrl.match(/xsec_token=([^&]+)/);
        const xsecToken = tokenMatch ? tokenMatch[1] : '';
        let targetUrl = `https://juns.page/go/xhs/?id=${noteMatch[1]}`;
        if (xsecToken) targetUrl += `&xsec_token=${encodeURIComponent(xsecToken)}`;
        return jsonResponse({
          platform: 'xhs',
          name: '小红书',
          icon: '📕',
          title: extractedTitle || '小红书笔记',
          param: 'id',
          value: noteMatch[1],
          url: targetUrl
        });
      }
    }

    // 阿里系短链 (淘宝 / 闲鱼 m.tb.cn / e.tb.cn)
    if (inputUrl.includes('.tb.cn') || inputUrl.includes('taobao.com') || inputUrl.includes('goofish.com')) {
      let targetUrl = inputUrl;
      if (inputUrl.includes('.tb.cn')) {
        const resp = await fetch(inputUrl, {
          headers: { 'User-Agent': userAgent }
        });
        const html = await resp.text();
        const m = html.match(/var url = '([^']+)'/);
        if (m) targetUrl = m[1];
      }

      // 区分闲鱼与淘宝
      if (targetUrl.includes('goofish.com') || targetUrl.includes('itemId=')) {
        const itemMatch = targetUrl.match(/[?&]itemId=(\d+)/) || targetUrl.match(/[?&]id=(\d+)/);
        if (itemMatch) {
          return jsonResponse({
            platform: 'goofish',
            name: '闲鱼',
            icon: '🐟',
            title: extractedTitle || '闲鱼宝贝',
            param: 'id',
            value: itemMatch[1],
            url: `https://juns.page/go/goofish/?id=${itemMatch[1]}`
          });
        }
      } else {
        const tbMatch = targetUrl.match(/[?&]id=(\d+)/);
        if (tbMatch) {
          return jsonResponse({
            platform: 'tb',
            name: '淘宝',
            icon: '🛍️',
            title: extractedTitle || '淘宝商品',
            param: 'id',
            value: tbMatch[1],
            url: `https://juns.page/go/tb/?id=${tbMatch[1]}`
          });
        }
      }
    }

    // 京东 (3.cn / jd.com)
    if (inputUrl.includes('3.cn') || inputUrl.includes('jd.com')) {
      let finalUrl = inputUrl;
      let pageTitle = '';
      if (inputUrl.includes('3.cn')) {
        const resp = await fetch(inputUrl, {
          headers: { 'User-Agent': userAgent },
          redirect: 'follow'
        });
        finalUrl = resp.url || inputUrl;
        const html = await resp.text();
        const tm = html.match(/<title>(.*?)<\/title>/);
        if (tm) {
          pageTitle = cleanHtmlTitle(tm[1], ['京东', '图片 价格 品牌 评论']);
        }
      }
      const skuMatch = finalUrl.match(/(?:product\/|item\.jd\.com\/)(\d+)/) || finalUrl.match(/[?&]sku=(\d+)/);
      if (skuMatch) {
        return jsonResponse({
          platform: 'jd',
          name: '京东',
          icon: '🐶',
          title: pageTitle || extractedTitle || '京东商品',
          param: 'sku',
          value: skuMatch[1],
          url: `https://juns.page/go/jd/?sku=${skuMatch[1]}`
        });
      }
    }

    // 拼多多 (yangkeduo.com / pinduoduo.com)
    if (inputUrl.includes('yangkeduo.com') || inputUrl.includes('pinduoduo.com')) {
      let finalUrl = inputUrl;
      let pageTitle = '';
      const resp = await fetch(inputUrl, {
        headers: { 'User-Agent': userAgent },
        redirect: 'follow'
      });
      finalUrl = resp.url || inputUrl;
      const html = await resp.text();
      const tm = html.match(/<title>(.*?)<\/title>/);
      if (tm) {
        pageTitle = cleanHtmlTitle(tm[1], ['拼多多', '手机版']);
      }
      const goodsMatch = finalUrl.match(/[?&]goods_id=(\d+)/);
      if (goodsMatch) {
        return jsonResponse({
          platform: 'pdd',
          name: '拼多多',
          icon: '🛒',
          title: pageTitle || extractedTitle || '拼多多商品',
          param: 'id',
          value: goodsMatch[1],
          url: `https://juns.page/go/pdd/?id=${goodsMatch[1]}`
        });
      }
    }

    // 抖音 (v.douyin.com / douyin.com)
    if (inputUrl.includes('douyin.com')) {
      let finalUrl = inputUrl;
      if (inputUrl.includes('v.douyin.com')) {
        const resp = await fetch(inputUrl, {
          headers: { 'User-Agent': userAgent },
          redirect: 'manual'
        });
        finalUrl = resp.headers.get('location') || inputUrl;
      }
      const videoMatch = finalUrl.match(/(?:video\/)(\d+)/);
      if (videoMatch) {
        return jsonResponse({
          platform: 'douyin',
          name: '抖音',
          icon: '🎵',
          title: extractedTitle || '抖音视频',
          param: 'id',
          value: videoMatch[1],
          url: `https://juns.page/go/douyin/?id=${videoMatch[1]}`
        });
      }
    }

    // 酷安 (coolapk.com)
    if (inputUrl.includes('coolapk.com')) {
      const feedMatch = inputUrl.match(/feed\/(\d+)/);
      if (feedMatch) {
        return jsonResponse({
          platform: 'coolapk',
          name: '酷安',
          icon: '🌿',
          title: extractedTitle || '酷安动态',
          param: 'id',
          value: feedMatch[1],
          url: `https://juns.page/go/coolapk/?id=${feedMatch[1]}`
        });
      }
    }

    // 知乎 (zhihu.com)
    if (inputUrl.includes('zhihu.com')) {
      const pMatch = inputUrl.match(/zhuanlan\.zhihu\.com\/p\/(\d+)/);
      if (pMatch) {
        return jsonResponse({
          platform: 'zhihu',
          name: '知乎专栏',
          icon: '💡',
          title: extractedTitle || '知乎专栏',
          param: 'id',
          value: pMatch[1],
          url: `https://juns.page/go/zhihu/?type=article&id=${pMatch[1]}`
        });
      }
      const ansMatch = inputUrl.match(/question\/\d+\/answer\/(\d+)/) || inputUrl.match(/answer\/(\d+)/);
      if (ansMatch) {
        return jsonResponse({
          platform: '知乎回答',
          name: '知乎',
          icon: '💡',
          title: extractedTitle || '知乎回答',
          param: 'id',
          value: ansMatch[1],
          url: `https://juns.page/go/zhihu/?type=answer&id=${ansMatch[1]}`
        });
      }
    }

    return jsonResponse({ error: '未能成功从该链接中解析出已知平台的目标内容' }, 422);
  } catch (err) {
    return jsonResponse({ error: err.message || '服务器解析错误' }, 500);
  }
}

// 从文本中智能提取标题的算法
function extractTitleFromText(text) {
  if (!text) return '';
  let clean = text.replace(/https?:\/\/[^\s\u4e00-\u9fa5]+/g, '');
  clean = clean.replace(/【(淘宝|闲鱼|京东|哔哩哔哩|小红书|拼多多|抖音)】/g, '');
  clean = clean.replace(/(?:复制打开抖音|复制本条信息|打开【.*?】|看看【.*?的作品】|进入【.*?】|点击链接直接打开|或者复制文案打开.*|复制一下这行字.*)/g, '');
  clean = clean.replace(/[a-zA-Z0-9]{4,6}:\/[^\s]*/g, '');
  clean = clean.replace(/CZ\d+|HU\d+|CA\d+/g, '');
  clean = clean.replace(/tk=[a-zA-Z0-9]+/g, '');
  clean = clean.replace(/:\d{1,2}(?:am|pm|分|点).*/g, '');
  clean = clean.replace(/\b\d+\/\d+\b\s*后?$/g, '');

  // 优先匹配书名号、括号、双引号内容
  const quoteMatch = clean.match(/[「【“](.*?)[」】”]/);
  if (quoteMatch && quoteMatch[1].trim().length > 1) {
    let sub = quoteMatch[1].trim();
    sub = sub.replace(/^(?:快来捡漏|更新必看[❗️!]*|好物推荐|推荐)/g, '');
    sub = sub.replace(/[-_—|]哔哩哔哩.*$/g, '');
    if (sub.length > 1) return sub.trim();
  }

  // 兜底：取长度合适的一截正文文本
  const parts = clean.split(/[\n,，。！!]+/).map(p => p.trim()).filter(p => p.length > 2);
  for (const part of parts) {
    if (!/^[\d\.\:@\/\-_\s]+$/.test(part)) {
      return part.slice(0, 40).trim();
    }
  }
  return '';
}

function cleanHtmlTitle(title, ignoreWords = []) {
  if (!title) return '';
  let res = title.trim();
  for (const w of ignoreWords) {
    res = res.replace(new RegExp(`[-_—|【\\[]?${w}[-_\\]】]?`, 'gi'), '');
  }
  return res.trim().slice(0, 50);
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
