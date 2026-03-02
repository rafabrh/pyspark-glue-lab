param(
  [Parameter(Mandatory=$true)][int]$Id,
  [Parameter(Mandatory=$true)][string]$Slug,
  [ValidateSet("easy","medium","hard")][string]$Level="easy"
)

$root = Split-Path -Parent $PSScriptRoot
$destDir = Join-Path $root "leetcode\python\$Level"
New-Item -ItemType Directory -Force -Path $destDir | Out-Null

$idPadded = "{0:D4}" -f $Id
$slugNorm = $Slug.ToLower() -replace "[^a-z0-9_]", "_"

$module = "lc_${idPadded}_${slugNorm}"
$solutionPath = Join-Path $destDir "${module}.py"
$testPath = Join-Path $destDir "test_${module}.py"

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

def solve(*args, **kwargs):
    raise NotImplementedError
"@ | Set-Content -Encoding UTF8 $solutionPath

@"
from $module import solve

def test_basic():
    raise NotImplementedError
"@ | Set-Content -Encoding UTF8 $testPath

Write-Host "Created:"
Write-Host " - $solutionPath"
Write-Host " - $testPath"
