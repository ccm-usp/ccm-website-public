function Remove-Diacritics {
    param ([String]$src = [String]::Empty)
    $normalized = $src.Normalize([Text.NormalizationForm]::FormD)
    $sb = New-Object Text.StringBuilder
    $normalized.ToCharArray() | ForEach-Object {
        if ([Globalization.CharUnicodeInfo]::GetUnicodeCategory($_) -ne [Globalization.UnicodeCategory]::NonSpacingMark) {
            [void]$sb.Append($_)
        }
    }
    $sb.ToString()
}

$Directory = Get-Location #Set Directory
$Files = Get-ChildItem $Directory | Where-Object {$_.Name -like "*.jpg"} #Specify FileTypes
$SizeHD = 544
$SizeLQ = 272
ForEach ($File in $Files) {
    $newName = (Remove-Diacritics $File).ToLower() -replace ' ', '-'
    $newNameHD = $newName -replace '\.jpg$', '@2x.jpg'
    magick $File -resize $SizeHD -quality 95 $newNameHD
    magick $File -resize $SizeLQ -quality 95 $newName
}