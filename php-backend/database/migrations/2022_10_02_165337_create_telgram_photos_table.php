<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateTelgramPhotosTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('telegram_photos', function (Blueprint $table) {
            $table->bigInteger('id');
            $table->unsignedBigInteger('telegram_group_id')->nullable()->index();
            $table->bigInteger('grouped_id');
            $table->string('path');
            $table->timestamps();

            $table->primary(['id', 'telegram_group_id']);
            $table->foreign('telegram_group_id')->references('id')->on('telegram_groups')->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('telegram_photos');
    }
}
