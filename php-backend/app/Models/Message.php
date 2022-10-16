<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasOne;

class Message extends Model
{
    use HasFactory;

    protected $table = 'telegram_messages';

    public function photos(): HasMany
    {
        return $this->hasMany(Photo::class, 'grouped_id', 'grouped_id');
    }

    public function author(): BelongsTo
    {
        return $this->belongsTo(Author::class, 'telegram_author_id');
    }

    public function group(): BelongsTo
    {
        return $this->belongsTo(Group::class, 'telegram_group_id');
    }

    public function maxPriceByCityId($cityId): int
    {
        dd($cityId);
        return $this->where('city_id', $cityId)->max('price');
    }
}
