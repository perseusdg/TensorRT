import torch
import torch.nn as nn
import torch_tensorrt.fx.tracer.acc_tracer.acc_ops as acc_ops
from parameterized import parameterized
from torch.testing._internal.common_fx2trt import AccTestCase
from torch.testing._internal.common_utils import run_tests


class TestConverter(AccTestCase):
    @parameterized.expand(
        [
            ("2d_dim", "ij,jk->ik", (2, 3), (3, 4)),
            ("2d_dim_ext", "ij,kj->ik", (2, 3), (4, 3)),
            ("3d_dim", "cxd,cyd->cxy", (3, 4, 5), (3, 6, 5)),
            ("4d_dim", "bcwd,bcdh->bcwh", (2, 3, 4, 5), (2, 3, 5, 6)),
            ("4d_dim_ext", "bcxd,bcyd->bcxy", (2, 3, 4, 5), (2, 3, 6, 5)),
            # TRT does not support ellipsis or diagonal operations
        ]
    )
    def test_einsum(self, _, equation, x_size, y_size):
        class Einsum(nn.Module):
            def forward(self, x, y):
                return torch.einsum(equation, x, y)

        inputs = [torch.randn(*x_size), torch.randn(*y_size)]
        self.run_test(
            Einsum(),
            inputs,
            expected_ops={acc_ops.einsum},
            test_implicit_batch_dim=False,
        )


if __name__ == "__main__":
    run_tests()
