# Run this script as Administrator to map website.oil and website.h2o to 127.0.0.1
$hostsPath = "$env:windir\System32\drivers\etc\hosts"
$content = Get-Content -Path $hostsPath -Raw

if ($content -notmatch "website\.oil") {
    $entry = "`r`n127.0.0.1 website.oil`r`n127.0.0.1 website.h2o`r`n"
    Add-Content -Path $hostsPath -Value $entry
    Write-Host "SUCCESS: Mapped website.oil and website.h2o to 127.0.0.1"
} else {
    Write-Host "INFO: website.oil and website.h2o already present in hosts file."
}
