<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Author extends Model
{
    use HasFactory;

    protected $table = 'telegram_authors';

    protected $fillable = [
        'username',
        'type',
        'first_name',
        'last_name',
        'title',
        'avatar_path',
        'description',
    ];
}
