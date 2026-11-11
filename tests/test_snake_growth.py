import unittest
import xml.etree.ElementTree as ET
from scripts.snake_growth import MAX_SVG_BYTES, SVG, add_growth

FIXTURE = '''<svg xmlns="http://www.w3.org/2000/svg"><style>
.s{fill:var(--cs);animation:none linear 10000ms infinite}
@keyframes s1{0%,99%{transform:translate(16px,-16px)}1%{transform:translate(0px,-16px)}}
@keyframes c0{20%{fill:var(--c1)}20.02%,100%{fill:var(--ce)}}
@keyframes c1{21%{fill:var(--c1)}21.02%,100%{fill:var(--ce)}}
</style><rect class="s s0"/><rect class="s s1"/><rect class="s s2"/>
<rect class="s s3" width="10" height="10"/></svg>'''


class GrowthTests(unittest.TestCase):
    def test_bounded_tail_preserves_originals(self):
        root = ET.fromstring(add_growth(FIXTURE))
        self.assertEqual(len(root.findall(f'{{{SVG}}}rect')), 4)
        group = root.find(f"{{{SVG}}}g[@id='snake-growth']")
        self.assertEqual(len(group.findall(f'.//{{{SVG}}}rect')), 2)
        css = root.find(f'{{{SVG}}}style').text
        self.assertIn('0%,100%{opacity:0}', css)
        self.assertIn('animation-delay:200ms', ET.tostring(group, encoding='unicode'))
        self.assertEqual(css.count('20.00000%{opacity:0}'), 1)

    def test_idempotent(self):
        result = add_growth(FIXTURE)
        self.assertEqual(add_growth(result), result)

    def test_rejects_changed_upstream_structure(self):
        with self.assertRaises(ValueError):
            add_growth('<svg xmlns="http://www.w3.org/2000/svg"/>')

    def test_rejects_non_svg_xml_and_dtds(self):
        for text in (
            '<root/>',
            '<!DOCTYPE svg [<!ENTITY x "value">]><svg xmlns="http://www.w3.org/2000/svg"/>',
        ):
            with self.subTest(text=text), self.assertRaises(ValueError):
                add_growth(text)

    def test_rejects_oversized_input(self):
        with self.assertRaises(ValueError):
            add_growth(' ' * (MAX_SVG_BYTES + 1))

    def test_empty_graph_has_no_visible_growth(self):
        result = add_growth(FIXTURE.replace('@keyframes c0', '@keyframes z0').replace('@keyframes c1', '@keyframes z1'))
        css = ET.fromstring(result).find(f'{{{SVG}}}style').text
        self.assertNotIn('opacity:1', css)


if __name__ == '__main__':
    unittest.main()
