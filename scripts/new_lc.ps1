param(
  [Parameter(Mandatory=$true)][string]$Id,
  [Parameter(Mandatory=$true)][string]$Slug,
  [ValidateSet("easy","medium","hard")][string]$Level="easy"
)

$root = Split-Path -Parent $PSScriptRoot
$destDir = Join-Path $root "leetcode\python\$Level"
New-Item -ItemType Directory -Force -Path $destDir | Out-Null

$module = "${Id}_${Slug}".ToLower()
$module = $module -replace "[^a-z0-9_]", "_"

$solutionPath = Join-Path $destDir "$module.py"
$testPath = Join-Path $destDir "test_$module.py"

if (Test-Path $solutionPath) { throw "Já existe: $solutionPath" }

@"
"""
LeetCode: $Id - $Slug
Difficulty: $Level
Pattern: <fill>

Idea:
- <fill>

Complexity:
- Time: O(?)
- Space: O(?)

Pitfalls:
- <fill>
"""

from typing import List

def solve(nums: List[int], target: int) -> List[int]:
    raise NotImplementedError
"@ | Set-Content -Encoding UTF8 $solutionPath

@"
from $module import solve

def test_basic():
    assert solve([2,7,11,15], 9) == [0,1]
"@ | Set-Content -Encoding UTF8 $testPath

Write-Host "Created:"
Write-Host " - $solutionPath"
Write-Host " - $testPath"
