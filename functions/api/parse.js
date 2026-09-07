export async function onRequestPost(context) {
  try {
    const body = await context.request.json();
    const rawText = body.text || '';

    // 1. 尝试直接从文本中捕获特征码
    // B站 BV号
    const bvMatch = rawText.match(/\b(BV[a-zA-Z0-9]{10})\b/);
    if (bvMatch) {
      return jsonResponse({
        platform: 'bili',
        name: '哔哩哔哩',
        icon: '📺',
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
      if (inputUrl.includes('3.cn')) {
        const resp = await fetch(inputUrl, {
          headers: { 'User-Agent': userAgent },
          redirect: 'manual'
        });
        finalUrl = resp.headers.get('location') || inputUrl;
      }
      const skuMatch = finalUrl.match(/(?:product\/|item\.jd\.com\/)(\d+)/) || finalUrl.match(/[?&]sku=(\d+)/);
      if (skuMatch) {
        return jsonResponse({
          platform: 'jd',
          name: '京东',
          icon: '🐶',
          param: 'sku',
          value: skuMatch[1],
          url: `https://juns.page/go/jd/?sku=${skuMatch[1]}`
        });
      }
    }

    // 拼多多 (yangkeduo.com / pinduoduo.com)
    if (inputUrl.includes('yangkeduo.com') || inputUrl.includes('pinduoduo.com')) {
      let finalUrl = inputUrl;
      const resp = await fetch(inputUrl, {
        headers: { 'User-Agent': userAgent },
        redirect: 'manual'
      });
      finalUrl = resp.headers.get('location') || inputUrl;
      const goodsMatch = finalUrl.match(/[?&]goods_id=(\d+)/);
      if (goodsMatch) {
        return jsonResponse({
          platform: 'pdd',
          name: '拼多多',
          icon: '🛒',
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

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Access-Control-Allow-Origin': '*'
    }
  });
}
