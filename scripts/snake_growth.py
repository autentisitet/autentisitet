#!/usr/bin/env python3
"""Add two bounded, temporary tail segments to pinned Platane/snk SVG output."""
import argparse
import copy
import re
import xml.etree.ElementTree as ET
from pathlib import Path

SVG = 'http://www.w3.org/2000/svg'
MAX_SVG_BYTES = 2_000_000
ET.register_namespace('', SVG)


def add_growth(text: str) -> str:
    if len(text.encode('utf-8')) > MAX_SVG_BYTES:
        raise ValueError('SVG exceeds size limit')
    if re.search(r'<!\s*(?:DOCTYPE|ENTITY)\b', text, re.IGNORECASE):
        raise ValueError('DTD and entity declarations are not allowed')
    root = ET.fromstring(text)
    if root.tag != f'{{{SVG}}}svg':
        raise ValueError('Root element is not an SVG document')
    if root.find(f".//*[@id='snake-growth']") is not None:
        return text
    style = root.find(f'{{{SVG}}}style')
    if style is None or not style.text:
        raise ValueError('Missing snk CSS')
    css = style.text
    duration = re.search(r'\.s\{[^}]*?([\d.]+)ms', css)
    tail = root.find(f"{{{SVG}}}rect[@class='s s3']")
    # s1 follows the head by one grid step; its first keyframe gives the delay.
    step = re.search(r'@keyframes s1\{[^}]*\}([\d.]+)%', css)
    if duration is None or tail is None or step is None:
        raise ValueError('Unsupported snk snake structure')
    milliseconds = float(duration[1])
    delay = float(step[1]) * milliseconds / 100
    if not 0 < delay < milliseconds / 10:
        raise ValueError('Invalid snake step duration')
    eaten = sorted(float(value) * milliseconds / 100 for value in re.findall(
        r'@keyframes c\w+\{([\d.]+)%\{fill:', css
    ))
    # Avoid a permanently long tail on dense graphs: one pulse at most every 2.4s.
    pulses = []
    for time in eaten:
        if time > delay * 5 and time + 1800 < milliseconds:
            if not pulses or time - pulses[-1] >= 2400:
                pulses.append(time)
    group = ET.Element(f'{{{SVG}}}g', {'id': 'snake-growth'})
    for index in (1, 2):
        frames = ['0%,100%{opacity:0}']
        for time in pulses:
            start = time + (index - 1) * delay
            for offset, opacity in ((0, 0), (100, 1), (900, 1), (1300, 0)):
                frames.append(f'{(start + offset) / milliseconds * 100:.5f}%{{opacity:{opacity}}}')
        name = f'snake-growth-{index}'
        css += f'@keyframes {name}' + '{' + ''.join(frames) + '}'
        wrapper = ET.SubElement(group, f'{{{SVG}}}g', {
            'style': f'opacity:0;animation:{name} {milliseconds:g}ms linear infinite',
        })
        segment = copy.deepcopy(tail)
        segment.set('style', f'animation-delay:{delay * index:g}ms')
        wrapper.append(segment)
    # Paint new tail behind the original body; keep original snake/path untouched.
    root.insert(list(root).index(tail) - 3, group)
    style.text = css
    return ET.tostring(root, encoding='unicode') + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', nargs='+', type=Path)
    args = parser.parse_args()
    for path in args.files:
        if path.stat().st_size > MAX_SVG_BYTES:
            raise ValueError(f'SVG exceeds size limit: {path}')
        text = path.read_text(encoding='utf-8')
        result = add_growth(text)
        path.write_text(result, encoding='utf-8')


if __name__ == '__main__':
    main()
