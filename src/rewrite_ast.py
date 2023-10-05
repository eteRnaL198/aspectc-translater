import sys
from pycparser import c_generator

sys.path.extend([".", ".."])
from pycparser import c_parser

text = r"""
void func(void)
{
  x = 1;
}
"""

if __name__ == "__main__":
    parser = c_parser.CParser()
    ast = parser.parse(text)
    print("Before:")
    ast.show(offset=2)

    assign = ast.ext[0].body.block_items[0]
    assign.lvalue.name = "y"
    assign.rvalue.value = 2

    print("After:")
    # ast.show(offset=2)

    generator = c_generator.CGenerator()
    print(generator.visit(ast))
