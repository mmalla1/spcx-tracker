def get_color(change_pct):
    if change_pct > 0:
        return "#16a34a"
    elif change_pct < 0:
        return "#dc2626"
    return "#6b7280"

def get_arrow(change_pct):
    if change_pct > 0:
        return "▲"
    elif change_pct < 0:
        return "▼"
    return "—"

def recommendation_color(rec):
    colors = {
        "BUY NOW": "#16a34a",
        "WATCH CLOSELY": "#d97706",
        "APPROACHING — PREPARE": "#d97706",
        "DROPPING — MONITOR": "#dc2626",
        "HIGH ACTIVITY — WATCH": "#7c3aed",
        "HOLD OFF": "#2563eb",
    }
    return colors.get(rec, "#6b7280")

TARGET_PRICE = 80.00

def morning_email(data, rec, rec_reason, context):
    price = data["current_price"]
    change = data["day_change"]
    change_pct = data["day_change_pct"]
    color = get_color(change_pct)
    arrow = get_arrow(change_pct)
    target_gap = abs(data["distance_to_target"])
    target_pct = abs(data["pct_to_target"])
    rec_col = recommendation_color(rec)
    banner = ""
    if data.get("target_hit"):
        banner = '<tr><td style="background:#16a34a;padding:20px;text-align:center;"><p style="color:#fff;font-size:22px;font-weight:700;margin:0;">TARGET REACHED - $80 OR BELOW</p></td></tr>'
    rec = rec if rec else "HOLD OFF"
    facts = "".join(f"<li style='margin:6px 0;color:#374151;font-size:14px;'>{f}</li>" for f in context.get("key_facts", []))
    return f"""<!DOCTYPE html><html><head><meta charset="UTF8"></head>
<body style="margin:0;padding:0;background:#f3f4f6;font-family:sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="padding:24px 0;"><tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="background:#fff;border-radius:12px;overflow:hidden;max-width:600px;">
<tr><td style="background:#0f172a;padding:28px 32px;">
<p style="color:#94a3b8;font-size:12px;margin:0;">SpaceX Tracker</p>
<p style="color:#fff;font-size:24px;font-weight:700;margin:4px 0;">Good morning sunshine</p>
<p style="color:#64748b;font-size:13px;margin:4px 0;">{data['timestamp']} - NASDAQ: SPCX</p>
</td></tr>
{banner}
<tr><td style="padding:28px 32px;">
<table width="100%"><tr>
<td style="background:#f8fafc;border-radius:10px;padding:20px;border:1px solid #e2e8f0;">
<p style="color:#6b7280;font-size:12px;margin:0 0 6px;">Current price</p>
<p style="font-size:40px;font-weight:700;color:#0f172a;margin:0;">${price}</p>
<p style="font-size:15px;color:{color};margin:6px 0 0;">{arrow} ${abs(change):.2f} ({abs(change_pct):.2f}%)</p>
</td><td width="16"></td>
<td style="background:#f8fafc;border-radius:10px;padding:20px;border:1px solid #e2e8f0;">
<p style="color:#6b7280;font-size:12px;margin:0 0 6px;">Your $80 target</p>
<p style="font-size:40px;font-weight:700;color:#0f172a;margin:0;">$80</p>
<p style="font-size:15px;color:#6b7280;margin:6px 0 0;">${target_gap:.2f} away ({target_pct:.1f}%)</p>
</td></tr></table></td></tr>
<tr><td style="padding:0 40px 24px;">
<div style="border-left:4px solid {rec_col};background:#f8fafc;padding:16px 20px;">
<p style="color:{rec_col};font-size:11px;font-weight:700;text-transform:uppercase;margin:0 0 4px;">Morning call</p>
<p style="font-size:16px;font-weight:700;color:{rec_col};margin:0 4px;">{rec}</p>
<p style="font-size:14px;color:#374151;margin:0;line-height:1.6;">{rec_reason}</p>
</div></td></tr>
<tr><td style="padding:0 32px 24px;">
<p style="font-size:14px;color:#374151;line-height:1.7;margin:0;">{context.get('why_80_matters','')}</p>
</td></tr>
<tr><td style="background:#f8fafc;padding:20px 32px;border-top:1px solid #e2e8f0;">
<p style="font-size:12px;color:#9ca3af;margin:0;">Evening report at 6 PM. Not financial advice.</p>
</td></tr></table></td></tr></table></body></html>"""

def evening_email(data, rec, rec_reason, context):
    price = data["current_price"]
    change = data["day_change"]
    change_pct = data["day_change_pct"]
    color = get_color(change_pct)
    arrow = get_arrow(change_pct)
    target_gap = abs(data["distance_to_target"])
    target_pct = abs(data["pct_to_target"])
    rec_col = recommendation_color(rec)
    banner = ""
    if data.get("target_hit"):
        banner = '<tr><td style="background:#16a34a;padding:20px 32px;text-align:center;"><p style="color:#fff;font-size:20px;font-weight:700;margin:0;">TARGET HIT - TIME TO ACT </p></td></tr>'
    facts = "".join(f"<li style='margin:6px 0;color:#374151;font-size:14px;'>{f}</li>" for f in context.get("key_facts", []))
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"></head>
<body style="margin:0;padding:0;background:#f3f4f6;font-family:sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="padding:24px 0;"><tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="background:#fff;border-radius:12px;overflow:hidden;max-width:600px;">
<tr><td style="background:#0f172a;padding:28px 32px;">
<p style="color:#94a3b8;font-size:12px;margin:0;">SpaceX Tracker - Evening Report</p>
<p style="color:#fff;font-size:24px;font-weight:700;margin:4px 0h">SPCX Daily Analysis</p>
<p style="color:#64748b;font-size:13px;margin:4px 0;">{data['timestamp']} - NASDAQ: SPCX</p>
</td></tr>
{banner}
<tr><td style="padding:28px 32px16px;">
<table width="100%"><tr>
<td style="background:#f8fafc;border-radius:10px;padding:20px;border:1px solid #e2e8f0;">
<p style="color:#6b7280;font-size:12px;margin:0 0 6px;">Today close</p>
<p style="font-size:38px;font-weight:700;color:#0f172a;margin:0;">${price}</p>
<p style="font-size:15px;color:{color};margin:6px 0 0;">{arrow} ${abs(change):.2f} ({abs(change_pct):.2f}%)</p>
</td><td width="16"></td>
<td style="background:#f8fafc;border-radius:10px;padding:20px;border:1px solid #e2e8f0;">
<p style="color:#6b7280;font-size:12px;margin:0 0 6px;">Buy target</p>
<p style="font-size:38px;font-weight:700;color:#0f172a;margin:0;">$80</p>
<p style="font-size:15px;color:#6b7280;margin:6px 0 0;">${target_gap:.2f} away ({target_pct:.1f}%)</p>
</td></tr></table></td></tr>
<tr><td style="padding:0 32px 24px;">
<div style="border-left:4px solid {rec_col};background:#f8fafc;padding:18px 20px;">
<p style="color:{rec_col};font-size:11px;font-weight:700;text-transform:uppercase;margin:0 0 4px;">Tonight recommendation</p>
<p style="font-size:18px;font-weight:700;color:{rec_col};margin:0 0 8px;">{rec}</p>
<p style="font-size:14px;color:#374151;margin:0;line-height:1.7;">{rec_reason}</p>
</div></td></tr>
<tr><td style="padding:0 32px 24px;">
<p style="font-size:16px;font-weight:700;color:#0f172a;margin:0 0 14px;">Bull vs Bear</p>
<table width="100%"><tr>
<td width="48%" style="background:#f0fdf4;border-radius:10px;padding:16px;border:1px solid #bbf7d0;vertical-align:top;">
<p style="color:#16a34a;font-size:12px;font-weight:700;text-transform:uppercase;margin:0 0 8px;">Bull - $200+</p>
<p style="font-size:13px;color:#374151;margin0;line-height:1.6;">Starlink dominates global internet. Starship commercializes. Revenue explodes past $40B by 2028.</p>
</td><td width="4"></td>
<td width="48%" style="background:#fef2f2;border-radius:10px;padding:16px;border:1px solid #fecaca;vertical-align:top;">
<p style="color:#dc2626;font-size:12px;font-weight:700;text-transform:uppercase;margin:0 0 8px;">Bear - $75</p>
<p style="font-size:13px;color:#374151;margin:0;line-height:1.6;">$4.9B loss in 2025 unsustainable. P/S of 60x extreme. Musk distraction risk.</p>
</td></tr></table></td></tr>
<tr><td style="padding:0 32px 24px;">
<p style="font-size:16px;font-weight:700;color:#0f172a;margin:0 0 12px;">Key facts</p>
<ul style="margin:0;padding-left:20px;">{facts}</ul>
</td></tr>
<tr><td style="padding:0 32px 24px;">
<p style="font-size:16px;font-weight:700;color:#0f172a;margin:0 0 14px;">How to buy when it hits $80</p>
<table width="100%" style="border:1px solid #e2e8f0;border-radius:10px;overflow:hidden;">
<tr><td style="padding:10px 16px;border-bottom:1px solid #e2e8f0;"><strong style="color:#7c3aed;">1</strong>&nbsp;&nbsp;Open Fidelity, Schwab or Robinhood - search SPCX</td></tr>
<tr><td style="padding:10px 16px;border-bottom:1px solid #e2e8f0;"><strong style="color:#7c3aed;">2</strong>&nbsp;&nbsp;Place a LIMIT order at $80 (not market order)</td></tr>
<tr><td style="padding:10px 16px;border-bottom:1px solid #e2e8f0;"><strong style="color:#7c3aed;">3</strong>&nbsp;&nbsp;Only invest what you can keep for 3-5 years</td></tr>
<tr><td style="padding:10px 16px;"><strong style="color:#7c3aed;">4</strong>&nbsp;&nbsp;Consider buying in portions, not all at once</td></tr>
</table></td></tr>
<tr><td style="background:#f8fafc;padding:20px 32px;border-top:1px solid #e2e8f0;">
<p style="font-size:12px;color:#9ca3af;margin:0;">Next morning report at 8 AM. Not financial advice.</p>
</td></tr></table></td></tr></table></body></html>"""
